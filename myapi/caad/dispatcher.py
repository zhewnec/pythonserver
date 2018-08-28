# _*_ coding:utf-8 _*_
import json
from search_for import sqlserver, test_sqlserver
from caad import handle
from django.http import HttpResponse

def dispathapi(request):
    "请求单据"
    body = json.loads(request.body)
    data, result, config = handle(body)
    # {"result": result, "config": config, "data": data}
    return HttpResponse(json.dumps({"result": result, "config": config}), content_type="application/json")


def search(request):
    """根据caseid 和 number查询数据"""
    caseid = request.GET.get("caseid")
    number = request.GET.get("caseid")
    sql = "select State, id,Number,CaseId,SysOrgName from EntrustInformation where  CaseId='%s' or number='%s';" % (caseid,number)
    result = test_sqlserver(sql)

    if result is "null":
        data = sqlserver(sql)
        if data is "null":
            return HttpResponse(json.dumps({"result": "查无数据"}), content_type="application/json")
        else:
            return HttpResponse(data+u"测试环境", content_type="application/json")
    else:
        return HttpResponse(result, content_type="application/json")
