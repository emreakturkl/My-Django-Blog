#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404,render,HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
# Create your views here.


def home(request):

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
    favicon   = About.objects.all()[0].favicon

    return render_to_response('home.html', locals())

def about(request):
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
    favicon   = About.objects.all()[0].favicon

    return render_to_response('about.html', locals())

def contact(request):
    categories = Category.objects.all()
    header_title = About.objects.all()[0].header_title  
    header_contact = About.objects.all()[0].header_contact
    header_twitter = About.objects.all()[0].header_twitter
    header_linkedin = About.objects.all()[0].header_linkedin
    header_github = About.objects.all()[0].header_github

    footer_text = About.objects.all()[0].footer_text
    footer_text_url = About.objects.all()[0].footer_text_url
    footer_image   = About.objects.all()[0].footer_image
    favicon   = About.objects.all()[0].favicon

    return render_to_response('contact.html', locals())


def category(request, category_url):
    categories = Category.objects.all()
    header_title = About.objects.all()[0].header_title 
    header_twitter = About.objects.all()[0].header_twitter
    header_linkedin = About.objects.all()[0].header_linkedin
    header_github = About.objects.all()[0].header_github

    footer_text = About.objects.all()[0].footer_text
    footer_text_url = About.objects.all()[0].footer_text_url
    footer_image   = About.objects.all()[0].footer_image
    favicon   = About.objects.all()[0].favicon

    category = get_object_or_404(Category, category_url=category_url)
    return render_to_response('category.html', locals())



def post_list(request):
    categories = Category.objects.all()
    header_title = About.objects.all()[0].header_title
    header_twitter = About.objects.all()[0].header_twitter
    header_linkedin = About.objects.all()[0].header_linkedin
    header_github = About.objects.all()[0].header_github

    footer_text = About.objects.all()[0].footer_text
    footer_text_url = About.objects.all()[0].footer_text_url
    footer_image   = About.objects.all()[0].footer_image
    favicon   = About.objects.all()[0].favicon  

    object_list = Post.objects.order_by('-creation_date')
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
    return render_to_response('blog.html', locals())

@csrf_exempt
def post_details(request, slug):
    categories = Category.objects.all()
    header_title = About.objects.all()[0].header_title
    header_twitter = About.objects.all()[0].header_twitter
    header_linkedin = About.objects.all()[0].header_linkedin
    header_github = About.objects.all()[0].header_github

    footer_text = About.objects.all()[0].footer_text
    footer_text_url = About.objects.all()[0].footer_text_url
    footer_image   = About.objects.all()[0].footer_image
    favicon   = About.objects.all()[0].favicon  

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.slug = slug
            comment.save()
            return redirect('/blog/%s/'%slug)
    else:
        comment_form = CommentForm()


    comments = Comment.objects.filter(published=True).order_by('-created_date')
    yazi = get_object_or_404(Post, slug=slug)
    return render_to_response('post.html', locals())


# HTTP Error 400
def error404(request):
    return render_to_response('404.html')

