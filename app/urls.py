from django.contrib import admin
from django.urls import path
from cars.views import CarsView, NewCarView, UpdateCarView, CarDetailView, DeleteCarView
from accounts.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),

    ## Passwort Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', CarsView.as_view(), name='cars'),
    path('new_car/', NewCarView.as_view(), name='new_car'),
    path('delete_car/<int:id>', DeleteCarView.as_view(), name='delete_car'),
    path('detail_car/<int:id>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:id>/update/', UpdateCarView.as_view(), name='update_car'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
