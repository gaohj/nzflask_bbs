from urllib import request
from urllib import parse
import json
headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
}

    # url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize="+"%d"+"&t=0.7576443766726075&keyWord=python" %( i*10)
url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"
for i in range(100):
    params = {
        't':"0.7576443766726075",
        'pageSize':i*10,
    }

    data = parse.urlencode(params).encode()
    req = request.Request(url=url,headers=headers,data=data,unverifiable=True)
    response = request.urlopen(req)
    content = response.read().decode()

    # print(content)
    data_dict = json.loads(content)

    joblist = data_dict['returnValue']['datas']
    for job in joblist:
        degree = job.get('degree')
        departmentName = job.get('departmentName')
        workExperience = job.get('workExperience')
        requirement = job.get('requirement')

        with open('ali.txt','a+',encoding='utf-8') as fp:
            fp.write(str((degree,departmentName,workExperience,requirement))+"\n")
            fp.flush() #不按下回车键也能写入数据