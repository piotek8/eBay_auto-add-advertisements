# MOJ PROJEKT Z SCRAPPEREM0
import eBay.constants as const
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#super(ebay, self).__init__(options=options)

# The code is designed not to shut down Chrome after executing the script.

class ebay(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\\Users\\hp\\Downloads\\chromedriver", teardown =False):
        # Defines the functions in which the Chrome driver must work with the browser to communicate with program.
        
        self.driver_path = driver_path
        self.teardown = teardown

        super(ebay,self).__init__(options=options)
        # In this code, the super variable is used to refer to the parent class (webdriver.Chrome) and call it is constructor method (__init__).
        # This allows for the correct configuration of the Chrome browser for use in eBay tests when creating an instance of the eBay class.
        # Using super() in this way helps to avoid repeating code that already exists in the parent class. By using the super() method, we avoid redefining the same attributes or methods that are already defined in the parent class.
        # This allows for efficient use of class inheritance and increases code flexibility.
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def load_first_page(self):
        self.get(const.BASE_URL)

    def autologin_first_page(self):
        self.find_element(By.XPATH,
                            '(//input[@id="userid"])[1]').send_keys(const.LOGIN)

        click_login = self.find_element('xpath',
                            "//button[@id='signin-continue-btn']")
        click_login.click()
        # The scripts enters the e-mail


        self.implicitly_wait(25)


        self.find_element(By.XPATH,  # password
                            "//input[@id='pass']").send_keys(const.PASSWORD)

        self.find_element(By.XPATH,  # password buttom
                            "//button[@id='sgnBt']").click()
        # The scripts enters the password

    def go_to_ad_setings (self):
        self.find_element(By.CSS_SELECTOR,
                            ".gh-p").click()  # sprzedaj buttom

        #        driver.implicitly_wait(2.5)
        self.find_element(By.CSS_SELECTOR,
                            "div[class='image-banner-card white-background'] a[class='textual-display image-banner-card__action fake-btn fake-btn--fluid fake-btn--primary']").click()  # wystaw przedmiot buttom

        self.find_element(By.CSS_SELECTOR,
                            "body > div:nth-child(2) > div:nth-child(2) > main:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys(
            const.PHONE_MODEL)  # Title ustaw

        self.find_element(By.XPATH,  # Title find buttom
                            "/html[1]/body[1]/div[2]/div[2]/main[1]/div[1]/div[1]/div[1]/button[1]").click()

        self.find_element(By.XPATH,
                            "//input[@id='s0-1-1-24-10-@prelist-radix-body-2-20-2-1-0-14-5-3-5-10-14-@input-textbox']").send_keys(
            'Telefony i Akcesoria > Telefony komórkowe i smartfony')
        self.find_element(By.XPATH,
                            "//input[@id='s0-1-1-24-10-@prelist-radix-body-2-20-2-1-0-14-5-3-5-10-18-categoryId-9355']").click()

        ##############

        self.find_element(By.XPATH,  # press the buttom 'continue without matching'
                            "//button[normalize-space()='Kontynuuj bez dopasowania']").click()

        self.implicitly_wait(2.5)


        def category():
            Now = self.find_element(By.XPATH,
                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-1000']") # set state: Nowy
            NowInny = self.find_element(By.XPATH,
                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-1500']") # set state: Nowy: inny
            Uzy = self.find_element(By.XPATH,
                                       "//input[@id='s0-1-1-24-10-@prelist-radix-body-0-1-1-0-14-5-2-6-condition-3000']") # set state: Używany
            Usz = self.find_element(By.XPATH,
                                       "//div[4]//span[1]//span[1]//*[name()='svg'][1]/*[name()='use'][1]") # set state: Na części lub nie działa

            STATUS = const.STATUS

            if STATUS == 'nowy' or STATUS == 'new':       # | can be like or
                Now.click()
            elif STATUS == 'nowy: inny' or STATUS == 'new: other':
                NowInny.click()
            elif STATUS == 'uzywany' or STATUS == 'używany' or STATUS == 'used' :
                Uzy.click()
            elif STATUS == 'Na części lub nie działa' or STATUS == 'Na czesci lub nie dziala' or STATUS == 'broken':
                Usz.click()
            else:
                print('APPLICATION ERROR. You need to set the status of the announcement')
        category()

        self.find_element(By.XPATH, # press the buttom 'continue without matching'
                                 "//button[@class='textual-display btn btn--primary condition-dialog-radix__continue-btn']").click()

    def ad_all_informations_(self):
        set_title = self.find_element(By.ID,
                                        "wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-TITLE__-titleField__-textbox")
        set_title.clear()
        set_title.send_keys(const.TITLE)
        # set Title in advertisement


        time.sleep(1)
        self.find_element(By.ID,  # press buttom mark
                            #"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
                            "wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-REQUIRED_GROUP__-REQUIRED_ATTRIBUTE_GRID__-requiredAttrList.1__-valueSelect-inlineSelect").click()

        set_brand = self.find_element(By.XPATH,  # set Apple mark
                               #"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/input[1]").send_keys(const.PHONE_BRAND)
                                "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-REQUIRED_GROUP__-REQUIRED_ATTRIBUTE_GRID__-requiredAttrList.1__-valueSelect-searchBox-input']")
        set_brand.send_keys(const.PHONE_BRAND)
        set_brand.send_keys(Keys.ENTER)
        # set phone brand in advertisement



        time.sleep(3)
        COLOR = const.COLOR


        self.find_element(By.XPATH,"//button[@id='wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-REQUIRED_GROUP__-REQUIRED_ATTRIBUTE_GRID__-requiredAttrList.3__-valueSelect-inlineSelect']").click()

        if COLOR == 'beżowy' or COLOR == 'bezowy' or COLOR == 'beige':  # | can be like or
            self.find_element('xpath', "//li[@data-value='Beżowy']").click()
        elif COLOR == 'biały' or COLOR == 'bialy' or COLOR == 'white':
            self.find_element('xpath', "//li[@data-value='Biały']").click()
        elif COLOR == 'brązowy' or COLOR == 'brazowy' or COLOR == 'brown':
            self.find_element('xpath', "//li[@data-value='Brązowy']").click()
        elif COLOR == 'czarny' or COLOR == 'black':
            self.find_element('xpath', "//li[@data-value='Czarny']").click()
        elif COLOR == 'czerwony' or COLOR == 'red':
            self.find_element('xpath', "//li[@data-value='Czerwony']").click()
        elif COLOR == 'fioletowy' or COLOR == 'purpurowy' or COLOR == 'Violet' or COLOR == 'Magenta':
            self.find_element('xpath', "//li[@data-value='Fioletowy/purpurowy']").click()
        elif COLOR == 'niebieski' or COLOR == 'blue':
            self.find_element('xpath', "//li[@data-value='Niebieski']").click()
        elif COLOR == 'pomarańczowy' or COLOR == 'pomaranczowy' or COLOR == 'orange':
            self.find_element('xpath', "//li[@data-value='Pomarańczowy']").click()
        elif COLOR == 'przezroczysty' or COLOR == 'transparent':
            self.find_element('xpath', "//li[@data-value='Przezroczysty']").click()
        elif COLOR == 'różowy' or COLOR == 'rose':
            self.find_element('xpath', "//li[@data-value='Różowy']").click()
        elif COLOR == 'srebrny' or COLOR == 'silver':
            self.find_element('xpath', "//li[@data-value='Srebrny']").click()
        elif COLOR == 'szary' or COLOR == 'gray':
            self.find_element('xpath', "//li[@data-value='Szary']").click()
        elif COLOR == 'wielokolorowy' or COLOR == 'multicolour':
            self.find_element('xpath', "//li[@data-value='Wielokolorowy']").click()
        elif COLOR == 'zielony' or COLOR == 'green':
            self.find_element('xpath', "//li[@data-value='Zielony']").click()
        elif COLOR == 'zloty' or COLOR == 'złoty' or COLOR == 'gold':
            self.find_element('xpath',"//li[@data-value='Złoty']").click()
        elif COLOR == 'zolty' or COLOR == 'żółty' or COLOR == 'yellow':
            self.find_element('xpath', "//li[@data-value='Żółty']").click()
        else:
            print('APPLICATION ERROR. You need to set the status of the announcement')
        # set color in advertisement



        time.sleep(2)
        self.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[3]/button[1]").click()
        MEMORY_OPTIONS = ['16', '32', '64', '128', '256', '512']
        if const.MEMORY in MEMORY_OPTIONS:
            Memory_ = f" {const.MEMORY} GB"
            M = self.find_element(By.XPATH,"//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-REQUIRED_GROUP__-REQUIRED_ATTRIBUTE_GRID__-requiredAttrList.4__-valueSelect-searchBox-input']")
            M.send_keys(Memory_)
            M.send_keys(Keys.ENTER)
        elif const.MEMORY == '1':
            Memory_ = f" {const.MEMORY} TB"
            M = self.find_element(By.XPATH, "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-ATTRIBUTES__-ATTRIBUTES_GH__-ATTRIBUTES_DIY_VIEW__-REQUIRED_GROUP__-REQUIRED_ATTRIBUTE_GRID__-requiredAttrList.4__-valueSelect-searchBox-input']")
            M.send_keys(Memory_)
            M.send_keys(Keys.ENTER)
        else:
            print('you have set to memory in your description')
        # set memory in advertisement


        #self.execute_script("window.scrollBy(0, 1500)")

#PHOTOS NO WORK
#        self.implicitly_wait(10)
#        allPhotos = const.P1 + " \n " + const.P2 + " \n " + const.P3 + " \n " + const.P4 + " \n " + const.P5 + " \n " + const.P6
#        c1 = self.find_element(By.CLASS_NAME,"jsPhotoUploaderButton needsclick")
#        c1.send_keys(allPhotos)
#        # add photos in advertisement


        self.execute_script("window.scrollBy(0, 1500)")
        time.sleep(3.5)
        self.find_element(By.XPATH,"(//span[@data-value='RTE_EDITOR'])[1]").click()


        #self.execute_script("window.scrollBy(0, 1500)")
        #editor_element = WebDriverWait(self, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, "(//span[@data-value='RTE_EDITOR'])[1]")))
        #editor_element.click()


        #self.implicitly_wait(10)
        set_desc = self.find_element(By.ID,'wc0-w0-LIST_PAGE_WRAPPER__-OCS_DESCRIBE_SECTION__-DESCRIPTION__-descriptionField__-editorSource')

        set_desc.clear()
        set_desc.send_keys(const.DESCRIPTION)
        # set description advertisement

        #   #   #   #   #

        time.sleep(1.5)
        def PriceAuction():
            yes = self.find_element(By.XPATH,  # set auction option
                                      "//label[@for='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w0-auctionDiyPriceGroup__-auctionSelection__-checkbox']")

            AUCTION = const.AUCTION
            PRICE_AUCTION = const.PRICE_AUCTION

            if AUCTION == 'no':
                yes.click()
                pass
            elif AUCTION == 'yes':
                self.find_element(By.XPATH,
                                    "(//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w0-auctionDiyPriceGroup__-auctionDiyPriceGroupNew__-startPrice__-textbox'])[1]").send_keys(PRICE_AUCTION)
            else:
                print('Error! You have to set "yes" or "no" option')

        def BuyNow():
            yes = self.find_element(By.XPATH,  # set buy option
                                      "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w1-binDiyPriceGroup__-binPriceSelection__-checkbox']")

            BUY_AUCTION = const.BUY_AUCTION

            if BUY_AUCTION == 'yes':
                yes.click()

                #time.sleep(5)

                t = self.find_element(By.XPATH,
                                    "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w1-binDiyPriceGroup__-binDiyPriceGroupNew__-binPrice__-textbox']")
                time.sleep(4)
                t.send_keys(const.PRICE_BUY_AUCTION)
            else:
                pass

        #def Shipping():
        #    button = self.find_element(By.XPATH,"wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY_WRAPPER__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-shippingAvailableNotSelected__-shippingPrimaryServiceSelectService__")
        #    self.execute_script("arguments[0].click();", button)
#
        #    self.find_element(By.ID,  # set shipping option
        #                            "wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY_WRAPPER__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-shippingAvailableNotSelected__-shippingPrimaryServiceSelectService__").click()
#
        #    Standard_services = self.find_element(By.XPATH,
        #                                           "//div[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_PRIMARY_SERVICE_OVERLAY__-shippingPrimaryServiceDetails__-0-w1-w0']//span[@class='listShippingServiceSelect__groupContentCell serviceName']")
        #    Expedited_services = self.find_element(By.XPATH,
        #                                           "//div[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_PRIMARY_SERVICE_OVERLAY__-shippingPrimaryServiceDetails__-0-w3-w0']//span[@class='listShippingServiceSelect__groupContentCell serviceName']")
        #    Other_services = self.find_element(By.XPATH,
        #                                       "//div[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_PRIMARY_SERVICE_OVERLAY__-shippingPrimaryServiceDetails__-0-w5-w0']//span[@class='listShippingServiceSelect__groupContentCell serviceName']")







        #    DELIVERY = const.DELIVERY
#
        #    if DELIVERY == 'standard':
        #        Standard_services.click()
        #    elif DELIVERY == 'priority':
        #        Expedited_services.click()
        #    elif DELIVERY == 'abroad':
        #        Other_services.click()
        #    elif DELIVERY == 'no':
        #        pass
        #    else:
        #        print('ERROR')
#
        #    self.implicitly_wait(1)

        def Next_step():
            self.execute_script("window.scrollBy(0, 1000)")
            time.sleep(2)
        #    self.find_element("//span[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-shipYourItem__-w1']").click()
            #self.find_element('//*[@id="wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY_WRAPPER__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-shippingAvailableNotSelected__-shippingPrimaryServiceSelectService__"]').click()
            #self.find_element(By.XPATH,  # set 'Ty płacisz' option
            #                        "//input[@id='wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY_WRAPPER__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-SHIP_PRIMARY_SERVICES_COST__-w1-SHIP_PRIMARY_DIY_COST__-shippingPrimaryServicePaymentType__-SP']").click()
            self.find_element(By.XPATH,"(//button[@id='wc0-w0-LIST_PAGE_WRAPPER__-CTA_AND_LEGAL__-CTA__-CTA_VIEW__-listItCallToAction__'])[1]").click()
        PriceAuction()
        BuyNow()
        #Shipping()
        Next_step()








