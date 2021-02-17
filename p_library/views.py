from .models import Book, Publisher, Author, Friend
from .forms import AuthorForm, BookForm, FriendForm, PublisherForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, redirect, render
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


def main_page(request):
    template = loader.get_template('book_list.html')
    books = Book.objects.all()
    b_data = {
        "books": books,
        "title": "БИБИЛИОТЕКА"
    }
    return HttpResponse(template.render(b_data, request))


def index(request):
    template = loader.get_template('index.html')
    # books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку", "books": books}
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publishers(request):
    template = loader.get_template('publisher.html')
    publishers = Publisher.objects.all()
    p_data = {
        "publishers": publishers,
    }
    return HttpResponse(template.render(p_data, request))


# добавление издательства
class PublisherCreate(CreateView):
    model = Publisher
    form_class = PublisherForm
    success_url = reverse_lazy('p_library:publishers')
    template_name = 'publisher_add.html'


# Создание книги
class BookAdd(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:main_page')
    template_name = 'manage_book.html'

# def book_add(request):
#     form = BookForm()
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             if 'avatar' in request.FILES:
#                 form.avatar = request.FILES['avatar']
#             form.save(commit=True)
#             return HttpResponse('Изображение загружено')
#         else:
#             print(form.errors)
#         return reverse_lazy('p_library:main_page')


class BookEdit(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:main_page')
    template_name = 'book_edit.html'


class BookDelete(DeleteView):
    model = Book
    form_class = BookForm
    fields = ["title", "author"]
    success_url = reverse_lazy('p_library:main_page')
    template_name = 'book_delete.html'


class AuthorAdd(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_add.html'


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'


class FriendAdd(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'manage_friend.html'


class FriendEdit(UpdateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'edit_friend.html'


def friends(request):
    template = loader.get_template('friend_list.html')
    friends = Friend.objects.all()
    p_data = {
        "friends": friends,
    }
    return HttpResponse(template.render(p_data, request))


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=1)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


def book_author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=1)
    BookFormSet = formset_factory(BookForm, extra=1)
    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')
        if author_formset.is_valid() and book_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            for book_form in book_formset:
                book_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
        book_formset = BookFormSet(prefix='books')
    return render(
        request,
        'manage_books_authors.html',
        {
            'author_formset': author_formset,
            'book_formset': book_formset,
        }
    )
