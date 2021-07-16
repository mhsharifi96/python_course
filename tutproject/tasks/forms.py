from django import forms

from .models import Task

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit



# Python | Form validation using django
# refrence link : https://www.geeksforgeeks.org/python-form-validation-using-django/ 

class simpleForm(forms.Form):
    title = forms.CharField(max_length=10)
    description = forms.CharField( max_length=100,widget=forms.Textarea)
    PRIORITIES = (
        ('adanger', 'Priority High'),
        ('bwarning', 'Priority Medium'),
        ('csuccess', 'Priority Low')
    )
    priority = forms.ChoiceField(choices=PRIORITIES)

class TaskManualForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TaskManualForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    title = forms.CharField( max_length=20,widget=forms.TextInput(attrs={'placeholder': "title",'id':'test_id'}))
    
    description = forms.CharField( max_length=250,widget=forms.Textarea,)
    PRIORITIES = (
        ('adanger', 'Priority High'),
        ('bwarning', 'Priority Medium'),
        ('csuccess', 'Priority Low')
    )
    priority = forms.ChoiceField(choices=PRIORITIES,)

    def clean_title(self):
        super(TaskManualForm, self).clean() 
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class([
                'تو رو خدا بیشتر از پنجتا وارد کن خلاصمون کن:)'])


# این کلاس از کریسپی استفاده شده است 
# که نشان میدهد چقدر لوس بازی در می آورد :)
class ExampleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button btn-danger')
            )
        )

    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )






class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'date_of_creation', ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "What's on your mind today?"}),
            'description': forms.Textarea(attrs={'placeholder': "Describe your task ..", 'cols': 80, 'rows': 3}),
        }
    def clean_title(self):
        super(TaskForm, self).clean() 
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class([
                'اینم فارسی که خیالت راحت شه'])

    def clean(self):
        # data from the form is fetched using super function
        super(TaskForm, self).clean()
        
        # extract the title and text field from the data
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')

        # # conditions to be met for the title length
        # if len(title) < 5:
        #     self._errors['title'] = self.error_class([
        #         'Minimum 5 characters required'])
        if len(description) <10:
            self._errors['description'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data




# class UsernameForm(ModelForm):
#     class Meta:
#         model = Username
#         fields = '__all__'

#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': "Enter a username"}),
#         }

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         queryset = Username.objects.filter(username=username).count()
#         if queryset > 0:
#             raise forms.ValidationError('This username is already taken! Try a different one :)')
#         return username
