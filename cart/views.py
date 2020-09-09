from django.shortcuts import render

# Create your views here.


def cart_contents(request):
    """
    View that renders the cart content page
    """
    return render(request, "cart.html")
