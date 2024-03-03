class LoginObject:
    def __init__(self):
        self.buttonLoginRegis = "//span[contains(text(), 'Log in/Register')]"
        self.clickForgotPassword = "//a[contains(text(),'Forgot Password?!')]"
        self.formEmail = "//p[contains(text(), 'Email')]"
        self.inccorectEmailFormat = "//p[contains(text(), 'Incorrect email format')]"
        self.form_inputPhone =  "//input[@id='phone']"
        self.form_inputEmail =  "//input[@id='fld_Email']"
        self.form_inputPassword = "//input[@id='fld_Password']"
        self.form_buttonLogin = "//button[@id='btn_Login']"
        self.helloLogin = "//div[contains(text(),'Hello!')]"
        self.popWrongPW = "//h3[contains(text(),'Wrong phone number or password')]"
        self.popLoginUnregistered = "//h3[contains(text(),'This account has not been registered.')]"
        self.popUnregistered = "//h3[contains(text(),'This account has not been registered.')]"
        # element myprofile paling kiri
        self.myProfile = "(//div[@class='profiles-container lessThanRow']//div//div//div//img)[1]"
