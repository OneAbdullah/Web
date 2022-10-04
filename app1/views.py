from django.shortcuts import render
from .models import *
from django.core.files.storage import FileSystemStorage
from webapp.settings import BASE_DIR
import os
from .enhance import enh

#render homepage
def home(request):
    template = "home.html"
    context = {}
    return render(request,template,context)

#render result page
def ret(request):
    template = "return.html"
    context = {}
    if request.method == 'POST':
        obj = images_to_binarize()
        #saving input image
        image = request.FILES['upd']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        obj.input_image = filename
        obj.save()

        #creating directory of input image
        temp = os.path.join(BASE_DIR, "media")
        temp = os.path.join(temp, filename)

        #creating directory of output image
        temp2 = os.path.join(BASE_DIR, "media")
        temp2 = os.path.join(temp2, filename.split(".")[0]+"_bined.png")

        #binarizing file using DE-GAN Algorithm
        enh(BASE_DIR,temp,temp2)

        #saving processed image in database
        obj.output_image = filename.split(".")[0]+"_bined.png"
        obj.save()

        context['obj'] = obj
    return render(request,template,context)

#render suggestion page
def suggest(request):
    template = "suggest.html"
    context = {}
    if request.method == 'POST':
        #adding suggestion to database
        obj = suggestion()
        obj.name = request.POST['name']
        obj.email = request.POST['email']
        obj.note = request.POST['note']
        obj.save()
        context['message'] = "Your suggestion has been recieved successfully! Thank you for the feedback."
    return render(request,template,context)