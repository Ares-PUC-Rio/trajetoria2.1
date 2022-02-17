set xlabel 'Velocidade (Km/h)'
set ylabel 'Coeficiente de Arrasto'
set title 'Curva CD vs V'
set grid
set time
set style data linespoints
set key left bottom
plot 'Curva_Epsilon_1.txt'using 2:3 notitle linetype
pause -1 ' Continua ? '
set term png nocrop enhanced size 1280,720
set out 'Curva_Epsilon_1.png'             
replot

