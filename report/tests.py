# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils import timezone
import datetime
from report.models import Report

class ReportTests(TestCase):
    def setUp(self):
        self.name = u'ReportTest'
        self.slug = u'RT'
        self.description = u'ReportTest description'
        self.parent_model = u'report'
        self.distinct = True
        self.favorite = u''

    def test_getmodels(self):
        """Models in the project"""
        self.assertGreater(Report.get_models(), 0)