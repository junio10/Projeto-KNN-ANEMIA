from tkinter import *
import knn as k


def te():
    
    if k.Treinar(radio_Btn.get(),box_hemoglobin.get(),box_Mch.get(),box_Mchc.get(),box_Mcv.get()) == 1:
        tex = 'anemico'
    else:
        tex = 'não tem anemia'
    
    texto = f'''
    {tex}
    '''
    text2['text'] = texto
    
    
    
    


janela = Tk()
radio_Btn = IntVar()
box_hemoglobin = DoubleVar()
box_Mch = DoubleVar()
box_Mchc = DoubleVar()
box_Mcv = DoubleVar()





janela.title("Diagnóstico de anemia")

txt_titulo = Label(janela, text="Diagnóstico de anemia")
txt_titulo.grid(column=0, row=0)

txt_genero = Label(janela, text="Selecione o genero:")
txt_genero.grid(column = 0, row = 2)
rdioMasculino = Radiobutton(janela, text="Masculino", variable=radio_Btn, value=1)
rdioFeminino = Radiobutton(janela, text= "Feminino", variable=radio_Btn, value=0)

rdioMasculino.grid(column=0, row=4, sticky="W")
rdioFeminino.grid(column=1, row=4, sticky="W")

txt_Hemoglobin = Label(janela, text="Digite o valor da Hemoglobina")
txt_Hemoglobin.grid(column= 0, row=6)
value_Hemoglobin = Entry(janela,textvariable=box_hemoglobin)
value_Hemoglobin.grid(column=0, row =7)

txt_Mch = Label(janela, text="Digite o valor do Mch")
txt_Mch.grid(column= 0, row=8)
value_Mch = Entry(janela,textvariable=box_Mch,)
value_Mch.grid(column=0, row =9)

txt_Mchc = Label(janela, text="Digite o valor do Mchc")
txt_Mchc.grid(column= 0, row=10)
value_Mchc = Entry(janela,textvariable=box_Mchc)
value_Mchc.grid(column=0, row =11)

txt_Mcv = Label(janela, text="Digite o valor do Mcv")
txt_Mcv.grid(column= 0, row=12)
value_Mcv = Entry(janela,textvariable=box_Mcv)
value_Mcv.grid(column=0, row =13)


butao = Button(janela,text='teste',command=te)
butao.grid(column=0, row=15)

text2 = Label(janela,text='')
text2.grid(column=0,row=16)
#chamada da funcao


#labelValue = Label(janela, textvariable=)
#labelValue.grid(column = 0, row = 5)



janela.mainloop()






