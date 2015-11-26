from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class MicroInsurance(StaticLiveServerTestCase):
	fixtures = ['admin_user.json']

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_insert_into_branches(self):

		#Bon visits the website microinsurance
		self.browser.get(self.live_server_url)

		#He notice the title of the site is for microinsurance
		self.assertIn('Creative - Start Bootstrap Theme', self.browser.title)

		#He notice the login button at the upper-right side of the form
		login_button = self.browser.find_element_by_id('login')
		login_button.click()

		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('admin')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Vance MicroInsurance', body.text)

		branch_button = self.browser.find_element_by_link_text('Branches')
		branch_button.click()

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('0 branch', body.text)

		add_branch = self.browser.find_element_by_link_text('Add branch')
		add_branch.click()

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Add branch', body.text)

		branch_field = self.browser.find_element_by_name('branch_name')
		branch_field.send_keys('Cebuana')

		button_save = self.browser.find_element_by_name('_save')
		button_save.click()