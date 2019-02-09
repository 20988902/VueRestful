from rest_framework import serializers
from app01 import models

class CourseSerializer(serializers.ModelSerializer):
    '''课程序列化'''
    class Meta:
        model = models.Course
        fields = '__all__'
        depth = 1  # 获取关联表的数据,数据量大


class CourseDetailSerializer(serializers.ModelSerializer):
    '''课程详情序列化'''
    title = serializers.CharField(source='course.title')  # 自定义字段。source表示获取数据库的字段(one2one, fk, choice)
    level = serializers.CharField(source='course.get_level_display')
    img = serializers.CharField(source='course.course_img')

    # many2many 多条数据
    recommends = serializers.SerializerMethodField()
    def get_recommends(self, obj):  # obj代指CourseDetail的对象
        queryset = obj.recommend_courses.all()
        return [{'id': row.id, 'title': row.title} for row in queryset]

    chapter = serializers.SerializerMethodField()
    def get_chapter(self, obj):
        queryset = obj.course.chapter_set.all()
        return [{'id': row.id, 'name': row.name} for row in queryset]

    class Meta:
        model = models.CourseDetail
        fields = ['course', 'title', 'level', 'img', 'recommends', 'slogon', 'why', 'chapter']





