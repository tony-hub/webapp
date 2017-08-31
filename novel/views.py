from django.shortcuts import render,render_to_response
from novel.models import Novel,NovelCopy,Chapter,ChapterCopy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    hot_list=NovelCopy.objects.filter().order_by('?')[:4]
    hot = NovelCopy.objects.filter()
    fantasy=NovelCopy.objects.filter(type=1).order_by('?')[:6]
    romance = NovelCopy.objects.filter(type=4).order_by('?')[:6]
    return render(request,'index.html',locals())

def more(request,type,novelid):
    page = novelid
    page = int(page)
    # pages = NovelCopy.objects.filter(type=type).order_by('novelid').all().count()
    # img=NovelCopy.objects.filter(type=type).order_by('novelid')[page*10:(page+1)*10]
    title=NovelCopy.objects.filter(type=type)[0].sort
    novel_list = NovelCopy.objects.filter(type=type).all()
    paginator = Paginator(novel_list, 10) # Show 10 contacts per page
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('more.html',locals())

def detail(request,novelid):
    chapter =ChapterCopy.objects.filter(novelid=novelid).order_by('chapterid').all()
    chapter_first = ChapterCopy.objects.filter(novelid=novelid).order_by('chapterid')[0]
    novel = NovelCopy.objects.filter(novelid=novelid)[0]
    total =len((ChapterCopy.objects.filter(novelid=novelid).all()))
    return render_to_response('detail.html',locals())
def chapter(request,chapterid):
    chapter = ChapterCopy.objects.filter(chapterid=chapterid).order_by('chapterid')[0]
    novel =  ChapterCopy.objects.filter(chapterid=chapterid)[0].novelid
    sorts = ChapterCopy.objects.filter(novelid=novel).order_by('chapterid').all()
    lss = ChapterCopy.objects.filter(novelid=novel).order_by('chapterid').all()
    ls=[]
    for i in lss:
        ls.append(i.chapterid)

    if ls.index(int(chapterid))==0 :
        up=int(chapterid)
        down = ls[ls.index(int(chapterid))+1]
    elif ls.index(int(chapterid))==len(ls)-1:
        down=int(chapterid)
        up = ls[ls.index(int(chapterid))-1]
    else:
        up = ls[ls.index(int(chapterid))-1]  # 获取当页面的索引  在减去一 就是上一页了
        down = ls[ls.index(int(chapterid))+1]
    return render_to_response('chapter.html',locals())

def search(request):
    keyword=request.GET.get('kw','')
    if keyword:
        display=NovelCopy.objects.filter(novelname__icontains=keyword).all()
    else:
        display=NovelCopy.objects.filter().order_by('?').all()[:100]
    random = NovelCopy.objects.filter().order_by('?').all()[:6]
    return render_to_response('search.html',locals())