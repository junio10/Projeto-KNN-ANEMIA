from tkinter import *
import knn as k
from tkinter import messagebox


def diagnosticar():
    if k.Treinar(radio_Btn_gender.get(),box_hemoglobin.get(),box_Mch.get(),box_Mchc.get(),box_Mcv.get(),radio_Algoritmo.get()) == 1:
        messagebox.showwarning(title="Resultado do diagnóstico",message='Você foi diagnosticado com anemia. Recomendado procurar o centro de saúde mais próximo.')     
    else:
        messagebox.showinfo(title="Resultado do diagnóstico",message='Você não foi diagnosticado com anemia.')     
   
janela = Tk()

radio_Btn_gender = IntVar()
box_hemoglobin = DoubleVar()
box_Mch = DoubleVar()
box_Mchc = DoubleVar()
box_Mcv = DoubleVar()
radio_Algoritmo = IntVar()

janela.title("Diagnóstico de anemia")
janela.geometry("%dx%d+%d+%d"% (520,300,400,200))

txt_titulo = Label(janela, 
                   text="Diagnóstico de anemia",
                   font="Roboto 20",
                   relief="solid",
                   border= 1,
                   )
txt_titulo.grid(column=0, row=0, columnspan=5, pady=17)

rdioMasculino = Radiobutton(janela, 
                            text="Homem",
                            variable=radio_Btn_gender,
                            value=1,
                            font="Roboto 13",
                            )
rdioFeminino = Radiobutton(janela, 
                           text= "Mulher", 
                           variable=radio_Btn_gender, 
                           value=0,
                           font="Roboto 13",
                           )

rdioMasculino.grid(column=0, row=2,columnspan=3, pady=15)
rdioFeminino.grid(column=1, row=2,columnspan=5)

txt_Hemoglobin = Label(janela, text="Hemoglobina")
txt_Hemoglobin.grid(column= 0, row=4,columnspan=5, sticky="w")
value_Hemoglobin = Entry(janela,textvariable=box_hemoglobin,relief="solid",value=None)
value_Hemoglobin.grid(column=0, row =5,padx=3)

txt_Mch = Label(janela, 
                text="MCH",
                font="Roboto 9",
                )
txt_Mch.grid(column= 1, row=4, columnspan=5, sticky="w")
value_Mch = Entry(janela,textvariable=box_Mch,relief="solid")
value_Mch.grid(column=1, row =5,padx=3)

txt_Mchc = Label(janela,
                 text="MCHC",
                 font="Roboto 9"
                 )
txt_Mchc.grid(column= 2, row=4,columnspan=5, sticky="w")
value_Mchc = Entry(janela,textvariable=box_Mchc,relief="solid")
value_Mchc.grid(column=2, row =5,padx=3)

txt_Mcv = Label(janela,
                text="MCV",
                font="Roboto 9"
                )
txt_Mcv.grid(column= 3, row=4,columnspan=5, sticky="w")
value_Mcv = Entry(janela,textvariable=box_Mcv,relief="solid")
value_Mcv.grid(column=3, row =5,padx=3)

rdio_Knn = Radiobutton(janela, 
                       text="KNN", 
                       variable=radio_Algoritmo, 
                       value=1,
                       font="Roboto 11"
                       )
rdio_Preceptron = Radiobutton(janela, 
                              text= "Preceptron", 
                              variable=radio_Algoritmo, 
                              value=0,
                              font="Roboto 11"
                              )

rdio_Knn.grid(column = 1, row = 6, pady=15)
rdio_Preceptron.grid(column = 2, row = 6)
botao = Button(janela,text='Diagnósticar',
               fg = 'white', 
               bg = 'green',
               command=diagnosticar,
               font="Roboto 13",
               relief="ridge",
               border=3,
               )
botao.grid(column=0, row=7,columnspan=5)

botao_sair = Button(janela,text='Sair',
               fg = 'white', 
               bg = 'Red',
               command=quit,
               font="Roboto 13",
               relief="ridge",
               border=3,
               )
botao_sair.grid(column=1, row=7,columnspan=5,sticky="w")


text2 = Label(janela,text='')
text2.grid(column=0, row=8,columnspan=5)
#chamada da funcao


#labelValue = Label(janela, textvariable=)
#labelValue.grid(column = 0, row = 5)

janela.mainloop()






