
'''Automated Testing to verify "TheFlowDrive App functionality on Android devices

Below is the code for doing automated testing using Appium, Android-Studio and Python.

'''

import unittest
from appium import webdriver
import time


class TheFlowDriveApp(unittest.TestCase):

    #*************************************Basic Setup and Teardown for the test*********************************'''
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = "D:\\Downloads\\8b3d8e298a.apk"  #Mention the path to the .apk file
        desired_caps['appPackage'] = 'com.thefloow.flo'
        desired_caps['appActivity'] = 'com.thefloow.flo.activity.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.delay = lambda :time.sleep(8)
        self.BACK = lambda :self.driver.keyevent(4)
        self.textFieldsList = "android.widget.TextView"
        self.editText = "android.widget.EditText"
        self.USER = "midhun.mohan@aricent.com"
        self.PASS = "zxcvbnm1"
        self.AGGREEMENT_PAGE={
            "agreement": "com.thefloow.flo:id/btn_agree"
        }
        self.LOGIN_PAGE={
            "email" : "com.thefloow.flo:id/edit_text_email",
            "pass" : "com.thefloow.flo:id/edit_text_password",
            "login_button" : "com.thefloow.flo:id/btn_login",
            "forgot-pass" : "com.thefloow.flo:id/text_view_forgot_password",
            "get-code" : "com.thefloow.flo:id/btn_get_code",
            "new-pass" : "com.thefloow.flo:id/edit_text_new_password",
            "confirm-pass" : "com.thefloow.flo:id/edit_text_confirm_password",
            "submit" : "com.thefloow.flo:id/btn_submit",
            "layout-code": "com.thefloow.flo:id/layout_got_code",
            "text-code" : "com.thefloow.flo:id/edit_text_code",
            "first-name" : "com.thefloow.flo:id/edit_text_first_name",
            "surname" : "com.thefloow.flo:id/edit_text_surname",
            "dob" : "com.thefloow.flo:id/edit_text_date_of_birth",
            "post-code" : "com.thefloow.flo:id/edit_text_postcode",
            "company" : "com.thefloow.flo:id/edit_text_company_name",
            "register" : "com.thefloow.flo:id/button_register",
            "create-account" :  "com.thefloow.flo:id/text_view_create_account",
            "dob-select" : "android:id/numberpicker_input"

        }
        self.HOME_PAGE={
            "home" : "com.thefloow.flo:id/tab_home",
            "welcome" : "com.thefloow.flo:id/btn_welcome_close",
            "start" : "com.thefloow.flo:id/btn_start",
            "stop" : "com.thefloow.flo:id/btn_stop"

        }
        self.JOURNEYS={
            "journey" : "com.thefloow.flo:id/tab_journeys"
        }
        self.SCORE={
            "score-main" : "com.thefloow.flo:id/tab_score",
            "score" : "com.thefloow.flo:id/btn_component_score",
            "time-task" : "com.thefloow.flo:id/component_score_time_task",
            "time-day" : "com.thefloow.flo:id/component_score_time_day",
            "score-speed" : "com.thefloow.flo:id/component_score_speed",
            "smooth-drive" : "com.thefloow.flo:id/component_score_smooth_drive",
            "mobile-usage" : "com.thefloow.flo:id/component_score_mobile_usage",
            "score-info" : "com.thefloow.flo:id/btn_score_information",
            "screen-name" : "com.thefloow.flo:id/social_screen_name"

        }
        self.SOCIAL={
            "social" : "com.thefloow.flo:id/tab_social",
            "menu-friends" : "com.thefloow.flo:id/social_menu_friends",
            "add-friends" : "com.thefloow.flo:id/social_friends_add_friends",
            "add-by-email" : "com.thefloow.flo:id/btn_social_add_by_email",
            "friend-email": "com.thefloow.flo:id/friend_email",
            "social-add": "com.thefloow.flo:id/btn_social_add",
            "back-to-friends": "com.thefloow.flo:id/btn_social_back_to_friends"

        }
        self.HELP={
            "help" : "com.thefloow.flo:id/tab_help",
            "view-username" :  "com.thefloow.flo:id/text_view_username",
            "view-licenses" : "com.thefloow.flo:id/text_view_licenses",
            "text-message" : "com.thefloow.flo:id/edit_text_message",
            "send" : "com.thefloow.flo:id/button_send",
            "categories" : "com.thefloow.flo:id/spinner_categories",
            "index0" : "com.thefloow.flo:id/index_0",
            "index1": "com.thefloow.flo:id/index_0",
            "index2": "com.thefloow.flo:id/index_0",
            "index3": "com.thefloow.flo:id/index_0"
        }

    def tearDown(self):
        #To tear down the session
        self.driver.quit()

    # ************************************* 1. To verify login to app with wrong user credentials *********************************'''
    def test_1(self):
        try:
            #Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

            #Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys('mohan.midhun@yahoo.com')
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys("zxcvbnm")
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

            #Verification
            self.assertEqual('User name/password not found. Are you registered?', self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
        except Exception as e:
            raise e

    # ************************************* 2. To verify login to app with invalid email address *********************************'''

    def test_2(self):
        try:
            # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

            # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys('mohan.midhun123gmail.com')
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys("zxcvbnm")
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

            #Verification
            self.assertEqual('Invalid e-mail address', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # ************************************* 3. To verify login to app with wrong password *********************************'''
    def test_3(self):
        try:
            # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

            # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys("zxcvbnm")
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

            #Verification
            self.assertEqual('User name/password not found. Are you registered?',self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
        except Exception as e:
            raise e

    # ************************************* 4. To verify login to app with valid credentials *********************************'''
    def test_4(self):
        try:
            # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

            #Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

            #Verification
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # ************************************* 5. To verify If traversing through different App "Tabs" is possible after login *********************************'''
    def test_5(self):
         try:
                # Agreeing to the agreement
                self.delay()
                self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
                self.delay()

                # Attempting Login
                self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
                self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
                self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
                self.delay()

                #Swiping through Pages and verication
                self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
                self.driver.swipe(700,500,5,500,200)
                self.delay()
                self.assertEqual('What do I need to do next?', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
                self.driver.swipe(700,500,5,500,200)
                self.delay()
                self.assertEqual('Need help with anything else?', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)

                #Closing Welcome Message
                self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
                self.delay()

                #Traversing through different tabs and verification
                self.driver.find_element_by_id(self.HOME_PAGE.get("home")).click()
                self.delay()
                self.assertEqual('Do not interact with the device while driving.', self.driver.find_elements_by_class_name(self.textFieldsList)[2].text)
                self.driver.find_element_by_id(self.JOURNEYS.get("journey")).click()
                self.JOURNEYS.get("journey")
                self.delay()
                self.assertEqual('Date', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
                self.driver.find_element_by_id("com.thefloow.flo:id/tab_score").click()
                self.delay()
                self.assertEqual('NO HISTORICAL SCORE DATA\nAVAILABLE AT THIS TIME.', self.driver.find_elements_by_class_name(self.textFieldsList)[2].text)
                self.driver.find_element_by_id(self.HELP.get("help")).click()
                self.delay()
                self.assertEqual('FAQs', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)

         except Exception as e:
            raise e

    # ************************************* 6. To verify that Install/Uninstall Android App is Successful *********************************'''
    def test_6(self):
        try:
            self.delay()
            self.driver.remove_app('com.thefloow.flo')

        except Exception as e:
            raise e

    # ************************************* 7. To Verify if App is hanging or not by perfoming Random clicks at differrent pages *********************************'''
    def test_7(self):
        try:
           # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

           #Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

           #Closing welcome message
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.delay()

           #Random clicks in home Tab and Score Tab
            self.driver.find_element_by_id(self.HOME_PAGE.get("home")).click()
            self.delay()
            self.driver.find_element_by_id(self.HOME_PAGE.get("start")).click()
            self.delay()
            self.driver.find_element_by_id(self.SCORE.get("score-main")).click()
            self.delay()
            self.driver.find_element_by_id(self.SCORE.get("score")).click()
            self.delay()
            self.driver.find_element_by_id(self.SCORE.get("time-task")).click()
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.SCORE.get("time-day")).click()
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.SCORE.get("score-speed")).click()
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.SCORE.get("smooth-drive")).click()
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.SCORE.get("mobile-usage")).click()
            self.delay()
            self.BACK()
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.SCORE.get("score-info")).click()
            self.delay()
            self.BACK()

        except Exception as e:
            raise e

    # ************************************* 8. To Check Forgot Password option with email id of wrong format*********************************'''
    def test_8(self):
        try:
        # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        #Attempting Login
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys("mohan.midhun123")
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("get-code")).click()
            self.delay()
            self.assertEqual("Invalid e-mail address", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)

        except Exception as e:
            raise e

    # ************************************* 9. To Check Forgot Password option with valid registered email id*********************************'''
    def test_9(self):
        try:
        # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        #Attempting Login
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("get-code")).click()
            self.delay()

        #Verification
            self.assertEqual("Code Sent Successfully", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)

        except Exception as e:
            raise e

    # ************************************* 10.Forgot Password Test with email id in correct format but unregistered*********************************'''
    def test_10(self):
        try:
        # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        # Attempting Login
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys("mohan.midhun123@gmail.com")
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("get-code")).click()
            self.delay()

        #Verification
            self.assertEqual("Code Sent Successfully", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    #  ************************************* 11. Attempting Password reset when you already have a code which is incorrect*********************************'''
    def test_11(self):
        try:
        # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        # forgot password
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("layout-code")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("text-code")).send_keys("1")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("new-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("confirm-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("submit")).click()

        #Verification
            self.assertEqual("There was an error resetting your password. Please check your e-mail address and recovery code. Codes expire after 24 hours.", self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
        except Exception as e:
            raise e

    # ************************************* 12. Password reset when you already have a wrong code of long digits*********************************'''
    def test_12(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # forgot password
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("layout-code")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("text-code")).send_keys("1222222222222222222222222222222222222222222222222222222222222222222222")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("new-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("confirm-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("submit")).click()

         # Verification
            self.assertEqual("Please enter the 4 digit recovery code.", self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)

        except Exception as e:
            raise e

    # # ************************************* 13. Password reset with wrong email address format*********************************'''
    def test_13(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #Password reset
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("layout-code")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("text-code")).send_keys("0000")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys("abc@gmail@com")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("new-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("confirm-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("submit")).click()

         #Verification
            self.assertNotEqual("Error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)

        except Exception as e:
            raise e

    # # ************************************* 14. Password reset password not meeting the requirement*********************************'''
    def test_14(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #Password reset
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("layout-code")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("text-code")).send_keys("0000")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("new-pass")).send_keys("@#$")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("confirm-pass")).send_keys("@#$")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("submit")).click()

         #verification
            self.assertNotEqual("Error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # # ************************************* 15. Password reset password mismatch*********************************'''
    def test_15(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #password reset
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("layout-code")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("text-code")).send_keys("0000")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("new-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("confirm-pass")).send_keys("zxcvbnm123")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("submit")).click()

         #Verification
            self.assertNotEqual("Error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # # ************************************* 16. Password reset correct credentials*********************************'''
    def test_16(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #password reset
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("layout-code")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("text-code")).send_keys("9268") #put the correct code here. Code is valid for 24 hrs
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("new-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("confirm-pass")).send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("submit")).click()

         #Verification
            self.assertNotEqual("Error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)

        except Exception as e:
            raise e

    # ************************************* 17. Create Account Test with already registered email address *********************************'''
    def test_17(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #Create Account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("midhun")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("mohan")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2000")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("122001")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz&*()^$$####")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()

          #Verification
            self.delay()
            self.assertEqual("Registration error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # ************************************* 18. Create Account Test with age less than 17 *********************************'''
    def test_18(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #Create account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("midhun")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("mohan")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2016")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("122001")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz&*()^$$####")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()
            self.delay()

        # Verification
            self.assertEqual("You must be over 17 years of age.", self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
        except Exception as e:
            raise e

    # # ************************************* 19. Create Account Test with wrong email format *********************************'''
    def test_19(self):
        try:
         #Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        #create account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("midhun")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("mohan")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2000")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys("mohan.midhun123.com")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("122001")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz&*()^$$####")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()
            self.delay()
        #verification
            self.assertEqual("Enter a valid e-mail address.", self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
        except Exception as e:
            raise e

    # # ************************************* 20. Create Account Test and password doesnt meet requirement *********************************'''
    def test_20(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # Create Account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("midhun")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("mohan")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2000")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("122001")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz&*()^$$####")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys("zxcvbn")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys("zxcvbn")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()
            self.delay()
         #Verification
            self.assertEqual("Password: 8 characters needed.", self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
        except Exception as e:
            raise e

    # # ************************************* 21. Create Account Test - Firstname and surname should not take numbers or other characters*********************************'''
    def test_21(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         #Create account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("!@###$$")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("123456789")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2000")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("122001")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz&*()^$$####")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()
            self.delay()

         #verification
            self.assertEqual("Error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # # ************************************* 22. Create Account Test - postcode code shouldnt take other characters other than numbers*********************************'''
    def test_22(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        # Create account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("midhun")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("mohan")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2000")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("@#$%%^^&&&AA!ddafa")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz&*()^$$####")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys("self.PASS")
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()
            self.delay()


         #Verification
            self.assertEqual("Error", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # ************************************* 23. Create Account Test - Success scenario*********************************'''
    def test_23(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # Creating Account
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("create-account")).click()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("first-name")).send_keys("Midhun")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("surname")).send_keys("Mohan")
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("dob")).click()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].clear()
            self.driver.find_elements_by_id(self.LOGIN_PAGE.get("dob-select"))[2].send_keys("2009")
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys("mohan.midhun@gmail.com")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[4].send_keys("122001")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[5].send_keys("xyz")
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[6].send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_elements_by_class_name(self.editText)[7].send_keys(self.PASS)
            self.delay()
            self.BACK()
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("register")).click()

         #Verification
            self.assertNotEqual("Success", self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
        except Exception as e:
            raise e

    # ************************************* 24. Exiting app after successful login attempt *********************************'''
    def test_24(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()

        # Exiting App
            self.delay()
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.BACK()
            self.driver.find_element_by_id("android:id/button1").click()
            self.delay()


        except Exception as e:
            raise e

    #************************************* 25. Check if About Section HELP Tab shows valid information *********************************'''
    def test_25(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

         #Help section verification
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.driver.find_element_by_id(self.HELP.get("help")).click()
            self.delay()

            self.driver.find_elements_by_class_name(self.textFieldsList)[3].click()
            self.assertEqual(self.USER, self.driver.find_element_by_id(self.HELP.get("view-username")).text)


        except Exception as e:
            raise e

    # ************************************* 26. Successfuly traversing through all HelP Tab sections *********************************'''
    def test_26(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()
            self.delay()

         # Traversing through help sections
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.driver.find_element_by_id(self.HELP.get("help")).click()
            self.delay()

            self.driver.find_elements_by_class_name(self.textFieldsList)[0].click()
            self.delay()
            textfield = self.driver.find_elements_by_class_name("android.widget.TextView")
            textfield[0].click()
            self.delay()
            textfield[0].click()
            textfield = self.driver.find_elements_by_class_name("android.widget.TextView")
            textfield[1].click()
            self.delay()
            textfield[1].click()
            textfield = self.driver.find_elements_by_class_name("android.widget.TextView")
            textfield[2].click()
            self.delay()
            textfield[2].click()
            textfield = self.driver.find_elements_by_class_name("android.widget.TextView")
            textfield[3].click()
            self.delay()
            textfield[3].click()
            self.BACK()
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.assertEqual('Connect to T2 Devices', self.driver.find_elements_by_id("android:id/title")[2].text)
            self.BACK()
            self.driver.find_elements_by_class_name(self.textFieldsList)[2].click()
            self.assertEqual('Messages', self.driver.find_elements_by_class_name("android.widget.TextView")[0].text)
            self.BACK()
            self.driver.find_elements_by_class_name(self.textFieldsList)[3].click()
            self.assertEqual('Software License Acknowledgements', self.driver.find_element_by_id(self.HELP.get("view-licenses")).text)
            self.BACK()
            self.driver.find_elements_by_class_name(self.textFieldsList)[4].click()
            self.assertEqual('Enter your message...',self.driver.find_element_by_id(self.HELP.get("text-message")).text)
            self.BACK()

        except Exception as e:
            raise e

    # ************************************* 27. Testing functionality involving Acquiring and locking GPS*********************************'''
    def test_27(self):
        try:
         # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

         # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()

        # Testing functionality
            self.delay()
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.delay()
            self.driver.find_element_by_id(self.HOME_PAGE.get("start")).click()
            timeout = time.time() + 60 * 5
            while True :
                try:
                    self.driver.find_element_by_id("com.thefloow.flo:id/btn_stop")
                    break
                except:
                    if time.time() > timeout:
                        break
                    else:
                        continue
            self.delay()

            if int((self.driver.find_element_by_id("com.thefloow.flo:id/chrono_duration").text).split(":")[1])>00:
                self.driver.find_element_by_id(self.HOME_PAGE.get("stop")).click()
                self.delay()
                self.assertEqual("This journey will not be recorded because it did not meet the minimum distance of 0.5 mile and the minimum speed of 5 mph.",self.driver.find_elements_by_class_name(self.textFieldsList)[1].text)
                self.driver.find_element_by_id("android:id/button1").click()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("social")).click()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("menu-friends")).click()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("add-friends")).click()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("add-by-email")).click()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("friend-email")).send_keys("mohan.midhun123@gmail.com")
                self.BACK()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("social-add")).click()
                self.delay()
                self.driver.find_element_by_id(self.SOCIAL.get("back-to-friends")).click()

        except Exception as e:
            raise e

    # ************************************* 28. Test Flow Drive App to check report problem functionality *********************************'''
    def test_28(self):
        try:
            # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

            # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()

            #report problem functionality
            self.delay()
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.delay()
            self.driver.find_element_by_id(self.HELP.get("help")).click()
            self.delay()
            self.driver.find_elements_by_class_name(self.textFieldsList)[4].click()
            self.delay()
            self.driver.find_element_by_id(self.HELP.get("categories")).click()
            self.driver.find_elements_by_class_name("android.widget.CheckedTextView")[2].click()
            self.driver.find_element_by_id(self.HELP.get("text-message")).send_keys("ZXCVBNNMASDFGHJKLL!@#$$%^&&**123455677")
            self.driver.find_element_by_id(self.HELP.get("send")).click()
            self.BACK()

        except Exception as e:
            raise e

    # ************************************* 29. Test Flow Drive App to check setting preferences options*********************************'''
    def test_29(self):
        try:
        # Agreeing to the agreement
            self.delay()
            self.driver.find_element_by_id(self.AGGREEMENT_PAGE.get("agreement")).click()
            self.delay()

        # Attempting Login
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("email")).send_keys(self.USER)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("pass")).send_keys(self.PASS)
            self.driver.find_element_by_id(self.LOGIN_PAGE.get("login_button")).click()

        #Traversing through preference section
            self.delay()
            self.assertEqual('Welcome to FlowDrive', self.driver.find_elements_by_class_name(self.textFieldsList)[0].text)
            self.driver.find_element_by_id(self.HOME_PAGE.get("welcome")).click()
            self.delay()
            self.driver.find_element_by_id(self.HELP.get("help")).click()
            self.delay()
            self.driver.find_elements_by_class_name(self.textFieldsList)[1].click()
            self.delay()
            self.driver.find_elements_by_class_name("android.widget.CheckBox")[0].click()
            self.delay()
            self.driver.find_elements_by_class_name("android.widget.CheckBox")[1].click()
            self.delay()
            self.driver.find_elements_by_class_name("android.widget.CheckBox")[2].click()
            self.delay()
            self.driver.find_element_by_id("index_0").click()
            self.driver.find_element_by_id("index_1").click()
            self.driver.find_element_by_id("index_2").click()
            self.driver.find_element_by_id("index_3").click()
            self.BACK()

        except Exception as e:
            raise e




if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TheFlowDriveApp)
        unittest.TextTestRunner(verbosity=4).run(suite)