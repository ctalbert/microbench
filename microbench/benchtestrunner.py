import os
import socket
import moznetwork

from mozhttpd import MozHttpd
from benchtest import MicroBenchTestCase
from marionette import MarionetteTestRunner
from marionette.runtests import cli

class MicroBenchTestRunner(MarionetteTestRunner):
    def register_handlers(self):
        self.test_handlers.extend([MicroBenchTestCase])

    def start_httpd(self):
        host = moznetwork.get_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("",0))
        port = s.getsockname()[1]
        s.close()
        self.baseurl = 'http://%s:%d/' % (host, port)
        self.logger.info('running webserver on %s' % self.baseurl)
        self.logger.info('webserver docroot: %s' % os.path.join(os.path.dirname(__file__), 'tests'))
        self.httpd = MozHttpd(host=host, port=port,
                              docroot=os.path.join(os.path.dirname(__file__), 'tests'))

def main():
    cli(runner_class=MicroBenchTestRunner)

if __name__ == "__main__":
    main()