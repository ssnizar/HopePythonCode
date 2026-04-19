class MultiFunctionCls():
    def oddEven():
        num1=input("Enter the number:")
        if not (num1.isdigit()):
            #print("No Number")
            Messge="No Number"
            return Messge
        
        num=int(num1)
        if ((num%2)==0):
            Messge="Even Number"
            #print("Even Number")
        else:
            Messge="Odd Number"
            #print("Odd Number")
        return Messge

    def BMI():
        bmi=float(input("Enter the BMI Index"))
        if (bmi<18.4):
            Messge="Under Weight"
            print("Under Weight")
        elif (bmi<=24.9):
            Messge="Healthy BMI"        
            print("Healthy BMI")
        elif (bmi<=29.9):
            Messge="OverWeight"
            print("OverWeight")
        else:
            Messge="Very OverWeight"
            print("Very OverWeight")
        return Messge