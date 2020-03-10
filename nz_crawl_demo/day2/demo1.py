from urllib import request
import re
headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
}

url = "https://search.51job.com/list/180200%252C190200%252C020000%252C040000%252C080200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

req = request.Request(url,headers=headers)

res = request.urlopen(req)


html = res.read().decode('gbk')

#处理数据
job_num_re = '<div class="rt">(.*?)</div>'
comp = re.compile(job_num_re,re.S)
jobnum_str = comp.findall(html)[0]
# print(jobnum_str) # 共14080条职位 及空格

#提取数字
num_re = ".*?(\d+).*?"
num = re.findall(num_re,jobnum_str)[0]
# print(int(num))


#获取第一个岗位名称
joblist_re = '<div class="el">(.*?)</div>'
joblist_str = re.findall(joblist_re,html,re.S)
# print(joblist_str[0])
# print(joblist_str[0])

# joblist_re1 = 'onmousedown="">(.*?)</a>'
# joblist_str1= re.findall(joblist_re1,joblist_str[0],re.S)
# print(joblist_str1)

for job in joblist_str:
    joblist_re1 = 'onmousedown="">(.*?)</a>'
    try:
        joblist_str1 = re.findall(joblist_re1,job,re.S)
        print("岗位名称:",joblist_str1[0].strip())
    except:
        pass