a1=float(input("Введите первое число: "))
operation=input("Введите операцию (+, -, *, /): ")
a2=float(input("Введите второе число: "))

while operation!='1':
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
    operation=input("Чтобы завершить вычисление нажмите 1. Чтобы продолжить - снова выберите операцию (+, -, *, /):")
    if operation!='1':
        a1=rezult
        a2=float(input("Введите второе число: "))
else:
    print("Вычисление завершено.")
