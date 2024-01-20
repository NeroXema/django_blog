from django.contrib import admin
from blog.models import PostModel,CategoryModel,CommentModel,UserDetailModel,CategoryDetailModel
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
 list_display = ("title", "body","created_at")
 list_filter = ("created_at", )
 search_fields = ("title", "body", )
admin.site.register(PostModel, PostModelAdmin)
admin.site.register(CategoryModel)
admin.site.register(CommentModel)
admin.site.register(UserDetailModel)
admin.site.register(CategoryDetailModel)