print('Silahkan masukan dua angka untuk pembagian.')
try:
    num1 = int(input('Masukan angka yang akan dibagi: '))
    num2 = int(input('Masukan angka pembogi: '))
    print('{0} dibagi {1} = {2}'.format (num1, num2, num1/num2))
except ZeroDivisionError:
    print('Error: tidak bisa membagi bilangan dengan nol. ')
