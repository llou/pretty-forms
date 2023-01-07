from django.forms import models
from . import widgets

class BaseModelForm(models.BaseModelForm):
    template_name_div = "bulma/div.html"
    template_name_p = "bulma/p.html"
    template_name_table = "bulma/table.html"
    template_name_ul = "bulma/ul.html"
    template_name_label = "bulma/label.html"


class ModelForm(BaseModelForm, metaclass=models.ModelFormMetaclass):
    pass


class InlineForeignKeyField(models.InlineForeignKeyField):
    widget = widgets.HiddenInput


class ModelChoiceField(models.ModelChoiceField):
    widget = widgets.Select
    

class ModelMultipleChoiceField(models.ModelChoiceField):
    widget = widgets.SelectMultiple
    hidden_widget = widgets.MultipleHiddenInput
    
