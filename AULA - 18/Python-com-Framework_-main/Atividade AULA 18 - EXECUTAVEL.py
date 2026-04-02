import tkinter as tk

print('HOSPITAL GERAL')


def mostrar():
    dado =  input_1.get()
    print(dado, input_2.get(), input_3.get(), input_4.get())
    texto1.config(text=dado)
    texto2.config(text=input_2.get())
    texto3.config(text=input_3.get())
    texto4.config(text=input_4.get())       


janela  =  tk.Tk()
janela.geometry('1500x1500')
janela.configure(bg = 'white')
# janela.iconbitmap('hospital.ico')

# tk.Label(janela, text = 'ISSO É UM TESTE...').pack()
texto1 = tk.Label(janela, text = 'DIGITE SEU NOME :', font=('arial', 20), bg = 'white')
texto1.pack()
texto2 = tk.Label(janela, text = 'DIGITE SUA IDADE :', font=('arial', 20), bg = 'white')
texto2.pack()
texto3 = tk.Label(janela, text = 'DIGITE SEU ENDEREÇO :', font=('arial',20), bg = 'white')
texto3.pack()
texto4 = tk.Label(janela, text = 'DIGITE SEU EMAIL :', font=('arial', 20), bg = 'white')
texto4.pack()

input_1  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
input_1.pack()

input_2  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
input_2.pack()

input_3  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
input_3.pack()

input_4  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
input_4.pack()

btn  =  tk.Button(janela, text= 'MOSTRAR', font=('arial', 15), bg = '#e5e5e5', command=mostrar)
btn.pack(pady=65)

texto1 = tk.Label(janela, text = 'SEU NOME', font=('arial', 20), bg = 'white')
texto1.pack(pady=10)
texto2 = tk.Label(janela, text = 'SUA IDADE', font=('arial', 20), bg = 'white')
texto2.pack(pady=10)
texto3 = tk.Label(janela, text = 'SEU ENDEREÇO', font=('arial', 20), bg = 'white')
texto3.pack(pady=10)
texto4 = tk.Label(janela, text = 'SEU EMAIL', font=('arial', 20), bg = 'white')
texto4.pack(pady=10)    


janela.mainloop()