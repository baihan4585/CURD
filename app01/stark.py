from stark.service import v1
from app01 import models
from django.utils.safestring import mark_safe
from django.shortcuts import render,HttpResponse,redirect
from django.conf.urls import url
from django.forms import ModelForm


class UserInfoModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        error_messages = {
            'name':{
                'required':'用户名不能为空'
            }
        }

print('aaa')
class UserInfoConfig(v1.StarkConfig):


    def extra_url(self):
        '''
        预留扩展url（基本url不够时支持扩展）
        :return:
        '''
        url_list = [
            url(r'^xxxx/$', self.func),
        ]
        return url_list

    def func(self,request):
        return HttpResponse('...')

    list_display = ['id','name']
    #可以根据权限需要重写get_list_display方法，添加url

    model_form_class = UserInfoModelForm

v1.site.register(models.UserInfo,UserInfoConfig)

class RoleConfig(v1.StarkConfig):
    list_display = ['name']

v1.site.register(models.Role,RoleConfig)

class UserTypeConfig(v1.StarkConfig):
    list_display = ['id','xxx']

v1.site.register(models.UserType,UserTypeConfig)

class HostModelForm(ModelForm):
    class Meta:
        model = models.Host
        fields = ['id','hostname','ip','port']
        error_messages = {
            'hostname':{
                'required':'主机名不能为空',
            },
            'ip':{
                'required': 'IP不能为空',
                'invalid': 'IP格式错误',
            }

        }




class HostConfig(v1.StarkConfig):
    def ip_port(self,obj=None,is_header=False):
        if is_header:
            return '自定义列'
        return "%s:%s" %(obj.ip,obj.port,)

    list_display = ['id','hostname','ip','port',ip_port]
    # get_list_display

    show_add_btn = True
    # get_show_add_btn

    model_form_class = HostModelForm
    # get_model_form_class


    def extra_url(self):
        urls = [
            url('^report/$',self.report_view)
        ]
        return urls

    def report_view(self,request):
        return HttpResponse('自定义报表')

    def delete_view(self,request,nid,*args,**kwargs):
        if request.method == "GET":
            return render(request,'stark/my_delete.html')
        else:
            self.model_class.objects.filter(pk=nid).delete()
            return redirect(self.get_list_url())


v1.site.register(models.Host,HostConfig)