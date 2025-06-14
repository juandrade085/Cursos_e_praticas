l =float(input('Largura da parede: '))
a =float(input('Altura da parede: '))
área =l*a
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {} m²'.format(l, a, área))
print('Para pintaar essa parede, você precisará de {}l de tinta.'.format(área/2))