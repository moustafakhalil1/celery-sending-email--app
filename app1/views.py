from django.http import HttpResponse
from .task import sendemail
# Create your views here.

def index(request):
    sendemail.delay('nipik40202@mnsaf.com')
    return HttpResponse("hellos")