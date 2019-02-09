from rest_framework import views
from rest_framework.response import Response
from app01 import models

import uuid


class AuthView(views.APIView):

    def post(self, request, *args, **kwargs):
        '''用户登录认证'''
        ret = {'code': 1000}
        # print(request.data)
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        user = models.UserInfo.objects.filter(user=user).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            # 登录成功，创建token
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(
                user=user, defaults={'token': uid}
            )
            ret['token'] = uid
        return Response(ret)


from api.auth.auth import BackAuth
class MicroView(views.APIView):
    authentication_classes = [BackAuth,]  # 使用自定义认证组件
    def get(self,request,*args,**kwargs):
        print(request.user)  # 认证组件返回的元组
        print(request.auth)  # 认证组件返回的元组
        ret = {'code':1000,'title':'微职位'}
        return Response(ret)









