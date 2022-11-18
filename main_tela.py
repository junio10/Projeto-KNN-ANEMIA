from tkinter import *
import knn as k


def te():
    
    if k.Treinar(radio_Btn_gender.get(),box_hemoglobin.get(),box_Mch.get(),box_Mchc.get(),box_Mcv.get(),radio_Algoritmo.get()) == 1:
        tex = 'anemico'
    else:
        tex = 'não tem anemia'
    
    texto = f'''
    {tex}
    '''
    text2['text'] = texto
    
    
    
    


janela = Tk()
radio_Btn_gender = IntVar()
box_hemoglobin = DoubleVar()
box_Mch = DoubleVar()
box_Mchc = DoubleVar()
box_Mcv = DoubleVar()
radio_Algoritmo = IntVar()





janela.title("Diagnóstico de anemia")
janela.geometry('520x300')

txt_titulo = Label(janela, text="Diagnóstico de anemia")
txt_titulo.grid(column=0, row=0, columnspan=5, pady=17)

rdioMasculino = Radiobutton(janela, text="Masculino", variable=radio_Btn_gender, value=1)
rdioFeminino = Radiobutton(janela, text= "Feminino", variable=radio_Btn_gender, value=0)

rdioMasculino.grid(column=0, row=2,columnspan=3, pady=15)
rdioFeminino.grid(column=1, row=2,columnspan=5)

txt_Hemoglobin = Label(janela, text="Hemoglobina")
txt_Hemoglobin.grid(column= 0, row=4,columnspan=5, sticky="w")
value_Hemoglobin = Entry(janela,textvariable=box_hemoglobin)
value_Hemoglobin.grid(column=0, row =5,padx=3)

txt_Mch = Label(janela, text="MCH")
txt_Mch.grid(column= 1, row=4, columnspan=5, sticky="w")
value_Mch = Entry(janela,textvariable=box_Mch,)
value_Mch.grid(column=1, row =5,padx=3)

txt_Mchc = Label(janela, text="MCHC")
txt_Mchc.grid(column= 2, row=4,columnspan=5, sticky="w")
value_Mchc = Entry(janela,textvariable=box_Mchc)
value_Mchc.grid(column=2, row =5,padx=3)

txt_Mcv = Label(janela, text="MCV")
txt_Mcv.grid(column= 3, row=4,columnspan=5, sticky="w")
value_Mcv = Entry(janela,textvariable=box_Mcv)
value_Mcv.grid(column=3, row =5,padx=3)

rdio_Knn = Radiobutton(janela, text="KNN", variable=radio_Algoritmo, value=1)
rdio_Preceptron = Radiobutton(janela, text= "Preceptron", variable=radio_Algoritmo, value=0)

rdio_Knn.grid(column = 1, row = 6, pady=15)
rdio_Preceptron.grid(column = 2, row = 6)

butao = Button(janela,text='teste',command=te)
butao.grid(column=0, row=7,columnspan=5,)

text2 = Label(janela,text='')
text2.grid(column=0,row=6)
#chamada da funcao


#labelValue = Label(janela, textvariable=)
#labelValue.grid(column = 0, row = 5)



janela.mainloop()






