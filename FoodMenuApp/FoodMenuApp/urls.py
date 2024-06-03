
from django.contrib import admin
from django.urls import path, include
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', user_view.register, name='register'),
    path('login/', user_view.login_user, name='login'),
    path('logout/', user_view.logout_user, name='logout'),
    path('change_password/', user_view.pass_change, name='change_password')
]
