from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app01 import models


class BackAuth(BaseAuthentication):
    ''' 自定义认证组件 '''
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserToken.objects.filter(token=token).first()
        if not obj:
            # 认证失败，抛异常
            raise AuthenticationFailed({'code':1001,'error':'认证失败'})
        return (obj.user.user, obj)  # 认证成功，返回元组