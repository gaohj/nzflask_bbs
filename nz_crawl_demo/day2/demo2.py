from urllib import request
import json
headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
}
for i in range(10):
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start="+"%s" %(i*20)
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    content = response.read().decode()
    # print(content)
        #解析json
    # print(json.loads(content))
    data = json.loads(content)
    data_list = data.get('subjects')
    for movie in data_list:
        title = movie['title']
        url = movie['url']
        print(title,url)