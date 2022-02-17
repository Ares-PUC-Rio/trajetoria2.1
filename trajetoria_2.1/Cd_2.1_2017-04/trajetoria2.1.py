import os
import subprocess
from tkinter import *
# import time

class App:
    def __init__(self, master=None):
        self.frame = Frame()
        
        self.titulo = Label(self.frame, text="Dados")
        self.titulo["font"] = ("Arial", "10", "bold")        
        self.aLabel = Label(self.frame,text="Unidade utilizada nas medidas do foguete (1=milímetros, 2=pés, 3=polegadas)")
        self.a = Entry(self.frame)
        self.bLabel = Label(self.frame,text="Temperatura atmosférica local (°C)")
        self.b = Entry(self.frame)
        self.cLabel = Label(self.frame,text="Pressão atmosférica local (kPa)")
        self.c = Entry(self.frame)
        self.dLabel = Label(self.frame,text="Número de Reynolds de transição para corpos de revolução")
        self.d = Entry(self.frame)
        self.fLabel = Label(self.frame,text="Número de Reynolds de transição para empenas")
        self.f = Entry(self.frame)
        self.gLabel = Label(self.frame,text="Número de mach máximo")
        self.g = Entry(self.frame)
        self.hLabel = Label(self.frame,text="Número de pontos do gráfico")
        self.h = Entry(self.frame)
        self.iLabel = Label(self.frame,text="Tipo de nariz (1=elpsoide, 2=ogiva, 3=cônico, 4=parabólico)")
        self.i = Entry(self.frame)
        self.jLabel = Label(self.frame,text="Comprimento total do nariz (mm)")
        self.j = Entry(self.frame)
        self.kLabel = Label(self.frame,text="Diâmetro do nariz (mm)")
        self.k = Entry(self.frame)
        self.lLabel = Label(self.frame,text="Comprimento do tubo (mm) ")
        self.l = Entry(self.frame)
        self.mLabel = Label(self.frame,text="Diâmetro do tubo (mm)")
        self.m = Entry(self.frame)
        self.nLabel = Label(self.frame,text="Número de empenas")
        self.n = Entry(self.frame)
        self.oLabel = Label(self.frame,text="Tipo de seção transversal(0=quadrada, 1=arredondada)")
        self.o = Entry(self.frame)
        self.pLabel = Label(self.frame,text="Espessura (mm)")
        self.p = Entry(self.frame)
        self.qLabel = Label(self.frame,text="Comprimento da base (mm)")
        self.q = Entry(self.frame)
        self.rLabel = Label(self.frame,text="Comprimento do topo (mm)")
        self.r = Entry(self.frame)
        self.sLabel = Label(self.frame,text="Altura (mm)")
        self.s = Entry(self.frame)
        self.tLabel = Label(self.frame,text="Comprimento do contorno (mm)")
        self.t = Entry(self.frame)
        self.uLabel = Label(self.frame,text="Posição do motor (0=interno, 1=externo)")
        self.u = Entry(self.frame)
        self.vLabel = Label(self.frame,text="Comprimento do motor (mm)")
        self.v = Entry(self.frame)
        self.wLabel = Label(self.frame,text="Diâmetro do motor (mm)")
        self.w = Entry(self.frame)
        self.xLabel = Label(self.frame,text="Condição do motor (ligado)(1=sim, 0=não)")
        self.x = Entry(self.frame)
        self.yLabel = Label(self.frame,text="Diâmetro da tubeira (mm)")
        self.y = Entry(self.frame)
        self.zLabel = Label(self.frame,text="Presença de tubo-guia (1=sim, 0=não)")
        self.z = Entry(self.frame)
        self.zaLabel = Label(self.frame,text="Diâmetro externo do tubo-guia (mm)")
        self.za = Entry(self.frame)
        self.zbLabel = Label(self.frame,text="Espessura do tubo-guia (mm)")
        self.zb = Entry(self.frame)
        self.zcLabel = Label(self.frame,text="Comprimento do tubo-guia (mm)")
        self.zc = Entry(self.frame)
        self.zdLabel = Label(self.frame,text="Presença de estopim externo (1=sim, 0=não)")
        self.zd = Entry(self.frame)
        self.zeLabel = Label(self.frame,text="Diâmetro do estopim (mm)")
        self.ze = Entry(self.frame)
        self.zfLabel = Label(self.frame,text="Comprimento do estopim (mm)")
        self.zf = Entry(self.frame)
        
        self.execute = Button(self.frame)
        self.execute["text"] = "Executar"
        self.execute["command"] = self.preencherDados

        self.mensagem = Label(self.frame, text="")

        self.titulo.grid(   row=0, column=1, sticky=W, pady=3,padx=3)
        self.aLabel.grid(  row=1, column=1, sticky=W, pady=3,padx=3)
        self.a.grid(  row=1, column=2, sticky=E, pady=3,padx=3)
        self.bLabel.grid(  row=2, column=1, sticky=W, pady=3,padx=3)
        self.b.grid(  row=2, column=2, sticky=E, pady=3,padx=3)
        self.cLabel.grid(  row=3, column=1, sticky=W, pady=3,padx=3)
        self.c.grid(  row=3, column=2, sticky=E, pady=3,padx=3)
        self.dLabel.grid(  row=4, column=1, sticky=W, pady=3,padx=3)
        self.d.grid(  row=4, column=2, sticky=E, pady=3,padx=3)
        self.fLabel.grid(  row=5, column=1, sticky=W, pady=3,padx=3)
        self.f.grid(  row=5, column=2, sticky=E, pady=3,padx=3)
        self.gLabel.grid(  row=6, column=1, sticky=W, pady=3,padx=3)
        self.g.grid(  row=6, column=2, sticky=E, pady=3,padx=3)
        self.hLabel.grid(  row=7, column=1, sticky=W, pady=3,padx=3)
        self.h.grid(  row=7, column=2, sticky=E, pady=3,padx=3)
        self.iLabel.grid(  row=8, column=1, sticky=W, pady=3,padx=3)
        self.i.grid(  row=8, column=2, sticky=E, pady=3,padx=3)
        self.jLabel.grid(  row=9, column=1, sticky=W, pady=3,padx=3)
        self.j.grid(  row=9, column=2, sticky=E, pady=3,padx=3)
        self.kLabel.grid(  row=10, column=1, sticky=W, pady=3,padx=3)
        self.k.grid(  row=10, column=2, sticky=E, pady=3,padx=3)
        self.lLabel.grid(  row=11, column=1, sticky=W, pady=3,padx=3)
        self.l.grid(  row=11, column=2, sticky=E, pady=3,padx=3)
        self.mLabel.grid(  row=12, column=1, sticky=W, pady=3,padx=3)
        self.m.grid(  row=12, column=2, sticky=E, pady=3,padx=3)
        self.nLabel.grid(  row=13, column=1, sticky=W, pady=3,padx=3)
        self.n.grid(  row=13, column=2, sticky=E, pady=3,padx=3)
        self.oLabel.grid(  row=14, column=1, sticky=W, pady=3,padx=3)
        self.o.grid(  row=14, column=2, sticky=E, pady=3,padx=3)
        self.pLabel.grid(  row=15, column=1, sticky=W, pady=3,padx=3)
        self.p.grid(  row=15, column=2, sticky=E, pady=3,padx=3)
        self.qLabel.grid(  row=16, column=1, sticky=W, pady=3,padx=3)
        self.q.grid(  row=16, column=2, sticky=E, pady=3,padx=3)
        self.rLabel.grid(  row=17, column=1, sticky=W, pady=3,padx=3)
        self.r.grid(  row=17, column=2, sticky=E, pady=3,padx=3)
        self.sLabel.grid(  row=18, column=1, sticky=W, pady=3,padx=3)
        self.s.grid(  row=18, column=2, sticky=E, pady=3,padx=3)
        self.tLabel.grid(  row=19, column=1, sticky=W, pady=3,padx=3)
        self.t.grid(  row=19, column=2, sticky=E, pady=3,padx=3)
        self.uLabel.grid(  row=20, column=1, sticky=W, pady=3,padx=3)
        self.u.grid(  row=20, column=2, sticky=E, pady=3,padx=3)
        self.vLabel.grid(  row=21, column=1, sticky=W, pady=3,padx=3)
        self.v.grid(  row=21, column=2, sticky=E, pady=3,padx=3)
        self.wLabel.grid(  row=22, column=1, sticky=W, pady=3,padx=3)
        self.w.grid(  row=22, column=2, sticky=E, pady=3,padx=3)
        self.xLabel.grid(  row=23, column=1, sticky=W, pady=3,padx=3)
        self.x.grid(  row=23, column=2, sticky=E, pady=3,padx=3)
        self.yLabel.grid(  row=24, column=1, sticky=W, pady=3,padx=3)
        self.y.grid(  row=24, column=2, sticky=E, pady=3,padx=3)
        self.zLabel.grid(  row=25, column=1, sticky=W, pady=3,padx=3)
        self.z.grid(  row=25, column=2, sticky=E, pady=3,padx=3)
        self.zaLabel.grid(  row=26, column=1, sticky=W, pady=3,padx=3)
        self.za.grid(  row=26, column=2, sticky=E, pady=3,padx=3)
        self.zbLabel.grid(  row=27, column=1, sticky=W, pady=3,padx=3)
        self.zb.grid(  row=27, column=2, sticky=E, pady=3,padx=3)
        self.zcLabel.grid(  row=28, column=1, sticky=W, pady=3,padx=3)
        self.zc.grid(  row=28, column=2, sticky=E, pady=3,padx=3)
        self.zdLabel.grid(  row=29, column=1, sticky=W, pady=3,padx=3)
        self.zd.grid(  row=29, column=2, sticky=E, pady=3,padx=3)
        self.zeLabel.grid(  row=30, column=1, sticky=W, pady=3,padx=3)
        self.ze.grid(  row=30, column=2, sticky=E, pady=3,padx=3)
        self.zfLabel.grid(  row=31, column=1, sticky=W, pady=3,padx=3)
        self.zf.grid(  row=31, column=2, sticky=E, pady=3,padx=3)
        self.execute.grid(row=32, column=2, pady=3, padx=3)
        self.frame.grid(row=0, column=0)

    def preencherDados(self):
        arq = "arquivo_dados.txt"
        
        with open("Dados.txt", "r") as file:
            lines = file.readlines()
		
        lines[0] = arq
        with open("Dados.txt", "w") as file:
            for line in lines:
                file.write(line)   

        with open("Dados_LAE_22.txt", "r") as file:
            lines = file.readlines()
			
        lines[1] = self.a.get() + "\n"
        lines[2] = self.b.get() + "\n"
        lines[3] = self.c.get() + "\n"
        lines[4] = self.d.get() + "\n"
        lines[5] = self.f.get() + "\n"
        lines[6] = self.g.get() + "\n"
        lines[7] = self.h.get() + "\n"
        lines[8] = self.i.get() + "\n"
        lines[9] = self.j.get() + "\n"
        lines[10] = self.k.get() + "\n"
        lines[11] = self.l.get() + "\n"
        lines[12] = self.m.get() + "\n"
        lines[13] = self.n.get() + "\n"
        lines[14] = self.o.get() + "\n"
        lines[15] = self.p.get() + "\n"
        lines[16] = self.q.get() + "\n"
        lines[17] = self.r.get() + "\n"
        lines[18] = self.s.get() + "\n"
        lines[19] = self.t.get() + "\n"
        lines[20] = self.u.get() + "\n"
        lines[21] = self.v.get() + "\n"
        lines[22] = self.w.get() + "\n"
        lines[23] = self.x.get() + "\n"
        lines[24] = self.y.get() + "\n"
        lines[25] = self.z.get() + "\n"
        lines[26] = self.za.get() + "\n"
        lines[27] = self.zb.get() + "\n"
        lines[28] = self.zc.get() + "\n"
        lines[29] = self.zd.get() + "\n"
        lines[30] = self.ze.get() + "\n"
        lines[31] = self.zf.get() + "\n"
		
        with open(arq, "w") as file:
            for line in lines:
                file.write(line)        

        subprocess.Popen("CD 2.1.exe")

root = Tk()
root.geometry("700x400+300+100")
root.title("Trajetória")
App(root)
root.mainloop()
