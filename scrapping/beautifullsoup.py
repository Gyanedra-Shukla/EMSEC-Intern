import pandas as pd
from bs4 import BeautifulSoup
import pandas
import requests

url='https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartphone%7CMobiles&requestId=62ffd683-932b-4d74-9aef-a363e453bc90&as-searchtext=smartp'

page = requests.get(url)
arr = []
arr2 = []
arr3=[]
s = BeautifulSoup(page.content, "html.parser")
d = s.find_all("div", class_="_4rR01T")
d1 = s.find_all("div", class_="_30jeq3 _1_WHN1")
d2= s.find_all("a",class_="_1fQZEK")


print(d2)

for i in range(len(d)):
    arr.append(d[i].string)
    arr2.append(d1[i].string)
    arr3.append(d2[i].get_atrribute("href"))

# print(arr3)
# print(arr2)
# df=pd.DataFrame({"name of phone":arr, "Price of phone":arr2})
# df.to_csv('data.csv',index=False)
#print(df)


