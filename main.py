from selenium import webdriver
from time import sleep


def sendMessage(driver, conversa, mensagem):
    try:
        sleep(1)
        chats = driver.find_elements_by_class_name('_ccCW.FqYAR.i0jNr')
        for chat in chats:
            if chat.text == conversa:
                chat.click()
                break

        input_div = driver.find_elements_by_class_name('_13NKt.copyable-text.selectable-text')[1]
        input_div.send_keys(mensagem)
        driver.find_element_by_class_name('_4sWnG').click()
    except:
        sendMessage(conversa, mensagem)


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://web.whatsapp.com')

conversa = input('Com quem quer falar: ')
mensagem = input('Mensagem: ')

sendMessage(driver, conversa, mensagem)
driver.close()
