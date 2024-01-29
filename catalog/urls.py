from django.urls import path


from . import views
from .views import LoginView

from .views import GenreListCreateView

from .views import AuthorListCreateView,AuthorUpdateView



from .views import LanguageListCreateView

from .views import BookListCreateView
from .views import BorrowBookAPI


urlpatterns = [
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookListCreateView.as_view(), name='book-delete'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/languages/', LanguageListCreateView.as_view(), name='language-list-create'),
    path('api/languages/<str:name>/', LanguageListCreateView.as_view(), name='language-delete'),
    path('api/genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('api/genres/<str:name>/', GenreListCreateView.as_view(), name='genre-delete'),
    path('api/authors/', AuthorListCreateView.as_view(), name='author-view'),
    path('api/authors/create/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/delete/<str:first_name>/', AuthorListCreateView.as_view(), name='author-delete'),
    path('api/authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('api/borrow-books/', BorrowBookAPI.as_view(), name='borrow-book-list'),
    # Add other API patterns as needed
]




urlpatterns += [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
]


urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('book/<uuid:pk>/borrow/', views.borrow_book, name='borrow-book'),
]


# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]


# Add URLConf to list, view, create, update, and delete genre
urlpatterns += [
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genre/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete'),
]

# Add URLConf to list, view, create, update, and delete languages
urlpatterns += [
    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('language/<int:pk>', views.LanguageDetailView.as_view(),
         name='language-detail'),
    path('language/create/', views.LanguageCreate.as_view(), name='language-create'),
    path('language/<int:pk>/update/',
         views.LanguageUpdate.as_view(), name='language-update'),
    path('language/<int:pk>/delete/',
         views.LanguageDelete.as_view(), name='language-delete'),
]

# Add URLConf to list, view, create, update, and delete bookinstances
urlpatterns += [
    path('bookinstances/', views.BookInstanceListView.as_view(), name='bookinstances'),
    path('bookinstance/<uuid:pk>', views.BookInstanceDetailView.as_view(),
         name='bookinstance-detail'),
    path('bookinstance/create/', views.BookInstanceCreate.as_view(),
         name='bookinstance-create'),
    path('bookinstance/<uuid:pk>/update/',
         views.BookInstanceUpdate.as_view(), name='bookinstance-update'),
    path('bookinstance/<uuid:pk>/delete/',
         views.BookInstanceDelete.as_view(), name='bookinstance-delete'),
]

