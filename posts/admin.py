from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post,Review,Category


class PostAdmin(SummernoteModelAdmin):
    list_display=['user','title','draft','publish_date']
    list_filter=['draft']
    search_fields=['title','content']

    summernote_fields = ('content',)


admin.site.register(Post,PostAdmin)
admin.site.register(Review)
admin.site.register(Category)
