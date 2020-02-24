from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Teacher,Score,Course
from django.db.models import Avg,Count,Sum,F,Q
from django.db import connection
# Create your views here.
def index(request):
    students = Student.objects.annotate(score_avg=Avg('score__number')).filter(score_avg__gt=60).values('id','score_avg')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('查询平均成绩大于60分的同学的id和平均成绩')
def index2(request):
    #查询所有同学的id、姓名、选课的数量、总成绩；
    students = Student.objects.annotate(course_numbers=Count('score__id'),total=Sum('score__number')).values('id','name','course_numbers','total')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('查询所有同学的id、姓名、选课的数量、总成绩')

def index3(request):
    #select * from teacher where name like '李%'；
    count = Teacher.objects.filter(name__startswith='李').count()
    print(count)
    print(connection.queries)
    return HttpResponse('查询姓“李”的老师的个数')

#查询没学过“李老师”课的同学的id、姓名
def index4(request):
    #查询没学过“李老师”课的同学的id、姓名
    students = Student.objects.exclude(score__course__teacher__name='李老师').values('id','name')
    for student in students:
        print(student)
    print(connection.queries[-1])
    return HttpResponse('查询没学过“李老师”课的同学的id、姓名')

#查询学过课程id为1和2的所有同学的id、姓名 子查询
#先到score表中查出 course 为1 和2 的成绩  然后再到用户表中
def index5(request):
    students = Student.objects.filter(score__course__in=[1,2,3]).values('id','name').distinct()
    for student in students:
        print(student)
    print(connection.queries[-1])
    return HttpResponse('查询学过课程id为1和2的所有同学的id、姓名')

#查询学过“黄老师”所教的“所有课”的
#先找到每一位学生学习黄老师课程的数量 A
#在课程表中 找到黄老师教的课程的数量  B
#如果A等于B 那么意味着学生学习了黄老师所有课程
#否则 并没有学习全部
def index6(request):
    #A 1.统计学生选课的数量
    #A 2.找出课程老师是黄老师的数量
    #B Course.objects.filter(teacher__name=黄老师)
    students = Student.objects.annotate(nums=Count('score__course',filter=Q(score__course__teacher__name="黄老师"))).filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id','name')
    for student in students:
        print(student)
    print(connection.queries[-1])
    return HttpResponse('查询学过“黄老师”所教的“所有课”的同学的id、姓名')
