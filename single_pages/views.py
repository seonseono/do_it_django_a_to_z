from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html',
        # html 문서는 무조건 templates 폴더 안에 있어야함
        # single_pages 앱에 templates 폴더 생성
        # templates 폴더 안에 또 single_pages 폴더 생성
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

