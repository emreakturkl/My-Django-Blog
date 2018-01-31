from .models import *
from .forms import CommentForm
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def home(request):  
    try:
        categories = Category.objects.all()
        header_title = About.objects.all()[0].header_title
        header_twitter = About.objects.all()[0].header_twitter
        header_linkedin = About.objects.all()[0].header_linkedin
        header_github = About.objects.all()[0].header_github

        home_title = About.objects.all()[0].home_title
        home_image = About.objects.all()[0].home_image
        home_text = About.objects.all()[0].home_text
        home_twitter = About.objects.all()[0].home_twitter

        footer_text = About.objects.all()[0].footer_text
        footer_text_url = About.objects.all()[0].footer_text_url
        footer_image   = About.objects.all()[0].footer_image
        favicon = About.objects.all()[0].favicon

    except IndexError:
        pass
    
    return render_to_response('home.html',locals())

def about(request):
    try:
        categories = Category.objects.all()
        header_title = About.objects.all()[0].header_title
        header_twitter = About.objects.all()[0].header_twitter
        header_linkedin = About.objects.all()[0].header_linkedin
        header_github = About.objects.all()[0].header_github


        about_image = About.objects.all()[0].about_image
        about_text = About.objects.all()[0].about_text
        about_social = About.objects.all()[0].about_social

        footer_text = About.objects.all()[0].footer_text
        footer_text_url = About.objects.all()[0].footer_text_url
        footer_image   = About.objects.all()[0].footer_image
        favicon = About.objects.all()[0].favicon

    except IndexError:
        pass

    return render_to_response('about.html', locals())

def contact(request):
    try:
        categories = Category.objects.all()
        header_title = About.objects.all()[0].header_title  
        header_contact = About.objects.all()[0].header_contact
        header_twitter = About.objects.all()[0].header_twitter
        header_linkedin = About.objects.all()[0].header_linkedin
        header_github = About.objects.all()[0].header_github

        footer_text = About.objects.all()[0].footer_text
        footer_text_url = About.objects.all()[0].footer_text_url
        footer_image   = About.objects.all()[0].footer_image
        favicon = About.objects.all()[0].favicon

    except IndexError:
        pass

    return render_to_response('contact.html', locals())


def category(request, category_url):
    try:
        categories = Category.objects.all()
        header_title = About.objects.all()[0].header_title 
        header_twitter = About.objects.all()[0].header_twitter
        header_linkedin = About.objects.all()[0].header_linkedin
        header_github = About.objects.all()[0].header_github

        footer_text = About.objects.all()[0].footer_text
        footer_text_url = About.objects.all()[0].footer_text_url
        footer_image   = About.objects.all()[0].footer_image
        favicon = About.objects.all()[0].favicon

    except IndexError:
        pass

    category = get_object_or_404(Category, category_url=category_url)
    return render_to_response('blog/category.html', locals())



def post_list(request):
    try:
        categories = Category.objects.all()
        header_title = About.objects.all()[0].header_title
        header_twitter = About.objects.all()[0].header_twitter
        header_linkedin = About.objects.all()[0].header_linkedin
        header_github = About.objects.all()[0].header_github

        footer_text = About.objects.all()[0].footer_text
        footer_text_url = About.objects.all()[0].footer_text_url
        footer_image   = About.objects.all()[0].footer_image
        favicon   = About.objects.all()[0].favicon  


    except IndexError:
        pass

    object_list = Post.objects.all()
    paginator = Paginator(object_list , 3)
    page_request_var = 'page'
    page = request.GET.get( page_request_var )

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except(EmptyPage, InvalidPage):
        object_list = paginator.page(paginator.num_pages)

    context= {
        "object_list": object_list,
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render_to_response('blog/blog.html', locals())


def post_details(request, slug):
    try:
        categories = Category.objects.all()
        header_title = About.objects.all()[0].header_title
        header_twitter = About.objects.all()[0].header_twitter
        header_linkedin = About.objects.all()[0].header_linkedin
        header_github = About.objects.all()[0].header_github

        footer_text = About.objects.all()[0].footer_text
        footer_text_url = About.objects.all()[0].footer_text_url
        footer_image   = About.objects.all()[0].footer_image
        favicon = About.objects.all()[0].favicon 

    except IndexError:
        pass

    yazi = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = yazi
            comment.save()
            messages.success(request, 'Yorumunuz Gönderildi.', extra_tags='alert-success')
            return redirect('/blog/%s/'%slug)
        else:
            messages.warning(request, 'Yorumunuz Gönderilemedi.', extra_tags='alert-danger')
    else:
        comment_form = CommentForm()

    comments = Comment.objects.filter(published=True, post=yazi)
    paginator = Paginator(comments , 5)
    page_request_var = 'page'
    page = request.GET.get( page_request_var )

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except(EmptyPage, InvalidPage):
        comments = paginator.page(paginator.num_pages)

    context= {
        "comments": comments,
        "title": "List",
        "page_request_var": page_request_var,
    }

    
    return render(request,'blog/post.html', locals())

# HTTP Error 400
def error404(request):
    return render_to_response('404.html')

