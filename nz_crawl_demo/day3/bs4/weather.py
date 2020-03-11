import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
ALL_DATA = []
def parse_city(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Referer": "http: // www.weather.com.cn / textFC / hd.shtml"
    }
    res = requests.get(url,headers=headers)
    text =res.content.decode('utf-8')
    # pip install html5lib
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            # print(city)
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            # print(min_temp)
            # print(city_td,temp_td)
            ALL_DATA.append({"city":city,"min_temp":min_temp})
    # print(ALL_DATA)
    return ALL_DATA






def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]
    for url in urls:
        parse_city(url)

    #气温进行排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    data = ALL_DATA[0:10]
    cities = list(map(lambda x:x['city'],data))
    min_temp = list(map(lambda x:x['min_temp'],data))
    print(cities)
    print(min_temp)
    bar = Bar()
    bar.add_xaxis(cities)
    bar.add_yaxis("气温", min_temp)
    bar.render('temprature.html')

if __name__ == "__main__":
    main()
    # ALL_DATA = [
    #     {'city': '澳门', 'min_temp': '19'},
    #     {'city': '台北', 'min_temp': '15'},
    #     {'city': '高雄', 'min_temp': '20'},
    # ]
    # ALL_DATA.sort(key=lambda data:data['min_temp'])
    # print(ALL_DATA)