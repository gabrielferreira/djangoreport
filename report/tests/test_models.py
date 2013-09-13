# -*- coding: utf-8 -*-
from django.test import TestCase
from report.models import *

class Report(TestCase):
	def setUp(self):
        self.name = u'ReportTest'
        self.slug = u'RT'
        self.description = u'ReportTest description'
        self.parent_model = u'report'
        self.distinct = True
        self.favorite = u''