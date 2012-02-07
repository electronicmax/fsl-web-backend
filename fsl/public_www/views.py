from django.http import HttpResponseRedirect, HttpResponse

import sys,string,time,logging
import tempfile,os

logging.basicConfig(filename=os.sep.join([tempfile.gettempdir(),"fsl-www-log"+repr(int(time.time()))]),level=logging.DEBUG)

def post_email(req):
    import public_www.models as m
    address = req.GET['address']
    if m.Email.objects.filter(address=address).count() == 0:
        em = m.Email(address=address)
        em.save()
        logging.debug('saved email address %s, id: %d' % (address, em.id))
    response = HttpResponse('ok', 'text/html');
    response.status_code = 200
    return response
