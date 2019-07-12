import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()


def main():
    from myechartsite.models import Zhexiancheck
    with open("zhexiancheck.json", 'r') as json_data:
        s = json.load(json_data)
        ZhexianList=[]
        for i in range(len(s["cus_id"])):
            ZhexianList.append(Zhexiancheck(cus_id=s["cus_id"][i],ph=s["ph"][i],jigan=s["jigan"][i],niaobizhong=s["niaobizhong"][i],niaodanyuan=s["niaodanyuan"][i],weidanbai=s["weidanbai"][i]))
    Zhexiancheck.objects.bulk_create(ZhexianList)


if __name__ == "__main__":
    main()
    print('Done!')