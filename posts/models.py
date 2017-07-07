from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
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
	slug = models.SlugField(max_length = 200)
	author = models.CharField(max_length = 100, blank = False)
	date = models.DateField(blank = False)
	text = RichTextUploadingField(config_name = 'awesome_ckeditor', blank = True)
	section = models.ForeignKey(Section, blank = False)
	tags = models.ManyToManyField(Tag, blank = False)
	thumbnail = RestFileField(content_types=['image/jpeg', 'image/png'], max_upload_size=102400,
                             upload_to="thumbnail-photo", default = '')
	views = models.PositiveIntegerField(blank=True, default = 0)
	readtime = models.PositiveIntegerField(blank=False, default = 3)		
	
	def get_tags(self):
		return ', '.join([elem.tag for elem in self.tags.all()])

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date','-id']