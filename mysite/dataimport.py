# import pymysql
#
# # 连接database
# conn = pymysql.connect(
#     host='localhost',
#     user ="root",
#     password ="password",
#     database ="myechartsite",
#     )
#
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
# # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# # 定义要执行的SQL语句
# sql = """
# INSET INTO myechartsite_disewheather (
# """
#
# # 执行SQL语句
# cursor.execute(sql)
#
# # 关闭光标对象
# cursor.close()
#
# # 关闭数据库连接
# conn.close()

# !/usr/bin/env python
import os
import django
import json
import  numpy as np
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django.setup()



def diseindicatorimport():
    from myechartsite.models import Diseindicator
    import numpy as np
    datalist = []
    data = np.random.uniform(0, 100, size=(7, 7))
    data = np.round(data,decimals=2)
    name = ['ndb','nph','jg','g','nbz','dhs','yxsy']
    for i,s in enumerate(name):
        a = Diseindicator(name=s,rsgxy=data[i][0],hhd=data[i][1],sy=data[i][2],nsz=data[i][3],pgy=data[i][4],sjs=data[i][5],tnb=data[i][6])
        datalist.append(a)
    Diseindicator.objects.bulk_create(datalist)

def disewheatherimport():
    from myechartsite.models import Disewheather
    datalist = []
    with open("./myechartsite/json/disewheather.json", "r") as f:
        data = json.load(f)
        for s in data['data']:
            a = Disewheather(name=s['name'], qing=s['qing'], mai=s['mai'], wu=s['wu'], xue=s['xue'], yu=s['yu'],
                             yin=s['yin'])
            datalist.append(a)
    Disewheather.objects.bulk_create(datalist)

def disewheatherimport2():
    from myechartsite.models import Disewheather
    import numpy as np
    np.set_printoptions(precision=2)
    name = ['nephritis','cystitis','urolithiasis','diabetes','urethritis','nuclearja','pregnancyhy']
    datalist = []

    yearlist=range(2019,2020)
    for j in yearlist:
        data = np.random.uniform(0, 50, size=(7, 6))
        for i,s in enumerate(data):
            s = np.around(s, decimals=2)
            a = Disewheather(name=name[i], year =j, qing=s[0], mai=s[1], wu=s[2], xue=s[3], yu=s[4],
                         yin=s[5])
            datalist.append(a)
    Disewheather.objects.bulk_create(datalist)

def pieimport():
    from myechartsite.models import Diseage
    datalist = []
    diselist = ["sy","sysy","pgy","ndy","ndjh","rxxhd"]
    year=range(2008,2020)
    with open("./myechartsite/json/dise_age.json", "rb") as f:
        s = json.load(f)
        s = s['data']
        for i,y in enumerate(year):
            for x in diselist:
                a = Diseage(name=x, year=year[i], age0_1=s[str(y)][x][0]['value'], age1_10=s[str(y)][x][1]['value'], age11_20=s[str(y)][x][2]['value'],age21_30=s[str(y)][x][3]['value'], age31_40=s[str(y)][x][4]['value'], age41_50=s[str(y)][x][5]['value'], age51_60=s[str(y)][x][6]['value'], age61_70=s[str(y)][x][7]['value'])
                datalist.append(a)
    Diseage.objects.bulk_create(datalist)

def sex_ageimport():
    from myechartsite.models import Disegenderage
    diselist = ["慢性/急性肾炎","膀胱炎","尿道结核","尿道炎","溶血性黄疸"]
    disemap = {"慢性/急性肾炎":"sy","膀胱炎":"pgy","尿道结核":"ndjh","尿道炎":"ndy","溶血性黄疸":"rxxhd"}
    year=[2019,2018,2017]
    datalist = []
    with open("./myechartsite/json/sexulity_age.json", "rb") as f:
        s = json.load(f)
        s = s['data']
        for x in diselist:
            for y in year:
                y = str(y)
                a = Disegenderage(name=disemap[x], year=y, sex='male',age0_1=s[x][y][0][0], age1_10=s[x][y][0][1], age10_20=s[x][y][0][2],age20_30=s[x][y][0][3], age30_40=s[x][y][0][4], age40_50=s[x][y][0][5], age50_60=s[x][y][0][6], age60_70=s[x][y][0][7], age70_80=s[x][y][0][8],age80_90=s[x][y][0][9])
                datalist.append(a)
                b = Disegenderage(name=disemap[x], year=y, sex='female',age0_1=s[x][y][1][0], age1_10=s[x][y][1][1], age10_20=s[x][y][1][2],age20_30=s[x][y][1][3], age30_40=s[x][y][1][4], age40_50=s[x][y][1][5], age50_60=s[x][y][1][6], age60_70=s[x][y][1][7], age70_80=s[x][y][1][8],age80_90=s[x][y][1][9])
                datalist.append(b)
    Disegenderage.objects.bulk_create(datalist)

def user_indiimport():
    from myechartsite.models import Userindicator
    from myechartsite.models import User
    namelist = ["series1","series2"]
    indilist = ["PH","尿比重","尿胆原","微量蛋白","抗坏血酸","肌酐","蛋白质","钙","亚硝酸盐","潜血","白细胞","胆红素","葡萄糖","酮体"]
    datalist = []
    username="用户"
    with open("./myechartsite/json/userdata.json", "rb") as f:
        s = json.load(f)
        b = User.objects.get(name=username)
        a = Userindicator(name=username, ph=s["series1"][0][1], ph_c=s["series1"][0][2],nbz=s["series1"][1][1],nbz_c=s["series1"][1][2],ndy=s["series1"][2][1],ndy_c=s["series1"][2][2],wldb=s["series1"][3][1],wldb_c=s["series1"][3][2],khxs=s["series1"][4][1],khxs_c=s["series1"][4][2],jg=s["series1"][5][1],jg_c=s["series1"][5][2],
                          dbz=s["series1"][6][1], dbz_c=s["series1"][6][2],g=s["series1"][7][1],g_c=s["series1"][7][2],yxsy=s["series2"][0][1],yxsy_c=s["series2"][0][2],qx=s["series2"][1][1],qx_c=s["series2"][1][2],
                          bxb=s["series2"][2][1], bxb_c=s["series2"][2][2],dhs=s["series2"][3][1],dhs_c=s["series2"][3][2],ptt=s["series2"][4][1],ptt_c=s["series2"][4][2],tt=s["series2"][5][1],tt_c=s["series2"][5][2])
        a.user=b
        datalist.append(a)
    Userindicator.objects.bulk_create(datalist)

def indi_trendimport():
    from myechartsite.models import Inditrend
    from myechartsite.models import User
    datalist = []
    username='用户'
    with open("./myechartsite/json/inditrend.json", "rb") as f:
        s = json.load(f)
        for i in range(len(s.keys())):
            b = User.objects.get(name=username)
            s2 = list(s.keys())[i]
            s1 = s[s2]
            a = Inditrend(name=list(s.keys())[i], indi2008=s1["value"][0], indi2009=s1["value"][1], indi2010=s1["value"][2], indi2011=s1["value"][3],
                          indi2012=s1["value"][4], indi2013=s1["value"][5], indi2014=s1["value"][6], indi2015=s1["value"][7], indi2016=s1["value"][8],
                          indi2017=s1["value"][9], indi2018=s1["value"][10], indi2019=s1["value"][11],)
            a.user = b
            datalist.append(a)
    Inditrend.objects.bulk_create(datalist)

def dise_yearimport():
    from myechartsite.models import Diseyear
    datalist = []
    with open("./myechartsite/json/dise_year.json", "rb") as f:
        s = json.load(f)
        for i in range(len(s.keys())):
            s2 = list(s.keys())[i]
            s1 = s[s2]
            a = Diseyear(name=list(s.keys())[i], dise2008=s1["value"][0], dise2009=s1["value"][1], dise2010=s1["value"][2], dise2011=s1["value"][3],
                          dise2012=s1["value"][4], dise2013=s1["value"][5], dise2014=s1["value"][6], dise2015=s1["value"][7], dise2016=s1["value"][8],
                          dise2017=s1["value"][9], dise2018=s1["value"][10], dise2019=s1["value"][11],)
            datalist.append(a)
    Diseyear.objects.bulk_create(datalist)

def dise_tempimport():
    from myechartsite.models import Disetemp
    import numpy as np
    datalist = []
    data = np.random.uniform(0, 100, size=(84, 12))
    data = np.round(data, decimals=2)
    name = ['rsgxy', 'hhd', 'sy', 'nsz', 'pgy', 'sjs', 'tnb']
    year = range(2008,2020)
    i=0
    for y in year:
        for s in name:
            a = Disetemp(name=s, year=y, temp20_15=data[i][0], temp15_10=data[i][1], temp10_5=data[i][2], temp5_0=data[i][3], temp0_5=data[i][4],
                         temp5_10=data[i][5], temp10_15=data[i][6], temp15_20=data[i][7], temp20_25=data[i][8], temp25_30=data[i][9],
                         temp30_35=data[i][10], temp35_40 = data[i][11])
            datalist.append(a)
            i+=1
    Disetemp.objects.bulk_create(datalist)

def dise_monthimport():
    from myechartsite.models import Disemonth
    import numpy as np
    datalist = []
    data = np.random.uniform(0, 100, size=(84, 12))
    data = np.round(data, decimals=2)
    name = ['rsgxy', 'hhd', 'sy', 'nsz', 'pgy', 'sjs', 'tnb']
    year = range(2008,2020)
    i=0
    for y in year:
        for s in name:
            a = Disemonth(name=s, year=y, month1=data[i][0], month2=data[i][1], month3=data[i][2], month4=data[i][3], month5=data[i][4],
                         month6=data[i][5], month7=data[i][6], month8=data[i][7], month9=data[i][8], month10=data[i][9],
                         month11=data[i][10], month12 = data[i][11])
            datalist.append(a)
            i+=1
    Disemonth.objects.bulk_create(datalist)

def wheatherimport():
    from myechartsite.models import Wheather
    wheatherc = ['雨', '多云闪电', '雪', '晴', '多云', '多风']
    locationlist = ['北京','天津','西安','广州']
    datalist=[]
    for x in locationlist:
        data = {}

        tempd = np.random.randint(10, 30, 2)
        t2 = np.max(tempd)
        t1 = np.min(tempd)
        # wheather = {'雨': 'rain', '多云闪电': 'cloud-lightning', '雪': 'snow', '晴': 'sun', '多云': 'cloud', '多风': 'wind'}
        # rootpath = "../../static/myechartsite/img/wheatherimg/"
        # if t1 != t2:
        #     #     data['temp'] = np.random.randint(t1, t2, size=1)[0]
        #     # else:
        #     #     data['temp'] = t1
        data['tempmin'] = t1
        if t1 == t2:
            t2 = t1+5
        data['tempmax'] = t2
        data['tempnow'] = np.random.randint(t1, t2, size=1)[0]
        data['aqi'] = np.random.randint(50, 200, size=1)[0]
        if data['aqi'] > 100:
            data['aqic'] = "差"
        else:
            data['aqic'] = "优"
        data['wheather'] = random.choice(wheatherc)
        print(data)
        # data['imgurl'] = rootpath + wheather[data['weather']] + ".png"
        a = Wheather(location=x, tempnow=data['tempnow'], tempmin=data['tempmin'], tempmax=data['tempmax'],
                         aqi=data['aqi'], aqic=data['aqic'], wheather=data['wheather'], )
        datalist.append(a)
    Wheather.objects.bulk_create(datalist)

def articleimport():
    from myechartsite.models import Article
    import chardet
    datalist = []
    rootpath="./myechartsite/json/articles/"
    article = Article.objects.get(id=4)
    print(article.imgurl)
    # for x in articles:
    #     print(x.id)
    # for x in os.listdir(rootpath):
    #     with open(os.path.join(rootpath,x), "rb") as f:
    #         txt = f.read()
    #         type = chardet.detect(txt)
    #         s = txt.decode(type['encoding'],errors='ignore').splitlines()
    #         title=str(s[0])
    #         imgurl = str(s[1])
    #         introduction = str(s[2])
    #         content = "".join(s[3:])
    #         a = Article(title=title, content=content,introduction=introduction,imgurl=imgurl)
    #         print(title)
    #         print(introduction)
    #         print(content)
    #         datalist.append(a)
    # Article.objects.bulk_create(datalist)

def diseaqiimport():
    from myechartsite.models import Diseaqi
    timeline= [
        2019,
        2018,
        2017,
        2016,
        2015,
        2014
    ]
    disease = ["慢性/急性肾炎","膀胱炎","尿道结核","尿道炎","溶血性黄疸"]
    pollution=["PM2.5","PM10","NO2","SO2","O3","CO" ]
    datalist = []
    with open("./myechartsite/json/disease_pollution.json", "rb") as f:
        s = json.load(f)
        s = s['data']
        for x in disease:
            for i in range(len(timeline)):

                a = Diseaqi(name=x, year=timeline[i], ratio=s[x][i][0], pm2_5=s[x][i][1],
                                  pm10=s[x][i][2], NO2=s[x][i][3], SO2=s[x][i][4],
                                        O3 =s[x][i][5], CO=s[x][i][6])
                datalist.append(a)
    Diseaqi.objects.bulk_create(datalist)

def provinceimport():
    from myechartsite.models import Province
    datalist = []
    with open("./myechartsite/json/hospital-map-data.json", "rb") as f:
        s = json.load(f)
        for x in s['province']:
            a = Province(name=x)
            datalist.append(a)
        Province.objects.bulk_create(datalist)

def cityimport():
    from myechartsite.models import Province
    from myechartsite.models import City
    datalist = []
    with open("./myechartsite/json/hospital-map-data.json", "rb") as f:
        s = json.load(f)
        s=s['city']
        for b in Province.objects.all():
            for x in s[b.name]:
                a = City(name=x)
                a.province = b
                datalist.append(a)
        City.objects.bulk_create(datalist)

def modeltest():
    from myechartsite.models import User
    username="闫海"
    if User.objects.get(id=1).name != username:
        same_name_user = User.objects.filter(name=username)
        if same_name_user:  # 用户名唯一
            message = '用户已经存在，请重新选择用户名！'
            print(message,User.objects.get(id=1).name)
if __name__ == "__main__":
    user_indiimport()
    print('Done!')
