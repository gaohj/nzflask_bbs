from urllib import request

headers = {
    "User-Agent":"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Cookie":"anonymid=k7lk0d66y5mtud; depovince=NMG; jebecookies=15f53123-f0c7-4def-89b5-0fa3944825fb|||||; _r01_=1; ick_login=aec74675-5f38-424e-88ec-16d2089c5704; taihe_bi_sdk_uid=37f9cd36a45e1197451328e2b036a7d7; taihe_bi_sdk_session=043baa58c0f2f710027f7d1f89b9a438; _de=28A69782AB906D4A677B8FA35C706602; p=ea113d9ab092b22c38ed46c3931bf75b3; first_login_flag=1; ln_uact=gaohj5@163.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=975c7ed8c413cffa8ee74d1eb77016123; societyguester=975c7ed8c413cffa8ee74d1eb77016123; id=541197383; xnsid=3cb8e965; ver=7.0; loginfrom=null; JSESSIONID=abcXF-niHqo3jd54Xrddx; jebe_key=7ce76353-4541-48eb-bb60-d8d79054b7a0%7C67510b08b897c5e3b50e55d3a235a53c%7C1583824184828%7C1%7C1583824184050; jebe_key=7ce76353-4541-48eb-bb60-d8d79054b7a0%7C67510b08b897c5e3b50e55d3a235a53c%7C1583824184828%7C1%7C1583824184054; wp=1; wp_fold=1"
}


# request.urlretrieve('http://www.renren.com/541197383/profile','renren.html')
url = "http://www.renren.com/541197383/profile"
req = request.Request(url,headers=headers)
res = request.urlopen(req)

with open('renren1.html','w',encoding='utf-8') as fp:
    fp.write(res.read().decode('utf-8'))