from stark.service import v1
from app01 import models
from django.utils.safestring import mark_safe

print('aaa')
class UserInfoConfig(v1.StarkConfig):
    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return '选择'
        return mark_safe('<input type="checkbox" name="bk" value="%s">' %(obj.id))
    def edit(self,obj=None,is_header=False):
        if is_header:
            return '操作'
        return mark_safe('<a herf="/edit/%s">编辑</a>' %(obj.id))

    list_display = [checkbox,'id','name',edit]

v1.site.register(models.UserInfo,UserInfoConfig)

class RoleConfig(v1.StarkConfig):
    list_display = ['name']

v1.site.register(models.Role,RoleConfig)

class UserTypeConfig(v1.StarkConfig):
    list_display = ['id','xxx']

v1.site.register(models.UserType,UserTypeConfig)