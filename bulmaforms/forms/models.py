from django.forms import models as forms_models
from django.db.models.utils import AltersData
from django.db import models
from .renderers import DjangoTemplates
from .utils import ErrorList
from . import widgets
from bulmaforms.forms import forms
from bulmaforms.forms import fields as bulmafields

import pdb; pdb.set_trace()

EQUIVALENCES_MODEL_FORM = {
    models.CharField: bulmafields.CharField(),
    models.IntegerField: bulmafields.IntegerField(),
    models.FloatField: bulmafields.FloatField(),
    models.DateField: bulmafields.DateField(),
    models.TimeField: bulmafields.TimeField(),
    models.DateTimeField: bulmafields.DateTimeField(),
    models.DurationField: bulmafields.DurationField(),
    models.EmailField: bulmafields.EmailField(),
    models.FileField: bulmafields.FileField(),
    models.ImageField: bulmafields.ImageField(),
    }

def formfield_callback(model_field, **kwargs):
    if model_field.__class__ in EQUIVALENCES_MODEL_FORM:
        field = EQUIVALENCES_MODEL_FORM[model_field.__class__]
        return field
    return None

class BaseModelForm(forms.BaseForm, AltersData):
    def __init__(
        self,
        data=None,
        files=None,
        auto_id="id_%s",
        prefix=None,
        initial=None,
        error_class=ErrorList,
        label_suffix=None,
        empty_permitted=False,
        instance=None,
        use_required_attribute=None,
        renderer=None,
    ):
        opts = self._meta
        if opts.model is None:
            raise ValueError("ModelForm has no model class specified.")
        if instance is None:
            # if we didn't get an instance, instantiate a new one
            self.instance = opts.model()
            object_data = {}
        else:
            self.instance = instance
            object_data = model_to_dict(instance, opts.fields, opts.exclude)
        # if initial was provided, it should override the values from instance
        if initial is not None:
            object_data.update(initial)
        # self._validate_unique will be set to True by BaseModelForm.clean().
        # It is False by default so overriding self.clean() and failing to call
        # super will stop validate_unique from being called.
        self._validate_unique = False
        super().__init__(
            data,
            files,
            auto_id,
            prefix,
            object_data,
            error_class,
            label_suffix,
            empty_permitted,
            use_required_attribute=use_required_attribute,
            renderer=renderer,
        )
        for formfield in self.fields.values():
            forms_models.apply_limit_choices_to_to_formfield(formfield)

class ModelForm(BaseModelForm, metaclass=forms_models.ModelFormMetaclass):
    pass


class ModelChoiceIterator(forms_models.ModelChoiceIterator):
    pass


class InlineForeignKeyField(forms_models.InlineForeignKeyField):
    widget = widgets.HiddenInput


class ModelChoiceField(forms_models.ModelChoiceField):
    widget = widgets.Select
    

class ModelMultipleChoiceField(forms_models.ModelChoiceField):
    widget = widgets.SelectMultiple
    hidden_widget = widgets.MultipleHiddenInput
