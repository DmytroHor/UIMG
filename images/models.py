import os
from functools import partial
from io import BytesIO

from django.core.files import File
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from utils.image_unifier import ImageUnifier


def user_directory_path(instance, filename, unique=False):
    filename, ext = os.path.splitext(filename)
    filename = filename.split('/')[-1]
    return f'user_images/{instance.owner.username}/{filename}{"_unique" if unique else ""}{ext}'


class Image(models.Model):
    image = models.ImageField(_('image'), unique=True, upload_to=user_directory_path)
    result_image = models.ImageField(
        _('result image'),
        unique=True,
        upload_to=partial(user_directory_path, unique=True)
    )
    owner = models.ForeignKey('users.User', related_name='images', on_delete=models.CASCADE)
    random_from = models.SmallIntegerField(
        default=0,
        help_text='Value from -255 to 255',
        validators=[
            MinValueValidator(-255),
            MaxValueValidator(255),
        ]
    )
    random_to = models.SmallIntegerField(
        default=0,
        help_text='Value from -255 to 255',
        validators=[
            MinValueValidator(-255),
            MaxValueValidator(255),
        ]
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        self.create_unique_image()
        super().save(*args, **kwargs)

    def image_preview(self):
        return format_html(f'<img src="{self.image.url}" width="500" height="500"/>') if self.image else ''

    def result_image_preview(self):
        return format_html(f'<img src="{self.result_image.url}" width="500" height="500"/>') if self.image else ''

    def create_unique_image(self):
        unifier = ImageUnifier(self.image)
        result_image = unifier.create_new_image()
        image_file = BytesIO()
        result_image.save(image_file, 'JPEG')
        self.result_image.save(
            self.image.name,
            File(image_file),
            save=False
        )


@receiver(pre_delete, sender=Image)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
    if instance.result_image:
        instance.result_image.delete(False)
