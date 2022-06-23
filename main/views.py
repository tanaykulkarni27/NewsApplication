from django.shortcuts import render,HttpResponse
import requests
__Data = None
def elab(request,title):
    global __Data
    # json_obj = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=6eeec874600546b4be9d3b37d6697ab8")
    # data = json_obj.json().get("articles")
    for i in __Data:
        if  title in i.get("title") :
            temp = []
            temp.append(i.get("author"))
            temp.append(i.get("title"))
            temp.append(i.get("urlToImage"))
            temp.append(i.get("publishedAt"))
            temp.append(i.get("description"))
            temp.append(i.get("content"))
            return render(request,"single.html",{"datas":[temp]})
    return HttpResponse("Incorrect Dynamic Link Found")
def index(request):
    global __Data
    json_obj = requests.get("https://newsapi.org/v2/everything?q=Technology&apiKey=6eeec874600546b4be9d3b37d6697ab8")
    data = json_obj.json().get("articles")
    __Data = data;
    data_list = []
    for i in data:
         temp = []
         temp.append(i.get("author"))
         temp.append(i.get("title"))
         temp.append(i.get("urlToImage"))
         temp.append(i.get("publishedAt"))=
         data_list.append(temp)
    return render(request,'index.html',{"obj":data,"content":data_list})
'''
[ author, Title Image Date]
'''    