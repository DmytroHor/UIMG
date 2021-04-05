from django.contrib import admin

from . import models


class ImageAdmin(admin.ModelAdmin):
    fields = (
        'image', 'image_preview', 'result_image', 'result_image_preview',
        'random_from', 'random_to',
    )
    readonly_fields = ('image_preview', 'result_image', 'result_image_preview',)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


admin.site.register(models.Image, ImageAdmin)
