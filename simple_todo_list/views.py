
from django.shortcuts import render
from django.http import HttpResponse

def main(req):
    return render(req, 'main.html', {})

