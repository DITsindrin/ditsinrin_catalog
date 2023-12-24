from django.core.exceptions import ValidationError

from .models import Product, ProductVersion
from django.forms import ModelForm


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'price', 'image',)

    def clean_title(self):
        title = self.cleaned_data['title']
        title_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for item in title_list:
            if item in title.lower():
                raise ValidationError(f'Название продукта не должно содержать {item}')

        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        description_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        for item in description_list:
            if item in description.lower():
                raise ValidationError(f'Описание продукта не должно содержать {item}')

        return description


class ProductUpdateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('title', 'description', 'category', 'image', 'price',)
        # exclude = ('views_count')

    def clean_title(self):
        title = self.cleaned_data['title']
        title_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for item in title_list:
            if item in title.lower():
                raise ValidationError(f'Название продукта не должно содержать {item}')

        return title

    def clean_description(self):
        description = self.cleaned_data['description']
        description_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']

        for item in description_list:
            if item in description.lower():
                raise ValidationError(f'Описание продукта не должно содержать {item}')

        return description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = ProductVersion
        # fields = '__all__'
        fields = ('product', 'version_number', 'version_name', 'version_flag',)
        # exclude = ('views_count')
