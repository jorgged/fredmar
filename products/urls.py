from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='products'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('categoria/<str:category>/',views.SearchCategory.as_view(),name='search_category'),
    path('contacto/',views.ContactView.as_view(),name='contact'),
    path('preguntar/',views.Preguntar,name='preguntar'),
    # path('about/',views.ProductSearchView.as_view(),name='product_search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
