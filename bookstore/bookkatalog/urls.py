from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('books', views.BooksView.as_view(), name='books'),
    path('book_detail/<int:book_id>', views.BookDetail.as_view(), name='book_detail'),
    path('review_done', views.ReviewDone.as_view(), name='review_done')
]