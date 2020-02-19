from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
	"""
	Renders the cart content page
	"""
	return render(request, "cart/cart.html")

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        print(cart)
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))

    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))
