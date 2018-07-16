vC = ['Xd1', 'Xd2', 'Xd3', 'Xd4', 'Xr1', 'Xr2', 'Xr3', 'Xr4', 'Xf1', 'Xf2', 'Xf3', 'Xf4', 'Xg1', 'Xg2', 'Xg3', 'Xg4',
      'Xn1', 'Xn2', 'Xn3', 'Xn4', 'Xj1', 'Xj2', 'Xj3', 'Xj4', 'Xl1', 'Xl2', 'Xl3', 'Xl4']
fC = '(Xd1$vXd2$vXd3$vXd4)$n(Xr1$vXr2$vXr3$vXr4)$n(Xf1$vXf' \
     '2$vXf3$vXf4)$n(Xg1$vXg2$vXg3$vXg4)$n(Xn1$vXn2$vXn3$vXn4)$n(Xj1$vXj2$vXj3$vXj4)$n(Xl1$vXl2$v' \
     'Xl3$vXl4)$n(Xd1$vXr1$vXf1$vXg1$vXn1$vXj1$vXl1)$n(Xd2$vXr2$vXf2$vXg2$vXn2$vXj2$vXl2)$n(Xd3$vXr3$vXf3$vXg3$vXn3$vXj3$vXl3)$' \
     'n(Xd4$vXr4$vXf4$vXg4$vXn4$vXj4$vXl4)$n(~Xd1$v~Xj2)$n(~Xd1$v~Xj3)$n(~Xd1$v~Xj4)$n(~Xd2$v~Xj3)$n(~Xd2$v~Xj4)$n(~Xd3$v~Xj4)$n(~Xd2$v' \
     '~Xj1)$n(~Xd3$v~Xj1)$n(~Xd4$v~Xj1)$n(~Xd3$v~Xj2)$n(~Xd4$v~Xj2)$n(~Xd4$v~Xj3)$n(~Xd1$v~Xl2)$n(~Xd1$v~Xl3)$n(~Xd1$v~Xl4)$n(~Xd2$v~Xl3)$n(~X' \
     'd2$v~Xl4)$n(~Xd3$v~Xl4)$n(~Xd2$v~Xl1)$n(~Xd3$v~Xl1)$n(~Xd4$v~Xl1)$n(~Xd3$v~Xl2)$n(~Xd4$v~Xl2)$n(~Xd4$v~Xl3)$n(~Xr1$v~Xl2)$n(~Xr1$v~Xl3)$n' \
     '(~Xr1$v~Xl4)$n(~Xr2$v~Xl3)$n(~Xr2$v~Xl4)$n(~Xr3$v~Xl4)$n(~Xr2$v~Xl1)$n(~Xr3$v~Xl1)$n(~Xr4$v~Xl1)$n(~Xr3$v~Xl2)$n(~Xr4$v~Xl2)$n(~Xr4$v~Xl3)' \
     '$n(~Xr1$v~Xj2)$n(~Xr1$v~Xj3)$n(~Xr1$v~Xj4)$n(~Xr2$v~Xj3)$n(~Xr2$v~Xj4)$n(~Xr3$v~Xj4)$n(~Xr2$v~Xj1)$n(~Xr3$v~Xj1)$n(~Xr4$v~Xj1)$n(~Xr3$v~Xj2)' \
     '$n(~Xr4$v~Xj2)$n(~Xr4$v~Xj3)$n(~Xf1$v~Xg2)$n(~Xf1$v~Xg3)$n(~Xf1$v~Xg4)$n(~Xf2$v~Xg3)$n(~Xf2$v~Xg4)$n(~Xf3$v~Xg4)$n(~Xf2$v~Xg1)$n(~Xf3$v~Xg1)' \
     '$n(~Xf4$v~Xg1)$n(~Xf3$v~Xg2)$n(~Xf4$v~Xg2)$n(~Xf4$v~Xg3)$n(~Xf1$v~Xn2)$n(~Xf1$v~Xn3)$n(~Xf1$v~Xn4)$n(~Xf2$v~Xn3)$n(~Xf2$v~Xn4)$n(~Xf3$v~Xn4)' \
     '$n(~Xf2$v~Xn1)$n(~Xf3$v~Xn1)$n(~Xf4$v~Xn1)$n(~Xf3$v~Xn2)$n(~Xf4$v~Xn2)$n(~Xf4$v~Xn3)$n(~Xg1$v~Xl2)$n(~Xg1$v~Xl3)$n(~Xg1$v~Xl4)$n(~Xg2$v~Xl3)$' \
     'n(~Xg2$v~Xl4)$n(~Xg3$v~Xl4)$n(~Xg2$v~Xl1)$n(~Xg3$v~Xl1)$n(~Xg4$v~Xl1)$n(~Xg3$v~Xl2)$n(~Xg4$v~Xl2)$n(~Xg4$v~Xl3)$n(~Xg1$v~Xj2)$n(~Xg1$v~Xj3)$n' \
     '(~Xg1$v~Xj4)$n(~Xg2$v~Xj3)$n(~Xg2$v~Xj4)$n(~Xg3$v~Xj4)$n(~Xg2$v~Xj1)$n(~Xg3$v~Xj1)$n(~Xg4$v~Xj1)$n(~Xg3$v~Xj2)$n(~Xg4$v~Xj2)$n(~Xg4$v~Xj3)$n' \
     '(~Xn1$v~Xl2)$n(~Xn1$v~Xl3)$n(~Xn1$v~Xl4)$n(~Xn2$v~Xl3)$n(~Xn2$v~Xl4)$n(~Xn3$v~Xl4)$n(~Xn2$v~Xl1)$n(~Xn3$v~Xl1)$n(~Xn4$v~Xl1)$n(~Xn3$v~Xl2)$n' \
     '(~Xn4$v~Xl2)$n(~Xn4$v~Xl3)'
