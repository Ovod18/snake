def main():
    
    def get_name():
        name =  input('введите имя: ')
        return name
    
#    print('ваше имя: ', get_name())
    def is_even(number):
        if (number % 2) == 0:
            status = True
        else:
            status = False
        return status 

#    number = int(input('введите число: '))
#    if is_even(number):
#        print('число чётное')
#    else:
#        print('число нечётное')
    
    numbers = list(range(3))
    print(numbers[:])
main()    
