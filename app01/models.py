from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=64, verbose_name='课程名称')
    course_img = models.ImageField(upload_to='image',verbose_name='课程图片')
    level_choices = (
        (1,'初级'),
        (2,'中级'),
        (3,'高级'),
    )
    level = models.IntegerField(choices=level_choices,verbose_name='难易程度')

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    course = models.OneToOneField(to='Course')
    slogon = models.CharField(max_length=255,verbose_name='口号')
    why = models.CharField(max_length=255,verbose_name='学习原因')
    recommend_courses = models.ManyToManyField(to='Course',related_name='rc',verbose_name='推荐课程')

    def __str__(self):
        return "课程详细:"+self.course.title


class Chapter(models.Model):
    num = models.IntegerField(verbose_name='章节')
    name = models.CharField(max_length=32, verbose_name='章节名称')
    course = models.ForeignKey(to='Course',verbose_name='所属课程')

    def __str__(self):
        return self.name




