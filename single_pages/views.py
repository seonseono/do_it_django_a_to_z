from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html',
        # html 문서는 무조건 templates 폴더 안에 있어야 함
        # single_pages 앱(패키지)에 templates 폴더 생성
        # templates 폴더 안에 single_pages 폴더 생성 후 html 파일 생성
        # single_pages(landing.html 파일이 있는)에 templates 라는 속성이 있기 때문에
        # 이름이 같아도 충돌이 일어나지 않음
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

