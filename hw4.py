def rep_char(c,n) :
    print(c*n)
def draw_line_string(msg) :
    nstr = len(msg)
    rep_char('-',nstr * 2 + 4)
    print('Hello '+f'{msg},')
    print('Welcome to seoul.')
    rep_char('-',nstr * 2 + 4)
N = str(input('Input his/her name: '))
draw_line_string(N)









