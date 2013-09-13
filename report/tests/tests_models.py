# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils import timezone
import datetime
from report.models import Report


class ReportTestCase(TestCase):
    def setUp(self):
        rep = Report()
        rep.name = u'ReportTest'
        rep.slug = u'RT'
        rep.description = u'ReportTest description'
        rep.parent_model = Report.get_models()[0]
        rep.distinct = True
        rep.save()

    def test_should_output_payment_type_information(self):
        self.report = Report.objects.filter(name=u'ReportTest').all()[0]
        self.assertEqual(unicode(self.report), self.report.name)