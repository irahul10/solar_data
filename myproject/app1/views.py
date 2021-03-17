from django.shortcuts import render
from .models import *
import pymysql
from astropy.io import fits
import os
import urllib.request
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
import pandas as pd


# Create your views here.

def studentreg(request):
    if request.method=='POST':
        obj=Student()
        obj1=Logindata()
        name=request.POST['T1']
        branch=request.POST['T2']
        email=request.POST['T3']
        password=request.POST['T4']
        usertype='student'
        obj.name=name
        obj.branch=branch
        obj.email=email
        obj1.email=email
        obj1.password=password
        obj1.usertype=usertype
        obj.save()
        obj1.save()
        return render(request, 'StudentReg.html',{'data':"success"})
    else:
        return render(request,'StudentReg.html')


def showdata(request):
    obj = Student.objects.all()
    return render(request,'showdata.html',{'key1':obj})

def solar_data_new(request):
    #file_path = 'G:\FitsTest'
    #file_path  = 'E:\solar_flask\FitsTest'
    file_path = 'G:\solar_project\myproject\FitsTest'
    file_type = '.fits'
    paths = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.lower().endswith(file_type.lower()):
                paths.append(os.path.join(root, file))

    for path in paths:
        hdul = fits.open(path)
        header_dict = hdul[1].header
        keys = ['NAXIS1', 'NAXIS2', 'DATE-OBS', 'PROGRAM']
        dict2 = {x: header_dict[x] for x in keys}
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='solardata',autocommit=True)
        cur=conn.cursor()
        sql = "insert into data_solar values ('" + str(path) + "','" + str(dict2['NAXIS1']) + "','" + str(dict2['NAXIS2']) + "','" + str(dict2['DATE-OBS']) + "','" + str(dict2['PROGRAM']) + "')"
        cur.execute(sql)
        temp = str(path)
    n = cur.rowcount
    if(n==1):
        return render(request,'solar_data.html', {'result': temp})
    else:
        return render(request,'solar_data.html', {'result': 'failure'})

def delete_data(request):
    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='solardata',autocommit=True)
    cur=conn.cursor()
    sql="delete from data_solar"
    cur.execute(sql)
    n=cur.rowcount
    if(n>1):
        return render(request,'delete_data.html',{'result': 'success'})
    else:
        return render(request,'delete_data.html',{'result': 'failure'})


def show_solar(request):
    conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='solardata',autocommit=True)
    cur=conn.cursor()
    cur.execute("SELECT * from data_solar")
    result = cur.fetchall()
    return render(request,'show_solar_data.html', {'result': result})


def filtter_data(request):
    if request.method == "POST":
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='solardata', autocommit=True)
        cur = conn.cursor()
        sql = "select * from data_solar  where date >= '" + start_date + "' AND date <= '" + end_date + "'"
        cur.execute(sql)
        result = cur.fetchall()
        return render(request, 'show_filtter.html',{'result': result})


def download(request):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='solar', autocommit=True)
    cur = conn.cursor()
    cur.execute("SELECT * from test2")
    result = cur.fetchall()
    return render(request, 'show_test.html', {'result': result})

def temp(request):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='solar', autocommit=True)
    cur = conn.cursor()
    path = 'E:\solar_flask\FitsTest\2013\August\1\2013-08-01T23_11_32.812000.fits'
    sql = "insert into test2 values ('" + str(path) + "')"
    cur.execute(sql)
    temp = str(path)
    n = cur.rowcount
    if (n == 1):
        return render(request, 'solar_data.html', {'result': temp})
    else:
        return render(request, 'solar_data.html', {'result': 'failure'})

# def zip(request):
#     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='solar', autocommit=True)
#     cur = conn.cursor()
#     cur.execute("SELECT * from test where ")
#     result = cur.fetchall()
#     return render(request, 'show_test.html', {'result': result})
