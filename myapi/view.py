# _*_ coding:utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render
import json
import MySQLdb
import jenkins



def index(request):
    context = {}
    context['hello'] = 'Welcome Test Report!'
    return render(request, 'index.html', context)



def soanr(request):
    path = "D:\python\demo\PythonServer\static\output.txt"
    text = open(path, "a")
    text.write(request.body)
    return HttpResponse("hello")


def jenkinsapi(request):
    # jenkins 调用
    job_name = request.GET.get("name")
    url = 'http://172.16.2.83:8080'
    username = 'caad'
    token = '03b6f6e3ef321d15b3f85eb626791e38'
    # job_name = "api"
    # 实例化 jenkins
    server = jenkins.Jenkins(url, username, token)
    jobs = []
    for i in server.get_all_jobs():
        jobs.append(i["name"].encode('utf-8'))
    if job_name in jobs:
        # 构建项目
        json.dumps(server.build_job(job_name))
        # time.sleep(5)
        # 获取任务最后的构建号
        build_number = server.get_job_info(job_name)['lastBuild']['number']
        # 是否构建中
        result = server.get_build_info(job_name, build_number)['building']
        return HttpResponse(result, content_type="application/json")
    else:
        result = "请检查job名称是否正确：" + str(jobs)
        return HttpResponse(result, content_type="application/json")


# Create your views here.
def report(reques):
    return render(reques, "test.html")


# def dispathapi(request):
#
#     body = json.loads(request.body)
#     data, result, config = handle(body)
#     return HttpResponse(json.dumps({"data": data, "config": config, "result": result}), content_type="application/json")
#

def db(sql):
    # 打开数据库连接
    dbs = MySQLdb.connect("172.16.2.154", "sonar", "9s5Jld719k46z09b", "test_case", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = dbs.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    dbs.commit()
    # 使用 fetchone() 方法获取一条数据
    # data = cursor.fetchone()
    # 关闭数据库连接
    dbs.close()
    return data





def CheckReport(reques):
    """这个是自检报告"""
    return render(reques, "CheckReport.html")


def FormalReport(reques):
    # 这个是api正式环境测试报告
    return render(reques, "FormalReport.html")


def TestrePort(reques):
    # 这个是api测试环境测试报告"""
    return render(reques, "TestrePort.html")


def page_not_found(request):
    return render(request, '404.html')
