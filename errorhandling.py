

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        #print(f'please enter numbers: error as follows - {err}')
        print(err)

#print(sum(1, '0'))



while True:
    try:
        age = int(input('what is your age?'))
        #age = 100/age
        if age < 5.555:
            raise Exception('must be above 18')
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter an age above zero')
    else:
        print('thanks')
        break
    finally: # Finally will run at the end of each loop no matter what, exception or no exception.
        print('ok I am finally done')
    print('this will print if the loop does not reach else as else has a break')
