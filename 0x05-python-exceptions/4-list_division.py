#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    err_type = None
    for i in range(0, list_length):
        try:
            results.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            err_type = "division by 0"
            results.append(0)
        except TypeError:
            err_type = "wrong type"
            results.append(0)
        except IndexError:
            err_type = "out of range"
            results.append(0)
        finally:
            if (err_type):
                print(err_type)
    return results
