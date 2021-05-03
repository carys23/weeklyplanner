from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"), 
    path("notes/", views.notes, name="notes"),
    path("notes2/", views.notes2, name="notes2"),
    path ('delete/<note_id>',views.delete, name='delete'),
    path ('cross_off/<note_id>',views.cross_off, name='cross_off'),
    path ('uncross/<note_id>',views.uncross, name='uncross'),
    path ('edit/<note_id>',views.edit, name='edit'),
    path ('edit_profile/', views.edit_profile, name='edit_profile'),
    path ('change_password/', views.change_password, name='change_password'),
]


# url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
#     url(r'^event/new/$', views.event, name='event_new'),
# 	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),