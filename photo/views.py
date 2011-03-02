from django.http import HttpReponse
from django.template import Contex, loader
from photo.models import Photo

def index(request):
	latestPhotoList = Photo.objects.all().order_by('-pubDate')[:5]
	t = loader.get_template('photo/index.html')
	c = Context({
		'latestPhotoList': latestPhotoList,
	})
	return HttpReponse(t.render(c)) 	
