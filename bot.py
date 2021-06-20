from selenium import webdriver
import time
import os, time


#El controlador encargado del manejo de la prueba, este es
#dependiente del navegador a usat
driver = webdriver.Chrome(executable_path=r"C:\Users\Erwin\Documents\GitHub\Bot_WhatsApp\chromedriver.exe")

#Apertura la pagina a desplegar en este Caso WhatsApp Web
driver.get("https://web.whatsapp.com")

#tiempo en el cual permite estar activa una pagina
#esta esta medida en segundos
time.sleep(10)

#En esta area esta el numero de telefono con el respectivo codigo de area
#Eliminar las "X" por la cantidad de numeros que correspondan, recordar que incluye codigo de area
celular = " "XXXXXXXX""
#Mensaje a establecer
msj = "Hola, este es el primer BOT"

#creacion del link de WhatsApp API concatenando el numero mas el mensaje
driver.get("https://wa.me/"+celular+"?text="+msj)
time.sleep(5)

#acceder al chat
btn = driver.find_element_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)

#Si WhatsApp no esta instalado activa el boton de descargar
btn =driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(25)

#Boron enviar
btn =  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(5)

print("-- Fin del BOT --")

time.sleep(25)
driver.close()
