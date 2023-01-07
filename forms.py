from django.forms import forms 

class BaseForm(forms.BaseForm):
    template_name_div = "bulma/div.html"
    template_name_p = "bulma/p.html"
    template_name_table = "bulma/table.html"
    template_name_ul = "bulma/ul.html"
    template_name_label = "bulma/label.html"

class Form(BaseForm, metaclass=forms.DeclarativeFieldsMetaclass):
    pass
