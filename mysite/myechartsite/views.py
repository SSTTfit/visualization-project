#coding=utf-8
from django.shortcuts import render
import json
from django.shortcuts import redirect
from django.urls import reverse
import requests
import hashlib
import math
from django.http import HttpResponse,JsonResponse

# from django.template import loader
#from pyecharts import Line3D



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


def index(request):

    return render(request, "myechartsite/index.html")

def login(request):
    from myechartsite.forms import UserForm
    from myechartsite.models import User
    if request.session.get('is_login', None):
        return redirect(reverse('myechartsite:index'))
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
                    return redirect(reverse('myechartsite:index'))
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
        return redirect(reverse('myechartsite:index'))
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            level = register_form.cleaned_data['level']
            sex = register_form.cleaned_data['sex']
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
                new_user.sex = sex
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
        # 如果本来就未登录，也就没有登出一说
        return redirect(reverse('myechartsite:index'))
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect(reverse('myechartsite:index'))

def disewheather(request):
    # data = {
    #     "shenyan": [10, 20, 20, 15, 15, 20],
    #     "pgyan": [10, 15, 15, 39, 11, 10]
    # }
    s = authenticate()

    sql = "select disease from test "
    result = query(sql, s)
    s1 = result[0][0].split()
    s2 = result[1][0].split()
    data = {}
    data[s1[0]] = s1[1:]
    data[s2[0]] = s2[1:]
    return render(request, "myechartsite/disewheather.html", {'data': json.dumps(data)})


def radar(request):
    from myechartsite.models import Radar
    data_name = list(Radar.objects.values_list('name', flat=True))
    data_value = list(Radar.objects.values_list('qing', 'mai', 'wu', 'xue', 'yu', 'yin'))
    data={}
    for i,s in enumerate(data_name):
        data[s]=data_value[i]

    return render(request,"myechartsite/radar.html",{'data':json.dumps(data)})
    #return HttpResponse(json.dumps(data))

'''
def zhexiancheck(request):
    from myechartsite.models import Zhexiancheck
    ph = list(Zhexiancheck.objects.values_list('ph', flat=True))
    jigan = list(Zhexiancheck.objects.values_list('jigan', flat=True))
    niaobizhong = list(Zhexiancheck.objects.values_list('niaobizhong', flat=True))
    niaodanyuan = list(Zhexiancheck.objects.values_list('niaodanyuan', flat=True))
    weidanbai = list(Zhexiancheck.objects.values_list('weidanbai', flat=True))
    data = [ph,jigan,niaobizhong,niaodanyuan,weidanbai]
    return render(request, "myechartsite/zhexiancheck.html", {'data': json.dumps(data)})
'''
#未决定具体图类型
def diseindicator(request):
    data = {
        'indicator1':[1,2,3,1],
        'indicator2':[2,1,3,1],
        'indicator3':[4,1,3,3],
        'indicator4':[1,2,1,5]
    }              #key为不同指标，每个value值为数组，数组各项为不同疾病患者，在该项指标（key）异常的患者数量（看情况进行归一化）
    return render(request, "myechartsite/diseindicator.html", {'data': json.dumps(data)})

def inciratio1(request):
    data = {
        'disease1': [1, 2, 3, 1],
        'disease2': [2, 1, 3, 1],
        'disease3': [4, 1, 3, 3],
        'disease4': [1, 2, 1, 5]
    }             #key为不同疾病，每个value值为数组，数组各项为不同省份，key值对应疾病的发病率
    return render(request, "myechartsite/inciratio1.html", {'data': json.dumps(data)})

def inciratio2(request):
    data = {
        'disease1': [1, 2, 3, 1],
        'disease2': [2, 1, 3, 1],
        'disease3': [4, 1, 3, 3],
        'disease4': [1, 2, 1, 5]
    }             #key为不同疾病，每个value值为数组，数组各项为不同月份，key值对应疾病的发病率
    return render(request, "myechartsite/inciratio2.html", {'data': json.dumps(data)})

def userinfo(request):
    data = {
        'custome':['某某某',22,'男','河北省','ph 肌酐'],

    }
    return render(request, "myechartsite/yonghu.html", {'data': json.dumps(data)})

def indichange(request):
    data = {"name":["PH","肌酐","尿比重","尿胆原","微量蛋白"],
            "value":[[1.0, 0.9, 0.4, 0.6, 0.8, 1.03, 1.06, 0.4, 0.4, 0.5, 1.02, 1.0],[5.0, 5.9, 5.4, 6.6, 7.8, 8.5, 6.6, 7.2, 6.4, 5.5, 6.9, 8.0],[5.0, 15, 25, 16, 6, 18, 10, 22, 5.6, 15.5, 16.9, 18.0],[5.0, 0.5, 25, 6, 6, 8, 0.2, 2, 5.6, 5.5, 6.9, 8.0],[5.0, 10.5, 25, 36, 26, 18, 10, 20, 25.6, 25.5, 26.9, 28.0]]
            }
    return render(request, "myechartsite/indichange.html", {'data': json.dumps(data)})


def weather(request):
    data = {
        'time': 20181212,
        'weather':'晴',
        'AQI':150
    }
    return render(request, "myechartsite/weather.html", {'data': json.dumps(data)})
def medicalinfo(request):
    data = {
        'title':'全科医生新变化',
        'content':'新闻内容',
        'link':'https:www.baidu.com'
    }
    return render(request, "myechartsite/medicalinfo.html", {'data': json.dumps(data)})
def AQImap(request):
    data = {
        'year':[2016,2017,2018],
        'AQI':[100,200,150]
    }
    return render(request, "myechartsite/AQImap.html", {'data': json.dumps(data)})
def areadisease(requet):
    data = {'area':[
        {"value": 33988, "name": '北京'},
        {"value": 23017, "name": '天津'},
        {"value": 21013, "name": '河北'},
        {"value": 18650, "name": '山西'},
        {"value": 17820, "name": '内蒙古'}
    ]}
    return render(request, "myechartsite/areadisease.html", {'data': json.dumps(data)})

def diseasechange(request):
    data = {
        'year':[2012,2013,2014,2015],
        'rate':[15,25,22,36]
    }
    return render(request, "myechartsite/diseasechange.html", {'data': json.dumps(data)})

def diseaseage1(request):
    data = { 'years':[
        {"value":107820,"name":"0-1"},
        {"value": 33988, "name": "1-10"},
        {"value": 23017, "name": "11-20"},
        {"value": 21013, "name": "21-30"}
    ]}
    return render(request, "myechartsite/diseaseage1.html", {'data': json.dumps(data)})
def diseaseage2(request):
    data = {"years":["0-20","21-40"],
        "disease": [
        {"value": 107820, "name": "肾炎"},
        {"value": 33988, "name": "膀胱炎"},
        {"value": 23017, "name": "尿道炎"},
        {"value": 107820, "name": "肾炎"},
        {"value": 33988, "name": "膀胱炎"},
        {"value": 23017, "name": "尿道炎"},

    ]}
    return render(request, "myechartsite/diseaseage2.html", {'data': json.dumps(data)})

def checkinfo(request):
    data = {[

            ["PH", 0.2, "正常"],
            ["尿比重", 0.5, "偏低"],
            ["尿胆原", 0.01, "正常"],
            ["微量蛋白", 0.2, "偏高"],
            ["抗坏血酸", 0.4, "偏高"],
            ["肌酐", 0.7, "偏高"],
            ["蛋白质", 0.55, "正常"],
            ["钙", 0.4, "正常"]

    ]}
    return render(request, "myechartsite/checkinfo.html", {'data': json.dumps(data)})

def genderage(request):
    data = {
    "age":["0-1","1-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90+"],
	"male":[3.5,5.5,5.8,6.9,7.0,6.5,5.0,3.0,3.4,2.0,0.5],
	"female":[4.5,6.8,7.0,6.5,5.8,5.5,5.1,3.4,2.1,1.5,0.6]
}
    return render(request, "myechartsite/disemaleage1.html", {'data': json.dumps(data)})
def disegenderage(request):
    with open("json/disease.json", 'r') as json_data1:
        data1 = json.load(json_data1)
    with open("json/sexuality.json", 'r') as json_data2:
        data2 = json.load(json_data2)
    data=[data1,data2]
    return render(request, "myechartsite/disemaleage2.html", {'data': json.dumps(data)})

