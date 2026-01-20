from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .forms import TodoForm
from .models import Todo

def index(request):
    item_list=Todo.objects.order_by("-date")
    form = TodoForm()

    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Item addes successfully!')
            return redirect('todo')
    

    page={
            'forms':form,
            'list':item_list,
            'title':'TODO LIST',

        }
    return render(request,'todo/index.html',page)

def remove(request,item_id):
    try:

        item=Todo.objects.get(id=item_id)
        item.delete()
        messages.info(request,'item removed successfully!!!')
    except Todo.DoesNotExist:
        messages.error(request,'Item does not exist!')


    return redirect('todo')