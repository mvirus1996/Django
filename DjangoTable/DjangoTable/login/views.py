from django.shortcuts import render, redirect
from .models import Login
from django.contrib import messages
import json, time

def table(request):
    if request.method == 'POST':
        details = (request.POST)
        try:
            logindata = Login.objects.get(username=details['username'], password=details['password'])
            start = time.time()
            jsonfile = json.loads(open('static/data.json').read())
            data = ""
            data = buildTable(jsonfile)
            stop = time.time()
            return render(request, "index.html", {"data": data})
        except Exception as e:
            messages.error(request, "Wrong username or password")
            return redirect('/')
    else:
        return redirect('/')



def buildTable(jsonfile):
    data = "<table cellspacing=0>"
    unikey = 0
    if check(jsonfile) == 1:
        data += tableForDict(jsonfile, unikey) 
    elif check(jsonfile) == 2:
        data += tableForList(jsonfile, unikey)
    data += "</table>"
    return data


def check(jsonfile):
    if isinstance(jsonfile, dict):
        return 1 
    elif isinstance(jsonfile, list):
        return 2
    else:
        return 3


def tableForDict(jsonfile, unikey):
    data = "<table border=1 cellspacing=0>"
    unikey += 1
    for key in jsonfile:
        if check(jsonfile[key]) == 1:
            data += "<tr><th>"+key+"</th><td><a id='"+key+str(unikey)+"' href='javascript:show(\""+key+str(unikey)+"\")'>Show</a><div class='tables' id='table"+key+str(unikey)+"'>"+tableForDict(jsonfile[key], unikey)+"</div></td></tr>"
        elif check(jsonfile[key]) == 2:
            data += "<tr><th>"+key+"</th><td><a id='"+key+str(unikey)+"' href='javascript:show(\""+key+str(unikey)+"\")'>Show</a><div class='tables' id='table"+key+str(unikey)+"'>"+tableForList(jsonfile[key], unikey)+"</div></td></tr>"
        else:
            data += "<tr><th>"+key+"</th><td>"+str(jsonfile[key])+"</td></tr>"
    data += "</table>"
    return data


def tableForList(jsonfile, unikey):
    if len(jsonfile) > 1:
        data = "<ul>"
        for index, num in enumerate(jsonfile):
            unikey += 1
            data += "<li>"+tableForDict(jsonfile[index], unikey)
    else:
        data = ""
        for index, num in enumerate(jsonfile):
            unikey += 1
            data += tableForDict(jsonfile[index], unikey)
    return data
