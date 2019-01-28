from django.shortcuts import render


def index(request):
    template_file = 'moon/index.html'
    return render(request, template_file)


def reconstruct(request):
    template_file = 'moon/reconstruct.html'
    return render(request, template_file)
