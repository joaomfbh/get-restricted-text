from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import ttk
# from selenium.webdriver.common.keys import Keys

# root = Tk()
# root.title("Lawer Toolkit")
# root.geometry("800x600")
#
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# lnk = StringVar()
# lnk_entry = ttk.Entry(mainframe, width=7, textvariable=lnk)
# lnk_entry.grid(column=2, row=1, sticky=(W, E))
#
# text = Text(root, width=20, height=20)
# # text_entry = ttk.Entry(mainframe)
# # text_entry.grid(column=1, row=2, sticky=(W, E))
#
# root.mainloop()

driver = webdriver.Firefox()
get_lnk = input("Insira o link do site desejado: ")
driver.get(get_lnk)

# content = driver.find_element(By.CLASS_NAME, "DocumentPage-content")
start_text = input('Início do texto: ')
end_text = input('Fim do texto: ')

content = driver.find_element(By.XPATH, "//*['text()={0}']".format(start_text)).text
list_content = content.split('\n')


proof_start_text = ''
real_start_loc = 0
# Get content to find start_text typed by user
for row, text in enumerate(list_content):
    if start_text in text:
        for proof in ''.join(text):
            proof_start_text += proof
            if len(start_text) == len(proof_start_text):
                if start_text == proof_start_text:
                    real_start_loc = row
                    break

list_content = list_content[real_start_loc:]

proof_end_text = ''
real_end_loc = 0
# Get reversed content to find end_text typed by user
for row, text in enumerate(reversed(list_content)):
    if end_text in text:
        for proof in reversed(''.join(text)):
            proof_end_text += proof
            if len(end_text) == len(proof_end_text):
                if end_text == proof_end_text[::-1]:
                    real_end_loc = row
                    break

list_content = list_content[:len(list_content) - real_end_loc]

with open('extracted_text.txt','w') as file:
    file.writelines('\n'.join(list_content))

# driver.close()
driver.quit()

# print(content.text)
