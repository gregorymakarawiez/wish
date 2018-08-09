var $form = $("signup-form"),  $successMsg = $(".alert");


$.validator.addMethod("domain", function(value, element) {
  regex="^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@disney[.]com$"
  return this.optional(element) || value == value.match(regex);
});

$form.validate({
  rules: {
    first_name: {
      required: true,
      minlength: 3,
      maxlength: 30
    },
  last_name: {
      required: true,
      minlength: 3,
      maxlength: 30
    },
  username: {
      required: true,
      minlength: 3,
      maxlength: 30
    },
  email: {
      required: true,
      email: true,
      //pattern:"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@disney[.]com$"
      domain: true
    }
  },
  messages: {
    first_name: "Please specify your first name (between 3 and 30 characters)",
    last_name: "Please specify your last name (between 3 and 30 characters)",
    username: "Please specify your username (between 3 and 30 characters)",
    email: "Please specify a valid email address, only @disney.com domain are allowed"
  },
  submitHandler: function() {
    $successMsg.show();
  }
});