from django.contrib import admin

# Register your models here.
from .models import Grades, Students

# I need to create two students when I create the grade.
# class StudentsInfo(admin.StackedInline): 新建的 Students 在同一列.
class StudentsInfo(admin.TabularInline):  # 信件的 students 在同一行.
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
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


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "Boy"
        else:
            return "Girl"
    # 设置页面列的名称:
    gender.short_description = "Sex" 
            
    # 列表页属性
    list_display = [  # before, this is only the toString, 现在可以显示各个字段,等信息
        "pk",
        "sname",
         gender,
        "scontend",
        "isdelete",
    ]
    list_per_page = 2
    
    # 控制 执行动作的位置.
    actions_on_bottom = True
    actions_on_top = False

# admin.site.register(Students,StudentsAdmin) --> 用@admin.register(Students) 代替.
