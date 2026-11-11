def demp_exe(choice):
    try:
        if choice == 1:
            num = int(input("enter a number: "))
            square = num * num
            print(f"The square of {num} is {square}.")
            
        elif choice == 2:
            lst1 = [10,20,30]
            item = lst1[5]
            print(f"The item at index 5 is {item}.")
        elif choice == 3:
            print(lst)
        
        elif choice == 4:
            sm= "num"+4
            print(sm)
            
        elif choice == 5:
            num1 = int(input("enter a number1: "))
            num2 = int(input("enter a number2: "))
            result = num1 / num2
            print(f"The result of division is {result}.")
            
    except ValueError as ve:
        print("valueerror",ve)
        
    except IndexError as e:
        print("indexerror",e)
        
    except NameError as ne:
        print("nameerror",ne)
        
    except TypeError as te:
        print("typeerror",te)
        
    except ZeroDivisionError as zde:
        print("zerodivisionerror",zde)
        
        
for i in range(1,6):
    print("------TEST CASE",i,"------")
    demp_exe(i)