from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
# Create your models here.

from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_id = models.CharField(max_length=20)
    department_hod = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    department_email = models.EmailField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.department_name}-{self.department_id}")
        super(Department, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.department_name}  ({self.department_id})"
