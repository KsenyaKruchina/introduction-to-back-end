from django.shortcuts import render, redirect
from .forms import CreateThingForm
from django.contrib import messages
from .models import Thing


def index_page_view(request):
    return redirect('/things')


def things_page_view(request):
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


def todo_details_view(request, pk):
    thing = Thing.objects.get(id=pk)
    return render(request, 'todo/todo_details.html', {'thing': thing})


def delete_things_page_view(request, pk):
    try:
        thing = Thing.objects.get(id=pk)
        thing.delete()
        return redirect('/things')
    except Thing.DoesNotExist:
        error = 'No tasks found.'
        messages.error(request, message=error)
        return redirect('/things')


def edit_todo_view(request, pk):
    if request.method == 'GET':
        thing = Thing.objects.get(id=pk)
        form = CreateThingForm(data={'title': thing.title, 'description': thing.description, 'due_date': thing.due_date,
                                     'status': thing.status})

        return render(request, 'todo/edit_todo.html', {'thing': thing, 'form': form})
    if request.method == 'POST':
        thing = Thing.objects.get(id=pk)
        form = CreateThingForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            status = form.data.get('status') == 'on'
            thing.title = title
            thing.description = description
            thing.due_date = due_date
            thing.status = status
            thing.save()
            return redirect(f'/things/{thing.id}/details')
