# from django.test import TestCase

# Create your tests here.
import numpy as np
import random
# import json
# with open("./json/inditrend.json", "rb") as f:
#     s = json.load(f)
#     print(list(s.keys()))
# page_count, tmp = divmod(record_count, page_record_limit)
#     if tmp:
#         page_count += 1
#     else:
#         self.page_count = page_count
from PIL import Image
import numpy as np
import os
import cv2
import pandas as pd
def buildmask():
    rootpath1="E:/inpaintdataset/1/"
    rootpath2="E:/inpaintdataset/2/"
    maskpath = "E:/inpaintdataset/mask/"
    df = pd.DataFrame(columns=['dir','mask'])
    for dir in os.listdir(rootpath1):
        img1 = cv2.imread(os.path.join(rootpath1,dir))
        img2 = cv2.imread(os.path.join(rootpath2,dir))
        subresult = cv2.subtract(img2, img1)
        if np.all(subresult==0):
            continue
        print(dir)
        print(img1.shape,img2.shape)
        a = np.any(subresult != 0, axis=2)
        print(a.shape)
        # mask2d = np.zeros_like(subresult[:,:,0])
        # mask2d[a]= 1
        mask = np.zeros((1,1024,1024,1),np.float32)
        mask[:,a,:]=1
        print(a[a==True].shape)
        print(mask.shape)
        np.save(os.path.join(maskpath,dir.split('.')[0]+'.npy'),mask)
        print("mask ok ",dir)
        # sub = mask.sum()
        # if sub<30:
        #     cv2.imwrite(os.path.join(rootpath3,dir), mask)
        #
        # print(mask)

        print(np.sum(a!=0),np.sum(mask!=0))
    # df.to_csv(os.path.join(maskpath,"masks.csv"))

def buildmaskedimg():
    rootpath1 = "E:/inpaintdataset/1/"
    rootpath2 = "E:/inpaintdataset/2/"
    savepath = "E:/inpaintdataset/maskedimg/"
    for dir in os.listdir(rootpath1):
        img11 = Image.open(os.path.join(rootpath1, dir))
        img1 = np.array(img11)
        img22 = Image.open(os.path.join(rootpath2, dir))
        img2= np.array(img22)
        subresult = img2-img1
        if np.all(subresult==0):
            continue
        img = img2.copy()
        # img3 = img2.copy()
        # img3[subresult != 0] = 255
        a=np.any(subresult!=0,axis=2)
        for i in range(3):
            img[:,:,i][a]=255
        print(img.shape)
        print(img[img!=img2].shape[0]/3)
        img.save(os.path.join(savepath,dir))
        # cv2.imwrite(os.path.join(savepath,dir), img)
        print(dir,"is saved")

        # hmerge = np.hstack((img, img3))
        # cv2.imshow("result",hmerge)
        # cv2.waitKey(0)
        # sub = mask.sum()
        # if sub<30:
        #     cv2.imwrite(os.path.join(rootpath3,dir), mask)
        #
        # print(mask)

        # print(np.sum(subresult != 0), np.sum(mask != 0))

def testdimension():
    a=np.zeros((1,2,2,1))

    b=[[True,False],[False,False]]
    a[:,b,:]=1
    print(a)
    # b[:50,:50]=True
    # b[50:,50:]=False
    # a[:,b,:]=0
    # print(a.shape,np.sum(a[a>0]))


if __name__== "__main__":
    # a=[]
    # for i in range(5):
    #     a.append((1,0))
    print([None]+[4])
    # testdimension()
    # buildmask()
    # # buildmaskedimg()
    # maskpath = "E:/inpaintdataset/mask/"
    # np.set_printoptions(threshold=np.inf)
    # x = np.load(os.path.join(maskpath,"0001_01_8.npy"))
    # print(x)















