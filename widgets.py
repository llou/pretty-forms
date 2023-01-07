from django.forms import widgets
from django.forms.widgets import CheckboxInput

class Input:
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {"class" : "input"}
        else:
            if "class" in attrs:
                attrs["class"] = "input" + " " + attrs["class"]
            else:
                attrs["class"] = "input" 
        super().__init__(attrs=attrs)


class TextInput(Input, widgets.TextInput):
    pass


class NumberInput(Input, widgets.NumberInput):
    pass


class EmailInput(Input, widgets.EmailInput):
    pass


class URLInput(Input, widgets.URLInput):
    pass


class PasswordInput(Input, widgets.PasswordInput):
    pass


class HiddenInput(Input, widgets.HiddenInput):
    pass


class MultipleHiddenInput(HiddenInput, widgets.HiddenInput):
    pass


class FileInput(Input, widgets.FileInput):
    pass


class ClearableFileInput(FileInput, widgets.FileInput):
    pass


class Textarea(widgets.Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {"class" : "textarea"}
        else:
            if "class" in attrs:
                attrs["class"] = "textarea" + " " + attrs["class"]
            else:
                attrs["class"] = "textarea" 
        super().__init__(attrs=attrs)



class DateTimeBaseInput(Input, widgets.TextInput):
    pass


class DateInput(DateTimeBaseInput, widgets.DateInput):
    pass


class DateTimeInput(DateTimeBaseInput, widgets.DateTimeInput):
    pass


class TimeInput(DateTimeBaseInput, widgets.TimeInput):
    pass


class Select(widgets.Select):
    template_name = "bulma/widgets/select.html"
    option_template_name = "bulma/widgets/select_option.html"


class SelectMultiple(widgets.SelectMultiple):
    template_name = "bulma/widgets/select.html"
    option_template_name = "bulma/widgets/select_option.html"


class RadioSelect(widgets.RadioSelect):
    template_name = "bulma/widgets/radio.html"
    option_template_name = "bulma/widgets/radio_option.html"


class CheckboxSelectMultiple(widgets.CheckboxSelectMultiple):
    template_name = "bulma/widgets/checkbox_select.html"
    option_template_name = "bulma/widgets/checkbox_option.html"


class MultiWidget(widgets.MultiWidget):
    template_name = "bulma/widgets/multiwidget.html"
    

class SplitDateTimeWidget(widgets.SplitDateTimeWidget):
    template_name = "bulma/widgets/splitdatetime.html"


class SplitHiddenDateTimeWidget(widgets.SplitHiddenDateTimeWidget):
    template_name = "bulma/widgets/splithiddendatetime.html"


class SelectDateWidget(widgets.SelectDateWidget):
    template_name = "bulma/widgets/select_date.html"
