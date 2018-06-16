# coding:utf-8          #声明编码为utf-8, 因为我们在代码中用到了中文,如果不声明就报错
from django.shortcuts import render

# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse        #引入HttpResponse，它是用来向网页返回内容的，就像Python中的 print 一样，只不过 HttpResponse 是把内容显示到网页上

from recommend.models import RecommendPost


#定义了一个recommend()函数，第一个参数必须是 request，与网页发来的请求有关，request 变量里面包含get或post的内容，用户浏览器，系统等信息在里面
def recommend(request):
    #results = homework.getResult()
    results = {}
    print(results)

    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    posts = RecommendPost.objects.all()
    posts.delete()

    for result in results["results"]["bindings"]:
        recommendPost = RecommendPost()
        recommendPost.surl = result["s"]["value"]
        recommendPost.name = result["name"]["value"]

        # 由于thumbnail可选，因此需要判断，否则会报错
        if ("thumbnail" in result):
            thumbnail = result["thumbnail"]["value"]
        else:
            thumbnail = '/static/no.png'
        recommendPost.thumbnail = thumbnail

        recommendPost.birthDate = result["birthDate"]["value"]
        recommendPost.description = result["description"]["value"]
        recommendPost.abstract = result["abstract"]["value"]
        recommendPost.save()

    posts = RecommendPost.objects.all()
    t = loader.get_template('archive.html')
    print(posts)
    #c = Context({'posts': posts})
    # 不可以是Context，只能是dict
    return HttpResponse(t.render({'posts': posts}))