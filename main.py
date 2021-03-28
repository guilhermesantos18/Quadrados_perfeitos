from math import sqrt


def find_next_square(sq):
    if sqrt(sq) == int:
        num = sqrt(sq) + 1
        result = int(num**2)
        return result


print(f'O proximo quadrado perfeito de 121 é {find_next_square(121)}')
print(f'O proximo quadrado perfeito de 625 é {find_next_square(625)}')
print(f'O proximo quadrado perfeito de 319225 é {find_next_square(319225)}')
print(f'O proximo quadrado perfeito de 15241383936 é {find_next_square(15241383936)}')
print(f'O proximo quadrado perfeito de 155 é {find_next_square(155)}')
print(f'O proximo quadrado perfeito de 342786627 é {find_next_square(342786627)}')
