from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_product, name='create-product'),
    path('read', views.read_product, name='read-all-products'),
    path('update/<int:id>', views.update_product, name='update-products'),
    path('delete', views.delete_view, name='delete-product')
]


# urlpatterns = [
#     # path("", mainmenu),
#     path("books/", books, name="books"),
#     path("detail/<int:id>/", book_detail, name="detail"),
# ]


# urlpatterns = [
#     path('create', create_book, name='create-product'),
#     path('read', books, name='read-all-products'),
# ]