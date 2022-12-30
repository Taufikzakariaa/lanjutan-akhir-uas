from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blogs),
    path('blog/', blogs, name='blog'),
    path('tambah/', Data_baru, name='data_baru'),
    path('blog/ubah/<int:id_data>', ubah_data, name='ubah_data'),
]
