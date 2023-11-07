
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from texttable import Texttable
import socket


def has_connection():
    try:
        socket.create_connection(('google.com',80))
        return True
    except OSError:
        return False


p_name = input("Enter the name of the product:- ")
num = int(input("Enter the number of products do you want to get:- "))
path = "C:\Program Files\Google\Chrome\Application\chrome.exe"


print("Checking Internet connection..")
sleep(2)
if not has_connection():
    print("check your internet connection...")
    sleep(3)
    exit()
else:
    print("Your Connection is okay. \nDirecting you to the Amazon Webpage...")
    sleep(2)

driver = webdriver.Chrome()


driver.maximize_window()

driver.get("https://amazon.com")

input_search = driver.find_element("id", "twotabsearchtextbox")
search_button = driver.find_element("id", "nav-search-submit-button")
input_search.send_keys(p_name)

sleep(1)
search_button.click()

a_products = []
a_prices = []

a_product = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
a_price = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
a = 1
for pr in a_price:
    if a > num:
        break
    else:
        pri = ''
        for i in pr.text:
            if i != ',':
                pri += i
    pri = int(pri)
    a_prices.append(pri*83)
    a += 1
print(len(a_prices))
a = 1
for p in a_product:
    if a > num:
        break
    else:
        a_products.append(p.text)
        a += 1
a = 1
if len(a_products) < num:
    a_products.clear()
    a_product = driver.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
    for p in a_product:
        if a > num:
            break
        else:
            a_products.append(p.text)
            a += 1

print(len(a_products))

driver.quit()




print("Checking Internet connection..")
sleep(2)
if not has_connection():
    print("check your internet connection...")
    sleep(3)
    exit()
else:
    print("Connection is okay directing to the Flipkart Webpage...")
    sleep(2)

driver = webdriver.Chrome()

driver.maximize_window()




driver.get("https://www.flipkart.com/")


input_search = driver.find_element(By.CLASS_NAME, "Pke_EE")
search_button = driver.find_element(By.CLASS_NAME, "_2iLD__")
input_search.send_keys(p_name)

sleep(1)
search_button.send_keys(Keys.ENTER)

f_products = []
f_prices = []

f_product = driver.find_elements(By.CLASS_NAME, "_4rR01T")
f_price = driver.find_elements(By.CLASS_NAME, "_25b18c")

a = 1


for pr in f_price:
    if a > num:
        break
    else:
        pri = ''
        countRupee = 0
        for i in pr.text:
            if i == "\u20B9":
                countRupee += 1
                continue
            if i == '\n':
                break

            if i != ',':
                if countRupee == 2:
                    break
                pri += i
    pri = int(pri)
    f_prices.append(pri)
    a += 1
print(len(f_prices))
a = 1
for p in f_product:
    if a > num:
        break
    else:
        f_products.append(p.text)
        a += 1
a = 1
if len(f_products) == 0:
    f_product = driver.find_elements(By.CLASS_NAME, "s1Q9rs")
    for p in f_product:
        if a > num:
            break
        else:
            f_products.append(p.text)
            a += 1
a = 1
if len(f_products) == 0:
    f_product = driver.find_elements(By.CLASS_NAME, "_2WkVRV")
    for p in f_product:
        if a > num:
            break
        else:
            f_products.append(p.text)
            a += 1

print(len(f_products))

driver.quit()

if len(a_products) != len(a_prices) != len(f_products) != len(f_prices):
    print("sorry but there is some defects with the webpage they have some different tag coming for some of the names or prices,\n please bear with us now but surely it would be fixed in the future updates\nstay tuned\nthanks for using!!")
    exit()

if len(a_products) < num and len(a_prices) < num and len(f_products) < num and len(f_prices) < num:
    print("No results found")
    exit()


final_ans_list_1 = []
final_ans_list_2 = []

for i in range(num):
    ans_list = []
    ans_list.append(a_products[i])
    ans_list.append(a_prices[i])
    final_ans_list_1.append(ans_list)
for i in range(num):
    ans_list = []
    ans_list.append(f_products[i])
    ans_list.append(f_prices[i])
    final_ans_list_2.append(ans_list)

t = Texttable()
t.add_rows(
    [['Amazon products', 'Amazon Prices'], final_ans_list_1[0], final_ans_list_1[1],
     final_ans_list_1[2], final_ans_list_1[3]])
print(t.draw())

q = Texttable()
q.add_rows(
    [['Flipkart products', 'Flipkart Prices'], final_ans_list_2[0], final_ans_list_2[1],
     final_ans_list_2[2], final_ans_list_2[3]])
print(q.draw())
