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

def home(request): #this view obtains post objects and filters out from only public posts, this is shown on the home page
	context = {
		'posts': Post.objects.filter(private=False).order_by('date_posted')
 	}
	return render(request, 'app/index.html',context) #the post context is ten rendered on the html page


def signup(request): #this is a definition of signup 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #UserRegisterfrom is generated
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)             #user is logged in after signning up
            return redirect('home') #user is redirected to home
    else:
        form = UserRegisterForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required #login tags to ensure users are logged in before accessing certain files
def profile(request):
    context ={
        'user' : request.user  #current user is requested
    }
    return render(request,'app/profile.html',context)

@login_required
def editprofile(request,pk):   # this is the edit profile definition which takes user and a private key which django defines in order to delete users
    user = get_object_or_404(User, pk=pk) 
    if request.method == "POST":
        form = UserRegisterForm(request.POST,instance=user) # a form is created and is populated with the user instance variables 
        
        if form.is_valid():
                form.save()       #form is saved and user is redirected to home
                return redirect('home')

    else:
            form = UserRegisterForm(instance=user)

            context = {
                'form':form,
                'user':user,
            }
            return render(request,'app/signup.html',context)

@login_required
def deleteprofile(request,pk):   #followes same functionality editprofile 
        user = get_object_or_404(User, pk=pk)
        if request.method == "POST":
            form = UserRegisterForm(request.POST,instance=user) #form is used again, user must type in values to further confirm deletion of account
            user.delete()
            return redirect('home')
        else:
            form = UserRegisterForm(instance=user)
            context = {
                'form':form,
                'user':user,
          
            }
            return render(request,'app/signup.html',context)


def logout_view(request): ##logout view
    logout(request)
    return render(request, 'app/logout.html')

@login_required
def userpostnew(request):  #New post view for users 
    if request.method == 'POST':
        form = Userpostform(request.POST) #Userpostformis created and defined 
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
def post_list_admin(request): #postlist for specific user, this is used for the my posts seciton of the application
    context = {
        'posts': Post.objects.filter(author=request.user).order_by('date_posted'), #request-user ensures current user instance is used

    }
    return render(request,'app/post_list.html',context)



@login_required 
def edit_post(request, pk):  #post edit functiionality 
    post = get_object_or_404(Post, pk=pk) #private key and Post variables are passed to obtain current post
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
def delete_post(request,pk):  #delete post functionality 
        post = get_object_or_404(Post, pk=pk) #current post and private key are used to obtain current post
        if request.method == "POST":
            form = Userpostform(request.POST,instance=post)
            post.delete() #post is deleted 
            return redirect('post-list')
        else:
            form = Userpostform(instance=post)
            context = {
                'form':form,
                'post':post,
          
            }
            return render(request,'app/userpostnew.html',context)

def search(request): #this is search functionality
    template = "app/index.html"
    query = request.GET.get('q') #query is definied in the search tags 
    results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)) #the query is compared to title and content data within the database
    context = {
        'posts': results
    }
    return render(request,'app/index.html',context) #this is then passed to the index html page which uses posts and return the results