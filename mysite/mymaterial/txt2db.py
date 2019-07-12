import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

def main():
    from myechartsite.models import Radar
    f = open('radar.txt')
    RadarList = []
    for line in f:
        parts = line.split(',,,,')
        RadarList.append(Radar(name=parts[0],qing=parts[1],mai=parts[2],wu=parts[3],xue=parts[4],yu=parts[5],yin=parts[6]))

    f.close()

    Radar.objects.bulk_create(RadarList)



if __name__ == "__main__":
    main()
    print('Done!')