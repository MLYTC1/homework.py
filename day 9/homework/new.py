tickrt_price = 25

age = input ("how old are you?\n")
if int(age) > 18 :
  print("bileti girs 25 lari")
human_quantity = input("how much humans are there?\n")
adult_quantity = input("how much adults are there?\n")
kids_quantity = input("how much kids are there?\n")
tickets_total_price = (25*int(human_quantity)-25*int(kids_quantity))
print(str(tickets_total_price)  +  "lari iqneba gadasaxdeli jsmshi") 