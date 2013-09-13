# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils import timezone
import datetime
from report.models import Report
from django.contrib import admin as django_admin


class ReportTest(TestCase):
    def setUp(self):
        rep = Report()
        rep.name = u'ReportTest'
        rep.slug = u'RT'
        rep.description = u'ReportTest description'
        rep.parent_model = Report.get_models()[0]
        rep.distinct = True
        rep.save()

    def test_should_output_report_information(self):
        self.report = Report.objects.filter(name=u'ReportTest').all()[0]
        self.assertEqual(unicode(self.report), self.report.name)


class ReportAdminTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_Report_model_should_be_registered_within_the_admin(self):
        self.assertIn(Report, django_admin.site._registry)