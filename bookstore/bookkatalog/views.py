from .models import Book, Review
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "bookkatalog/register.html", {"form": form})


class HomeView(TemplateView):
    template_name = 'bookkatalog/home.html'


class BooksView(ListView):
    template_name = 'bookkatalog/book_list.html'
    model = Book
    context_object_name = 'books'


class BookDetail(FormView):
    form_class = ReviewForm
    template_name = 'bookkatalog/book_detail.html'
    success_url = '/review_done'

    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.get_book()  # Привязываем книгу к отзыву
        review.save()
        return super(BookDetail, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_book()
        context['book'] = self.get_book()
        context['reviews'] = Review.objects.filter(book=book)
        context['reviews'] = context['reviews'][:3]
        return context

    def get_book(self):
        book_id = self.kwargs.get('book_id')  # Используем `book_id` из URL
        return Book.objects.get(id=book_id)


class ReviewDone(TemplateView):
    template_name = 'bookkatalog/done.html'