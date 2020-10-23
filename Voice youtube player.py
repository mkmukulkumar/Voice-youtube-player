import time
import speech_recognition as sr
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
engine = pyttsx3.init() 
r = sr.Recognizer()
with sr.Microphone() as source:  
    r.adjust_for_ambient_noise(source, duration = 5)
   
    engine.say("Konsa  gaana  sunna  cha hen gay") 
    engine.runAndWait()
    print("say something") 
    audio = r.listen(source)  
         
try:
    text = r.recognize_google(audio)
    engine.say("You said:"+ format(text)) 
    engine.runAndWait()
    print(format(text))
    driver = webdriver.Chrome("D:\software\chrome driver\chromedriver.exe") # Optional argument, if not specified will search path.
    driver.maximize_window()  
    driver.get('https://www.youtube.com/')
    element = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
    element.send_keys(text)
    element.send_keys(Keys.RETURN)
    ele= driver.find_element_by_id("thumbnail")
    ele.click()
    driver.fullscreen_window()
 
except:
    print("Sorry could not recognize your voice")

