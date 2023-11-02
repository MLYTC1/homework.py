score1 = int(input("enter your garde!:"))
score2 = int(input("enter your garde!:"))
score3 = int(input("enter your garde!:"))
score4 = int(input("enter your garde!:"))



grade = (score1+score2+score3+score4)/4
if grade > 9 :
   print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif grade < 5 :
   print("გილოცავ გაექეცი მატრიცას")
elif grade > 5 and grade < 9 :
   print("YOU ARE MID")
elif grade < 0 and grade > 10 :
   print("there is something wrong with you" )


