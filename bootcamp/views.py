from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.shortcuts import render, redirect
from .models import  Articles , Messages , Feeds
from .forms import SignUpForm , MyForm , FeedsForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,update_session_auth_hash


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def indexPage(request):
	return render(request, 'index.html', {})


@login_required(redirect_field_name='login')
def profile(request):
	registerd_user=  str(request.user.get_full_name()).title()
	feeds= Feeds.objects.order_by('last_modified')
	form=FeedsForm()
	context={
		'registerd_user':registerd_user,
		'feeds_list': feeds,
		'form':form	}
	if request.method == 'POST':
		print('here')
		form=FeedsForm()
		status = request.POST.get('text')
		user =  request.user
		b= Feeds(status=status, user=user)
		b.save()
		return redirect('profile')
	else:
		form=FeedsForm()
	return render(request, 'profile.html', context)
# Create your views here.

@login_required(redirect_field_name='login')
def articles(request):
	registerd_user=  str(request.user.get_full_name()).title()
	articles= Articles.objects.order_by('last_modified')
	form=MyForm()
	context={
		'registerd_user':registerd_user,
		'articles_list': articles,
		'form':form	}
	if request.method == 'POST':
		print('here')
		form=MyForm()
		text = request.POST.get('text')
		title = request.POST.get('title')
		user =  request.user
		b= Articles(article=text, author=user, title=title)
		b.save()
		return redirect('articles')
	else:
		form=MyForm()
	return render(request, 'articles.html', context)

@login_required(redirect_field_name='login')
def messages(request):
	registerd_user=  str(request.user.get_full_name()).title()
	context = {
		'registerd_user':registerd_user
	}
	return render(request, 'messages.html', context)

def create_articles(request):
	registerd_user=  str(request.user.get_full_name()).title()
	context = {
		'registerd_user':registerd_user
	}
	return render(request, 'create_articles.html', context)

