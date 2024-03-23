from django.shortcuts import render, redirect
from .forms import CreateThingForm

from .models import Thing


def index_page(request):
    if request.method == 'GET':
        form = CreateThingForm()
        things = Thing.objects.all()
        return render(request, 'todo/index.html', {'things': things, 'form': form})
    elif request.method == 'POST':
        print(request.POST)

        form = CreateThingForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            due_date = form.cleaned_data.get('due_date')
            print(due_date)
            status = form.cleaned_data.get('status')
            thing = Thing(title=title, description=description, due_date=due_date, status=status)
            thing.save()
            return redirect(request.path)
        else:
            things = Thing.objects.all()
            return render(request, 'todo/index.html', {'things': things, 'form': form})


def todo_details(request, pk):
    things = Thing.objects.get(id=pk)
    return render(request, 'todo/todo_details.html', {'things': things})


def delete_things(request, pk):
    try:
        thing = Thing.objects.get(id=pk)
        thing.delete()
        return redirect('/things')
    except Thing.DoesNotExist:
        return redirect('/things')

