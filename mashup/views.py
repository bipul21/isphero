from django.shortcuts import render_to_response,get_object_or_404
from django.http import Http404,HttpResponse
from django.template import RequestContext
import urllib
import json
from settings import q,sphero,mailCount
import spherohelper
import math,sendgrid
import settings

def getDistance(c1,c2):
    sqr = lambda x:x*x
    x = sqr(c2[0]-c1[0])
    y = sqr(c2[1] - c1[1])
    dist = int(math.sqrt(x+y))
    return dist

def getAngle(c1,c2):
    x = c2[0]-c1[0]
    y = c2[1] - c1[1]
    angle=int(math.degrees(math.atan2(x,y)))
    if angle < 0:
        angle = 360+angle
    return angle
        


def processMovemovent():
    if len(q) <= 1:
        spherohelper.stop(sphero)
        return
    
    c1=q.popleft()
    c2=q.popleft()
    q.appendleft(c2)
    dist = getDistance(c1,c2)
    angle = getAngle(c1,c2)
    spherohelper.roll(sphero,dist,angle)
    return 

def reset(request):
    q.clear()
    spherohelper.stop(sphero)
    return HttpResponse('')

def push(request):
    x=request.GET["x"]
    y=request.GET["y"]
    q.append((int(x),int(y)))
    processMovemovent()
    return HttpResponse('')

def showHead(request):
    flag = request.GET["flag"]
    if flag:
        spherohelper.showHeadLight(sphero,flag)
    else:
        spherohelper.showHeadLight(sphero,flag)
    return HttpResponse('')


def sendInvite(request):
    mail = request.GET["mail"]
    invite(mail)
    return HttpResponse("Done!")

def changeColor(request):
    color = request.GET["color"]
    spherohelper.changeColor(sphero,color)
    return HttpResponse('')

def home(request):
   return render_to_response("index.html",{},RequestContext(request))

