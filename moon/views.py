from django.shortcuts import render


def reconstruct(request):
    template_file = 'moon/reconstruct.html'
    return render(request, template_file)
