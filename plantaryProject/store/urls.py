from django.urls import path
import store.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    path('', store.views.storemain, name='storemain'),
    path('storemanager/', store.views.storemanager, name='storemanager'),
    path('registerproduct/', store.views.registerproduct, name='registerproduct'),
    path('product/<int:product_id>/', store.views.productdetail, name='productdetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)