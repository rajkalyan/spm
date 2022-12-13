from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, widgets
from Restaurant_app.models import Breads, Rice, Starters, Rolereq, User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from Restaurant import settings
class usgform(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2",
        "placeholder":"Enter Password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2",
        "placeholder":"ConfirmPassword",
    }))
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","mobilenumber","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Firstname",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Lastname",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter E-mail",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobilenumber",
            }),
            "uimg":forms.FileInput(attrs={
                "class":"form-control"
            })

        }

# class ItemsForm(forms.ModelForm):
#     class Meta:
#         model=Itemlist
#         fields = ["iname","icategory","iprice","iimage"]
#         widgets = {
#             "iname":forms.TextInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Enter name",
#             }),
#             "icategory":forms.Select(attrs={
#                "class":"form-control my-2",
#             }),
#             "iprice":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Enter Price",
#             })
#         }

class Startersform(forms.ModelForm):
    class Meta:
        model=Starters
        fields = ["sname","scategory","sprice","simage"]
        widgets = {
            "sname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter name",
            }),
            "scategory":forms.Select(attrs={
               "class":"form-control my-2",
            }),
            "sprice":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Price",
            })
        }
        
class Breadsform(forms.ModelForm):
    class Meta:
        model=Breads
        fields = ["bname","bprice"]
        widgets = {
            "bname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter name",
            }),
            "bprice":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Price",
            })
        }

class Riceform(forms.ModelForm):
    class Meta:
        model=Rice
        fields = ["rbname","rbcategory","rbprice"]
        widgets = {
            "rbname":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter name",
            }),
            "rbcategory":forms.Select(attrs={
               "class":"form-control my-2",
            }),
            "rbprice":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Price",
            })
        }
        
class Rltype(forms.ModelForm):
    class Meta:
        model = Rolereq
        fields= ["Uname","rltype"]
        widgets= {
            "rltype":forms.Select(attrs={
                "class":"form-control my-2"
            })
        }

class Rlupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","role"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":True,
            }),
            "role":forms.Select(attrs={
                "class":"form-control my-2",
            }),
        }

class Pfupd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","age","mobilenumber","uimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Age",
			}),
		"mobilenumber":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Mobile Number",
			}),
		}

class Chgepwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter Old Password"
		}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Password",
		}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2","placeholder":"Enter New Confirm Password",
		}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Userorder
#         fields = ["person","iname","iname_quantity","starters","starters_quantity","starters1","starters_quantity1",
#                   "mandi","mandi_quantity","mandi1","mandi_quantity1","desserts","desserts_quantity",
#                   "desserts1","desserts_quantity1"]
#         widgets = {
#             "iname":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item",
#             }),
#             "person":forms.TextInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Enter Ordering person name",
#             }),
#             "iname_quantity":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#             "starters":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item",
#             }),
#             "starters_quantity":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#             "starters1":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item"
#             }),
#             "starters_quantity1":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#             "mandi":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item"
#             }),
#             "mandi_quantity":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#             "mandi1":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item"
#             }),
#             "mandi_quantity1":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#             "desserts":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item"
#             }),
#             "desserts_quantity":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#             "desserts1":forms.Select(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select item"
#             }),
#             "desserts_quantity1":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Select quantity"
#             }),
#         }


# class Qform(forms.ModelForm):
#     class Meta:
#         model = Cart
#         fields = ["iname","iprice","iquant"]
#         widgets = {
#              "iname":forms.TextInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Enter name",

#             }),
#             "iprice":forms.NumberInput(attrs={
#                 "class":"form-control my-2",
#                 "placeholder":"Enter Price",
#                 "readonly":True,
#             }),
#             "iquant":forms.NumberInput(attrs={
#                 "Class":"form-control my-2",
#                 "placeholder":"Enter quantity"
#             })
#         }