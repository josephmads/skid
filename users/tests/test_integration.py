from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.common.by import By
from selenium import webdriver


class SeleniumTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1440,1600')
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(10)

        User.objects.create_user(
            username='testertim',
            email='tim.timons@test.test',
            first_name='Tim',
            last_name='Timons',
            password='001234567',
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


class UserAuthenticationTests(SeleniumTestCase):

    def test_user_login_and_logout_form(self):
        self.driver.get(self.live_server_url + '/accounts/login/')
        user_name = self.driver.find_element(By.ID, 'id_login')
        user_password = self.driver.find_element(By.ID, 'id_password')
        submit = self.driver.find_element(By.ID, 'id_login_submit')

        user_name.send_keys('testertim')
        user_password.send_keys('001234567')
        submit.click()
        
        messages = self.driver.find_element(By.CLASS_NAME, 'messages')
        self.assertEqual(messages.text, 'Successfully signed in as testertim.')

        logout_nav_button = self.driver.find_element(By.ID, 'id_nav_logout')
        logout_nav_button.click()
        self.driver.implicitly_wait(5)

        logout_button = self.driver.find_element(By.ID, 'id_logout_submit')
        logout_button.click()

        messages = self.driver.find_element(By.CLASS_NAME, 'messages')
        self.assertEqual(messages.text, 'You have signed out.')

class UserProfileTests(SeleniumTestCase):

    def test_user_profile(self):
        # User Login
        self.driver.get(self.live_server_url + '/accounts/login/')
        user_name = self.driver.find_element(By.ID, 'id_login')
        user_password = self.driver.find_element(By.ID, 'id_password')
        submit = self.driver.find_element(By.ID, 'id_login_submit')

        user_name.send_keys('testertim')
        user_password.send_keys('001234567')
        submit.click()

        # Profile Test
        self.driver.get(self.live_server_url + '/users/1/')
        self.assertIn('tim.timons@test.test', self.driver.page_source)

        edit_button = self.driver.find_element(By.ID, 'id_edit_info')
        edit_button.click()
    
        save_button = self.driver.find_element(By.ID, 'id_save_edit')
        save_button.click()

        messages = self.driver.find_element(By.CLASS_NAME, 'messages')
        self.assertEqual(messages.text, 'Profile updated successfully.')
