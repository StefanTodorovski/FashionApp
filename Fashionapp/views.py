from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category, UserProfile
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Category, Product, UserProfile
from .models import Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, AddProductForm


def home(request):
    products = Product.objects.filter()
    context = {"product": products}
    return render(request, 'home.html', context=context)


def categories(request):
    query = request.GET.get('query')  # Retrieve the search query from the request

    if query:
        categoriess = Category.objects.filter(name__icontains=query).exclude(name__in=['Newest', 'Sale'])
    else:
        categoriess = Category.objects.exclude(name__in=['Newest', 'Sale'])

    context = {"categories": categoriess}
    return render(request, 'categories.html', context=context)



from django.shortcuts import redirect, render
from .models import Category, Product, Cart


def shirts(request):
    try:
        category = Category.objects.get(name="shirts")  # Get the "shirts" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')

        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'shirts.html', context=context)


# @login_required(login_url='login')
def cart(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in first to access your cart.")
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    user_cart = Cart.objects.filter(user=request.user)

    for item in user_cart:
        item.total_price = item.product.price * item.quantity

    context = {"cart": user_cart}
    return render(request, 'cart.html', context=context)


def delete_item(request, item_id):
    cart_item = Cart.objects.get(pk=item_id)
    cart_item.delete()
    return redirect('cart')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def addproduct(request):
    if request.method == "POST":
        print("View executed")
        form_data = AddProductForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            print("Form is valid")
            form = form_data.save(commit=False)  # Create a new post object but don't save it yet
            form.created_by = request.user  # Set the author to the current user
            form.save()  # Save the post
            messages.success(request, 'Product successfully added!')
            print("Post saved")
            return redirect('addproduct')
        else:
            print("Form errors:", form_data.errors)
    else:
        print("Request method:", request.method)

    context = {"form": AddProductForm}
    return render(request, 'addproduct.html', context=context)


def sunglasses(request):
    try:
        category = Category.objects.get(name="Sunglasses")  # Get the "Sunglasses" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'sunglasses.html', context=context)


def jeans(request):
    try:
        category = Category.objects.get(name="Jeans")  # Get the "Jeans" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'jeans.html', context=context)


def shoes(request):
    try:
        category = Category.objects.get(name="Shoes")  # Get the "Shoes" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'shoes.html', context=context)


def dresses(request):
    try:
        category = Category.objects.get(name="Dresses")  # Get the "Dresses" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'dresses.html', context=context)


def jackets(request):
    try:
        category = Category.objects.get(name="Jackets")  # Get the "Dresses" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'jackets.html', context=context)


def payment(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    user_cart = Cart.objects.filter(user=request.user)

    for item in user_cart:
        item.total_price = item.product.price * item.quantity

    context = {"cart": user_cart}
    return render(request, 'payment.html', context=context)


def newest(request):
    try:
        category = Category.objects.get(name="Newest")  # Get the "Dresses" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'newest.html', context=context)



def sale(request):
    try:
        category = Category.objects.get(name="Sale")  # Get the "Dresses" category
        products = Product.objects.filter(category=category)  # Filter products by category
    except Category.DoesNotExist:
        products = []  # Empty list if the category doesn't exist

    paginator = Paginator(products, 6)  # Limit 6 products per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    if request.method == 'POST' and 'add_to_cart' in request.POST:
        if not request.user.is_authenticated:
            messages.error(request, "Please log in first to access your cart.")
            return redirect('login')
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(pk=product_id)

        # Check if the item is already in the cart for the current user
        existing_item = Cart.objects.filter(user=request.user, product=product).first()

        if existing_item:
            # If the item exists, update the quantity
            existing_item.quantity += quantity
            existing_item.save()
        else:
            # If the item does not exist, create a new cart item
            Cart.objects.create(user=request.user, product=product, quantity=quantity)

        return redirect('cart')  # Redirect to the cart page

    context = {"products": page_obj}
    return render(request, 'sale.html', context=context)
