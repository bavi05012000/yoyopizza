from django.conf.urls import url
from django.contrib import admin
from .models import PlaceOrder

admin.site.site_header = 'Yo Yo Pizza..!'
admin.site.site_title = 'Yo Yo Pizza'
admin.site.index_title = 'Place Order Portal'
admin.site.register(PlaceOrder)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]