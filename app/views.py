from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse #追加


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse #追加

import json
import csv
import cmath
import math
import copy
import os

def json_create(r,w,h,a):
    j = {"ActiveInPauseMenu": True, 
        "Movements": [{"StartPos": {"x": 0, "y": 0, "z": 0}, 
                        "StartRot": {"x": 0, "y": 0, "z": 0}, 
                        "EndPos": {"x": 0, "y": 0, "z": 0}, 
                        "EndRot": {"x": 0, "y": 0, "z": 0}, 
                        "Duration": 0, 
                        "Delay": 0, 
                        "EaseTransition": True}
                    ]
        }

    need_step = math.ceil(40/w)

    for i in range(need_step-1):
        new_j = copy.deepcopy(j["Movements"][0])
        j["Movements"].append(new_j)

    h -= a

    for i in range(need_step):

        rad = 2*math.pi*i/need_step
        next_rad = 2*math.pi*(i+1)/need_step

        #位置のセット
        j["Movements"][i]["Duration"] = 0.1
        j["Movements"][i]["StartPos"]["x"] = r*math.cos(rad)
        j["Movements"][i]["StartPos"]["y"] = h
        j["Movements"][i]["StartPos"]["z"] = r*math.sin(rad)
        j["Movements"][i]["EndPos"]["x"] = r*math.cos(next_rad)
        j["Movements"][i]["EndPos"]["y"] = h
        j["Movements"][i]["EndPos"]["z"] = r*math.sin(next_rad)

        #角度の計算1
        c = complex(-math.cos(rad),-math.sin(rad))
        rad = cmath.phase(c)
        deg = -math.degrees(rad)+90
        j["Movements"][i]["StartRot"]["y"] = deg 
        
        c = complex(-math.cos(next_rad),-math.sin(next_rad))
        rad = cmath.phase(c)
        deg = -math.degrees(rad)+90
        j["Movements"][i]["EndRot"]["y"] = deg

        #角度の計算2 
        c2 = complex(r,h)
        rad2 = cmath.phase(c2)
        deg2 = math.degrees(rad2)
        j["Movements"][i]["StartRot"]["x"] = deg2

        c2 = complex(r,h)
        rad2 = cmath.phase(c2)
        deg2 = math.degrees(rad2)
        j["Movements"][i]["EndRot"]["x"] = deg2

        j["Movements"][i]["EaseTransition"] = False

    return j

def index(request):#追加
    r = 2
    if "r" in request.GET:
        r = float(request.GET["r"])
    w = 1
    if "w" in request.GET:
        w = float(request.GET["w"])
    h = 2
    if "h" in request.GET:
        h = float(request.GET["h"])
    a = 1
    if "a" in request.GET:
        a = float(request.GET["a"])
    debug = "{}{}{}{}<br>".format(r,w,h,a)
    text = str(json_create(r,w,h,a))
    return HttpResponse(text)#追加

def index(request):#追加
    return HttpResponse("はろわ")#追加