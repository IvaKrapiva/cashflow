from django.shortcuts import render, redirect, get_object_or_404  # Добавлен redirect
from .models import CashFlow, Status, Type, Category, Subcategory
from .forms import CashFlowForm, StatusForm, TypeForm, CategoryForm, SubcategoryForm, CashFlowFilterForm
from django.http import JsonResponse

def cashflow_list(request):
    cashflows = CashFlow.objects.all().order_by('-created_at')
    filter_form = CashFlowFilterForm(request.GET or None)

    # Если форма валидна, применяем фильтры
    if filter_form.is_valid():
        date_from = filter_form.cleaned_data.get('date_from')
        date_to = filter_form.cleaned_data.get('date_to')
        status = filter_form.cleaned_data.get('status')
        type_ = filter_form.cleaned_data.get('type')
        category = filter_form.cleaned_data.get('category')
        subcategory = filter_form.cleaned_data.get('subcategory')

        if date_from:
            cashflows = cashflows.filter(created_at__gte=date_from)
        if date_to:
            cashflows = cashflows.filter(created_at__lte=date_to)
        if status:
            cashflows = cashflows.filter(status=status)  # Фильтруем по объекту Status
        if type_:
            cashflows = cashflows.filter(type=type_)  # Фильтруем по объекту Type
        if category:
            cashflows = cashflows.filter(category=category)  # Фильтруем по объекту Category
        if subcategory:
            cashflows = cashflows.filter(subcategory=subcategory)  # Фильтруем по объекту Subcategory

    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request, 'dds/cashflow_list.html', {
        'cashflows': cashflows,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'filters': request.GET,
        'filter_form': filter_form,
    })

def cashflow_create(request):
    if request.method == 'POST':
        form = CashFlowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cashflow_list')
    else:
        form = CashFlowForm()
    return render(request, 'dds/cashflow_form.html', {'form': form, 'title': 'Создать запись'})

def cashflow_edit(request, pk):
    cashflow = get_object_or_404(CashFlow, pk=pk)
    if request.method == 'POST':
        form = CashFlowForm(request.POST, instance=cashflow)
        if form.is_valid():
            form.save()
            return redirect('cashflow_list')
    else:
        form = CashFlowForm(instance=cashflow)
    return render(request, 'dds/cashflow_form.html', {'form': form, 'title': 'Редактировать запись'})

def cashflow_delete(request, pk):
    cashflow = get_object_or_404(CashFlow, pk=pk)
    if request.method == 'POST':
        cashflow.delete()
        return redirect('cashflow_list')
    return render(request, 'dds/cashflow_confirm_delete.html', {'cashflow': cashflow})

def get_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

def status_list(request):
    statuses = Status.objects.all()
    return render(request, 'dds/status_list.html', {'statuses': statuses})

def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm()
    return render(request, 'dds/status_form.html', {'form': form, 'title': 'Создать статус'})

def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('status_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'dds/status_form.html', {'form': form, 'title': 'Редактировать статус'})

def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('status_list')
    return render(request, 'dds/status_confirm_delete.html', {'status': status})

def type_list(request):
    types = Type.objects.all()
    return render(request, 'dds/type_list.html', {'types': types})

def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('type_list')
    else:
        form = TypeForm()
    return render(request, 'dds/type_form.html', {'form': form, 'title': 'Создать тип'})

def type_edit(request, pk):
    type_ = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_)
        if form.is_valid():
            form.save()
            return redirect('type_list')
    else:
        form = TypeForm(instance=type_)
    return render(request, 'dds/type_form.html', {'form': form, 'title': 'Редактировать тип'})

def type_delete(request, pk):
    type_ = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        type_.delete()
        return redirect('type_list')
    return render(request, 'dds/type_confirm_delete.html', {'type': type_})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dds/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'dds/category_form.html', {'form': form, 'title': 'Создать категорию'})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dds/category_form.html', {'form': form, 'title': 'Редактировать категорию'})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'dds/category_confirm_delete.html', {'category': category})

def subcategory_list(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'dds/subcategory_list.html', {'subcategories': subcategories})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm()
    return render(request, 'dds/subcategory_form.html', {'form': form, 'title': 'Создать подкатегорию'})

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'dds/subcategory_form.html', {'form': form, 'title': 'Редактировать подкатегорию'})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('subcategory_list')
    return render(request, 'dds/subcategory_confirm_delete.html', {'subcategory': subcategory})

