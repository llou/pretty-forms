from django.forms.utils import RenderableFormMixin, ErrorDict, ErrorList

class ErrorDict(ErrorDict):
    template_name = 'bulma/errors/dict/default.html'
    template_name_text = 'bulma/errors/dict/text.txt'
    template_name_ul = 'bulma/errors/dict/ul.html'


class ErrorList(ErrorList):
    template_name = 'bulma/errors/list/default.html'
    template_name_text = 'bulma/errors/list/text.txt'
    template_name_ul = 'bulma/errors/list/ul.html'

