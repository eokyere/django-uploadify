import os
import time
import uuid

from django.conf import settings

def upload_handler(FILES):
    file = FILES['Filedata']

    DEST_DIR = settings.UPLOADIFY_UPLOAD_PATH+"/"+time.strftime('%Y/%m/%d')

    try:
        os.makedirs(DEST_DIR, 0755)
    except Exception, e:
        print "Exception:",str(e)
        pass

    ext = file.name.split('.')[-1]
    fileName = "%s.%s" % (uuid.uuid4(), ext)
    destination = open(DEST_DIR + "/" + fileName, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)

    return (file.name, fileName, DEST_DIR)
