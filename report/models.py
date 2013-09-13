# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Report(models.Model):
	@staticmethod
	def get_models():
		_models = ContentType.objects.all()
		if getattr(settings, 'REPORT_MODEL_INCLUDE', False):
		    _models = models.filter(name__in=settings.REPORT_MODEL_INCLUDE)
		if getattr(settings, 'REPORT_MODEL_EXCLUDE', False):
			_models = models.exclude(name__in=settings.REPORT_MODEL_EXCLUDE)
		return _models

	class Meta:
		verbose_name = u'Report'
		verbose_name_plural = u'Reports'

	name = models.CharField(max_length=250)
	slug = models.SlugField(verbose_name=u'Short Name', unique=True)
	description = models.TextField(blank=True, null=True)
	parent_model = models.ForeignKey(ContentType, limit_choices_to={'pk__in':get_models})
	created = models.DateField(auto_now_add=True)
	modified = models.DateField(auto_now=True)
	user_created = models.ForeignKey(AUTH_USER_MODEL, editable=False, blank=True, null=True)
	user_modified = models.ForeignKey(AUTH_USER_MODEL, editable=False, blank=True, null=True, related_name="report_modified_set")
	distinct = models.BooleanField()
	favorite = models.ManyToManyField(AUTH_USER_MODEL, blank=True,
									help_text="These users favorite this report.",
									related_name="report_favorite_set")

	def add_aggregates(self, queryset):
	    for display_field in self.displayfield_set.filter(aggregate__isnull=False):
	        if display_field.aggregate == "Avg":
	            queryset = queryset.annotate(Avg(display_field.path + display_field.field))
	        elif display_field.aggregate == "Max":
	            queryset = queryset.annotate(Max(display_field.path + display_field.field))
	        elif display_field.aggregate == "Min":
	            queryset = queryset.annotate(Min(display_field.path + display_field.field))
	        elif display_field.aggregate == "Count":
	            queryset = queryset.annotate(Count(display_field.path + display_field.field))
	        elif display_field.aggregate == "Sum":
				queryset = queryset.annotate(Sum(display_field.path + display_field.field))
		return queryset

	def __unicode__(self):
		return self.name