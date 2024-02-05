#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    _list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            _list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            _list.append(0)
        except IndexError:
            print("out of range")
            _list.append(0)
        else:
            _list.append(result)
        finally:
            pass
    return _list
