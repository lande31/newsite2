from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from .forms import ItemForm
from django.template import loader


def index(request):
    item_list = item.objects.all()
    #template= loader.get_template('food/index.html')
    context = {
        'item_list':item_list,

    }
   # return HttpResponse(item_list)
    #return HttpResponse(template.render(context,request))
    return render(request, 'food/index.html',context)


def love(request):
    return HttpResponse('home alone')

def detail(request, item_id):
    items = item.objects.get(pk=item_id)
    context ={
        'items':items,

    }

   # return HttpResponse('This is item no/id: %s' % item_id)
    return render(request, 'food/detail.html', context)

def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/add_item.html',{'form':form})
#update item
def update_item(request, id):
    data = item.objects.get(id = id)


    form = ItemForm(request.POST or None, instance =data)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/add_item.html', {'form': form, 'data':data})

def delete_item(request, id):
    data = item.objects.get(id=id)

    if request.method == 'POST':
        data.delete()
        return redirect('food:index')
    return render(request, 'food/delete-item.html', {'data': data})



