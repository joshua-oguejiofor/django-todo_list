from django import forms
from .models import Todo


# ModelForm automatically builds form fields based on the Todo model,
# so we don't have to redefine each field by hand
class TodoForm(forms.ModelForm):
    class Meta:
        # Which model this form is tied to
        model = Todo
        # Which model fields should appear on the form
        fields = ['title', 'description', 'completed']
        # Customize the HTML widgets/attributes for a nicer look
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Details (optional)'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
