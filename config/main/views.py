
from django.shortcuts import render,redirect,get_object_or_404
from.models import Product
def home(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request,'home.html', context)

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        quantity = request.POST.get('quantity')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image,
            quantity=quantity
        )

        return redirect('home')

    return render(request, 'create.html')
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')

        if request.FILES.get('image'):
            product.image = request.FILES.get('image')

        product.save()
        return redirect('home')

    return render(request, 'update.html', {'product': product})
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()

    return redirect('home')