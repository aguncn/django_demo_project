from django.contrib import admin
from bbs.models import Board, Topic, Post


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # 显示的标签字段，字段不能是 ManyToManyField 类型
    list_display = ('subject', 'board', 'starter', 'views', 'last_updated')
    # 设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # 设置默认可编辑字段
    # list_editable = ['subject']
    # 排除一些不想被编辑的 fields, 没有在列表的不可被编辑
    fields = ('subject', 'board')
    # 设置哪些字段可以点击进入编辑界面
    # list_display_links = ('board',)
    # 进行数据排序，负号表示降序排序
    ordering = ('-id',)
    # 显示过滤器
    list_filter = ('board', 'subject', 'starter')
    # 显示搜索框，搜索框大小写敏感
    search_fields = ('subject',)
    # 详细时间分层筛选
    date_hierarchy = 'last_updated'
    # 外键新开窗口选择
    raw_id_fields = ('board', 'starter')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


