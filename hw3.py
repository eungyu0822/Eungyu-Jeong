def get_rate() :
    rate = int(input('할인율은?'))
    global exchange_rate
    exchange_rate = 100 - rate
def A_Price() :
    A = int(input('A상품의 할인된 가격은?'))
    global A_O
    A_O = A / exchange_rate * 100
def B_Price() :
    B = int(input('B상품의 할인된 가격은?'))
    global B_O
    B_O = B / exchange_rate * 100
def get_fixed_price() :
    get_rate()
    A_Price()
    B_Price()
    print('A상품의 정가는', A_O ,'원')
    print('B상품의 정가는', B_O ,'원')
get_fixed_price()
    
