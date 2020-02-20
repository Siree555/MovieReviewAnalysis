# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import csv
import sys
from django.shortcuts import render, HttpResponse
import re
from importlib import reload
from textblob import TextBlob



# Create your views here.


# Add the two views we have been talking about  all this time :)

def HomePageView(request):
    return render(request,'index.html')


def tweetsPageView(request):
    reload(sys)
    #sys.setdefaultencoding('utf-8')
    with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/tweets.csv','r') as read_file:
        csv_reader=csv.reader(read_file)
        list1=[]
        next(csv_reader)
        for line in csv_reader:
            list1.append(line[1])
        positive=0
        negative=0
        neutral=0
        positive_tweets=[]
        negative_tweets=[]
        neutral_tweets=[]
        for line in list1:
            analysis=TextBlob(line)
            if(analysis.sentiment.polarity>0):
                positive+=1
                positive_tweets.append(line)
            elif(analysis.sentiment.polarity<0):
                negative+=1
                negative_tweets.append(line)
            elif(analysis.sentiment.polarity==0):
                neutral+=1
                neutral_tweets.append(line)

    return render(request,'tweets.html',{'pt1':positive_tweets[0],'pt2':positive_tweets[1],'pt3':positive_tweets[2],'pt4':positive_tweets[3],'pt5':positive_tweets[4],'pt6':positive_tweets[5],'pt7':positive_tweets[6],'pt8':positive_tweets[7],'pt9':positive_tweets[8],'pt10':positive_tweets[9],'pt11':positive_tweets[10],'pt12':positive_tweets[11],'pt13':positive_tweets[12],'pt14':positive_tweets[13],'pt15':positive_tweets[14],'pt16':positive_tweets[15],'pt17':positive_tweets[16],'pt18':positive_tweets[17],'pt19':positive_tweets[18],'pt20':positive_tweets[19],'ngt1':negative_tweets[0],'ngt2':negative_tweets[1],'ngt3':negative_tweets[2],'ngt4':negative_tweets[3],'ngt5':negative_tweets[4],'ngt6':negative_tweets[5],'ngt7':negative_tweets[6],'ngt8':negative_tweets[7],'ngt9':negative_tweets[8],'ngt10':negative_tweets[9],'ngt11':negative_tweets[10],'ngt12':negative_tweets[11],'ngt13':negative_tweets[12],'ngt14':negative_tweets[13],'ngt15':negative_tweets[14],'ngt16':negative_tweets[15],'ngt17':negative_tweets[16],'ngt18':negative_tweets[17],'ngt19':negative_tweets[18],'ngt20':negative_tweets[19],'nt1':neutral_tweets[0],'nt2':neutral_tweets[1],'nt3':neutral_tweets[2],'nt4':neutral_tweets[3],'nt5':neutral_tweets[4],'nt6':neutral_tweets[5],'nt7':neutral_tweets[6],'nt8':neutral_tweets[7],'nt9':neutral_tweets[8],'nt10':neutral_tweets[9],'nt11':neutral_tweets[10],'nt12':neutral_tweets[11],'nt13':neutral_tweets[12],'nt14':neutral_tweets[13],'nt15':neutral_tweets[14],'nt16':neutral_tweets[15],'nt17':neutral_tweets[16],'nt18':neutral_tweets[17],'nt19':neutral_tweets[18],'nt20':neutral_tweets[19],})

def oaPageView(request):
    list1=[]

    with open('/Users/prakash/Desktop/SE final project Group_17/Project code Group_17/mywebsite/Filmatory/reviews.csv','r') as read_file:
       csv_reader=csv.reader(read_file)

       for line in csv_reader:
               list1.append(line[1])

    goodlist=list1[0]
    badlist=list1[1]
    avglist=list1[2]
    return render(request,'oa.html',{'content':goodlist, 'content1':badlist,'content2':avglist})
