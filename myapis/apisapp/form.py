from django import forms

class Login(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email','class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','class': 'form-control',
    }))

#for the boostrap styling
class Boot1(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email','class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','class': 'form-control',
    }))
#end of the bootsrap styling


class Register(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your name','class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email','class': 'form-control',
    }))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Your phone number','class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','class': 'form-control',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','class': 'form-control',
    }), label='Repeat password')


class Message1(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter message here...', 'class': 'form-control',
    }))
#for admin
class add_std(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Student name','class': 'form-control',
    }))
    admission_no = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'e.g 1004','class': 'form-control',
    }))
    form = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'e.g 1004','class': 'form-control',
    }))
    classteacher = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Mr. Kivinya','class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email','class': 'form-control',
    }))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Your phone number','class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','class': 'form-control',
    }))
    billed = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'20000','class': 'form-control',
    }))
    paid = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'16000','class': 'form-control',
    }))


#deregister form 
class Deregister(forms.Form):
    id_number = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Enter id / admission no.','class': 'form-control',
    }))

#for the quiz part 

class Quiz(forms.Form):
    Q1_CHOICES = [
    ('A', 'Uhuru Kenyatta'),
    ('B', 'Izaack Newton'),
    ('C', 'Jomo Kenyatta'),
    ('D', 'William Ruto'),
    ]
    Q2_CHOICES = [
    ('A', 'Kenya'),
    ('B', 'Tanzania'),
    ('C', 'Uganda'),
    ('D', 'Rwanda'),
    ]
    Q3_CHOICES = [
    ('A', 'Kisumu'),
    ('B', 'Kakamega'),
    ('C', 'Migori'),
    ('D', 'Victoria'),
    ]
    Q4_CHOICES = [
    ('A', 'Atlantic'),
    ('B', 'Indian'),
    ('C', 'Pacific'),
    ('D', 'Japanic'),
    ]
    Q5_CHOICES = [
    ('A', 'Lion'),
    ('B', 'Goat'),
    ('C', 'Elephant'),
    ('D', 'Cheetah'),
    ]
    q1 = forms.MultipleChoiceField(choices=Q1_CHOICES,
                                     widget=forms.RadioSelect,
                                     label='1.Who was the first president of Kenya?'
                                     )
    q2 = forms.MultipleChoiceField(choices=Q2_CHOICES,
                                     widget=forms.RadioSelect,
                                     label='2.Where is Mt.Kenya located?'
                                     )
    q3 = forms.MultipleChoiceField(choices=Q3_CHOICES,
                                     widget=forms.RadioSelect,
                                     label='3.Where is Lake Victoria located?'
                                     )
    q4 = forms.MultipleChoiceField(choices=Q4_CHOICES,
                                     widget=forms.RadioSelect,
                                     label='4.Which one is not a name of ocean?'
                                     )
    q5 = forms.MultipleChoiceField(choices=Q5_CHOICES,
                                     widget=forms.RadioSelect,
                                     label='4.Which one is not a wild animal?'
                                     )

#for the send coins
class sendCoin(forms.Form):
    personID = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Recepient ID', 'class':'form-control',
    }))
    Amount = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Amount to send', 'class':'form-control',
    }))
    Password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your password', 'class':'form-control',
    }))
#for the buy coins part
class buyCoin(forms.Form):
    Amount = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Amount to send', 'class':'form-control',
    }))
#for the coins login part
class coinLogin(forms.Form):
    Email = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Your email', 'class':'form-control',
    }))
    
    Password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your password', 'class':'form-control',
    }))
    