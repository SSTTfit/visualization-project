from django.db import models

# Create your models here.
class Radar(models.Model):
    name = models.CharField(max_length=50,default='')
    qing = models.IntegerField()
    mai = models.IntegerField()
    wu = models.IntegerField()
    xue = models.IntegerField()
    yu = models.IntegerField()
    yin = models.IntegerField()
    def __unicode__(self):
            return self.name

class User(models.Model):
    cus_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    abindicator = models.CharField(max_length=100)
    def __unicode__(self):
            return self.name

class inciratio1(models.Model):
    disease = models.CharField(max_length=50)
    beijing = models.FloatField()
    tianjing = models.FloatField()
    shanghai = models.FloatField()
    hebei = models.FloatField()
    hubei = models.FloatField()
    def __unicode__(self):
            return self.name

class inciratio2(models.Model):
    disease = models.CharField(max_length=50)
    jan = models.FloatField()
    feb = models.FloatField()
    mar = models.FloatField()
    apr = models.FloatField()
    jun = models.FloatField()
    jul = models.FloatField()
    aug = models.FloatField()
    sep = models.FloatField()
    oct = models.FloatField()
    nov = models.FloatField()
    dec = models.FloatField()
    def __unicode__(self):
            return self.name

class record_ph(models.Model):
    cus_id = models.IntegerField(unique=True)
    ph2007 = models.FloatField()
    ph2008 = models.FloatField()
    ph2009 = models.FloatField()
    ph2010 = models.FloatField()
    ph2011 = models.FloatField()
    ph2012 = models.FloatField()
    ph2013 = models.FloatField()
    ph2014 = models.FloatField()
    ph2015 = models.FloatField()
    ph2016 = models.FloatField()
    ph2017 = models.FloatField()
    ph2018 = models.FloatField()
    phcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_nitrite(models.Model):
    cus_id = models.IntegerField(unique=True)
    nitrite2007 = models.FloatField()
    nitrite2008 = models.FloatField()
    nitrite2009 = models.FloatField()
    nitrite2010 = models.FloatField()
    nitrite2011 = models.FloatField()
    nitrite2012 = models.FloatField()
    nitrite2013 = models.FloatField()
    nitrite2014 = models.FloatField()
    nitrite2015 = models.FloatField()
    nitrite2016 = models.FloatField()
    nitrite2017 = models.FloatField()
    nitrite2018 = models.FloatField()
    nitritecondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_usg(models.Model):
    cus_id = models.IntegerField(unique=True)
    usg2007 = models.FloatField()
    usg2008 = models.FloatField()
    usg2009 = models.FloatField()
    usg2010 = models.FloatField()
    usg2011 = models.FloatField()
    usg2012 = models.FloatField()
    usg2013 = models.FloatField()
    usg2014 = models.FloatField()
    usg2015 = models.FloatField()
    usg2016 = models.FloatField()
    usg2017 = models.FloatField()
    usg2018 = models.FloatField()
    usgcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_ubp(models.Model):
    cus_id = models.IntegerField(unique=True)
    ubp2007 = models.FloatField()
    ubp2008 = models.FloatField()
    ubp2009 = models.FloatField()
    ubp2010 = models.FloatField()
    ubp2011 = models.FloatField()
    ubp2012 = models.FloatField()
    ubp2013 = models.FloatField()
    ubp2014 = models.FloatField()
    ubp2015 = models.FloatField()
    ubp2016 = models.FloatField()
    ubp2017 = models.FloatField()
    ubp2018 = models.FloatField()
    ubpcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_microprotein(models.Model):
    cus_id = models.IntegerField(unique=True)
    microprotein2007 = models.FloatField()
    microprotein2008 = models.FloatField()
    microprotein2009 = models.FloatField()
    microprotein2010 = models.FloatField()
    microprotein2011 = models.FloatField()
    microprotein2012 = models.FloatField()
    microprotein2013 = models.FloatField()
    microprotein2014 = models.FloatField()
    microprotein2015 = models.FloatField()
    microprotein2016 = models.FloatField()
    microprotein2017 = models.FloatField()
    microprotein2018 = models.FloatField()
    microproteincondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_ascor(models.Model):
    cus_id = models.IntegerField(unique=True)
    ascor2007 = models.FloatField()
    ascor2008 = models.FloatField()
    ascor2009 = models.FloatField()
    ascor2010 = models.FloatField()
    ascor2011 = models.FloatField()
    ascor2012 = models.FloatField()
    ascor2013 = models.FloatField()
    ascor2014 = models.FloatField()
    ascor2015 = models.FloatField()
    ascor2016 = models.FloatField()
    ascor2017 = models.FloatField()
    ascor2018 = models.FloatField()
    ascorcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_occultblood(models.Model):
    cus_id = models.IntegerField(unique=True)
    occultblood2007 = models.FloatField()
    occultblood2008 = models.FloatField()
    occultblood2009 = models.FloatField()
    occultblood2010 = models.FloatField()
    occultblood2011 = models.FloatField()
    occultblood2012 = models.FloatField()
    occultblood2013 = models.FloatField()
    occultblood2014 = models.FloatField()
    occultblood2015 = models.FloatField()
    occultblood2016 = models.FloatField()
    occultblood2017 = models.FloatField()
    occultblood2018 = models.FloatField()
    occultbloodcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_whitebloodcell(models.Model):
    cus_id = models.IntegerField(unique=True)
    whitebloodcell2007 = models.FloatField()
    whitebloodcell2008 = models.FloatField()
    whitebloodcell2009 = models.FloatField()
    whitebloodcell2010 = models.FloatField()
    whitebloodcell2011 = models.FloatField()
    whitebloodcell2012 = models.FloatField()
    whitebloodcell2013 = models.FloatField()
    whitebloodcell2014 = models.FloatField()
    whitebloodcell2015 = models.FloatField()
    whitebloodcell2016 = models.FloatField()
    whitebloodcell2017 = models.FloatField()
    whitebloodcell2018 = models.FloatField()
    whitebloodcellcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_creatinine(models.Model):
    cus_id = models.IntegerField(unique=True)
    creatinine2007 = models.FloatField()
    creatinine2008 = models.FloatField()
    creatinine2009 = models.FloatField()
    creatinine2010 = models.FloatField()
    creatinine2011 = models.FloatField()
    creatinine2012 = models.FloatField()
    creatinine2013 = models.FloatField()
    creatinine2014 = models.FloatField()
    creatinine2015 = models.FloatField()
    creatinine2016 = models.FloatField()
    creatinine2017 = models.FloatField()
    creatinine2018 = models.FloatField()
    creatininecondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_bilirubin(models.Model):
    cus_id = models.IntegerField(unique=True)
    bilirubin2007 = models.FloatField()
    bilirubin2008 = models.FloatField()
    bilirubin2009 = models.FloatField()
    bilirubin2010 = models.FloatField()
    bilirubin2011 = models.FloatField()
    bilirubin2012 = models.FloatField()
    bilirubin2013 = models.FloatField()
    bilirubin2014 = models.FloatField()
    bilirubin2015 = models.FloatField()
    bilirubin2016 = models.FloatField()
    bilirubin2017 = models.FloatField()
    bilirubin2018 = models.FloatField()
    bilirubincondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_glucose(models.Model):
    cus_id = models.IntegerField(unique=True)
    glucose2007 = models.FloatField()
    glucose2008 = models.FloatField()
    glucose2009 = models.FloatField()
    glucose2010 = models.FloatField()
    glucose2011 = models.FloatField()
    glucose2012 = models.FloatField()
    glucose2013 = models.FloatField()
    glucose2014 = models.FloatField()
    glucose2015 = models.FloatField()
    glucose2016 = models.FloatField()
    glucose2017 = models.FloatField()
    glucose2018 = models.FloatField()
    glucosecondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_protein(models.Model):
    cus_id = models.IntegerField(unique=True)
    protein2007 = models.FloatField()
    protein2008 = models.FloatField()
    protein2009 = models.FloatField()
    protein2010 = models.FloatField()
    protein2011 = models.FloatField()
    protein2012 = models.FloatField()
    protein2013 = models.FloatField()
    protein2014 = models.FloatField()
    protein2015 = models.FloatField()
    protein2016 = models.FloatField()
    protein2017 = models.FloatField()
    protein2018 = models.FloatField()
    proteincondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_ketone(models.Model):
    cus_id = models.IntegerField(unique=True)
    ketone2007 = models.FloatField()
    ketone2008 = models.FloatField()
    ketone2009 = models.FloatField()
    ketone2010 = models.FloatField()
    ketone2011 = models.FloatField()
    ketone2012 = models.FloatField()
    ketone2013 = models.FloatField()
    ketone2014 = models.FloatField()
    ketone2015 = models.FloatField()
    ketone2016 = models.FloatField()
    ketone2017 = models.FloatField()
    ketone2018 = models.FloatField()
    ketonecondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

class record_calcium(models.Model):
    cus_id = models.IntegerField(unique=True)
    calcium2007 = models.FloatField()
    calcium2008 = models.FloatField()
    calcium2009 = models.FloatField()
    calcium2010 = models.FloatField()
    calcium2011 = models.FloatField()
    calcium2012 = models.FloatField()
    calcium2013 = models.FloatField()
    calcium2014 = models.FloatField()
    calcium2015 = models.FloatField()
    calcium2016 = models.FloatField()
    calcium2017 = models.FloatField()
    calcium2018 = models.FloatField()
    calciumcondition = models.CharField(max_length=50)
    def __unicode__(self):
            return self.name

def weather(request):
    time = IntegerField()
    weather = CharField(max_length=100)
    AQI = IntegerField()

    def __unicode__(self):
        return self.name

def medicalinfo(request):
    title = CharField(max_length=50)
    content = TextField()
    link = CharField(max_length=150)

    def __unicode__(self):
        return self.name
'''
def areadisease(request):
    province = CharField(max_length=50)
    ratio = FloatField()
    def __unicode__(self):
        return self.name
'''


def diseasechange(request):
    disease = CharField(max_length=50)
    rate = FloatField()
    def __unicode__(self):
        return self.name

def disegenderage(request):
    disease = CharField(max_length=50)
    gender = CharField(max_length=50)
    file = CharField(max_length=50)
    color = CharField(max_length=50)
    agerange1 = IntegerField()
    agerange2 = IntegerField()
    agerange3 = IntegerField()
    agerange4 = IntegerField()
    agerange5 = IntegerField()
    agerange6 = IntegerField()
    agerange7 = IntegerField()
    agerange8 = IntegerField()
    agerange9 = IntegerField()
    agerange10 = IntegerField()
    agerange10 = IntegerField()

    def __unicode__(self):
        return self.name

