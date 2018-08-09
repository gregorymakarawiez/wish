from Wish import settings
from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
import json




class DatePickerWidget(forms.widgets.DateInput):

    class Media:

        css= {
            'all': (
                '//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',
             )
        }
        js = ('https://code.jquery.com/jquery-1.12.4.js',
              'https://code.jquery.com/ui/1.12.1/jquery-ui.js',
        )


    def __init__(self, attrs=None):

        default_attrs = {'disabled':'false', 'placeholder':''}

        if attrs:
           default_attrs.update(attrs)

        self.default_attrs=default_attrs

        super().__init__(default_attrs)



    def render(self, name, value, attrs=None):

        template_name='date_picker/date_picker.html'

        flat_attrs = flatatt(attrs)

        context={'name': name, 'value': value}
        context.update(self.default_attrs)
        context.update(self.attrs)

        html=render_to_string(template_name,context)
        return mark_safe(html)




class QuillWidget(forms.widgets.Textarea):
    # some documentation on how to embed Quill in a web site
    # https://quilljs.com/docs/quickstart/

    class Media:
        css= {
            'all': (
                settings.STATIC_URL + 'quill/css/quill.snow.css',
                settings.STATIC_URL + 'quill/css/quill_editor.css',
             )
        }
        js = ('https://code.jquery.com/jquery-1.12.4.js',
              'https://code.jquery.com/ui/1.12.1/jquery-ui.js',
              settings.STATIC_URL + 'quill/js/quill.min.js',
              "https://cdn.quilljs.com/1.3.6/quill.js",
        )

    def __init__(self, attrs=None):
        # Use slightly better defaults than HTML's 20x2 box


        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
           default_attrs.update(attrs)

        super().__init__(default_attrs)


    def render(self, name, value, attrs=None):

        flat_attrs = flatatt(attrs)

        default_attrs={'placeholder':'','disabled':'false'}
        context={'name': name, 'value': value}
        context.update(default_attrs)
        context.update(self.attrs)

        template_name='quill/quill.html'
        html=render_to_string(template_name,context)

        return mark_safe(html)


    def value_from_datadict(self, data, files, name):
        content=data.get(name, name)
        return content





    def value_from_datadict(self, data, files, name):
        content=data.get(name, name)
        return content
