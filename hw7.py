shopping_bag = {}
print('[구입]')
while True:
    item = str(input('상품명? '))
    if item == '' :
        break
    number = int(input('수량은? '))
    shopping_bag[item] = number
    print(f'장바구니에 {item} {number}개가 담겼습니다.')
print(f'>>> 장바구니 보기:[{shopping_bag}]')
print('[검색]')
I = str(input('장바구니에서 확인하고자 하는 상품은? '))
print(f'{I}은(는) {shopping_bag.get(I)}개 담겨 있습니다.')




