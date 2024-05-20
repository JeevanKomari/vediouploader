from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, HttpResponse
from .forms import *

def UploadFile(request):
    if request.method == 'POST':
        serializer = BlogForm(request.POST,request.FILES)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('The file is saved')
    else:
        form = BlogForm()
    context = {'form':form,}
    return render(request, 'upload.html', context)