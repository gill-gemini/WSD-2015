from django.http import HttpResponse, Http404
from django.shortcuts import render
from models import product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    """
     try:
        p = product.objects.get(pk=product_id)
    except product.DoesNotExist:
        raise Http404("product does not exist")
    return render(request, 'webshop/product_view.html', {'product': p})

    #return HttpResponse("product {}".format(product_id))

def available_products(request):
    """
    Write your view implementations for exercise 4 here.
    Remove the current return line below.
    This view should render a page with a list of all available products.
    A product is available if it has a quantity that's bigger than 0.
    The template product_list.html is expecting a single parameter products
    in the context which refers to an iterable of Product objects.
Your job is to make the view retrieve the the available products,
use them to render the template and return an HttpResponse object that
contains the resulting string.
Note: The dummy implementation of the return statement is there for
other exercises. Replace it with the required return statement.

    """
    Product.objects.all()
    return HttpResponse("View not implemented!")
