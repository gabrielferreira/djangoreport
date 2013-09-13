# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils import timezone
import datetime
from report.models import Report


class ReportTestCase(TestCase):
    def setUp(self):
        self.name = u'ReportTest'
        self.slug = u'RT'
        self.description = u'ReportTest description'
        self.parent_model = u'report'
        self.distinct = True
        self.favorite = u''

    def test_should_output_payment_type_information(self):
        self.report = Report.objects.filter(name=u'ReportTest').all()[0]
        self.assertEqual(unicode(self.report), self.report.name)