from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ourdiary, Photo
from django.contrib.auth.decorators import login_required # post_like함수가 실행될려면 먼저 로그인이 되어야 함
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from account.models import Profile
#댓글
from .forms import CommentForm
from .models import Comment


# Create your views here.
def ourdiary(request):
    ourdiarys = Ourdiary.objects.all().order_by('-id')
    current_user = request.user
    return render(request, 'ourdiary.html', {'ourdiarys':ourdiarys, 'current_user':current_user}) #'current_user':current_user

def detail(request, ourdiary_id):
    ourdiary = Ourdiary.objects.all()
    ourdiary_detail = get_object_or_404(Ourdiary, pk=ourdiary_id)
    current_user = request.user
    profile = Profile.objects.all()
    form = CommentForm()
    return render(request, 'detail.html', {'ourdiary':ourdiary_detail, 'current_user':current_user, 'form':form, 'profile':profile})

#comment
def add_comment(request, pk):
   #post
    post = get_object_or_404(Ourdiary, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('detail', pk)
    else:
        error = "no"
        return render(request, "detail.html", {'error':error})
        #form = CommentForm()
    #return render(request, 'detail.html', {'form':form})

def new(request):
    profile = Profile.objects.all()
    current_user = request.user
    return render(request, 'new.html', {'profile':profile, 'current_user':current_user})

def create(request):
    if not request.session.get('user'):
        return render(request, 'login.html')
    if (request.method == 'POST'):
        ourdiary = Ourdiary()
        ourdiary.title= request.POST['title']
        ourdiary.description = request.POST['body']
        ourdiary.author = request.user
        ourdiary.save()
        
        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.blog = ourdiary
            photo.image = img
            photo.save()
        return redirect('/ourdiary/'+str(ourdiary.id))#형변환 뒤 더해줌 
    else:
        return render(request, 'new.html')
    
    return render(request, 'new.html')

def update(request, ourdiary_id):
    ourdiary = get_object_or_404(Ourdiary, pk = ourdiary_id)
    photo = Photo.objects.all()
    profile = Profile.objects.all()
    current_user = request.user
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        ourdiary.title = title
        ourdiary.description = body
        ourdiary.save()
                    
        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.blog = ourdiary
            photo.image = img
            photo.save()
        return redirect('detail',ourdiary.id)
    return render(request, 'edit.html', {'ourdiary':ourdiary,'profile':profile, 'current_user':current_user})
    
def delete(request, ourdiary_id):
    ourdiary = get_object_or_404(Ourdiary, pk = ourdiary_id)
    ourdiary.delete()
    return redirect('/')

def mylist(request):
    ourdiarys = Ourdiary.objects.all()
    profile = Profile.objects.all()
    current_user = request.user
    ourdiary_list = ourdiarys.filter(author_id=request.user)
    return render(request,'mylist.html',{'ourdiary_list':ourdiary_list,'profile':profile, 'current_user':current_user})
    
@login_required #post_like함수가 실행될려면 먼저 로그인이 되어야 함. 
@require_POST #post request만 받기
def post_like(request):
    pk = request.POST.get('pk', None)
    ourdiary = get_object_or_404(Ourdiary, pk=pk)
    user = request.user

    if ourdiary.like_user_set.filter(id=user.id).exists():
        ourdiary.like_user_set.remove(user)
        message = '좋아요 취소'
    else:
        ourdiary.like_user_set.add(user)
        message = '좋아요'
    
    context = {'like_count':ourdiary.like_count, 'message':message, 'username':user.username} #에러가 이유 -> int형으로 바꿔줘야 함. 그런데 ourdiary.likes_count()가 함수라서 안된거임.
    return HttpResponse(json.dumps(context), content_type="application/json")



@login_required
def comment_approve(request, id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', id)

@login_required
def comment_remove(request, id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', id)

