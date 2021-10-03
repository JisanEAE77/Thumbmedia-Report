from django.db import models
import os
from django.conf import settings
from django.conf.urls.static import static

# Create your models here.


class Adsense(models.Model):
    file = models.FileField(upload_to='csv', blank=False)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Adsense, self).delete(*args, **kwargs)


class Premium(models.Model):
    file = models.FileField(upload_to='premium', blank=False)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Premium, self).delete(*args, **kwargs)


class Super(models.Model):
    file = models.FileField(upload_to='super', blank=False)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(Super, self).delete(*args, **kwargs)
