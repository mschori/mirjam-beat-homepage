from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WeddingImage, WeddingVideo


@login_required()
def list_images(request):
    """
    List all images and vidoes.
    :param request: request from user
    :return: rendered list of images and videos
    """
    return render(request, 'wedding/list_images.html', {
        'images': WeddingImage.objects.all().order_by('pk'),
        'videos': WeddingVideo.objects.all().order_by('pk')
    })
