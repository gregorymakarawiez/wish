from Wish import settings
from django import forms
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt






class MyQuillWidget(forms.Widget):
    # some documentation on how to embed Quill in a web site
    # https://quilljs.com/docs/quickstart/

    class Media:
        css= {
            'all': (
                settings.STATIC_URL + 'quill/css/quill.snow.css',
                settings.STATIC_URL + 'quill/css/quill_editor.css',
             )
        }
        js = (settings.STATIC_URL + 'quill/js/quill.min.js',
        )


    def render(self, name, value, attrs=None):
        flat_attrs = flatatt(attrs)


        html = '''

        <textarea name="%(name)s" style="display:none;"> %(value)s </textarea>

        <div id="%(name)s_editor" class="quill_editor">
            <div id="%(name)s_toolbar"></div>
            <div id="%(name)s_content">
            </div>
        </div>

        <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>

        <script>


            $(document).ready(function(){

                // instantiate quill editor
                var quill_%(name)s = new Quill('#%(name)s_content',{ // ace editor
                    modules:{
                        toolbar:[
                            [{ 'font': [] }],
                            [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
                            [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
                            ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                            [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
                            [{ 'list': 'ordered'},{ 'list': 'bullet'}],
                            [{ 'align': [] }]
                        ],
                    },
                    placeholder: 'compose an epic...',
                    theme: 'snow'
                });

                // create handle to DOM hidden textarea
                var textarea_%(name)s = $('textarea[name="%(name)s"]'); // hidden textarea to save editor content

                // on page loading, get db saved content that django has restored into DOM hidden textarea
                var insert_text=textarea_%(name)s.val();

                if (insert_text==' None '){
                   insert_text='{}';
                }

                try{
                    var insert_json=JSON.parse(insert_text);
                }
                catch(e){
                    console.error("Parsing error:", e);
                }
                quill_%(name)s.setContents(insert_json); // on DOM loading, copy hidden textarea content into quill editor
                quill_%(name)s.on("text-change", function () {
                    var save_json=quill_%(name)s.getContents() ;
                    var save_txt=JSON.stringify(save_json);
                    textarea_%(name)s.val(save_txt); // whenever quill editor content change, copy change back into hidden textarea
                });
            });

        </script>
        ''' % {'name': name, 'value': value}

        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        print(data.get(name, name))
        return data.get(name, name)


class MyQuillWidget2(forms.Widget):
    # some documentation on how to embed Quill in a web site
    # https://quilljs.com/docs/quickstart/

    class Media:
        css= {
            'all': (
                settings.STATIC_URL + 'quill/css/quill.snow.css',
                settings.STATIC_URL + 'quill/css/quill_editor.css',
             )
        }
        js = (settings.STATIC_URL + 'quill/js/quill.min.js',
        )


    def render(self, name, value, attrs=None):
        flat_attrs = flatatt(attrs)


        html = '''

        <textarea name="%(name)s" style="display:none;"> %(value)s </textarea>

        <div id="%(name)s_editor" class="quill_editor">
            <div id="%(name)s_toolbar"></div>
            <div id="%(name)s_content">
            </div>
        </div>


        <script>


            $(document).ready(function(){

                // instantiate quill editor
                var quill_%(name)s = new Quill('#%(name)s_content',{ // ace editor
                    modules:{
                        toolbar:[
                            [{ 'font': [] }],
                            [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
                            [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
                            ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                            [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
                            [{ 'list': 'ordered'},{ 'list': 'bullet'}],
                            [{ 'align': [] }]
                        ],
                    },
                    placeholder: 'compose an epic...',
                    theme: 'snow'
                });

                // create handle to DOM hidden textarea
                var textarea_%(name)s = $('textarea[name="%(name)s"]'); // hidden textarea to save editor content

                // on page loading, get db saved content that django has restored into DOM hidden textarea
                var insert_text=textarea_%(name)s.val();

                if (insert_text==' None '){
                   insert_text='{}';
                }

                try{
                    var insert_json=JSON.parse(insert_text);
                }
                catch(e){
                    console.error("Parsing error:", e);
                }
                quill_%(name)s.setContents(insert_json); // on DOM loading, copy hidden textarea content into quill editor
                quill_%(name)s.on("text-change", function () {
                    var save_json=quill_%(name)s.getContents() ;
                    var save_txt=JSON.stringify(save_json);
                    textarea_%(name)s.val(save_txt); // whenever quill editor content change, copy change back into hidden textarea
                });
            });

        </script>
        ''' % {'name': name, 'value': value}

        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        print(data.get(name, name))
        return data.get(name, name)



class MyQuillWidget3(forms.Widget):
    # some documentation on how to embed Quill in a web site
    # https://quilljs.com/docs/quickstart/

    class Media:
        css= {
            'all': (
                "https://cdn.quilljs.com/1.3.6/quill.snow.css",
                "https://cdn.quilljs.com/1.3.6/quill.core.css",
             )
        }
        js = ("https://cdn.quilljs.com/1.3.6/quill.min.js",
              "https://cdn.quilljs.com/1.3.6/quill.core.js"
        )


    def render(self, name, value, attrs=None):
        flat_attrs = flatatt(attrs)


        html = '''

        <div id="editor">
            <p>Hello World!</p>
            <p>Some initial <strong>bold</strong> text</p>
            <p><br></p>
        </div>

        <!-- Include the Quill library -->
        <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>

        <!-- Initialize Quill editor -->
        <script>

            var quill = new Quill('#editor', {
                theme: 'snow'
            });


        </script>



        ''' % {'name': name, 'value': value}

        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        print(data.get(name, name))
        return data.get(name, name)



class MyQuillWidget4(forms.Widget):
    # some documentation on how to embed Quill in a web site
    # https://quilljs.com/docs/quickstart/

    class Media:
        css= {
            'all': (
                settings.STATIC_URL + 'quill/css/quill.snow.css',
                settings.STATIC_URL + 'quill/css/quill_editor.css',
             )
        }
        js = (settings.STATIC_URL + 'quill/js/quill.min.js',
        )


    def render(self, name, value, attrs=None):
        flat_attrs = flatatt(attrs)


        html = '''

        <textarea name="%(name)s" style="display:none;"> %(value)s </textarea>

        <div id="%(name)s_editor" class="quill_editor">
            <div id="%(name)s_toolbar"></div>
            <div id="%(name)s_content">
            </div>
        </div>

        <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>

        <script>




            // instantiate quill editor
            var quill_%(name)s = new Quill('#%(name)s_content',{ // ace editor
                modules:{
                    toolbar:[
                        [{ 'font': [] }],
                        [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
                        [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
                        ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                        [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
                        [{ 'list': 'ordered'},{ 'list': 'bullet'}],
                        [{ 'align': [] }]
                    ],
                },
                placeholder: 'compose an epic...',
                theme: 'snow'
            });

            // create handle to DOM hidden textarea
            var textarea_%(name)s = $('textarea[name="%(name)s"]'); // hidden textarea to save editor content

            // on page loading, get db saved content that django has restored into DOM hidden textarea
            var insert_text=textarea_%(name)s.val();

            if (insert_text==' None '){
               insert_text='{}';
            }

            try{
                var insert_json=JSON.parse(insert_text);
            }
            catch(e){
                console.error("Parsing error:", e);
            }
            quill_%(name)s.setContents(insert_json); // on DOM loading, copy hidden textarea content into quill editor
            quill_%(name)s.on("text-change", function () {
                var save_json=quill_%(name)s.getContents() ;
                var save_txt=JSON.stringify(save_json);
                textarea_%(name)s.val(save_txt); // whenever quill editor content change, copy change back into hidden textarea
            });


        </script>
        ''' % {'name': name, 'value': value}

        return mark_safe(html)

    def value_from_datadict(self, data, files, name):
        print(data.get(name, name))
        return data.get(name, name)