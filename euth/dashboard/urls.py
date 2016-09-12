from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.dashboard,
        name='dashboard'),
    url(r'^profile$',
        views.DashboardProfileView.as_view(),
        name='dashboard-profile'),
    url(r'^(?P<organisation_slug>[-\w_]+)/profile$',
        views.DashboardProfileView.as_view(),
        name='dashboard-profile-org'),
    url(r'^(?P<organisation_slug>[-\w_]+)/projects/$',
        views.DashboardProjectListView.as_view(),
        name='dashboard-project-list'),
    url(r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/$',
        views.DashboardProjectUpdateView.as_view(),
        name='dashboard-project-edit'),
    url(r'^(?P<organisation_slug>[-\w_]+)/projects/(?P<slug>[-\w_]+)/users$',
        views.DashboardProjectUserView.as_view(),
        name='dashboard-project-users'),
    url(r'^(?P<organisation_slug>[-\w_]+)/projects/'
        r'(?P<slug>[-\w_]+)/users/invite$',
        views.DashboardProjectInviteView.as_view(),
        name='dashboard-project-invite'),
]
