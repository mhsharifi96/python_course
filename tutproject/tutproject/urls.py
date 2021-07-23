
from django.contrib import admin
from django.urls import path,include
import django.contrib.auth.urls
urlpatterns = [
    path('todo/', include('todo.urls')),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),

]
