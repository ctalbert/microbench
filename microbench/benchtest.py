import os
import sys
import json
import time
import re
import weakref
import time

from marionette import CommonTestCase
from marionette import Marionette

class MicroBenchTestCase(CommonTestCase):

    match_re = re.compile(r"test_(.*)\.html$")

    def __init__(self, marionette_weakref, methodName='run_test', htmlfile=None):
        self.htmlfile = htmlfile
        self._marionette_weakref = marionette_weakref
        self.marionette = None
        CommonTestCase.__init__(self, methodName)

    @classmethod
    def add_tests_to_suite(cls, mod_name, filepath, suite, testloader, marionette, testvars):
        suite.addTest(cls(weakref.ref(marionette), htmlfile=filepath))

    def run_test(self):
        if self.marionette.session is None:
            self.marionette.start_session()
        self.marionette.test_name = os.path.basename(self.htmlfile)
        # TODO: This is kind of a hack - depends on how we set up the httpd server
        # Would be better to have marionette test runner pass in url
        # TODO: For some reason mozhttpd isn't loading this URL not sure why
        #self.url = self.marionette.baseurl + '/tests/' + os.path.basename(self.htmlfile)
        self.url = 'http://localhost/%s' % os.path.basename(self.htmlfile)
        print "DBG::URL is: %s" % self.url
        self.marionette.execute_script("log('TEST-START: %s');" % self.htmlfile.replace('\\', '\\\\'))
        self.marionette.set_context("chrome")      
        self.marionette.navigate(self.url)
        # TODO: Set the timeouts by reading from the script file boilerplate: http://mxr.mozilla.org/mozilla-central/source/testing/marionette/client/marionette/marionette_test.py#186
        self.marionette.set_script_timeout(10000)
        # TODO: Should capture timeouts in try/except
        results = self.marionette.execute_script('window.document.start_test();',
                                                 new_sandbox=False,
                                                 special_powers=True)
        self.marionette.execute_script("log('TEST-END: %s');" % self.htmlfile.replace('\\', '\\\\'))
        self.marionette.test_name = None
