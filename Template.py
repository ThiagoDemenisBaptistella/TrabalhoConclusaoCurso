from Bibliotecas import *
from Funções import *

janela = Tk()

class run(func):
    def __init__(self):
        self.janela = janela
        self.pagina_inicial()
        self.frames()
        self.botoes()
        self.janela.mainloop()
    def pagina_inicial(self):
        self.janela.title("Processos Fermentativos Contínuos")
        self.janela.state("zoomed")
        self.janela.config(bg= "white")
        self.janela.resizable(False, False)
    def frames(self):

        self.frame_PI = Frame(self.janela, bg="white")
        self.frame_PI.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame_CSR = Frame(self.frame_PI, bd=1, relief="solid")
        self.frame_CSR.place(relx=0.025, rely=0.02, relwidth=0.3, relheight=0.96)
        self.frame_CCRE = Frame(self.frame_PI, bd=1, relief="solid")
        self.frame_CCRE.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.96)
        self.frame_CCRI = Frame(self.frame_PI, bd=1, relief="solid")
        self.frame_CCRI.place(relx=0.675, rely=0.02, relwidth=0.3, relheight=0.96)

        self.frame_CSR_SI = Frame(self.janela, bg="#E8E8E8")
        self.frame_CSR_SI_1 = Frame(self.frame_CSR_SI, bd=1, relief="solid")
        self.frame_CSR_SI_1.place(relx=0.01, rely=0.05, relwidth=0.25, relheight=0.93)
        self.frame_CSR_MO = Frame(self.janela, bg="#E8E8E8")
        self.frame_CSR_MO_1 = Frame(self.frame_CSR_MO, bd=1, relief="solid")
        self.frame_CSR_MO_1.place(relx=0.01, rely=0.05, relwidth=0.25, relheight=0.93)

        self.frame_CCRE_SI = Frame(self.janela, bg="#E8E8E8")
        self.frame_CCRE_SI_1 = Frame(self.frame_CCRE_SI, bd=1, relief="solid")
        self.frame_CCRE_SI_1.place(relx=0.01, rely=0.05, relwidth=0.25, relheight=0.93)
        self.frame_CCRE_MO = Frame(self.janela, bg="#E8E8E8")
        self.frame_CCRE_MO_1 = Frame(self.frame_CCRE_MO, bd=1, relief="solid")
        self.frame_CCRE_MO_1.place(relx=0.01, rely=0.05, relwidth=0.25, relheight=0.93)

        self.frame_CCRI_SI = Frame(self.janela, bg="#E8E8E8")
        self.frame_CCRI_SI_1 = Frame(self.frame_CCRI_SI, bd=1, relief="solid")
        self.frame_CCRI_SI_1.place(relx=0.01, rely=0.05, relwidth=0.25, relheight=0.93)
        self.frame_CCRI_MO = Frame(self.janela, bg="#E8E8E8")
        self.frame_CCRI_MO_1 = Frame(self.frame_CCRI_MO, bd=1, relief="solid")
        self.frame_CCRI_MO_1.place(relx=0.01, rely=0.05, relwidth=0.25, relheight=0.93)

    def botoes(self):

        #Títulos
        self.titulo_CSR = Label(self.frame_CSR, text="Contínuo Sem Reciclo", bg="#a6a6a6", bd=1, relief="solid", font=("Arial", 14))
        self.titulo_CSR.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)
        self.titulo_CCRE = Label(self.frame_CCRE, text="Contínuo Com Reciclo Externo", bg="#a6a6a6", bd=1, relief="solid",
                                font=("Arial", 14))
        self.titulo_CCRE.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)
        self.titulo_CCRI = Label(self.frame_CCRI, text="Contínuo Com Reciclo Interno", bg="#a6a6a6", bd=1, relief="solid",
                                font=("Arial", 14))
        self.titulo_CCRI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)


        self.titulo_CSR_SI = Label(self.frame_CSR_SI, text="Simulação Contínuo Sem Reciclo", bg="#a6a6a6", bd=1, relief="solid", font=("bold"))
        self.titulo_CSR_SI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)
        self.titulo_CSR_MO = Label(self.frame_CSR_MO, text="Modelagem Cotínuo Sem Reciclo", bg="#a6a6a6", bd=1, relief="solid", font=("bold"))
        self.titulo_CSR_MO.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)

        self.titulo_CCRE_SI = Label(self.frame_CCRE_SI, text="Simulação Contínuo Com Reciclo Externo", bg="#a6a6a6", bd=1,
                                   relief="solid", font=("bold"))
        self.titulo_CCRE_SI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)
        self.titulo_CCRE_MO = Label(self.frame_CCRE_MO, text="Modelagem Cotínuo Com Reciclo Externo", bg="#a6a6a6", bd=1,
                                   relief="solid", font=("bold"))
        self.titulo_CCRE_MO.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)

        self.titulo_CCRI_SI = Label(self.frame_CCRI_SI, text="Simulação Contínuo Com Reciclo Interno", bg="#a6a6a6", bd=1,
                                   relief="solid", font=("bold"))
        self.titulo_CCRI_SI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)
        self.titulo_CCRI_MO = Label(self.frame_CCRI_MO, text="Modelagem Cotínuo Com Reciclo Interno", bg="#a6a6a6", bd=1,
                                   relief="solid", font=("bold"))
        self.titulo_CCRI_MO.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.03)


        # TEXTOS
        self.texto_CSR = Label(self.frame_CSR, text="O processo contínuo sem reciclo é carecterizado\npela entrada e saída constante de volume do pro-\ncesso, de maneira que o volume presente no reator\nnão sofre variação ao longo do tempo. Além disso,\nnão há recuperação de células no processo.",
                                  anchor=NW, justify=LEFT, font=("Arial", 14))
        self.texto_CSR.place(relx=0.01, rely=0.57, relwidth=0.97, relheight=0.16)

        self.texto_CCRE = Label(self.frame_CCRE,
                               text="Um processo contínuo com reciclo externo é cara-\ncterizado pela entrada e saída constante de volume\ndo processo, de maneira que o volume presente no\nreator não varie, com realimentação de células no\nprocesso. Essas células são concentradas em uma\nunidade de separação externa ao reator.",
                               anchor=NW, justify=LEFT, font=("Arial", 14))
        self.texto_CCRE.place(relx=0.01, rely=0.57, relwidth=0.97, relheight=0.17)

        self.texto_CCRI = Label(self.frame_CCRI,
                               text="Um processo contínuo com reciclo interno é cara-\ncterizado pela entrada e saída constante de volume\ndo processo, de maneira que o volume presente no\nreator não varie, com retenção de células no proces-\nso. Essas células são concentradas em uma unida-\nde de separação interna ao reator.",
                               anchor=NW, justify=LEFT, font=("Arial", 14))
        self.texto_CCRI.place(relx=0.01, rely=0.57, relwidth=0.97, relheight=0.17)

        # IMAGENS
        self.CSR_png = PhotoImage(file="Imagens/ContinuoSemReciclo.png")
        self.imagem_CSR = Label(self.frame_CSR, image=self.CSR_png, bd=1, relief="solid")
        self.imagem_CSR.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.5)
        self.CCRE_png = PhotoImage(file="Imagens/ContinuoComRecicloExterno.png")
        self.imagem_CCRE = Label(self.frame_CCRE, image=self.CCRE_png, bd=1, relief="solid")
        self.imagem_CCRE.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.5)
        self.CCRI_png = PhotoImage(file="Imagens/ContinuoComRecicloInterno.png")
        self.imagem_CCRI = Label(self.frame_CCRI, image=self.CCRI_png, bd=1, relief="solid")
        self.imagem_CCRI.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.5)

        self.imagem_CSR_SI = Label(self.frame_CSR_SI_1, image=self.CSR_png, bd=1, relief="solid")
        self.imagem_CSR_SI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)
        self.imagem_CCRE_SI = Label(self.frame_CCRE_SI_1, image=self.CCRE_png, bd=1, relief="solid")
        self.imagem_CCRE_SI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)
        self.imagem_CCRI_SI = Label(self.frame_CCRI_SI_1, image=self.CCRI_png, bd=1, relief="solid")
        self.imagem_CCRI_SI.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)

        self.imagem_CSR_MO = Label(self.frame_CSR_MO_1, image=self.CSR_png, bd=1, relief="solid")
        self.imagem_CSR_MO.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)
        self.imagem_CCRE_MO = Label(self.frame_CCRE_MO_1, image=self.CCRE_png, bd=1, relief="solid")
        self.imagem_CCRE_MO.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)
        self.imagem_CCRI_MO = Label(self.frame_CCRI_MO_1, image=self.CCRI_png, bd=1, relief="solid")
        self.imagem_CCRI_MO.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)

        # BOTÕES INICIAIS
        self.botao_CSR_SI = Button(self.frame_CSR, text="Simulação", font=("Arial", 16), bg="#a6a6a6", command=lambda: self.tela_CSR_SI())
        self.botao_CSR_SI.place(relx=0.01, rely=0.75, relwidth=0.98, relheight=0.11)
        self.botao_CSR_MO = Button(self.frame_CSR, text="Modelagem", font=("Arial", 16), bg="#a6a6a6",
                                   command=lambda: self.tela_CSR_MO ())
        self.botao_CSR_MO.place(relx=0.01, rely=0.88, relwidth=0.98, relheight=0.11)
        self.botao_CCRE_SI = Button(self.frame_CCRE, text="Simulação", font=("Arial", 16), bg="#a6a6a6",
                                   command=lambda: self.tela_CCRE_SI())
        self.botao_CCRE_SI.place(relx=0.01, rely=0.75, relwidth=0.98, relheight=0.11)
        self.botao_CCRE_MO = Button(self.frame_CCRE, text="Modelagem", font=("Arial", 16), bg="#a6a6a6",
                                   command=lambda: self.tela_CCRE_MO())
        self.botao_CCRE_MO.place(relx=0.01, rely=0.88, relwidth=0.98, relheight=0.11)
        self.botao_CCRI_SI = Button(self.frame_CCRI, text="Simulação", font=("Arial", 16), bg="#a6a6a6",
                                    command=lambda: self.tela_CCRI_SI())
        self.botao_CCRI_SI.place(relx=0.01, rely=0.75, relwidth=0.98, relheight=0.11)
        self.botao_CCRI_MO = Button(self.frame_CCRI, text="Modelagem", font=("Arial", 16), bg="#a6a6a6",
                                    command=lambda: self.tela_CCRI_MO())
        self.botao_CCRI_MO.place(relx=0.01, rely=0.88, relwidth=0.98, relheight=0.11)


        # PARÂMETROS DE ENTRADA
        self.mimax_texto_CSR = Label(self.frame_CSR_SI_1, text="Velocidade específica máxima de crescimento (1/h):", anchor=E)
        self.mimax_valor_CSR = Entry(self.frame_CSR_SI_1)
        self.mimax_texto_CSR.place(relx=0.02, rely=0.52, relwidth=0.74, relheight=0.03)
        self.mimax_valor_CSR.place(relx=0.77, rely=0.52, relwidth=0.21, relheight=0.03)
        self.ks_texto_CSR = Label(self.frame_CSR_SI_1, text="Constante de Saturação (kg/m³):", anchor=E)
        self.ks_valor_CSR = Entry(self.frame_CSR_SI_1)
        self.ks_texto_CSR.place(relx=0.02, rely=0.555, relwidth=0.74, relheight=0.03)
        self.ks_valor_CSR.place(relx=0.77, rely=0.555, relwidth=0.21, relheight=0.03)
        self.Y_texto_CSR = Label(self.frame_CSR_SI_1, text="Rendimento de substrato em células (kg/kg):", anchor=E)
        self.Y_valor_CSR = Entry(self.frame_CSR_SI_1)
        self.Y_texto_CSR.place(relx=0.02, rely=0.59, relwidth=0.74, relheight=0.03)
        self.Y_valor_CSR.place(relx=0.77, rely=0.59, relwidth=0.21, relheight=0.03)
        self.alfa_texto_CSR = Label(self.frame_CSR_SI_1, text="Coeficiente de formação de produto associado\n ao crescimento (kg/kg):", anchor=E, justify=RIGHT)
        self.alfa_valor_CSR = Entry(self.frame_CSR_SI_1)
        self.alfa_texto_CSR.place(relx=0.02, rely=0.625, relwidth=0.74, relheight=0.06)
        self.alfa_valor_CSR.place(relx=0.77, rely=0.625, relwidth=0.21, relheight=0.06)
        self.Se_texto_CSR = Label(self.frame_CSR_SI_1, text="Concentração de substrato na vazão\nde alimentação (kg/m³):", anchor=E, justify=RIGHT)
        self.Se_valor_CSR = Entry(self.frame_CSR_SI_1)
        self.Se_texto_CSR.place(relx=0.02, rely=0.69, relwidth=0.74, relheight=0.06)
        self.Se_valor_CSR.place(relx=0.77, rely=0.69, relwidth=0.21, relheight=0.06)

        self.mimax_texto_CCRE = Label(self.frame_CCRE_SI_1, text="Velocidade específica máxima de crescimento (1/h):",
                                 anchor=E)
        self.mimax_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.mimax_texto_CCRE.place(relx=0.02, rely=0.52, relwidth=0.74, relheight=0.03)
        self.mimax_valor_CCRE.place(relx=0.77, rely=0.52, relwidth=0.21, relheight=0.03)
        self.ks_texto_CCRE = Label(self.frame_CCRE_SI_1, text="Constante de Saturação (kg/m³):", anchor=E)
        self.ks_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.ks_texto_CCRE.place(relx=0.02, rely=0.555, relwidth=0.74, relheight=0.03)
        self.ks_valor_CCRE.place(relx=0.77, rely=0.555, relwidth=0.21, relheight=0.03)
        self.Y_texto_CCRE = Label(self.frame_CCRE_SI_1, text="Rendimento de substrato em células (kg/kg):", anchor=E)
        self.Y_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.Y_texto_CCRE.place(relx=0.02, rely=0.59, relwidth=0.74, relheight=0.03)
        self.Y_valor_CCRE.place(relx=0.77, rely=0.59, relwidth=0.21, relheight=0.03)
        self.alfa_texto_CCRE = Label(self.frame_CCRE_SI_1,
                                text="Coeficiente de formação de produto associado\n ao crescimento (kg/kg):", anchor=E,
                                justify=RIGHT)
        self.alfa_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.alfa_texto_CCRE.place(relx=0.02, rely=0.625, relwidth=0.74, relheight=0.06)
        self.alfa_valor_CCRE.place(relx=0.77, rely=0.625, relwidth=0.21, relheight=0.06)
        self.Se_texto_CCRE = Label(self.frame_CCRE_SI_1, text="Concentração de substrato na vazão\nde alimentação (kg/m³):",
                              anchor=E, justify=RIGHT)
        self.Se_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.Se_texto_CCRE.place(relx=0.02, rely=0.69, relwidth=0.74, relheight=0.06)
        self.Se_valor_CCRE.place(relx=0.77, rely=0.69, relwidth=0.21, relheight=0.06)
        self.r_texto_CCRE = Label(self.frame_CCRE_SI_1, text="Razão de reciclo:", anchor=E)
        self.r_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.c_texto_CCRE = Label(self.frame_CCRE_SI_1, text="Fator de concentração celular:", anchor=E)
        self.c_valor_CCRE = Entry(self.frame_CCRE_SI_1)
        self.r_texto_CCRE.place(relx=0.02, rely=0.755, relwidth=0.74, relheight=0.03)
        self.r_valor_CCRE.place(relx=0.77, rely=0.755, relwidth=0.21, relheight=0.03)
        self.c_texto_CCRE.place(relx=0.02, rely=0.79, relwidth=0.74, relheight=0.03)
        self.c_valor_CCRE.place(relx=0.77, rely=0.79, relwidth=0.21, relheight=0.03)

        self.mimax_texto_CCRI = Label(self.frame_CCRI_SI_1, text="Velocidade específica máxima de crescimento (1/h):",
                                      anchor=E)
        self.mimax_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.mimax_texto_CCRI.place(relx=0.02, rely=0.52, relwidth=0.74, relheight=0.03)
        self.mimax_valor_CCRI.place(relx=0.77, rely=0.52, relwidth=0.21, relheight=0.03)
        self.ks_texto_CCRI = Label(self.frame_CCRI_SI_1, text="Constante de Saturação (kg/m³):", anchor=E)
        self.ks_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.ks_texto_CCRI.place(relx=0.02, rely=0.555, relwidth=0.74, relheight=0.03)
        self.ks_valor_CCRI.place(relx=0.77, rely=0.555, relwidth=0.21, relheight=0.03)
        self.Y_texto_CCRI = Label(self.frame_CCRI_SI_1, text="Rendimento de substrato em células (kg/kg):", anchor=E)
        self.Y_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.Y_texto_CCRI.place(relx=0.02, rely=0.59, relwidth=0.74, relheight=0.03)
        self.Y_valor_CCRI.place(relx=0.77, rely=0.59, relwidth=0.21, relheight=0.03)
        self.alfa_texto_CCRI = Label(self.frame_CCRI_SI_1,
                                     text="Coeficiente de formação de produto associado\n ao crescimento (kg/kg):",
                                     anchor=E,
                                     justify=RIGHT)
        self.alfa_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.alfa_texto_CCRI.place(relx=0.02, rely=0.625, relwidth=0.74, relheight=0.06)
        self.alfa_valor_CCRI.place(relx=0.77, rely=0.625, relwidth=0.21, relheight=0.06)
        self.Se_texto_CCRI = Label(self.frame_CCRI_SI_1,
                                   text="Concentração de substrato na vazão\nde alimentação (kg/m³):",
                                   anchor=E, justify=RIGHT)
        self.Se_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.Se_texto_CCRI.place(relx=0.02, rely=0.69, relwidth=0.74, relheight=0.06)
        self.Se_valor_CCRI.place(relx=0.77, rely=0.69, relwidth=0.21, relheight=0.06)
        self.H_texto_CCRI = Label(self.frame_CCRI_SI_1, text="Retenção celular na unidade de separação:", anchor=E)
        self.H_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.f_texto_CCRI = Label(self.frame_CCRI_SI_1, text="Razão entre F1 e Fe:", anchor=E)
        self.f_valor_CCRI = Entry(self.frame_CCRI_SI_1)
        self.H_texto_CCRI.place(relx=0.02, rely=0.755, relwidth=0.74, relheight=0.03)
        self.H_valor_CCRI.place(relx=0.77, rely=0.755, relwidth=0.21, relheight=0.03)
        self.f_texto_CCRI.place(relx=0.02, rely=0.79, relwidth=0.74, relheight=0.03)
        self.f_valor_CCRI.place(relx=0.77, rely=0.79, relwidth=0.21, relheight=0.03)

        self.Se_texto_CSR_MO = Label(self.frame_CSR_MO_1,
                                   text="Concentração de substrato na vazão\nde alimentação (kg/m³):",
                                   anchor=E, justify=RIGHT)
        self.Se_valor_CSR_MO = Entry(self.frame_CSR_MO_1)
        self.Se_texto_CSR_MO.place(relx=0.02, rely=0.52, relwidth=0.74, relheight=0.06)
        self.Se_valor_CSR_MO.place(relx=0.77, rely=0.52, relwidth=0.21, relheight=0.06)

        self.Se_texto_CCRE_MO = Label(self.frame_CCRE_MO_1,
                                   text="Concentração de substrato na vazão\nde alimentação (kg/m³):",
                                   anchor=E, justify=RIGHT)
        self.Se_valor_CCRE_MO = Entry(self.frame_CCRE_MO_1)
        self.Se_texto_CCRE_MO.place(relx=0.02, rely=0.52, relwidth=0.74, relheight=0.06)
        self.Se_valor_CCRE_MO.place(relx=0.77, rely=0.52, relwidth=0.21, relheight=0.06)
        self.r_texto_CCRE_MO = Label(self.frame_CCRE_MO_1, text="Razão de reciclo:", anchor=E)
        self.r_valor_CCRE_MO = Entry(self.frame_CCRE_MO_1)
        self.c_texto_CCRE_MO = Label(self.frame_CCRE_MO_1, text="Fator de concentração celular:", anchor=E)
        self.c_valor_CCRE_MO = Entry(self.frame_CCRE_MO_1)
        self.r_texto_CCRE_MO.place(relx=0.02, rely=0.585, relwidth=0.74, relheight=0.03)
        self.r_valor_CCRE_MO.place(relx=0.77, rely=0.585, relwidth=0.21, relheight=0.03)
        self.c_texto_CCRE_MO.place(relx=0.02, rely=0.62, relwidth=0.74, relheight=0.03)
        self.c_valor_CCRE_MO.place(relx=0.77, rely=0.62, relwidth=0.21, relheight=0.03)

        self.Se_texto_CCRI_MO = Label(self.frame_CCRI_MO_1,
                                      text="Concentração de substrato na vazão\nde alimentação (kg/m³):",
                                      anchor=E, justify=RIGHT)
        self.Se_valor_CCRI_MO = Entry(self.frame_CCRI_MO_1)
        self.Se_texto_CCRI_MO.place(relx=0.02, rely=0.52, relwidth=0.74, relheight=0.06)
        self.Se_valor_CCRI_MO.place(relx=0.77, rely=0.52, relwidth=0.21, relheight=0.06)
        self.H_texto_CCRI_MO = Label(self.frame_CCRI_MO_1, text="Retenção celular na unidade de separação:", anchor=E)
        self.H_valor_CCRI_MO = Entry(self.frame_CCRI_MO_1)
        self.f_texto_CCRI_MO = Label(self.frame_CCRI_MO_1, text="Razão entre F1 e Fe:", anchor=E)
        self.f_valor_CCRI_MO = Entry(self.frame_CCRI_MO_1)
        self.H_texto_CCRI_MO.place(relx=0.02, rely=0.585, relwidth=0.74, relheight=0.03)
        self.H_valor_CCRI_MO.place(relx=0.77, rely=0.585, relwidth=0.21, relheight=0.03)
        self.f_texto_CCRI_MO.place(relx=0.02, rely=0.62, relwidth=0.74, relheight=0.03)
        self.f_valor_CCRI_MO.place(relx=0.77, rely=0.62, relwidth=0.21, relheight=0.03)
    


        # BOTÕES SECUNDÁRIOS

        self.botao_simular_CSR = Button(self.frame_CSR_SI_1, text="Simular", command=lambda: self.simular_CSR(), bg="#a6a6a6")
        self.botao_simular_CSR.place(relx=0.01, rely=0.79, relwidth=0.98, relheight=0.06)
        self.botao_baixar_planilha= Button(self.frame_CSR_SI_1, text="Baixar Dados", command=lambda:self.baixar_planilha(), bg="#a6a6a6")
        self.botao_baixar_planilha.place(relx=0.01, rely=0.86, relwidth=0.98, relheight=0.06)
        self.botao_voltar = Button(self.frame_CSR_SI_1, text="Voltar", command=lambda:self.tela_voltar(), bg="#a6a6a6")
        self.botao_voltar.place(relx=0.01, rely=0.93, relwidth=0.98, relheight=0.06)


        self.botao_simular_CCRE = Button(self.frame_CCRE_SI_1, text="Simular", command=lambda: self.simular_CCRE(),
                                        bg="#a6a6a6")
        self.botao_simular_CCRE.place(relx=0.01, rely=0.83, relwidth=0.98, relheight=0.046)
        self.botao_baixar_planilha= Button(self.frame_CCRE_SI_1, text="Baixar Dados",
                                                command=lambda: self.baixar_planilha(), bg="#a6a6a6")
        self.botao_baixar_planilha.place(relx=0.01, rely=0.886, relwidth=0.98, relheight=0.046)
        self.botao_voltar = Button(self.frame_CCRE_SI_1, text="Voltar", command=lambda: self.tela_voltar(),
                                       bg="#a6a6a6")
        self.botao_voltar.place(relx=0.01, rely=0.942, relwidth=0.98, relheight=0.046)


        self.botao_simular_CCRI = Button(self.frame_CCRI_SI_1, text="Simular", command=lambda: self.simular_CCRI(),
                                         bg="#a6a6a6")
        self.botao_simular_CCRI.place(relx=0.01, rely=0.83, relwidth=0.98, relheight=0.046)
        self.botao_baixar_planilha = Button(self.frame_CCRI_SI_1, text="Baixar Dados",
                                                 command=lambda: self.baixar_planilha(), bg="#a6a6a6")
        self.botao_baixar_planilha.place(relx=0.01, rely=0.886, relwidth=0.98, relheight=0.046)
        self.botao_voltar = Button(self.frame_CCRI_SI_1, text="Voltar", command=lambda: self.tela_voltar(),
                                   bg="#a6a6a6")
        self.botao_voltar.place(relx=0.01, rely=0.942, relwidth=0.98, relheight=0.046)

        self.botao_modelar_CSR = Button(self.frame_CSR_MO_1, text="Modelar", command=lambda: self.modelar_CSR(), bg="#a6a6a6")
        self.botao_modelar_CSR.place(relx=0.01, rely=0.79, relwidth=0.98, relheight=0.06)
        self.botao_baixar_modelo = Button(self.frame_CSR_MO_1, text="Baixar Planilha Modelo", command=lambda: self.baixar_planilha_modelo_continuo(), bg="#a6a6a6")
        self.botao_baixar_modelo.place(relx=0.01, rely=0.86, relwidth=0.98, relheight=0.06)
        self.botao_voltar = Button(self.frame_CSR_MO_1, text="Voltar", command=lambda: self.tela_voltar(), bg="#a6a6a6")
        self.botao_voltar.place(relx=0.01, rely=0.93, relwidth=0.98, relheight=0.06)

        self.botao_modelar_CCRE = Button(self.frame_CCRE_MO_1, text="Modelar", command=lambda: self.modelar_CCRE(),
                                        bg="#a6a6a6")
        self.botao_modelar_CCRE.place(relx=0.01, rely=0.79, relwidth=0.98, relheight=0.06)
        self.botao_baixar_modelo = Button(self.frame_CCRE_MO_1, text="Baixar Planilha Modelo",
                                          command=lambda: self.baixar_planilha_modelo_continuo(), bg="#a6a6a6")
        self.botao_baixar_modelo.place(relx=0.01, rely=0.86, relwidth=0.98, relheight=0.06)
        self.botao_voltar = Button(self.frame_CCRE_MO_1, text="Voltar", command=lambda: self.tela_voltar(),
                                   bg="#a6a6a6")
        self.botao_voltar.place(relx=0.01, rely=0.93, relwidth=0.98, relheight=0.06)

        self.botao_modelar_CCRI = Button(self.frame_CCRI_MO_1, text="Modelar", command=lambda: self.modelar_CCRI(),
                                         bg="#a6a6a6")
        self.botao_modelar_CCRI.place(relx=0.01, rely=0.79, relwidth=0.98, relheight=0.06)
        self.botao_baixar_modelo = Button(self.frame_CCRI_MO_1, text="Baixar Planilha Modelo",
                                          command=lambda: self.baixar_planilha_modelo_continuo(), bg="#a6a6a6")
        self.botao_baixar_modelo.place(relx=0.01, rely=0.86, relwidth=0.98, relheight=0.06)
        self.botao_voltar = Button(self.frame_CCRI_MO_1, text="Voltar", command=lambda: self.tela_voltar(),
                                   bg="#a6a6a6")
        self.botao_voltar.place(relx=0.01, rely=0.93, relwidth=0.98, relheight=0.06)



run()