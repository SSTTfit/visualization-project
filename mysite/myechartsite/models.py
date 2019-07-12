from django.db import models

# Create your models here.
# class Radar(models.Model):
#     name = models.CharField(max_length=50,default='')
#     qing = models.IntegerField()
#     mai = models.IntegerField()
#     wu = models.IntegerField()
#     xue = models.IntegerField()
#     yu = models.IntegerField()
#     yin = models.IntegerField()
#     def __unicode__(self):
#             return self.name

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    levelchoices = (
        ('customer', "个人用户"),
        ('doctor', "专科医生"),
        ('expert', "疾控专家"),
    )
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=128,choices=levelchoices,default="customer")
    location = models.CharField(max_length=128,default="北京")


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"



class Wheather(models.Model):
    location = models.CharField(max_length=256)
    tempnow = models.IntegerField()
    tempmin = models.IntegerField()
    tempmax = models.IntegerField()
    aqi = models.IntegerField()
    aqic = models.CharField(max_length=128)
    wheather = models.CharField(max_length=256)
    def __str__(self):
        return self.wheather



class Disewheather(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(default=2019)
    qing = models.FloatField()
    mai = models.FloatField()
    wu = models.FloatField()
    xue = models.FloatField()
    yu = models.FloatField()
    yin = models.FloatField()

    def __unicode__(self):
        return self.name


class Diseindicator(models.Model):
    name = models.CharField(max_length=128)
    sy = models.FloatField()
    pgy = models.FloatField()
    nsz = models.FloatField()
    tnb = models.FloatField()
    sjs = models.FloatField()
    hhd = models.FloatField()
    rsgxy = models.FloatField()

    def __unicode__(self):
        return self.name

class Diseage(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    age0_1 = models.IntegerField()
    age1_10 = models.IntegerField()
    age11_20 = models.IntegerField()
    age21_30 = models.IntegerField()
    age31_40 = models.IntegerField()
    age41_50 = models.IntegerField()
    age51_60 = models.IntegerField()
    age61_70 = models.IntegerField()
    def __unicode__(self):
        return self.name

class Disegenderage(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    sex = models.CharField(max_length=32, choices=gender)
    age0_1 = models.IntegerField()
    age1_10 = models.IntegerField()
    age10_20 = models.IntegerField()
    age20_30 = models.IntegerField()
    age30_40 = models.IntegerField()
    age40_50 = models.IntegerField()
    age50_60 = models.IntegerField()
    age60_70 = models.IntegerField()
    age70_80 = models.IntegerField()
    age80_90 = models.IntegerField()
    def __unicode__(self):
        return self.name


class Userindicator(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128,default='test')
    ph = models.FloatField()
    ph_c = models.CharField(max_length=128)
    nbz = models.FloatField()
    nbz_c = models.CharField(max_length=128)
    ndy = models.FloatField()
    ndy_c = models.CharField(max_length=128)
    wldb = models.FloatField()
    wldb_c = models.CharField(max_length=128)
    khxs = models.FloatField()
    khxs_c = models.CharField(max_length=128)
    jg = models.FloatField()
    jg_c = models.CharField(max_length=128)
    dbz = models.FloatField()
    dbz_c = models.CharField(max_length=128)
    g = models.FloatField()
    g_c = models.CharField(max_length=128)
    yxsy = models.FloatField()
    yxsy_c = models.CharField(max_length=128)
    qx = models.FloatField()
    qx_c = models.CharField(max_length=128)
    bxb = models.FloatField()
    bxb_c = models.CharField(max_length=128)
    dhs = models.FloatField()
    dhs_c = models.CharField(max_length=128)
    ptt = models.FloatField()
    ptt_c = models.CharField(max_length=128)
    tt = models.FloatField()
    tt_c = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name

class Inditrend(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)
    indi2008 = models.FloatField()
    indi2009 = models.FloatField()
    indi2010 = models.FloatField()
    indi2011 = models.FloatField()
    indi2012 = models.FloatField()
    indi2013 = models.FloatField()
    indi2014 = models.FloatField()
    indi2015 = models.FloatField()
    indi2016 = models.FloatField()
    indi2017 = models.FloatField()
    indi2018 = models.FloatField()
    indi2019 = models.FloatField()
    def __unicode__(self):
        return self.name

class Diseyear(models.Model):
    name = models.CharField(max_length=128)
    dise2008 = models.FloatField()
    dise2009 = models.FloatField()
    dise2010 = models.FloatField()
    dise2011 = models.FloatField()
    dise2012 = models.FloatField()
    dise2013 = models.FloatField()
    dise2014 = models.FloatField()
    dise2015 = models.FloatField()
    dise2016 = models.FloatField()
    dise2017 = models.FloatField()
    dise2018 = models.FloatField()
    dise2019 = models.FloatField()

    def __unicode__(self):
        return self.name

class Disetemp(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    temp20_15 = models.FloatField()
    temp15_10 = models.FloatField()
    temp10_5 = models.FloatField()
    temp5_0 = models.FloatField()
    temp0_5 = models.FloatField()
    temp5_10 = models.FloatField()
    temp10_15 = models.FloatField()
    temp15_20 = models.FloatField()
    temp20_25 = models.FloatField()
    temp25_30 = models.FloatField()
    temp30_35 = models.FloatField()
    temp35_40 = models.FloatField()
    def __unicode__(self):
        return self.name

class Disemonth(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    month1 = models.FloatField()
    month2 = models.FloatField()
    month3 = models.FloatField()
    month4 = models.FloatField()
    month5 = models.FloatField()
    month6 = models.FloatField()
    month7 = models.FloatField()
    month8 = models.FloatField()
    month9 = models.FloatField()
    month10 = models.FloatField()
    month11 = models.FloatField()
    month12 = models.FloatField()
    def __unicode__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=255,unique = True)
    introduction = models.CharField(max_length=512)
    content = models.TextField()
    imgurl = models.URLField()
    collector = models.ManyToManyField(User)
    pub_date = models.DateField(auto_now_add=True)
    aid = models.IntegerField(default=111)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-pub_date']
class Diseaqi(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    ratio = models.FloatField()
    pm2_5 = models.FloatField()
    pm10 = models.FloatField()
    NO2= models.FloatField()
    SO2= models.FloatField()
    O3= models.FloatField()
    CO= models.FloatField()
    def __unicode__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255,unique=True)
    province = models.ForeignKey(
        'Province',
        on_delete=models.CASCADE,
    )
    def __unicode__(self):
        return self.name

