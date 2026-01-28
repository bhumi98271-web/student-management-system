class Student:
    def __init__(self,name,rollno,marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
        self.menu()
    def get_data(self):
        print(self.__name)
        print(self.__rollno)
        print(self.__marks)
    def menu(self):
        choice=int(input("1.Update Marks\n2.Calculate Average\n3.Display Report\n"))
        if choice==1:
            self.update_marks()
        elif choice==2:
            self.calculate_avrage()
        elif choice==3:
            self.display_report()
        else:
            print("invalid input")

    def update_marks(self):
        new_marks=[]
        for i in range(len(self.__marks)):
            enter_mark=int(input("enter the new mark"))
            new_marks.append(enter_mark)
            self.__marks=new_marks
        print("marks update successfully")
        self.menu()

    def calculate_avrage(self):

        print(f"your avg is = {sum(self.__marks)}/{len(self.__marks)}")
        self.menu()
    
    def display_report(self):

        print(f"NAME:{self.__name}\nROLLNO:{self.__rollno}\nMARKS:{self.__marks}")
        self.menu()
    
    

