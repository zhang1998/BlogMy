from django.contrib import admin
from .models import article
# Register your models here.

class BlogArticleAdmin(admin.ModelAdmin):
    list_display=("title","author","publish")
    list_filter=("publish","author")
    search_fields=('title',"body")
    raw_id_fields=("author",)  #这里  ,号 不要省略掉了 这里显示除了数据类型
    date_hierarchy="publish"
    ordering=['publish','author']
admin.site.register(article,BlogArticleAdmin)# 先是创建了article的模型 数据 然后在这里引入 但是想要在别的地方使用呢?以后就会明白了
