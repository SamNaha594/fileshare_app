from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from fileshare_app.forms import FileUploadForm
from fileshare_app.models import UploadedFile
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.



def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'fileshare_app/upload_file.html', {'form': form})

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'fileshare_app/file_list.html', {'files': files})

def file_share(request, file_id):
    file_obj = get_object_or_404(UploadedFile, id=file_id)
    file_url = request.build_absolute_uri(file_obj.file.url)
    # return HttpResponse(f"File link: {file_url}")
    return render(request, 'share_file.html', {'file_url': file_url})


def upload_success(request):
    return render(request, 'upload_success.html')



# def download_file(request, file_id):
    # file_obj = get_object_or_404(UploadedFile, id=file_id)
    # file_path = file_obj.file.path
    # with open(file_path, 'rb') as file:
    #     response = HttpResponse(file.read(), content_type='application/force-download')
    #     response['Content-Disposition'] = f'attachment; filename={file_obj.file.name}'
    # return response
def download_file(request, filename):
    print(filename)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)  # Assuming the file is in the MEDIA_ROOT folder
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse("File not found", status=40)



