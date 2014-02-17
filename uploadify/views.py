import os
import time
import uuid
import json

from django.conf import settings
from django.http import HttpResponse

from sorl.thumbnail import get_thumbnail

def upload(request):
    if request.session.has_key('form_img'):
        try:
            removeMe = settings.MEDIA_ROOT+"/"+request.session['form_img']
            os.unlink(removeMe)
        except Exception, e:
            print "Exception:",str(e)
            pass

    file = request.FILES['Filedata']

    RELATIVE_DEST_DIR = settings.UPLOADIFY_UPLOAD_PATH+"/"+time.strftime('%Y/%m/%d')
    DEST_DIR = settings.MEDIA_ROOT+"/"+RELATIVE_DEST_DIR

    try:
        os.makedirs(DEST_DIR, 0755)
    except Exception, e:
        print "Exception:",str(e)
        pass

    ext = file.name.split('.')[-1]
    fileName = "%s.%s" % (uuid.uuid4(), ext)
    SessionDestination = RELATIVE_DEST_DIR + "/" + fileName
    Destination = DEST_DIR + "/" + fileName

    destination = open(Destination, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)

    request.session['form_img'] = SessionDestination
    #return (file.name, fileName, DEST_DIR)
    return HttpResponse(json.dumps({'status':'uploaded', 'file':SessionDestination}), content_type="application/json")

def uploaded_view(request):
    if request.session.has_key('form_img'):
        img = get_thumbnail(request.session['form_img'], '200x200', crop='center', format="PNG")
        return HttpResponse('<img alt="Image" border="0" src="'+settings.MEDIA_URL+img.name+'" width="'+str(img.width)+'" height="'+str(img.height)+'">')
    return HttpResponse('No hay imagen', content_type='text/html')

def get_image_path(request):
    return request.session['form_img']
