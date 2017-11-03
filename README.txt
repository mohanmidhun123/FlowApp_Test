Automated App Testing for FlowDrive Application on Android devices

Below is the description of how automated testing can be attempted on Android and Iphone using Appium, Android-Studio and Python.
And running the same code on physical and cloud hosted devices. 
Appium allows to test multiplatform Android/Iphone by using the same code.

Please see the "Installation-requirement" and "Procedure" on how to run the testcases.


How to download the code:

1. Click on the Clone or download option
2. Download Zip file
3. Or directly clone to Windows desktop git local

TestCases:
I have written around 29 basic testcases which is a combination of basic functionality testing, Positive, Negative scenarios which revolves around traversing through different App Tab sections,Credentials, user management, unauthorised access, app functionality, hang test, sending text-code to email etc.

The complete test execution takes around 1 hour to complete.
Please see the excel sheet named "FlowDrive_AndroidAPP_testing_v0.1" for the testcases.


Bugs and issues:
There is an issue which I faced with the Cloud device testing using Bitbar testroid platform. 
This issue seems to be related new version of appium installed at the server side.

Error Obtained: 

******************************
2017-11-03 10:36:43:187 - [debug] [MJSONWP] Bad parameters: BadParametersError: Parameters were incorrect. We wanted {"required":["value"]} and you sent ["text","value","id","sessionId"]
******************************

I seem have an older version of python-appium client.

Please see the below link below for more details:

https://github.com/appium/python-client/issues/162
https://github.com/appium/appium/issues/6851
