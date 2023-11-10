from django.urls import path
from .import views

app_name='shop'

urlpatterns = [
    path('', views.goodsListView.as_view(), name='goods'),
    path('Listing/', views.CreateListingView.as_view(), name='Listing'),

    path('listing_done/',
        views.ListingSuccessView.as_view(),
        name='listing_done'),
]
