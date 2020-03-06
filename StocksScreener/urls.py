"""StocksScreener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from schema_graph.views import Schema


admin.autodiscover()

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),

    path('grappelli/', include('grappelli.urls')),  # grappelli URLS

    path('admin/', admin.site.urls),

    path('users/', include('users.urls', namespace='users')),
    path('users/api/v1/', include('users.api_urls', namespace='users_api')),

    path('market/', include('market.urls', namespace='market')),
    path('market/api/v1/', include('market.api_urls', namespace='market_api')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('egx/', include('egx.urls', namespace='egx')),

    # path('crypto/', include('crypto.urls', namespace='crypto')),
    # path('forex/', include('forex.urls', namespace='forex')),

]

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("StocksScreener.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]


urlpatterns += [
    path("schema/", Schema.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
######################################################################
admin.site.site_header = "Stocks-Screener"
admin.site.site_title = "Stocks Screener"
admin.site.index_title = "Stocks Screener Admin"
#######################################################################
