from django.shortcuts import render, redirect,HttpResponseRedirect, Http404
from .forms import registerUser, CommentForm, CartForm, FilterSearchForm
from django.contrib.auth.models import User as registUser
from django.contrib.auth import login as auth_login, authenticate, logout
from . models import book, order, Comment
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import functools
import difflib

def main(request):
    print(book.objects.filter(categories__name='В тренді'))
    return render(request, template_name='index.html', context={'title_name': 'Головна', 'books': book.objects.filter(categories__name='В тренді'), 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def about_us(request):
    return render(request, template_name='about-us.html', context={'title_name': 'Про нас', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def account(request):
    if request.user.is_authenticated:
        orders = order.objects.filter(user__id=request.user.id)
        return render(request, template_name='account.html', context={'title_name': 'Акаунт', 'orders': orders, 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})
    else:
        return redirect('/account-login')


def account_login(request):
    if request.user.is_authenticated:
        return redirect('/account')
    return render(request, template_name='account-login.html', context={'title_name': 'Вхід', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def account_register(request):
    return render(request, template_name='account-register.html', context={'title_name': 'Реєстрація', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def contact(request):
    return render(request, template_name='contact.html', context={'title_name': 'Контакти', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def shop(request):
    print(list(request.user.shopping_cart.all()))
    for i in list(request.user.shopping_cart.all()):
        print(i.name)
    return render(request, template_name='shop-three-columns.html', context={'title_name': 'Магазин', 'books': book.objects.all(), 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def shop_cart(request):
    return render(request, template_name='shop-cart.html', context={'title_name': 'Продукт', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def shop_checkout(request):
    if request.user.is_authenticated:
        price = 0
        for i in list(request.user.shopping_cart.all()):
            price += i.price
        return render(request, template_name='shop-checkout.html', context={'title_name': 'Вибір', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False, 'total': price})
    else:
        return redirect('/account-login')


def shop_compare(request):
    return render(request, template_name='shop-compare.html', context={'title_name': 'Формування', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})
def _compute_similarity_score(text1, text2, comp="basic"):
    if comp == "basic":
        text1_set = {word.lower() for word in text1.split()}
        text2_set = {word.lower() for word in text2.split()}
        return len(text1_set & text2_set)
    else:
        return difflib.SequenceMatcher(None, text1, text2).ratio()


def shop_threee_columns(request):
    return render(request, template_name='shop-threee-columns.html', context={'title_name': 'Каталог товарів', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def search_page(request):
    books = None
    form = FilterSearchForm(request.GET)
    print(4234)
    if form.is_valid():
        query = form.cleaned_data.get("query")
        maxprice = form.cleaned_data.get("maxprice")
        category_pk = form.cleaned_data.get("category")
        print(232)
        if category_pk:
            books = book.objects.filter(categories__pk=category_pk) \
                                .filter(price__lte=maxprice)
        else:
            books = book.objects.filter(price__lte=maxprice)
        books = list(books)
        if query:
            comp = functools.partial(_compute_similarity_score, query)
            books = [(book, comp(str(book).replace(",", "")))
                     for book in books]
            books.sort(key=lambda book_meta: book_meta[1], reverse=True)
            books = [book_meta[0] for book_meta in books if book_meta[1] > 0.1]
    else:
        books = book.objects.all()
    print(324)
    print(dict(
        books=books,
        form=form,
        super=request.user.is_superuser
    ))
    print(324)
    return render(request, "shop-three-columns.html", dict(
        books=books,
        form=form,
        super=request.user.is_superuser
    ))

def shop_wishlist(request):

    return render(request, template_name='shop-wishlist.html', context={{'title_name': 'Кошик', 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False}})


def single_product(request, id):
    if request.user.is_authenticated:
        is_comment_allowed = False
        if not request.user.is_authenticated:
            is_comment_allowed = False
        else:
            is_comment_allowed = (
                    not request.user.comments.filter(book__pk=id).exists()
            )
        if request.method == "GET" or not is_comment_allowed:
            print(request.user.is_superuser)
            print()
            return render(request, template_name='single-product.html',
                          context={'title_name': 'Продукт', 'book': book.objects.get(id=id),
                                   'genre': list(book.objects.get(id=id).categories.all()), 'is_comment_allowed': is_comment_allowed, 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book.objects.get(id=id)
            comment.author = request.user
            comment.save()

    return render(request, template_name='single-product.html', context={'title_name': 'Продукт', 'book': book.objects.get(id=id), 'genre': list(book.objects.get(id=id).categories.all()),
                                                                         'is_comment_allowed': False, 'Cart': list(request.user.shopping_cart.all()) if request.user.is_authenticated else False})


def log(request):
    if(request.user.is_authenticated):
        logout(request)
    return redirect('/account-login')



def by(request):
    if request.user.is_authenticated:
        phone = request.POST['phone']
        address = request.POST['address']
        if phone and address:
            d = list(request.user.shopping_cart.all())
            for boo in d:
                ord = order(adress=address,
                            phone=phone,
                            count=1,
                            price=boo.price,
                            book=boo,
                            user=request.user)
                ord.save()
                request.user.shopping_cart.remove(boo)
            return redirect('/account')
        else:
            return redirect('/by/' + str(id))
    else:
        return redirect(redirect('/account-login'))

def register(request):
    if request.method == 'POST':
        new = registerUser(request.POST)
        if new.is_valid():
            user = registUser.objects.create_user(
                username=new.cleaned_data['username'],
                email=new.cleaned_data['email'],
                password=new.cleaned_data['password']

            )
            user.save()
            return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth_login(request, user)
            # Перенаправление на "правильную" страницу
            return redirect('/')
        else:
            # Отображение страницы с ошибкой
            return redirect('/h')


@login_required
@require_POST
def shopping_cart_submit(request):
    books = list(request.user.shopping_cart.all())
    request.user.books.add(*books)
    request.user.shopping_cart.clear()
    request.user.save()

    for book in books:
        book.holders_count += 1
        book.save()

    return redirect("shopping_cart")

@login_required
@require_POST
def shopping_cart_add(request):
    form = CartForm(request.POST)
    if not form.is_valid():
        return redirect("/")
    book_pk = form.cleaned_data.get("book_pk")
    try:
        Book = book.objects.get(pk=book_pk)
    except Book.DoesNotExists:
        return redirect("/")

    request.user.shopping_cart.add(Book)
    request.user.save()
    return redirect(form.cleaned_data.get("next_link"))

@login_required
@require_POST
def shopping_cart_remove(request):
    form = CartForm(request.POST)
    if not form.is_valid():
        return redirect("/")
    book_pk = form.cleaned_data.get("book_pk")
    try:
        Book = book.objects.get(pk=book_pk)
    except Book.DoesNotExists:
        return redirect("/")

    request.user.shopping_cart.remove(Book)
    request.user.save()
    return redirect(form.cleaned_data.get("next_link"))