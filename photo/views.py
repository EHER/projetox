from django.shortcuts import render_to_response, get_object_or_404
from photo.models import Photo

def index(request):
	latest_photo_list = Photo.objects.all().order_by('-pubDate')[:5]
	return render_to_response('photo/index.html',{'latest_photo_list': latest_photo_list})

def show(request, photo_id):
	p = get_object_or_404(Photo, pk=photo_id)
	return render_to_response('photo/show.html', {'photo': photo})

