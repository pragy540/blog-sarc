from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from customutils.customfields import ContentTypeRestrictedFileField as RestFileField


class Section(models.Model):
	section = models.CharField(max_length=50)

	def __unicode__(self):
		return self.section

class Tag(models.Model):
	tag = models.CharField(max_length = 15)

	def __unicode__(self):
		return self.tag

class Post(models.Model):
	title = models.CharField(max_length = 200, blank = False)
	author = models.CharField(max_length = 100, blank = False)
	date = models.DateField(blank = False)
	text = RichTextField(config_name = 'awesome_ckeditor')
	section = models.ForeignKey(Section, blank = False)
	tags = models.ManyToManyField(Tag, blank = False)
	thumbnail = RestFileField(content_types=['image/jpeg', 'image/png'], max_upload_size=4194304,
                             upload_to="thumbnail-photo", default = '')
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']