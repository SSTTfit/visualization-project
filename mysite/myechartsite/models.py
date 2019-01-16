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



    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"




