from django.urls import path

from farm import views

urlpatterns=[
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('profile/',views.profile,name="profile"),
    path('my_crops/',views.crop_list_view,name="my_crops"),
    path('add_crop/',views.crop_create_view,name="crop_create"),
    path('edit_crop/<int:pk>',views.crop_update_view, name='crop_update'),
    path('delete_crop/<int:pk>',views.crop_delete_view, name='crop_delete'),
    path('detail_crops/<int:pk>',views.crop_detail_view, name='crop_detail'),
    path('crops_expenses/<int:crop_pk>',views.expense_create_view, name='expense_create'),
    path('crops_sales/<int:crop_pk>', views.sale_create_view, name='sale_create'),

]  #Here name is used for to use in html templates as urls
#'profile/',views.profile this links used to go into viewsfile (to functions)