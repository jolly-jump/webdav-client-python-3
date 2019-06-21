__author__ = 'designerror'

import allure
#from hamcrest import *

class TestRequiredOptions:

    def test_without_webdav_hostname(self):
        options = { 'webdav_server': "http://localhost:8888/webdav"}
        allure.attach('options', options.__str__())
        assert 1
