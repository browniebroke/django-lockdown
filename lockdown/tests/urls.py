from django.urls import path, re_path

from . import views

urlpatterns = [
    path('a/view/', views.a_view),
    path('locked/view/', views.locked_view),
    path('overridden/locked/view/', views.overridden_locked_view),
    re_path(r'^locked/view/with/exception1/', views.locked_view_with_exception),
    re_path(r'^locked/view/with/exception2/', views.locked_view_with_exception),
    re_path(r'^locked/view/with/ip_exception/',
        views.locked_view_with_ip_exception),
    re_path(r'^locked/view/with/ip_exception_ipv6/',
        views.locked_view_with_ip_exception_ipv6),
    re_path(r'^locked/view/with/ip_exception_subnet/',
        views.locked_view_with_ip_exception_subnet),
    re_path(r'^locked/view/with/ip_exception_ipv6_subnet/',
        views.locked_view_with_ip_exception_ipv6_subnet),
    re_path(r'^locked/view/with/extra/context/',
        views.locked_view_with_extra_context),
    re_path(r'^locked/view/until/yesterday/', views.locked_view_until_yesterday),
    re_path(r'^locked/view/until/tomorrow/', views.locked_view_until_tomorrow),
    re_path(r'^locked/view/after/yesterday/', views.locked_view_after_yesterday),
    re_path(r'^locked/view/after/tomorrow/', views.locked_view_after_tomorrow),
    re_path(r'^locked/view/until/and/after/', views.locked_view_until_and_after),
    path('auth/user/locked/view/', views.user_locked_view),
    path('auth/staff/locked/view/', views.staff_locked_view),
    path('auth/superuser/locked/view/', views.superuser_locked_view),
]
