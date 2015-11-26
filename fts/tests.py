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

	def can_access_admin_site(self):
		self.browser.get(self.live_server_url)

		#He notice the title of the site is for microinsurance
		self.assertIn('Vance MicroInsurance', self.browser.title)

		#He notice the login button at the upper-right side of the form
		login_button = self.browser.find_element_by_id('login')
		login_button.click()

		#He type in the username
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('admin')
		#He type in the username
		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)

		#He sees the Vance Microinsurance in the page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Vance MicroInsurance', body.text)

	def test_insert_into_branches(self):

		self.can_access_admin_site()

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

	def test_insert__into_insurance_types(self):

		self.can_access_admin_site()
		#He sees the discount button and click it
		discount_button = self.browser.find_element_by_link_text('Discounts')
		discount_button.click()
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('0 discount', body.text)

		#He click the add discount button to create new discounts
		add_discount = self.browser.find_element_by_link_text('Add discount')
		add_discount.click()

	def test_can_insert_insurance_type(self):
		self.can_access_admin_site()
		insurance_type = self.browser.find_element_by_link_text('Insurance types')
		insurance_type.click()

		add_insurance_type = self.browser.find_element_by_link_text('Add insurance type')
		add_insurance_type.click()

		insurance_add_type = self.browser.find_element_by_name('Insurance_Type_Name')
		insurance_add_type.send_keys('Fire Accident')

		button_save = self.browser.find_element_by_name('_save')
		button_save.click()