import os



def main():

    f = open('radar.txt')
    RadarList = []
    for line in f:
        a=line.split(',,,,')
        print(a)
        #name,qing,mai,wu,xue,yu,yin = line.split(',,,,')
        #print (name)

    f.close()




if __name__ == "__main__":
    main()
    print('Done!')