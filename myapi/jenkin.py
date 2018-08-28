# _*_ coding:utf-8 _*_

def all(server):
    jobs = []
    for i in server.get_all_jobs():
        jobs.append(i["name"].encode('utf-8'))
    return jobs