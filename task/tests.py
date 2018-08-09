from django.test import TestCase
from django.test import Client
from .models import Unit, Employee
from django.contrib.auth.models import User
from .forms import SignupForm
from Wish import settings



class Test_CreateTask(TestCase):


    def setUp(self):
        # Every test needs a client.
        self.client = Client(HTTP_USER_AGENT='Mozilla/5.0')



    def test_signup_form(self):
        """
            creation of one valid account
        """

        # create new unit
        unit = Unit(name="disney")
        unit.save()

        # employee data
        data = {
            'first_name': 'Scrooge',
            'last_name': 'Mcduck',
            'username': 'Scrooge',
            'password': 'dollar123',
            'email': 'scooge.mcduck@disney.com',
            'unit': str(unit.pk),
            'manager': '',
            'is_manager': 'True',
            'is_continuous_improvement_officer': 'True',
            'subscribed_to_newsletter': 'True',
        }

        # invoke form
        form=SignupForm(data)

        # test data validity
        self.assertIs(form.is_valid(), True)


    def test_signup_valid_account(self):
        """
            creation of one valid account
        """

        # create new unit
        unit = Unit(name="disney")
        unit.save()

        # employee data
        data = {
            'first_name': 'Scrooge',
            'last_name': 'Mcduck',
            'username': 'Scrooge',
            'password': 'dollar123',
            'email': 'scooge.mcduck@disney.com',
            'unit': str(unit.pk),
            'manager': '',
            'is_manager': 'True',
            'is_continuous_improvement_officer': 'True',
            'subscribed_to_newsletter': 'True',
        }

        # emulate client response
        response=self.client.post('/account/signup/',data, follow=True)

        # check that new employee has been correctly saved in database
        saved_employee=Employee.objects.filter(user__username="Scrooge")
        self.assertEqual(saved_employee.exists(),True)

        # check redirection to signin url
        self.assertRedirects(response,expected_url=settings.LOGIN_URL,target_status_code=200)


        # login new employee
        data = {
            'username': 'Scrooge',
            'password': 'dollar123',
        }
        response = self.client.post('/account/signin/', data, follow=True)

        # check redirection to home
        self.assertRedirects(response, expected_url='/task/', target_status_code=200)


    def test_signup_username_already_in_use(self):
        """
            creation of two accounts:
             - 1st one: a valid account
             - 2nd one: invalid, because has the same username as 1s account
        """

        # create new unit
        unit = Unit(name="disney")
        unit.save()

        # data for 1st employee
        data1 = {
            'first_name': 'Scrooge',
            'last_name': 'Mcduck',
            'username': 'Scrooge',
            'password': 'dollar123',
            'email': 'scooge.mcduck@disney.com',
            'unit': str(unit.pk),
            'manager': '',
            'is_manager': 'True',
            'is_continuous_improvement_officer': 'True',
            'subscribed_to_newsletter': 'True',
        }

        # data for 1st employee
        data2 = {
            'first_name': 'Scrooge',
            'last_name': 'Mcduck',
            'username': 'Scrooge',
            'password': 'dollar123',
            'email': 'donald.mcduck@disney.com',
            'unit': str(unit.pk),
            'manager': '',
            'is_manager': 'True',
            'is_continuous_improvement_officer': 'True',
            'subscribed_to_newsletter': 'True',
        }

        # create 1st employee
        response = self.client.post('/account/signup/', data1, follow=True)

        # check that 1st employee has been correctly saved in database
        saved_employee = Employee.objects.filter(user__username="Scrooge")
        self.assertEqual(saved_employee.exists(), True)

        # create 2nd employee
        response = self.client.post('/account/signup/', data2, follow=True)

        # count nb of saved instances in db that have the same username
        # if =1, the 2nd employee has not been created (as expected)
        nb_employee_with_same_username = Employee.objects.filter(user__username="Scrooge").count()
        self.assertEqual(nb_employee_with_same_username,1)

        # check redirection to signin url
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain==[],True)

        # check that error message is showing
        self.assertContains(response, 'Sorry, that username is already in use, please forward another one')



    def test_signup_email_already_in_use(self):
        """
            creation of two accounts:
             - 1st one: a valid account
             - 2nd one: invalid, because has the same email as 1s account
        """

        # create new unit
        unit = Unit(name="disney")
        unit.save()

        # data for 1st employee
        data1 = {
            'first_name': 'Scrooge',
            'last_name': 'Mcduck',
            'username': 'Scrooge1',
            'password': 'dollar123',
            'email': 'scooge.mcduck@disney.com',
            'unit': str(unit.pk),
            'manager': '',
            'is_manager': 'True',
            'is_continuous_improvement_officer': 'True',
            'subscribed_to_newsletter': 'True',
        }

        # data for 1st employee
        data2 = {
            'first_name': 'Scrooge',
            'last_name': 'Mcduck',
            'username': 'Scrooge2',
            'password': 'dollar123',
            'email': data1['email'],
            'unit': str(unit.pk),
            'manager': '',
            'is_manager': 'True',
            'is_continuous_improvement_officer': 'True',
            'subscribed_to_newsletter': 'True',
        }

        # create 1st employee
        response = self.client.post('/account/signup/', data1, follow=True)

        # check that 1st employee has been correctly saved in database
        saved_employee = Employee.objects.filter(user__email=data1['email'])
        self.assertEqual(saved_employee.exists(), True)

        # create 2nd employee
        response = self.client.post('/account/signup/', data2, follow=True)

        # count nb of saved instances in db that have the same email
        # if =1, the 2nd employee has not been created (as expected)
        nb_employee_with_same_email = Employee.objects.filter(user__email=data1['email']).count()
        self.assertEqual(nb_employee_with_same_email, 1)

        # check redirection to signin url
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain == [], True)

        # check that error message is showing
        self.assertContains(response, 'Sorry, that email is already in use, please forward another one')