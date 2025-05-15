from django import forms
from .models import CashFlow, Category, Subcategory, Status, Type

class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['created_at', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.type.categories.all()
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories.all()

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        type_ = cleaned_data.get('type')
        if category and type_ and category.type != type_:
            self.add_error('category', 'Категория не соответствует выбранному типу.')
        if subcategory and category and subcategory.category != category:
            self.add_error('subcategory', 'Подкатегория не соответствует выбранной категории.')
        if not cleaned_data.get('amount'):
            self.add_error('amount', 'Поле "Сумма" обязательно.')
        return cleaned_data

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class CashFlowFilterForm(forms.Form):
    date_from = forms.DateField(
        label='Дата от',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    date_to = forms.DateField(
        label='Дата до',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    status = forms.ModelChoiceField(
        label='Статус',
        queryset=Status.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    type = forms.ModelChoiceField(
        label='Тип',
        queryset=Type.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subcategory = forms.ModelChoiceField(
        label='Подкатегория',
        queryset=Subcategory.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )