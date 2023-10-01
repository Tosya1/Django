import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    text = "<h1>Hello world!</h1>"
    logger.info(" Index page accessed")
    return HttpResponse(text)


def about(request):
    text = "<h1>About us</h1>\
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt odio possimus, veritatis exercitationem soluta repudiandae vitae, autem voluptates architecto sequi quidem asperiores deleniti. Tenetur animi necessitatibus beatae aperiam temporibus repellendus.</p>"
    logger.info(" About page accessed")
    return HttpResponse(text)
