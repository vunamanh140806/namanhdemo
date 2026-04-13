from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['ProductName', 'Supplier', 'Category', 'QuantityPerUnit', 'OldPrice', 'UnitPrice', 'UnitsInStock', 'UnitsOnOrder', 'ReorderLevel', 'Discontinued']
        widgets = {
            'ProductName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập tên sản phẩm'}),
            'Supplier': forms.Select(attrs={'class': 'form-select'}),
            'Category': forms.Select(attrs={'class': 'form-select'}),
            'QuantityPerUnit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: Hộp 10 cái'}),
            'OldPrice': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giá cũ'}),
            'UnitPrice': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giá mới'}),
            'UnitsInStock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'UnitsOnOrder': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'ReorderLevel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'Discontinued': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'ProductName': 'Tên sản phẩm',
            'Supplier': 'Nhà cung cấp',
            'Category': 'Danh mục',
            'QuantityPerUnit': 'Đơn vị tính',
            'OldPrice': 'Giá cũ',
            'UnitPrice': 'Đơn giá',
            'UnitsInStock': 'Tồn kho',
            'UnitsOnOrder': 'Hàng đang giao',
            'ReorderLevel': 'Mức đặt lại',
            'Discontinued': 'Ngừng kinh doanh'
        }
