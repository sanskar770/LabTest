# Q1:Subtract a week ( 7 days)  from a given date in Python
from datetime import datetime, timedelta
da = input("Enter Date ")
da1= datetime.strptime(da, "%Y-%m-%d")
print(da1- timedelta(days=7))

#Q2: Add week ( 7 days) and 12 hours to a given date
da2=datetime(2024, 3, 22, 10, 0, 0)
da3 =da2+ timedelta(days=7, hours=12)
print(da3)

#Q3: Print ten dates, each two a week apart, starting from today, in the form YYYY-MM-DD.
tday = datetime.today()
for i in range(10):
    dx = tday + timedelta(weeks=2 * i)
    print(dx.strftime("%Y-%m-%d"))
    
#Q4:calculate the number of days between two given dates
dt1 = datetime(2020, 2, 25)
dt2 = datetime(2020, 9, 17)
delta = dt2 - dt1
print("Diffrence", delta.days)

#Q5:Write a Python script to display the
#a) Current date and time
# b) Current year in full
# c) Month of year full name
#d) Weekday of the week
#e) Day of the month
#f) Day of week in full name

ur = datetime.now()
print("Current D&T", ur)
print("Year", ur.strftime("%Y"))
print("Month:", ur.strftime("%B"))
print("Day Number", ur.strftime("%w"))
print("Month Day", ur.strftime("%d"))
print("Day Name", ur.strftime("%A"))

#Q6: Follow the steps:
#Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the__init__()method.
#Create a variable named number_of_sides and set it equal to 3.
# Create a method named check_angles. The sum of a triangle&#39;s three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and Falseotherwise.
# Create a variable named my_triangle and set it equal to a new instance of your Triangleclass. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

class Traingle:
    number_of_sides=3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    def check_angles(self):
        if(self.angle1+self.angle2+self.angle3==180):
            return True
        else:
            return false
    
my_traingle=Traingle()
print(my_traingle.number_of_sides)
print(my_traingle.check_angles())

#Q7: Define a class called Songs, it will show the lyrics of a song. Its __init__() method should have two arguments:self and lyrics.lyricsis a list. Inside your class create a method calledsing_me_a_song that prints each element of lyricson his own line. Define a varible:
class song:

    def sing_me_a_song():
        for i in self.lyrics:
            print(i)
        
    def __init__(self,lyrics):
        self.lyrics=lyrics
happy_bday = Song(["May god bless you",
"Have a sunshine on you"
"Happy Birthday to you !"])
happy_bday.sing_me_a_song()
        
#Q8:Define a class called Lunch.Its __init__() method should have two arguments:selfanfmenu.Where menu is a string. Add a method called menu_price.It will involve a ifstatement:
class Lunch:
    def __init__(self,menu):
        self.menu=menu
    def menu_price():
        if self.menu == "menu 1":
            print("Your choice:", self.menu, "Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice:", self.menu, "Price 13.40")
        else:
            print("Error in menu")
            
Paul = Lunch("menu 1")
Paul.menu_price()

#Q9: Write a Python class which has two methods get_String and print_String. get_String accept a 
# string from the user and print_String print the string in upper case.

class sanskar:
    def get_string(self,strin):
        self.strin=strin
    def print_string(self):
        print(self.strin)
sanskar35=sanskar()
sanskar35.get_string("CDAC")
sanskar35.print_string()

#Q10: Write a program to find the area and perimeter of a rectangle using classes and objects.

class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def peri(self):
        return 2*(self.l+ self.b)
l = int(input("Enter Length of a Rectangle: "))
b= int(input("Enter Breadth of a Rectangle: "))
rect=Rectn(l,b)
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Area of rectangle",rec.area())
    elif choice == 2:
        print("Perimeter of rectangle",rect.peri())
    else :
        print("End of the Program")
        



        