from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import UserRegisterForm,Userpostform
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q



# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.filter(private=False).order_by('date_posted')
 	}
	return render(request, 'app/index.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account Created!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def profile(request):
    context ={
        'user' : request.user
    }
    return render(request,'app/profile.html',context)

@login_required
def editprofile(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserRegisterForm(request.POST,instance=user)
        
        if form.is_valid():
                form.save()
                return redirect('home')

    else:
            form = UserRegisterForm(instance=user)

            context = {
                'form':form,
                'user':user,
            }
            return render(request,'app/signup.html',context)

@login_required
def deleteprofile(request,pk):
        user = get_object_or_404(User, pk=pk)
        if request.method == "POST":
            form = UserRegisterForm(request.POST,instance=user)
            user.delete()
            return redirect('home')
        else:
            form = UserRegisterForm(instance=user)
            context = {
                'form':form,
                'user':user,
          
            }
            return render(request,'app/signup.html',context)


def logout_view(request):
    logout(request)
    return render(request, 'app/logout.html')

@login_required
def userpostnew(request):
    if request.method == 'POST':
        form = Userpostform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = Userpostform()
        return render(request,'app/userpostnew.html',{'form': form})


def admin(request):
    return render(request,'admin/')

@login_required
def post_list_admin(request):
    context = {
        'posts': Post.objects.filter(author=request.user).order_by('date_posted'),

    }
    return render(request,'app/post_list.html',context)



@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Userpostform(request.POST,instance=post)
        
        if form.is_valid():
                form.save()
                return redirect('post-list')

    else:
            form = Userpostform(instance=post)

            context = {
                'form':form,
                 'post':post,
            }
            return render(request,'app/userpostnew.html',context)

@login_required
def delete_post(request,pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = Userpostform(request.POST,instance=post)
            post.delete()
            return redirect('post-list')
        else:
            form = Userpostform(instance=post)
            context = {
                'form':form,
                'post':post,
          
            }
            return render(request,'app/userpostnew.html',context)

def search(request):
    template = "app/index.html"
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {
        'posts': results
    }
    return render(request,'app/index.html',context)