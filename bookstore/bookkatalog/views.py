from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from .forms import ReviewForm


def home(request):
    return render(request, 'bookkatalog/home.html')


def books(request):
    book_list = Book.objects.all()

    return render(request, 'bookkatalog/book_list.html', context={ 'books':book_list})


def book_detail(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)

    # Получаем все отзывы, связанные с книгой
    reviews = Review.objects.filter(book=book)

    # Если POST-запрос, обрабатываем форму
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  # Не сохраняем сразу
            review.book = book  # Привязываем отзыв к конкретной книге
            review.save()  # Сохраняем отзыв
            return redirect('book_detail', book_id=book.id)  # Перенаправляем обратно на страницу книги
    else:
        form = ReviewForm()  # Пустая форма для GET-запроса

    # Передаем книгу, отзывы и форму в шаблон
    return render(request, 'bookkatalog/book_detail.html', context={
        'book': book,
        'reviews': reviews,
        'form': form
    })
