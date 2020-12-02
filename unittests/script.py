def do_stuff(num=0):
    try:
        if num == 0 or num:
            return int(num) + 5
        else:
            return 'please enter number'
    except (ValueError, TypeError) as err:
        return err
    #raise err
