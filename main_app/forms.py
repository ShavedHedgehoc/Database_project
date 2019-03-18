from django import forms


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

# class MyForm(forms.Form):
    
#     def __init__(self, *args, **kwargs):
#         super(MyForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'id-exampleForm'
#         self.helper.form_class = 'blueForms'
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'submit_survey'

#         self.helper.add_input(Submit('submit', 'Submit'))
# class MyForm(forms.Form):
    
#     my_name=forms.CharField(label='My name')
    
#     def __init__(self, *args, **kwargs):
#         super(MyForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))