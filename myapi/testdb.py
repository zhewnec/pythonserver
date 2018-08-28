# -*- coding: utf-8 -*-
from django.http import HttpResponse
from Model.models import Apiconfig


# 数据库操作
def testdb(request):
    list = Apiconfig.objects.all()
    print(list[0].name)
    # test1 = Test(name='runoob')
    # test1.save()
    return HttpResponse("<p>数据添加成功！</p>")