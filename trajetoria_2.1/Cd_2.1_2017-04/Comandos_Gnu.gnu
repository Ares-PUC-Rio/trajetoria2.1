set xlabel 'Velocidade (Km/h)'
set ylabel 'Coeficiente de Arrasto'
set title 'Curva CD vs V'
set grid
set time
set style data linespoints
set key left bottom
plot './Saida/Curva_Alfa_2.txt'using 2:3 notitle linetype 7                                         
pause -1 ' Continua ? '
set term png nocrop enhanced size 1280,720
set out './Saida/Curva_Alfa_2.png'                                                                  
replot

