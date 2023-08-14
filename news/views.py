from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    news=[
        {"onvan":"خبر 1 ", "titr":"حادثه تروریستی در حرم شاهچراغ !"},
        {"onvan":"خبر 2 ", "titr":"بانک ها ، تعطیل اما روشن!"},
        {"onvan":"خبر 3 ", "titr":"رئیس سنجش برکنار شد!"},
    ]
    return render (request,"news/index.html",context={"khabar":news})

def shownews(request,adad):
    return render(request,"news\show.html")
        
