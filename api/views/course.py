from rest_framework import views
from rest_framework.response import Response
from app01 import models
from api.serializers.course import CourseSerializer,CourseDetailSerializer

# 方式一：
class CourseView(views.APIView):
    def get(self, requeest, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


##############################################
# 方式二：
from rest_framework.viewsets import GenericViewSet, ViewSetMixin


class CourseView(ViewSetMixin, views.APIView):  # 继承ViewSetMixin类，as_view()才能加参数
    def list(self, request, *args, **kwargs):
        '''
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)  # 序列化获取的数据
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        '''
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = models.CourseDetail.objects.filter(course__id=pk).first()
            print(obj)
            ser = CourseDetailSerializer(instance=obj)  # 单条数据
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)
