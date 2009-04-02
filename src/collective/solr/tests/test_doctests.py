from unittest import TestSuite
from zope.testing import doctest
from Testing import ZopeTestCase as ztc
from collective.solr.tests.base import SolrFunctionalTestCase
from collective.solr.tests.base import SolrControlPanelTestCase
from collective.solr.tests.base import SolrFacetsTestCase
from collective.solr.tests.utils import pingSolr

optionflags = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def test_suite():
    suite = TestSuite([
        ztc.FunctionalDocFileSuite(
           'configlet.txt', package='collective.solr.tests',
           test_class=SolrControlPanelTestCase, optionflags=optionflags),
    ])
    if pingSolr():
        suite.addTest(
            ztc.FunctionalDocFileSuite(
               'errors.txt', package='collective.solr.tests',
               test_class=SolrFunctionalTestCase, optionflags=optionflags),
        )
        suite.addTest(
            ztc.FunctionalDocFileSuite(
               'search.txt', package='collective.solr.tests',
               test_class=SolrFunctionalTestCase, optionflags=optionflags),
        )
        suite.addTest(
            ztc.FunctionalDocFileSuite(
               'conflicts.txt', package='collective.solr.tests',
               test_class=SolrFunctionalTestCase, optionflags=optionflags),
        )
        suite.addTest(
            ztc.FunctionalDocFileSuite(
               'facets.txt', package='collective.solr.tests',
               test_class=SolrFacetsTestCase, optionflags=optionflags),
        )
    return suite