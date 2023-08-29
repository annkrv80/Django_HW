from django.shortcuts import render
import logging



logger = logging.getLogger(__name__)

def index(request):
    logger.info("Посещение главной страницы")
    return render(request, 'main.html')

def about(request):
    logger.info("Посещение страницы обо мне")
    return render (request, 'about.html')
