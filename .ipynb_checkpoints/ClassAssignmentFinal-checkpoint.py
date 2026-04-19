class AssignmentFinal():

    def Subfields():
        list1=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for value1 in list1:
            print(value1)

    def oddEven():
        num1=input("Enter the number:")
        if not (num1.isdigit()):
            #print("No Number")
            Messge="No Number"
            return Messge
        
        num=int(num1)
        if ((num%2)==0):
            Messge=f"{num1} is Even Number"
            #print("Even Number")
        else:
            Messge=f"{num1} is Odd Number"
            #print("Odd Number")
        return Messge

    def Elegible(gender,age):
        print("Your Gender:", gender)
        print("Your Age:",age)
        if ((gender=="Male") and (age>=21)):
            print("ELIGIBLE")
        elif ((gender=="Female") and (age>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELGIBLE")

    def percentage(m1,m2,m3,m4,m5):
        print("Subject1=", m1)
        print("Subject1=", m2)    
        print("Subject1=", m3)
        print("Subject1=", m4)
        print("Subject1=", m5)    
        total=m1+m2+m3+m4+m5
        print("total :",total)
        per=total/5
        print("Percentage :",per)

    def triangle_area(base, height):
        print("base :", base)
        print("height:",height)
        print("Area formula : (Height * base)/2)")
        area1 = (base*height)/2
        print("Area of triangle", area1)

    def triangle_perimeter(base, side1,side2):
        print("base:",base)
        print("side1:",side1)
        print("side2:",side2)
        perimeter=base+side1+side2
        print("Perimeter formula: base+side1+side2")
        print("Perimeter of Triangle:",perimeter)
