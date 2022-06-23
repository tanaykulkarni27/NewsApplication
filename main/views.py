from django.shortcuts import render,HttpResponse
import requests
from datetime import date 
import json
__Data = None
def elab(request,title):
    global __Data
    for i in __Data:
        if  title in i.get("title") :
            temp = []
            temp.append(i.get("author"))
            temp.append(i.get("title"))
            temp.append(i.get("media"))
            temp.append(i.get("published_date"))
            temp.append(i.get("summary"))
            temp.append('')
            return render(request,"single.html",{"datas":[temp]})
    return HttpResponse("Incorrect Dynamic Link Found")
def index(request):
    global __Data
    cur = date.today()
    params = {
            'q' : 'technology','lang':'en',
            'countries':'IN'
        }
    headers = {'x-api-key' : 'AzJfTMmZms6634PquqxcUrTF7Z1h0qUKCIlb3d2qn7s'}
    json_obj = requests.request("GET","https://api.newscatcherapi.com/v2/search",headers = headers,params = params)
    __Data = json.loads(json_obj.text).get('articles');
    data_list = []
    for i in __Data:
        for j in ("author","title","media","published_date"):
            if i.get(j) == '' or i.get(j) == None:
                break
        else:
            temp = []
            temp.append(i.get("author"))
            temp.append(i.get("title"))
            temp.append(i.get("media"))
            temp.append(i.get("published_date"))
            data_list.append(temp)
    return render(request,'index.html',{"obj":__Data,"content":data_list})
