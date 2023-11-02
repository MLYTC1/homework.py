#erator პროგრამა რომელშიც დაგენერირდბა პაროლი, 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#, 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347
import random



for char1 in range(2) :

 char1 = ["!#%(#)^#"]
char2 = ["ა,ბ,გ,ქ,წ,ე,კ,ჯ,ას,კ,ჯ,ქ,წ,ე"]
char3 = ["2,1,5,3,4,6,3,4,7,3,4,7"]


symbol1 = random.choice(char1)
symbol2 = random.choice(char2)
symbol3 = random.choice(char3)  


password = (random.choice(symbol1))+(random.choice(symbol1))+(random.choice(symbol2))+(random.choice(symbol2))+(random.choice(symbol3))+(random.choice(symbol3))+(random.choice(symbol3))+(random.choice(symbol3))
print(password)