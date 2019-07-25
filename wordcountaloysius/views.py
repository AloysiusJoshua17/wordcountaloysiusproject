from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def home(request):
	return render(request, 'home.html')

def blog(request):
	return HttpResponse('this is the blog test')

def about(request):
	return render(request, 'about.html')

def count(request):
	xtext = request.GET['xtext']
	xtextlist = xtext.split()

	sortedList = Counter(xtextlist)

	sortedList = dict(sortedList)

	return render(request, 'count.html',{'xtext':xtext,'ctx':sortedList})