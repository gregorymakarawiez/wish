//var form=$('#signupForm');
//var submit_button=$("#signupForm .btn[type='submit']");
var first_name_input=$("#signupForm input[name='first_name']");
var last_name_input=$("#signupForm input[name='last_name']");
var username_input=$("#signupForm input[name='username']");
var email_input=$("#signupForm input[name='email']");

//var is_form_valid = false;
//var is_username_valid = false;


/*function validateForm(){
        if (is_username_valid){
            is_form_valid=true;
            form.addClass('valid');
        }else{
            form.addClass('invalid');
        }
}*/



function validate_min_length(input_widget, params){

    var min_length=params['min_length'];

    var value=input_widget.val();

    if (value.length>=min_length){
        is_valid=true;
        input_widget.addClass('valid');
        input_widget.removeClass('invalid');
    }else{
        is_valid=false;
        input_widget.addClass('invalid');
        input_widget.removeClass('valid');
    }
    return is_valid;
}

function validate_max_length(input_widget, params){

    var max_length=params['max_length'];

    var value=input_widget.val();

    if (value.length<=max_length){
        is_valid=true;
        input_widget.addClass('valid');
        input_widget.removeClass('invalid');
    }else{
        is_valid=false;
        input_widget.addClass('invalid');
        input_widget.removeClass('valid');
    }
    return is_valid;
}

function validate_range_length(input_widget,params){

    var min_length=params['min_length'];
    var max_length=params['max_length'];

    var value=input_widget.val();

    if (value.length>=min_length && value.length<=max_length){
        is_valid=true;
        input_widget.addClass('valid');
        input_widget.removeClass('invalid');
    }else{
        is_valid=false;
        input_widget.addClass('invalid');
        input_widget.removeClass('valid');
    }
    return is_valid;
}


/*function validateForm() {

    is_first_name_valid=validate_min_length(first_name_input,1);
    is_last_name_valid=validate_min_length(last_name_input,1);
    is_username_valid=validate_min_length(username,1);

};

function validateUsername_sav() {
    var username=user_name_input.val();

    if (username.length>3){
        is_username_valid=true;
        user_name_input.addClass('valid');
        user_name_input.removeClass('invalid');
    }else{
        is_username_valid=false;
        user_name_input.addClass('invalid');
        user_name_input.removeClass('valid');
    }
};*/





function initialization(){

    validators=[
        {widget: first_name_input, event: 'keyup', validator: validate_min_length, params: {min_length: 1}},
        {widget: last_name_input, event: 'keyup', validator: validate_min_length, params: {min_length: 1}},
        {widget: username_input, event: 'keyup', validator: validate_min_length, params: {min_length: 2}}
    ];

    // link validators to widget events


    for (var i=0;i<validators.length;i++){
        widget=validators[i].widget;
        validator=validators[i].validator;
        params=validators[i].params;
        validator(widget,params);
    }

    for (var i=0;i<validators.length;i++){
        widget=validators[i].widget;
        event=validators[i].event;
        validator=validators[i].validator;
        params=validators[i].params;
        widget.on(event,function(){
            validator(widget,params);
        });

        //validator(widget,params);
    }
    //submit_button.click(validateForm());



}



$(document).ready(function() {
    initialization();


});