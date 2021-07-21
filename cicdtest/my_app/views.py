from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
	return HttpResponse('<h1><i>Hello, world!!!</i></h1>')
