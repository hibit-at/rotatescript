import cmath
import copy
import csv
import json
import math
import os

from django.http import HttpResponse  # 追加
from django.shortcuts import render

truestr = "true"
falsestr = "false"


def json_create(r, t, h, a, o):
    j = {"ActiveInPauseMenu": truestr,
         "Movements": [{"StartPos": {"x": 0, "y": 0, "z": 0},
                        "StartRot": {"x": 0, "y": 0, "z": 0},
                        "EndPos": {"x": 0, "y": 0, "z": 0},
                        "EndRot": {"x": 0, "y": 0, "z": 0},
                        "Duration": 0,
                        "Delay": 0,
                        "EaseTransition": falsestr}
                       ]
         }

    need_step = 36

    for i in range(need_step-1):
        new_j = copy.deepcopy(j["Movements"][0])
        j["Movements"].append(new_j)

    camera_h = h-a

    for i in range(need_step):

        rad = 2*math.pi*i/need_step
        next_rad = 2*math.pi*(i+1)/need_step

        # 位置のセット
        j["Movements"][i]["Duration"] = t/36
        j["Movements"][i]["StartPos"]["x"] = r*math.cos(rad)
        j["Movements"][i]["StartPos"]["y"] = h
        j["Movements"][i]["StartPos"]["z"] = r*math.sin(rad)+o
        j["Movements"][i]["EndPos"]["x"] = r*math.cos(next_rad)
        j["Movements"][i]["EndPos"]["y"] = h
        j["Movements"][i]["EndPos"]["z"] = r*math.sin(next_rad)+o

        # 角度の計算1
        deg = 270-math.degrees(rad)
        j["Movements"][i]["StartRot"]["y"] = deg
        deg = 270-math.degrees(next_rad)
        j["Movements"][i]["EndRot"]["y"] = deg

        # 角度の計算2
        c2 = complex(r, camera_h)
        rad2 = cmath.phase(c2)
        deg2 = math.degrees(rad2)
        j["Movements"][i]["StartRot"]["x"] = deg2
        j["Movements"][i]["EndRot"]["x"] = deg2

    return j


def index(request):  # 追加
    r = 2.
    if "r" in request.POST:
        r = float(request.POST["r"])
    t = 3.
    if "t" in request.POST:
        t = float(request.POST["t"])
    h = 2.
    if "h" in request.POST:
        h = float(request.POST["h"])
    a = 1.5
    if "a" in request.POST:
        a = float(request.POST["a"])
    o = 0.
    if "o" in request.POST:
        o = float(request.POST["o"])
    is3D = '1'
    if "is3D" in request.POST:
        is3D = request.POST["is3D"]
    text = str(json_create(r, t, h, a, o)).replace("'", '\"')
    par = {'r': r, 't': t, 'h': h, 'a': a, 'o': o}
    text = text.replace('"true"', 'true')
    text = text.replace('"false"', 'false')
    params = {'text': text, 'par': par, 'is3D': is3D}
    return render(request, 'app/index.html', params)  # 追加


def download(request):  # 追加
    r = 2.
    if "r" in request.GET:
        r = float(request.GET["r"])
    t = 1.
    if "t" in request.GET:
        t = float(request.GET["t"])
    h = 2.
    if "h" in request.GET:
        h = float(request.GET["h"])
    a = 1.5
    if "a" in request.GET:
        a = float(request.GET["a"])
    o = 0.
    if "o" in request.GET:
        o = float(request.GET["o"])
    text = str(json_create(r, t, h, a, o)).replace("'", '\"')
    text = text.replace('"true"', 'true')
    text = text.replace('"false"', 'false')
    return HttpResponse(text)


def sample(request):
    return render(request, 'app/three.html')


def params(request):
    return render(request, 'app/params.html')
