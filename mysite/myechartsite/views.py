#coding=utf-8
from django.shortcuts import render
import json
from django.shortcuts import redirect
from django.urls import reverse
import requests
import hashlib
import math
from django.http import HttpResponse,JsonResponse
import numpy as np
import random
# from django.template import loader
#from pyecharts import Line3D


def rdwheatherdata(x):
    from myechartsite.models import Wheather
    wheathermap = {'雨': 'rain', '多云闪电': 'cloud-lightning', '雪': 'snow', '晴': 'sun', '多云': 'cloud', '多风': 'wind'}
    rootpath = "/static/myechartsite/img/wheatherimg/"
    try:
        a = list(Wheather.objects.filter(location=x).values_list('tempmin', 'tempmax', 'tempnow', 'aqi', 'aqic', 'wheather'))[0]
    except:
        a = list(Wheather.objects.filter(location="北京").values_list('tempmin', 'tempmax', 'tempnow', 'aqi', 'aqic', 'wheather'))[0]
    data={'location': x, 'tempnow': a[2], 'aqi': a[3], 'aqic': a[4], 'wheather': a[5]}
    data['tempd'] = str(a[0])+'-'+str(a[1])
    data['imgurl'] = rootpath + wheathermap[data['wheather']] + ".png"
    return data

def authenticate():
    """
    authenticate user
    :return: session
    """
    url = 'http://10.112.226.2:7070/kylin/api/user/authentication'
    headers = {'Authorization': 'Basic QURNSU46S1lMSU4='}
    s = requests.session()
    s.headers.update({'Content-Type': 'application/json'})
    s.post(url, headers=headers)
    return s


def query(sql_str, session):
    """
    sql query
    :param sql_str: string of sql
    :param session: session object
    :return: results(type is list)
    """
    url = 'http://10.112.226.2:7070/kylin/api/query'
    json_str = '{"sql":"' + sql_str + '", "offset": 0, "limit": 50000, ' \
                                      '"acceptPartial": false, "project": "test"}'
    r = session.post(url, data=json_str)
    results1 = r.json()
    return results1['results']


def index_customer(request):
    from myechartsite.models import Article
    from myechartsite.pager import Pagination
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='customer':
        winfo = rdwheatherdata(request.session['location'])
        current_page = request.GET.get("page")
        record_count = Article.objects.all().count()
        page_record_limit = 4
        page_count_limit = 9
        page_obj = Pagination(current_page=current_page, record_count=record_count,
                              page_record_limit=page_record_limit, page_count_limit=page_count_limit)
        articles = Article.objects.all()[page_obj.start:page_obj.end]
        return render(request, "myechartsite/index_customer.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))


def search(request):
    from myechartsite.models import Article
    from myechartsite.pager import Pagination
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='customer':
        winfo = rdwheatherdata(request.session['location'])
    message = ""
    searchtitle = request.GET.get('searchtitle')
    if not searchtitle:
        message = "请填写搜索内容！"
    elif Article.objects.filter(title__icontains=searchtitle):
        # articles = Article.objects.filter(title__icontains=searchtitle)

        current_page = request.GET.get("page")
        record_count = Article.objects.filter(title__icontains=searchtitle).count()
        page_record_limit = 4
        page_count_limit = 9
        page_obj = Pagination(current_page=current_page, record_count=record_count,
                              page_record_limit=page_record_limit, page_count_limit=page_count_limit,searchtitle=searchtitle)
        articles = Article.objects.filter(title__icontains=searchtitle)[page_obj.start:page_obj.end]
    else:
        message = "查找的标题不存在！"

    return render(request, "myechartsite/article_index.html", locals())

def article(request,id):
    from myechartsite.models import Article
    from myechartsite.models import User
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='customer':
        winfo = rdwheatherdata(request.session['location'])
        article = Article.objects.get(id=id)
        user = User.objects.get(id=request.session['user_id'])
        article_id=id
        articleurl='myechartsite/articles/'+str(article.aid)+'.html'
        if request.GET.get('changecollected'):
            if user.article_set.filter(id=article_id):
                article.collecter.remove(user)
            else:
                article.collecter.add(user)
        collected = 0
        if user.article_set.filter(id=id):
            collected = 1
        return render(request, "myechartsite/article_detail.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))

def changece(request):
    from myechartsite.models import Article
    from myechartsite.models import User
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if not request.session.get('level', None) == 'customer':
        return redirect(reverse('myechartsite:firstindex'))
    if request.GET.get('changecollected'):
        article = Article.objects.get(id=request.GET.get('article_id'))
        user = User.objects.get(id=request.session['user_id'])
        if user.article_set.filter(id=request.GET.get('article_id')):
            article.collector.remove(user)
            data = "取消收藏"
        else:
            article.collector.add(user)
            data = "已收藏"
    return HttpResponse(data)

def index_expert(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/index_expert.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))
def index_doctor(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='doctor':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/index_doctor.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))

def login(request):
    from myechartsite.forms import UserForm
    from myechartsite.models import User
    if request.session.get('is_login', None):
        jpmap={
            'expert':'myechartsite:index_expert',
            'doctor':'myechartsite:index_doctor'
        }
        jp2=jpmap.get(request.session.get('level', None),'myechartsite:index_customer')
        return redirect(reverse(jp2))
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['level'] = user.level
                    request.session['location'] = user.location
                    return redirect(reverse('myechartsite:index_'+user.level))
                else:
                    message = "密码不正确！"
            except:
                message = ["用户名不存在！",username]
        return render(request, 'myechartsite/login.html', locals())
    login_form = UserForm()
    return render(request, 'myechartsite/login.html', locals())

def register(request):
    from myechartsite.forms import RegisterForm
    from myechartsite.models import User

    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect(reverse('myechartsite:login'))
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            level = register_form.cleaned_data['level']
            location = register_form.cleaned_data['location']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'myechartsite/register.html', locals())
            else:
                same_name_user =User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'myechartsite/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'myechartsite/register.html', locals())


                    # 当一切都OK的情况下，创建新用户

                new_user = User()
                new_user.name = username
                new_user.level = level
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.location = location
                new_user.save()

                return redirect(reverse('myechartsite:login'))  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'myechartsite/register.html', locals())

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

def logout(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    request.session.flush()
    return redirect(reverse('myechartsite:login'))

def changeinfo(request):
    from myechartsite.forms import ChangeForm
    from myechartsite.models import User
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.method == "POST":
        register_form =ChangeForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            email = register_form.cleaned_data['email']
            location = register_form.cleaned_data['location']


            if User.objects.get(id=request.session['user_id']).name!=username:
                same_name_user =User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'myechartsite/changeinfo.html',locals())
            if User.objects.get(id=request.session['user_id']).email != email:
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'myechartsite/changeinfo.html', locals())

            old_user = User.objects.get(id=request.session['user_id'])
            old_user.name = username
            old_user.password1 = hash_code(password1)
            old_user.location = location
            old_user.email = email
            old_user.save()
            request.session['user_name'] = username
            request.session['location'] = location
            return redirect(reverse('myechartsite:login'))  # 自动跳转到登录页面
    register_form = ChangeForm()
    winfo = rdwheatherdata(request.session['location'])
    return render(request, "myechartsite/changeinfo.html", locals())

def firstindex(request):
    onlinepeople = 900
    return render(request,'myechartsite/firstindex.html',locals())

def diseage(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None) == 'expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/diseage.html", locals())
    else:
        return redirect(reverse('myechartsite:firstindex'))
def diseage_data(request):
    from myechartsite.models import Diseage
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    data_all = {}
    data_year = range(2008, 2020)
    ynamelist = ['0-1', '1-10', '11-20', '21-30', '31-40', '41-50','51-60','61-70']
    for year in data_year:
        data_name = list(Diseage.objects.filter(year=str(year)).values_list('name', flat=True))
        data_value = list(
            Diseage.objects.filter(year=str(year)).values_list('age0_1', 'age1_10', 'age11_20', 'age21_30', 'age31_40', 'age41_50','age51_60','age61_70'))
        data = {}
        for i, s in enumerate(data_value):
            data1 = [{"value": s[j], "name": ynamelist[j]} for j in range(len(s))]
            data[data_name[i]] = data1
        data_all[str(year)] = data
    return JsonResponse(data_all)

def disewheather(request):
    # from myechartsite.models import Disewheather
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    # data_name = list(Disewheather.objects.values_list('name', flat=True))
    # data_value = list(Disewheather.objects.values_list('qing', 'mai', 'wu', 'xue', 'yu', 'yin'))
    # data = {}
    # for i, s in enumerate(data_name):
    #     data[s] = data_value[i]
    # s = authenticate()
    #
    # sql = "select disease from test "
    # result = query(sql, s)
    # s1 = result[0][0].split()
    # s2 = result[1][0].split()
    # data = {}
    # data[s1[0]] = s1[1:]
    # data[s2[0]] = s2[1:]
    if request.session.get('level', None) == 'expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/disewheather.html", locals())
    else:
        return redirect(reverse('myechartsite:firstindex'))

def disewheather_data(request):
    from myechartsite.models import Disewheather
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    data_all = {}
    data_year = range(2008,2020)
    for year in data_year:
        data_name = list(Disewheather.objects.filter(year=str(year)).values_list('name', flat=True))
        data_value = list(Disewheather.objects.filter(year=str(year)).values_list('qing', 'mai', 'wu', 'xue', 'yu', 'yin'))
        data = {}
        for i, s in enumerate(data_name):
            data[s] = data_value[i]
        data_all[str(year)] = data
    return JsonResponse(data_all)

def diseindicator(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    winfo = rdwheatherdata(request.session['location'])
    return render(request, "myechartsite/diseindicator.html", locals())

def diseindicator_data(request):
    from myechartsite.models import Diseindicator
    namelist=list(Diseindicator.objects.values_list('name'))[1]
    a = list(Diseindicator.objects.values_list('name','rsgxy','hhd','sy','nsz','pgy','sjs','tnb'))
    data={}
    for i,s in enumerate(a):
        data[s[0]]=s[1:]
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def disetemp(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None) == 'expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, 'myechartsite/disetemper.html', locals())
    else:
        return redirect(reverse('myechartsite:firstindex'))

def disetemp_data(request):
    from myechartsite.models import Disetemp
    data_all = {}
    data_year = range(2008, 2020)
    for year in data_year:
        data_name = list(Disetemp.objects.filter(year=str(year)).values_list('name', flat=True))
        data_value = list(
            Disetemp.objects.filter(year=str(year)).values_list('temp20_15', 'temp15_10', 'temp10_5', 'temp5_0', 'temp0_5',
                         'temp5_10', 'temp10_15', 'temp15_20', 'temp20_25', 'temp25_30',
                         'temp30_35', 'temp35_40'))
        data = {}
        for i, s in enumerate(data_name):
            data[s] = data_value[i]
        data_all[str(year)] = data
    return JsonResponse(data_all)

def disemonth(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    winfo = rdwheatherdata(request.session['location'])
    return render(request, "myechartsite/disemonth.html", locals())
def disemonth_data(request):
    from myechartsite.models import Disemonth
    data_all = {}
    data_year = range(2008, 2020)
    for year in data_year:
        data_name = list(Disemonth.objects.filter(year=str(year)).values_list('name', flat=True))
        data_value = list(
            Disemonth.objects.filter(year=str(year)).values_list('month1', 'month2', 'month3', 'month4', 'month5',
                         'month6', 'month7', 'month8', 'month9', 'month10','month11', 'month12'))
        data = {}
        for i, s in enumerate(data_name):
            data[s] = data_value[i]
        data_all[str(year)] = data
    return JsonResponse(data_all)

def inditrend(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    winfo = rdwheatherdata(request.session['location'])
    return render(request, "myechartsite/inditrend.html", locals())

def inditrend_data(request):
    from myechartsite.models import Inditrend
    data={}
    data_name = list(Inditrend.objects.values_list('name', flat=True))
    name_map={"tt":"酮体","yxsy":"亚硝酸盐","ptt":"葡萄糖","dhs":"胆红素","g":"钙","zhibiao1":"指标1","zhibiao2":"指标2","zhibiao3":"指标3"}
    for x in data_name:
        data_value = list(Inditrend.objects.filter(name=x).values_list('indi2008', 'indi2009', 'indi2010','indi2011', 'indi2012', 'indi2013', 'indi2014',
                                           'indi2015','indi2016','indi2017', 'indi2018' ,'indi2019'))
        data1 = {"value": data_value[0], "name": [name_map[x]]}
        data[x]=data1
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def diseyear(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    winfo = rdwheatherdata(request.session['location'])
    return render(request, "myechartsite/diseyear.html", locals())

def diseyear_data(request):
    from myechartsite.models import Diseyear
    data={}
    data_name = list(Diseyear.objects.values_list('name', flat=True))
    name_map={"rxxhd":"溶血性黄疸","sy":"急慢性肾炎","sysy":"肾盂肾炎","pgy":"膀胱炎","ndy":"尿道炎","ndjs":"尿道结石","jibing1":"疾病1","jibing2":"疾病2"}
    for x in data_name:
        data_value = list(Diseyear.objects.filter(name=x).values_list('dise2008', 'dise2009', 'dise2010','dise2011', 'dise2012', 'dise2013', 'dise2014',
                                           'dise2015','dise2016','dise2017', 'dise2018' ,'dise2019'))
        data1 = {"value": data_value[0], "name": [name_map[x]]}
        data[x]=data1

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def disegender(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/disegender.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))

def disegenderage_data(requset):
    from myechartsite.models import Disegenderage
    datause = {"disease": ["慢性/急性肾炎", "膀胱炎", "尿道结核", "尿道炎", "溶血性黄疸"],
    "age": ["0-1", "1-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90"],
    "time": [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010]}
    disemap = {"慢性/急性肾炎":"sy","膀胱炎":"pgy","尿道结核":"ndjh","尿道炎":"ndy","溶血性黄疸":"rxxhd"}
    data_year = [2019, 2018, 2017]

    data1 = {}
    for x in datause["disease"]:
        data = {}
        for y in data_year:
            data_value1 =list(
                Disegenderage.objects.filter(name=disemap[x],year=str(y),sex='male').values_list('age0_1','age1_10','age10_20','age20_30','age30_40','age40_50','age50_60','age60_70','age70_80','age80_90'))
            data_value2 = list(
                Disegenderage.objects.filter(name=disemap[x],year=str(y),sex='female').values_list('age0_1','age1_10','age10_20','age20_30','age30_40','age40_50','age50_60','age60_70','age70_80','age80_90'))

            data[str(y)]=[data_value1[0],data_value2[0]]
        data1[x] = data
    datause['data'] = data1

    return JsonResponse(datause,json_dumps_params={'ensure_ascii':False})

def userindi(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='customer':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/userindi.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))

def userindi_data(request):
    from myechartsite.models import Userindicator
    data={}
    series=["series1","series2"]
    indilist1 = ["PH", "尿比重", "尿胆原", "微量蛋白", "抗坏血酸", "肌酐", "蛋白质", "钙",]
    indilist2 = ["亚硝酸盐", "潜血", "白细胞", "胆红素", "葡萄糖", "酮体"]
    a1 = list(Userindicator.objects.values_list('ph','nbz', 'ndy', 'wldb', 'khxs', 'jg', 'dbz','g'))[0]
    b1 = list(Userindicator.objects.values_list('ph_c', 'nbz_c', 'ndy_c', 'wldb_c', 'khxs_c', 'jg_c', 'dbz_c', 'g_c'))[0]
    data[series[0]] = [[indilist1[i],a1[i],b1[i]] for i in range(len(a1))]
    a2 = list(Userindicator.objects.values_list('yxsy', 'qx', 'bxb', 'dhs', 'ptt', 'tt'))
    b2 = list(
        Userindicator.objects.values_list('yxsy_c', 'qx_c', 'bxb_c', 'dhs_c', 'ptt_c', 'tt_c'))
    data[series[1]]= [[indilist2[i], a2[0][i], b2[0][i]] for i in range(len(a2[0]))]
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def diseaqi(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/diseaqi.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))
def diseaqi_data(request):
    from myechartsite.models import Diseaqi
    data = {}
    data1 = {}
    timeline = [
        2019,
        2018,
        2017,
        2016,
        2015,
        2014
    ]
    disease = ["慢性/急性肾炎", "膀胱炎", "尿道结核", "尿道炎", "溶血性黄疸"]
    pollution = ["PM2.5", "PM10", "NO2", "SO2", "O3", "CO"]
    data['timeline'] = timeline
    data['disease'] = disease
    data['pollution'] = pollution
    for x in disease:
        a1 = list(Diseaqi.objects.filter(name=x).values_list('ratio','pm2_5','pm10','NO2','SO2','O3','CO','year'))
        data1[x]=a1
    data['data'] = data1
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def arearatiomap(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/arearatiomap.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))

def arearatiomap_data(request):
    data = {
  "disease": [["慢性/急性肾炎","nephritis"],["膀胱炎","cystitis"],["溶血性黄疸","jaundice"]],
  "time": [2018,2017,2016]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

def arearatiochange(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='expert':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/arearatiochange.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))


def article_collected(request):
    from myechartsite.models import Article
    from myechartsite.models import User
    from myechartsite.pager import Pagination
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None) == 'customer':
        winfo = rdwheatherdata(request.session['location'])
    current_page = request.GET.get("page")
    record_count = Article.objects.all().count()
    page_record_limit = 5
    page_count_limit = 9
    page_obj = Pagination(current_page=current_page,record_count=record_count,
                            page_record_limit=page_record_limit,page_count_limit=page_count_limit)
    user = User.objects.get(id=request.session['user_id'])
    articles = user.article_set.all()[page_obj.start:page_obj.end]
    return render(request, 'myechartsite/article_collected.html', locals())

def hospitalmap(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('myechartsite:login'))
    if request.session.get('level', None)=='customer':
        winfo = rdwheatherdata(request.session['location'])
        return render(request, "myechartsite/hospitalmap.html", locals())
    else:
        return redirect(reverse('myechartsite:login'))

def hospitalmap_data(request):
    from myechartsite.models import Province
    data={}
    s={}
    data["level"]= ["一丙", "一乙", "一甲", "二丙", "二乙", "二甲", "三丙", "三乙", "三甲"]
    data["features"]=["呼吸内科","消化内科","神经内科","心血管内科","肾内科","血液内科","免疫科","内分泌科","肿瘤内科","五官科","妇科"]
    data["province"] = [x.name for x in Province.objects.all()]
    for p in Province.objects.all():
        s[p.name] =[x.name for x in p.city_set.all()]
    data['city'] = s
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})