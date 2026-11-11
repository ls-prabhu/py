import threading
import time

def even(number_list):
    count = 0
    for num in number_list:
        if num % 2 == 0:
            count += 1
            time.sleep(1)
            print("Even number : ",num)
    print("Number of even numbers : ",count)


if __name__ == "__main__":
    num1 = input("please enter more than 1 number")
    list1 = [int(i) for i in num1.split()]

    num2 = input("please enter more than 1 number")
    list2 = [int(i) for i in num2.split()]

    t1 = threading.Thread(target=even, args=(list1,))
    t2 = threading.Thread(target=even, args=(list2,))
    t1.start()
    t2.start()  
    t1.join()
    t2.join()