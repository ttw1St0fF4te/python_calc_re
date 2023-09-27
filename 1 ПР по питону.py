import math
a = str(input('Введите оператор: '))
try:
    if a == "cos" or a == "sin" or a == "tan" or a == "sqrt" or a == "!":
        b = int(input('Введите число: '))
    else:
        c = int(input('Введите 1 число: '))
        d = int(input('Введите 2 число: '))
except ValueError:
    print("Вы ввели не число")
result = 0
flag = 0
while True:
    match a:
        case "+":
            if flag == 0:
                result += (c+d)
                print(result)
            else:
                result += f
                print(result)
        case "-":
            if flag == 0:
                result += (c-d)
                print(result)
            else:
                result -= f
                print(result)
        case "*":
            if flag == 0:
                result = (c*d)
                print(result)
            else:
                result *= f
                print(result)
        case "/":
            if flag == 0:
                if d == 0:
                    print('На ноль делить нельзя!')
                    break
                else:
                    result += (c/d)
            else:
                if f == 0:
                    print('На ноль делить нельзя!')
                    break
                else:
                    result /= f
                    print(result)
        case "!":
            if flag == 0:
                if (b<0):
                    print('Нельзя вывести факториал из отрицательного числа.')
                    break
                else:
                    result += math.factorial(b)
                    print(result)
            else:
                if (f<0):
                    print('Нельзя вывести факториал из отрицательного числа.')
                    break
                else:
                    result += math.factorial(f) 
                    print(result)
        case "pow":
            if flag == 0:
                result += math.pow(c,d)
                print(result)
            else:
                result += math.pow(result,f)
                print(result)
        case "sqrt":
            if flag == 0:
                if (b<0):
                    print('Нельзя вывести квадратный корень из отрицательного числа.')
                    break
                else:
                    result += math.sqrt(b)
                    print(result)
            else:
                if (f<0):
                    print('Нельзя вывести квадратный корень из отрицательного числа.')
                    break
                else:
                    result += math.sqrt(f) 
                    print(result)
        case "cos":
            if flag == 0:
                result += (math.cos(b))
                print(result)
            else:
                result += math.cos(f)
                print(result)
        case "sin":
            if flag == 0:
                result += (math.sin(b))
                print(result)
            else:
                result += math.sin(f)
                print(result)
        case "tan":
            if flag == 0:
                result += (math.tan(b))
                print(result)
            else:
                result += math.tan(f)
                print(result)
        case _:
            print('Вы ввели неверный оператор') 
    flag = 1
    print('Хотите продолжить? y/n')
    prod = str(input())
    if prod == "y":
        try:
            print('Введите число: ')
            f = int(input())
        except ValueError:
            print('Вы ввели не число') 
            break
        print('Введите оператор')
        a = str(input())
        continue 
    else:
        break