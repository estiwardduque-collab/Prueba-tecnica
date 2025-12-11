from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

class CheckoutPage(BasePage):
    # Step 2: Billing Details
    PAYMENT_ADDRESS_NEW = (By.CSS_SELECTOR, "input[name='payment_address'][value='new']")
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    ADDRESS_1 = (By.ID, "input-payment-address-1")
    CITY = (By.ID, "input-payment-city")
    POSTCODE = (By.ID, "input-payment-postcode")
    COUNTRY_SELECT = (By.ID, "input-payment-country")
    ZONE_SELECT = (By.ID, "input-payment-zone")
    BUTTON_PAYMENT_ADDRESS = (By.ID, "button-payment-address")

    # If address existing is selected by default (if logged in)
    PAYMENT_ADDRESS_EXISTING = (By.CSS_SELECTOR, "input[name='payment_address'][value='existing']")


    # Step 3: Delivery Details (if applicable for physical goods)
    # Note: Sometimes this step is skipped if virtual, but usually present.
    # Assuming Shipping Address is same as Payment or simplied flow.
    # If shipping address step appears:
    BUTTON_SHIPPING_ADDRESS = (By.ID, "button-shipping-address") 
    
    # Step 4: Delivery Method
    BUTTON_SHIPPING_METHOD = (By.ID, "button-shipping-method")
    
    # Step 5: Payment Method
    AGREE_TERMS = (By.NAME, "agree")
    BUTTON_PAYMENT_METHOD = (By.ID, "button-payment-method")
    
    # Step 6: Confirm Order
    BUTTON_CONFIRM = (By.ID, "button-confirm")
    
    # Success Page
    SUCCESS_HEADER = (By.CSS_SELECTOR, "#content h1")

    def fill_billing_details(self, address_data):
        # Check if "I want to use a new address" is needed or if it's the default
        # Since we just registered, sometimes it pre-fills. 
        # But if we need to enter it:
        try:
             # If "New Address" radio exists and not selected, click it. 
             # Or if we want to rely on existing address from registration, we might just click Continue.
             # However, often registration doesn't capture address. OpenCart usually asks for address in Checkout if not in Register.
             # Our Register test only filled Basic info. So we likely need to fill Address here.
             
             # Wait for accordion to be active?
             self.waits.wait_for_element_visible(self.FIRST_NAME) # If this is visible, we are in "New Address" or inputs form
             
             self.type(self.FIRST_NAME, "TestFirst") # Often prefilled if logged in
             self.type(self.LAST_NAME, "TestLast")
             self.type(self.ADDRESS_1, address_data['address'])
             self.type(self.CITY, address_data['city'])
             self.type(self.POSTCODE, address_data['postcode'])
             
             # Select Country
             country = Select(self.find_element(self.COUNTRY_SELECT))
             country.select_by_visible_text(address_data['country'])
             
             # Wait for zones to load
             time.sleep(1) # Small wait for AJAX
             zone = Select(self.find_element(self.ZONE_SELECT))
             zone.select_by_visible_text(address_data['region'])
             
        except:
             # If inputs are not found, maybe "Existing Address" is selected or steps are different.
             # For this test flow, assuming fresh user without address, so form should be there.
             pass

        self.click(self.BUTTON_PAYMENT_ADDRESS)

    def process_checkout_steps(self):
        # Depending on configuration, Shipping Address/Way might be skipped or required.
        # We try to click through the steps using generic waits or specific logic.
        
        # Shipping Details (if present)
        # Assuming we just use Default for everything to speed up
        
        # OpenCart Checkout is an accordion. We wait for next button to be clickable.
        
        # Since steps can vary, we will try to handle standard flow:
        # Billing Details (Already handled or clicked continue) -> Shipping Address -> Shipping Method -> Payment Method -> Confirm
        
        # Wait for potential Shipping Address step
        try:
            self.click(self.BUTTON_SHIPPING_ADDRESS)
        except:
            pass # Maybe skipped or not required
            
        # Shipping Method
        try:
            self.click(self.BUTTON_SHIPPING_METHOD)
        except:
            pass

        # Payment Method
        self.click(self.AGREE_TERMS)
        self.click(self.BUTTON_PAYMENT_METHOD)
        
        # Confirm
        self.click(self.BUTTON_CONFIRM)

    def get_final_confirmation(self):
        self.waits.wait_for_url_contains("checkout/success")
        return self.get_text(self.SUCCESS_HEADER)
