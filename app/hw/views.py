from django.shortcuts import render


def home(request):
    template_file = 'home.html'
    return render(request, template_file)
