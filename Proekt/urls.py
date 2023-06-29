"""
URL configuration for Proekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from Fashionapp import views
from django.contrib.auth import views as auth_views

from Fashionapp.views import home, categories, shirts, cart, delete_item, addproduct, sunglasses, jeans, payment, shoes, \
    dresses, jackets, newest, sale

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name="home"),
                  path('home/', RedirectView.as_view(url='/', permanent=True)),
                  path('categories/', categories, name="categories"),
                  path('shirts/', shirts, name="shirts"),
                  path('cart/', cart, name='cart'),
                  path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
                  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
                  path('signup/', views.signup, name='signup'),
                  path('addproduct/', addproduct, name='addproduct'),
                  path('Sunglasses/', sunglasses, name="sunglasses"),
                  path('Jeans/', jeans, name="jeans"),
                  path('payment/', payment, name="payment"),
                  path('Shoes/', shoes, name="shoes"),
                  path('Dresses/', dresses, name="dresses"),
                  path('Jackets/', jackets, name="jackets"),
                  path('Newest/', newest, name="newest"),
                  path('Sale/', sale, name="sale"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Avtomatski da se kreira nov url za sekoja novo dodadena kolona i da se dopravi signal receiver
