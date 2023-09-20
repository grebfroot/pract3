a1=float(input("Введите первое число: "))
operation=input("Введите операцию (+, -, *, /): ")
a2=float(input("Введите второе число: "))

if operation not in ('+','-','*','/'):
    print("Недопустимая операция.")
    
else:
    
    if operation=='/' and a2==0:
        print("Нельзя делить на ноль.")
        
    else:
        
        if operation=='+':
            rezult=a1+a2
        elif operation=='-':
            rezult=a1-a2
        elif operation=='*':
            rezult=a1*a2
        elif operation=='/':
            rezult=a1/a2

        print("Результат:", rezult)