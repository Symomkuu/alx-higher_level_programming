#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for i in range(list_length):
        try:
            x.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            x.append(0)
        except ZeroDivisionError:
            print("division by 0")
            x.append(0)
        except IndexError:
            print("out of range")
            x.append(0)
        finally:
            pass
    return (x)
