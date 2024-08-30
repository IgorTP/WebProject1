from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def render_index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/index.html")


def render_page_1(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_1.html")


def render_page_2(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_2.html")


def render_page_cond_operators(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_3.html")


def render_page_cycles(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="main_app/page_4.html")
