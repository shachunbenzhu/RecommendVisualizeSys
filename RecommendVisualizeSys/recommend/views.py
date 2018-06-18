# coding:utf-8          #声明编码为utf-8, 因为我们在代码中用到了中文,如果不声明就报错
from django.shortcuts import render

# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse        #引入HttpResponse，它是用来向网页返回内容的，就像Python中的 print 一样，只不过 HttpResponse 是把内容显示到网页上

from recommend.models import RecommendPost,FilmRecommendPost,BookRecommendPost,GameRecommendPost
from recommend import sparqlSelect


#定义了一个recommend()函数，第一个参数必须是 request，与网页发来的请求有关，request 变量里面包含get或post的内容，用户浏览器，系统等信息在里面
def init(request):
    results = sparqlSelect.getInitResult()
    print(results)

    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    posts = RecommendPost.objects.all()
    posts.delete()

    for result in results["results"]["bindings"]:
        recommendPost = RecommendPost()
        recommendPost.surl = result["movie"]["value"]
        recommendPost.name = result["name"]["value"]

        # 由于thumbnail可选，因此需要判断，否则会报错
        if ("thumbnail" in result):
            thumbnail = result["thumbnail"]["value"]
        else:
            thumbnail = '/static/no.png'
        recommendPost.thumbnail = thumbnail

        recommendPost.abstract = result["abstract"]["value"]
        recommendPost.subject = result["subject"]["value"]
        subject = str(recommendPost.subject)
        recommendPost.subject = subject[subject.rfind("/") + 1:len(subject)]
        recommendPost.save()

    posts = RecommendPost.objects.all()

    resultsFilm = sparqlSelect.getFilmResult()
    print(resultsFilm)
    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    postsFilmRecommend = FilmRecommendPost.objects.all()
    postsFilmRecommend.delete()
    for result in resultsFilm["results"]["bindings"]:
        filmRecommendPost = FilmRecommendPost()
        filmRecommendPost.surl = result["movie"]["value"]
        filmRecommendPost.name = result["name"]["value"]
        filmRecommendPost.save()
    postsFilmRecommend = FilmRecommendPost.objects.all()

    resultsBook = sparqlSelect.getBookResult()
    print(resultsBook)
    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    postsBookRecommend = BookRecommendPost.objects.all()
    postsBookRecommend.delete()
    for result in resultsBook["results"]["bindings"]:
        bookRecommendPost = BookRecommendPost()
        bookRecommendPost.surl = result["book"]["value"]
        bookRecommendPost.name = result["name"]["value"]
        bookRecommendPost.save()
    postsBookRecommend = BookRecommendPost.objects.all()

    resultsGame = sparqlSelect.getGameResult()
    print(resultsGame)
    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    postsGameRecommend = GameRecommendPost.objects.all()
    postsGameRecommend.delete()
    for result in resultsGame["results"]["bindings"]:
        gameRecommendPost = GameRecommendPost()
        gameRecommendPost.surl = result["game"]["value"]
        gameRecommendPost.name = result["name"]["value"]
        gameRecommendPost.save()
    postsGameRecommend = GameRecommendPost.objects.all()

    t = loader.get_template('recommend1.html')
    print(posts)
    #c = Context({'posts': posts})
    # 不可以是Context，只能是dict
    return HttpResponse(t.render({'posts': posts}))


def select(request):
    search_type = request.GET['search_type']
    search_condition = request.GET['search_condition']

    results = sparqlSelect.getSelectResult(search_type, search_condition)
    print(results)

    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    posts = RecommendPost.objects.all()
    posts.delete()

    for result in results["results"]["bindings"]:
        recommendPost = RecommendPost()
        recommendPost.surl = result["movie"]["value"]
        recommendPost.name = result["name"]["value"]

        # 由于thumbnail可选，因此需要判断，否则会报错
        if ("thumbnail" in result):
            thumbnail = result["thumbnail"]["value"]
        else:
            thumbnail = '/static/no.png'
        recommendPost.thumbnail = thumbnail

        recommendPost.abstract = result["abstract"]["value"]
        recommendPost.subject = result["subject"]["value"]
        subject = str(recommendPost.subject)
        recommendPost.subject = subject[subject.rfind("/")+1:len(subject)]
        recommendPost.save()

    posts = RecommendPost.objects.all()

    resultsFilm = sparqlSelect.getFilmResult()
    print(resultsFilm)
    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    postsFilmRecommend = FilmRecommendPost.objects.all()
    postsFilmRecommend.delete()
    for result in resultsFilm["results"]["bindings"]:
        filmRecommendPost = FilmRecommendPost()
        filmRecommendPost.surl = result["movie"]["value"]
        filmRecommendPost.name = result["name"]["value"]
        filmRecommendPost.save()
    postsFilmRecommend = FilmRecommendPost.objects.all()

    resultsBook = sparqlSelect.getBookResult()
    print(resultsBook)
    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    postsBookRecommend = BookRecommendPost.objects.all()
    postsBookRecommend.delete()
    for result in resultsBook["results"]["bindings"]:
        bookRecommendPost = BookRecommendPost()
        bookRecommendPost.surl = result["book"]["value"]
        bookRecommendPost.name = result["name"]["value"]
        bookRecommendPost.save()
    postsBookRecommend = BookRecommendPost.objects.all()

    resultsGame = sparqlSelect.getGameResult()
    print(resultsGame)
    # 在入数据库之前先删除数据，否则后面只是插入，不会更改数据
    postsGameRecommend = GameRecommendPost.objects.all()
    postsGameRecommend.delete()
    for result in resultsGame["results"]["bindings"]:
        gameRecommendPost = GameRecommendPost()
        gameRecommendPost.surl = result["game"]["value"]
        gameRecommendPost.name = result["name"]["value"]
        gameRecommendPost.save()
    postsGameRecommend = GameRecommendPost.objects.all()

    t = loader.get_template('recommend1.html')
    print(posts)

    return HttpResponse(t.render({'posts': posts, 'postsFilmRecommend': postsFilmRecommend, 'postsBookRecommend': postsBookRecommend, 'postsGameRecommend': postsGameRecommend}))