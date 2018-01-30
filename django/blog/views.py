from django.http import HttpResponse


# Create your views here.
def post_list(requets):
    # 1. 브라우저에서 요청
    # 2. 요청이 runserver로 실행중인 서버에 도착
    # 3. runserver는 요청을 Django code로 전달
    # 4. Django code중 config.urls모듈이 해당 요청을 받음
    # 5. config.urls모듈은 ''(admin/를 제외한 모든 요청)을 blog.urls모듈로 전달
    # 6. blog.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수 (view)를 실행
    # 8. 함수의 실행 결과(리턴값)을 브라우저로 다시 전달

    # HTTP프로토콜로 텍스트 데이터 응답을 변환
    return HttpResponse('<html><body><h1>Post List</h1><p>Post 목록을 보여줄 예정입니다.</p></body>')

