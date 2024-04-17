from django.shortcuts import render, redirect

from .forms import FileUploadForm
from .models import FileUpload

import uuid


from django.http import JsonResponse

def main(request):
    #테이블의 모든 데이터 가져오기
    pictures = FileUpload.objects.all()

    #뷰에 전달해서 출력
    #return render(request, "main.html", {'result': pictures})
    return JsonResponse({"list": list(pictures.values())})

#요청을 처리하는 함수
def fileUpload(request):
    #하나의 요청 처리 메서드에서 요청 방식에 따라 처리
    if request.method == "GET":
        fileuploadForm = FileUploadForm

        context = {
            'fileuploadForm': fileuploadForm,
        }
        #fileupload.html 파일을 출력
        return render(request, 'fileupload.html', context)
    elif request.method == "POST":
        #파라미터 읽기
        title = request.POST["title"]
        content = request.POST['content']
        img = request.FILES['imgfile']

        #파일 업로드되는 이름을 수정
        idx = img.name.rfind(".") #.의 마지막 위치 찾기
        #확장자가 없으면 uuid를 뒤에 추가하고 확장자가 있는 경우는 확장자 앞에 추가
        #이 구문이 없어도 업로드 가능한데 중복되는 이름을 회피하기 위해서 수행
        if idx != -1:
            img.name = img.name[:idx] + str(uuid.uuid4()) + img.name[idx:]
        else:
            img.name = img.name + str(uuid.uuid4())

        #데이터베이스에 저장할 객체를 생성
        fileupload = FileUpload(
            title = title,
            content = content,
            imgfile = img
        )

        #데이터베이스에 저장
        fileupload.save() #ORM - SQL을 사용하지 않고 객체를 이용해서 데이터베이스 작업
        return redirect('/') #작업이 끝나면 / 요청을 수행



