from Products.Five.testbrowser import Browser
from Products.PloneTestCase import PloneTestCase as ptc
from plone.app.controlpanel.tests.cptc import ControlPanelTestCase
from collective.solr.utils import activate
from collective.solr.tests.layer import SolrLayer, SolrFacetsLayer


ptc.setupPloneSite()


class SolrTestCase(ptc.PloneTestCase):
    """ base class for integration tests """

    layer = SolrLayer


class SolrControlPanelTestCase(ControlPanelTestCase):
    """ base class for control panel tests """

    layer = SolrFacetsLayer


class SolrFunctionalTestCase(ptc.FunctionalTestCase):
    """ base class for functional tests """

    layer = SolrLayer

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            user = ptc.default_user
            pwd = ptc.default_password
            browser.addHeader('Authorization', 'Basic %s:%s' % (user, pwd))
        return browser

    def setStatusCode(self, key, value):
        from ZPublisher import HTTPResponse
        HTTPResponse.status_codes[key.lower()] = value

    def activateAndReindex(self):
        """ activate solr indexing and reindex the existing content """
        activate()
        response = self.portal.REQUEST.RESPONSE
        original = response.write
        response.write = lambda x: x    # temporarily ignore output
        maintenance = self.portal.unrestrictedTraverse('@@solr-maintenance')
        maintenance.clear()
        maintenance.reindex()
        response.write = original


class SolrFacetsTestCase(SolrFunctionalTestCase):
    """ base class for functional tests with facets """

    layer = SolrFacetsLayer