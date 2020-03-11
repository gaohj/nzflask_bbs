import requests
from lxml import etree
BASE_DOMAIN = "https://www.dytt8.net"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Referer": "https://www.dytt8.net/"
}

#获取电影的详情信息
def parse_detail_info(url):
    movie = {}
    resp = requests.get(url,headers=headers,verify=True)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    movie['title'] = title
    Zoom = html.xpath("//div[@id='Zoom']")[0]
    imgs = Zoom.xpath(".//img/@src")
    try:
        cover = imgs[0]
        shoot = imgs[1]
        movie['cover'] = cover
        movie['shoot'] = shoot
    except:
        pass


    return movie

#获取每个电影的详情链接
def get_detail_urls(url):
    resp = requests.get(url,headers=headers,verify=False)
    text = resp.text #猜测 页面的编码 不管对不对 按照自己的方式解码
    #在这里只想要url 链接  所以不需要在 编码上下太多功夫
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = list(map(lambda url:BASE_DOMAIN+url,detail_urls))
    return detail_urls
    # def a(url):
    #     return BASE_DOMAIN+url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = a(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1

#获取每一页的 url链接
def spider():
    origin_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_{page}.html"
    movies  = []
    for x in range(1,9):
        url = origin_url.format(page=x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_info(detail_url)
            movies.append(movie)
    print(movies)


if __name__ == "__main__":
    spider()