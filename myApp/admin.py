from django.contrib import admin

# Register your models here.
from .models import Grades, Students


class GradesAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = [  # before, this is only the toString, 现在可以显示各个字段,等信息
        "pk",
        "gname",
        "gdate",
        "ggirlnum",
        "gboynum",
        "isdelete",
    ]
    list_filter = [
        "gname",
        "gdate",
        "ggirlnum",
        "gboynum",
        "isdelete"
    ]
    search_fields = [
        "gname",
        # "gdate",
        # "ggirlnum",
        # "gboynum",
        # "isdelete" 
    ]

    list_per_page = 3
    # 
    #  # 添加,修改页属性   
    #  属性的先后顺序
    # fields = [
    #     "gdate",
    #     "gname",
    #     "ggirlnum",
    #     "gboynum",
    #     "isdelete",
    #     "pk"]
    # 给属性分组,不能和上面的同时使用
    fieldsets = [
        ("num", {"fields": ["gdate", "gname"]}),
        ("base", {"fields": ["ggirlnum", "gboynum"]}),
    ]


admin.site.register(Grades, GradesAdmin)


class StudentsAdmin(admin.ModelAdmin):
    # 列表页属性
    list_display = [  # before, this is only the toString, 现在可以显示各个字段,等信息
        "pk",
        "sname",
        "sgender",
        "scontend",
        "isdelete",
    ]
    list_per_page = 2

admin.site.register(Students,StudentsAdmin)
