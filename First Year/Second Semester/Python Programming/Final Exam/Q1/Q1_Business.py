import Q1_db_Func as db


def validateUpdate():  # VALIDATES ENTRIES
    while True:
        code = input('Product Code: ')
        pCode = db.checkProductCode(code)
        if pCode == None:
            print('Product Not Found!')
        else:
            pass
            break
    while True:
        try:
            price = float(input('New Product Price: '))
            break
        except ValueError:
            print('Invalid Entry')

    return pCode, price
