import pandas as pd

class func():
    def esquecer_telas(self):
        self.frame_PI.place_forget()
        self.frame_CSR_SI.place_forget()
        self.frame_CSR_MO.place_forget()
        self.frame_CCRE_SI.place_forget()
        self.frame_CCRE_MO.place_forget()
        self.frame_CCRI_SI.place_forget()
        self.frame_CCRI_MO.place_forget()
    def tela_CSR_SI(self):
        self.esquecer_telas()
        self.frame_CSR_SI.place(relx=0, rely=0, relwidth=1, relheight=1)
    def tela_CSR_MO(self):
        self.esquecer_telas()
        self.frame_CSR_MO.place(relx=0, rely=0, relwidth=1, relheight=1)
    def tela_CCRE_SI(self):
        self.esquecer_telas()
        self.frame_CCRE_SI.place(relx=0, rely=0, relwidth=1, relheight=1)
    def tela_CCRE_MO(self):
        self.esquecer_telas()
        self.frame_CCRE_MO.place(relx=0, rely=0, relwidth=1, relheight=1)
    def tela_CCRI_SI(self):
        self.esquecer_telas()
        self.frame_CCRI_SI.place(relx=0, rely=0, relwidth=1, relheight=1)
    def tela_CCRI_MO(self):
        self.esquecer_telas()
        self.frame_CCRI_MO.place(relx=0, rely=0, relwidth=1, relheight=1)
    def tela_voltar(self):
        self.esquecer_telas()
        self.frame_PI.place(relx=0, rely=0, relwidth=1, relheight=1)
    def simular_CSR(self):
        import numpy as np
        from tkinter import Label
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        self.mimax = float(self.mimax_valor_CSR.get())
        self.ks = float(self.ks_valor_CSR.get())
        self.Y = float(self.Y_valor_CSR.get())
        self.a = float(self.alfa_valor_CSR.get())
        self.Se = float(self.Se_valor_CSR.get())
        self.h = float(0.001)
        self.Dc = self.Se * self.mimax / (self.ks + self.Se)
        self.Do = self.mimax * (1 - np.sqrt(self.ks / (self.Se + self.ks)))
        self.D = np.arange(0, self.Dc + self.h, self.h)
        self.S = self.ks * self.D / (self.mimax - self.D)
        self.X = (self.Se - self.S) * self.Y
        self.P = self.a * self.X
        self.mi = self.mimax*self.S/(self.ks+self.S)
        self.PR = self.X*self.D
        self.fig1, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.S, label="Substrato", color="red", linewidth=2, linestyle="-")
        self.ax1.plot(self.D, self.X, label="Células", color="blue", linewidth=2, linestyle="-")
        self.ax1.plot(self.D, self.P, label="Produto", color="green", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Concentração (kg/m³)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.ax1.legend(fontsize=15, edgecolor="black")
        self.grafico1 = FigureCanvasTkAgg(self.fig1, self.frame_CSR_SI)
        self.grafico1.get_tk_widget().place(relx=0.27, rely=0.05, relwidth=0.72, relheight=0.47)
        self.fig2, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.mi, color="black", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Velocidade espefífica de crescimento (1/h)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.grafico2 = FigureCanvasTkAgg(self.fig2, self.frame_CSR_SI)
        self.grafico2.get_tk_widget().place(relx=0.27, rely=0.57, relwidth=0.35, relheight=0.42)
        self.fig3, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.PR, color="black", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Produtividade (kg/(m³.h)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.grafico3 = FigureCanvasTkAgg(self.fig3, self.frame_CSR_SI)
        self.grafico3.get_tk_widget().place(relx=0.64, rely=0.57, relwidth=0.35, relheight=0.42)
        self.Dc_texto_CSR = Label(self.frame_CSR_SI, text="Taxa de diluição crítica:")
        self.Dc_texto_CSR.place(relx=0.50, rely=0.53, relwidth=0.08, relheight=0.03)
        self.Dc_str_CSR = str(round(self.Dc, 4))
        self.Dc_valor_CSR = Label(self.frame_CSR_SI, text=self.Dc_str_CSR)
        self.Dc_valor_CSR.place(relx=0.58, rely=0.53, relwidth=0.04, relheight=0.03)
        self.Do_texto_CSR = Label(self.frame_CSR_SI, text="Taxa de diluição ótima:")
        self.Do_texto_CSR.place(relx=0.64, rely=0.53, relwidth=0.08, relheight=0.03)
        self.Do_str_CSR = str(round(self.Do, 4))
        self.Do_valor_CSR = Label(self.frame_CSR_SI, text=self.Do_str_CSR)
        self.Do_valor_CSR.place(relx=0.72, rely=0.53, relwidth=0.04, relheight=0.03)
    def simular_CCRE(self):
        import numpy as np
        from tkinter import Label
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        self.mimax = float(self.mimax_valor_CCRE.get())
        self.ks = float(self.ks_valor_CCRE.get())
        self.Y = float(self.Y_valor_CCRE.get())
        self.a = float(self.alfa_valor_CCRE.get())
        self.Se = float(self.Se_valor_CCRE.get())
        self.r = float(self.r_valor_CCRE.get())
        self.c = float(self.c_valor_CCRE.get())
        self.h = float(0.001)
        self.Dc = self.Se * self.mimax / ((self.ks + self.Se) * (1 + self.r * (1 - self.c)))
        self.Do = self.mimax * (1 - np.sqrt(self.ks / (self.Se + self.ks))) / (1 + self.r * (1 - self.c))
        self.D = np.arange(0, self.Dc + self.h, self.h)
        self.S = (self.ks * self.D * (1 + self.r * (1 - self.c))) / (self.mimax - self.D * (1 + self.r * (1 - self.c)))
        self.X = (self.Se - self.S) * self.Y / (1 + self.r * (1 - self.c))
        self.P = self.a * self.Y * (self.Se - self.S)
        self.mi = self.mimax * self.S / (self.ks + self.S)
        self.PR = self.X * self.D
        self.fig1, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.S, label="Substrato", color="red", linewidth=2, linestyle="-")
        self.ax1.plot(self.D, self.X, label="Células", color="blue", linewidth=2, linestyle="-")
        self.ax1.plot(self.D, self.P, label="Produto", color="green", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Concentração (kg/m³)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.ax1.legend(fontsize=15, edgecolor="black")
        self.grafico1 = FigureCanvasTkAgg(self.fig1, self.frame_CCRE_SI)
        self.grafico1.get_tk_widget().place(relx=0.27, rely=0.05, relwidth=0.72, relheight=0.47)
        self.fig2, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.mi, color="black", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Velocidade espefífica de crescimento (1/h)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.grafico2 = FigureCanvasTkAgg(self.fig2, self.frame_CCRE_SI)
        self.grafico2.get_tk_widget().place(relx=0.27, rely=0.57, relwidth=0.35, relheight=0.42)
        self.fig3, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.PR, color="black", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Produtividade (kg/(m³.h)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.grafico3 = FigureCanvasTkAgg(self.fig3, self.frame_CCRE_SI)
        self.grafico3.get_tk_widget().place(relx=0.64, rely=0.57, relwidth=0.35, relheight=0.42)
        self.Dc_texto_CCRE = Label(self.frame_CCRE_SI, text="Taxa de diluição crítica:")
        self.Dc_texto_CCRE.place(relx=0.50, rely=0.53, relwidth=0.08, relheight=0.03)
        self.Dc_str_CCRE = str(round(self.Dc, 4))
        self.Dc_valor_CCRE = Label(self.frame_CCRE_SI, text=self.Dc_str_CCRE)
        self.Dc_valor_CCRE.place(relx=0.58, rely=0.53, relwidth=0.04, relheight=0.03)
        self.Do_texto_CCRE = Label(self.frame_CCRE_SI, text="Taxa de diluição ótima:")
        self.Do_texto_CCRE.place(relx=0.64, rely=0.53, relwidth=0.08, relheight=0.03)
        self.Do_str_CCRE = str(round(self.Do, 4))
        self.Do_valor_CCRE = Label(self.frame_CCRE_SI, text=self.Do_str_CCRE)
        self.Do_valor_CCRE.place(relx=0.72, rely=0.53, relwidth=0.04, relheight=0.03)
    def simular_CCRI(self):
        import numpy as np
        from tkinter import Label
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        self.mimax = float(self.mimax_valor_CCRI.get())
        self.ks = float(self.ks_valor_CCRI.get())
        self.Y = float(self.Y_valor_CCRI.get())
        self.a = float(self.alfa_valor_CCRI.get())
        self.Se = float(self.Se_valor_CCRI.get())
        self.H = float(self.H_valor_CCRI.get())
        self.f = float(self.f_valor_CCRI.get())
        self.h = float(0.001)
        self.Dc = self.Se * self.mimax / ((self.ks + self.Se) * (self.H * (1 - self.f) + self.f))
        self.Do = self.mimax * (1 - np.sqrt(self.ks / (self.Se + self.ks))) / (self.H * (1 - self.f) + self.f)
        self.D = np.arange(0, self.Dc + self.h, self.h)
        self.S = (self.ks * self.D * (self.H * (1 - self.f) + self.f)) / (
                    self.mimax - self.D * (self.H * (1 - self.f) + self.f))
        self.X = (self.Se - self.S) * self.Y / (self.H * (1 - self.f) + self.f)
        self.P = self.a * self.Y * (self.Se - self.S)
        self.mi = self.mimax * self.S / (self.ks + self.S)
        self.PR = self.X * self.D
        self.fig1, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.S, label="Substrato", color="red", linewidth=2, linestyle="-")
        self.ax1.plot(self.D, self.X, label="Células", color="blue", linewidth=2, linestyle="-")
        self.ax1.plot(self.D, self.P, label="Produto", color="green", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Concentração (kg/m³)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.ax1.legend(fontsize=15, edgecolor="black")
        self.grafico1 = FigureCanvasTkAgg(self.fig1, self.frame_CCRI_SI)
        self.grafico1.get_tk_widget().place(relx=0.27, rely=0.05, relwidth=0.72, relheight=0.47)
        self.fig2, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.mi, color="black", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Velocidade espefífica de crescimento (1/h)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.grafico2 = FigureCanvasTkAgg(self.fig2, self.frame_CCRI_SI)
        self.grafico2.get_tk_widget().place(relx=0.27, rely=0.57, relwidth=0.35, relheight=0.42)
        self.fig3, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.plot(self.D, self.PR, color="black", linewidth=2, linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Produtividade (kg/(m³.h)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.grafico3 = FigureCanvasTkAgg(self.fig3, self.frame_CCRI_SI)
        self.grafico3.get_tk_widget().place(relx=0.64, rely=0.57, relwidth=0.35, relheight=0.42)
        self.Dc_texto_CCRI = Label(self.frame_CCRI_SI, text="Taxa de diluição crítica:")
        self.Dc_texto_CCRI.place(relx=0.50, rely=0.53, relwidth=0.08, relheight=0.03)
        self.Dc_str_CCRI = str(round(self.Dc, 4))
        self.Dc_valor_CCRI = Label(self.frame_CCRI_SI, text=self.Dc_str_CCRI)
        self.Dc_valor_CCRI.place(relx=0.58, rely=0.53, relwidth=0.04, relheight=0.03)
        self.Do_texto_CCRI = Label(self.frame_CCRI_SI, text="Taxa de diluição ótima:")
        self.Do_texto_CCRI.place(relx=0.64, rely=0.53, relwidth=0.08, relheight=0.03)
        self.Do_str_CCRI = str(round(self.Do, 4))
        self.Do_valor_CCRI = Label(self.frame_CCRI_SI, text=self.Do_str_CCRI)
        self.Do_valor_CCRI.place(relx=0.72, rely=0.53, relwidth=0.04, relheight=0.03)
    def baixar_planilha(self):
        from tkinter import filedialog
        self.dados = pd.DataFrame(
            {"Taxa de Diluição (1/h)": self.D, "Substrato (kg/m³)": self.S, "Células (kg/m³)": self.X,
             "Produto (kg/m³)": self.P, "Velocidade específica de crescimento (1/h)": self.mi, "Produtividade (kg/(m³.h))": self.PR})
        self.dados.to_excel(filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")]), index=False)
    def baixar_planilha_modelo_continuo(self):
        from tkinter import filedialog
        self.modelo_continuo = pd.DataFrame({"Taxa de Diluição (1/h)": [], "Substrato (kg/m³)": [], "Células (kg/m³)": [], "Produto (kg/m³)": []})
        self.modelo_continuo.to_excel(filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")], initialfile="Planilha Modelo"), index=False)
    def modelar_CSR(self):
        import pandas as pd
        import numpy as np
        from scipy.optimize import differential_evolution
        import matplotlib.pyplot as plt
        from tkinter import filedialog
        from tkinter import Label
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        self.planilha_MO = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        self.dados = pd.read_excel("Planilha Modelo.xlsx")
        self.DE = np.asarray(self.dados["Taxa de Diluição (1/h)"])
        self.XE = np.asarray(self.dados["Células (kg/m³)"])
        self.SE = np.asarray(self.dados["Substrato (kg/m³)"])
        self.PE = np.asarray(self.dados["Produto (kg/m³)"])
        self.Se = float(self.Se_valor_CSR_MO.get())
        def modelo(D, p):
            self.S = p[1] * D / (p[0] - D)
            self.X = (self.Se - self.S) * p[2]
            self.P = p[3] * self.X
            return (self.X, self.S, self.P)
        def objetiva(p):
            self.X_pred = modelo(self.DE, p)[0]
            self.S_pred = modelo(self.DE, p)[1]
            self.P_pred = modelo(self.DE, p)[2]
            residuo = np.sqrt((sum((self.XE - self.X_pred) ** 2) / len(self.XE)) + (sum((self.SE - self.S_pred) ** 2) / len(self.SE)) + (
                        sum((self.PE - self.P_pred) ** 2) / len(self.PE)))
            return residuo
        self.resultado = differential_evolution(objetiva, [(0.1, 0.6), (0, 1000), (0.01, 0.1), (0, 1000)],
                                           maxiter=2000, popsize=30)
        self.parametros = self.resultado.x
        self.mimax_texto_CSR = Label(self.frame_CSR_MO, text="Velocidade específica de crescimento (1/h):")
        self.mimax_texto_CSR.place(relx=0.27, rely=0.96, relwidth=0.15, relheight=0.03)
        self.mimax_str_CSR = str(round(self.parametros[0], 4))
        self.mimax_valor_CSR = Label(self.frame_CSR_MO, text=self.mimax_str_CSR)
        self.mimax_valor_CSR.place(relx=0.42, rely=0.96, relwidth=0.03, relheight=0.03)
        self.ks_texto_CSR = Label(self.frame_CSR_MO, text="Constante de saturação (kg/m³):")
        self.ks_texto_CSR.place(relx=0.455, rely=0.96, relwidth=0.12, relheight=0.03)
        self.ks_str_CSR = str(round(self.parametros[1], 4))
        self.ks_valor_CSR = Label(self.frame_CSR_MO, text=self.ks_str_CSR)
        self.ks_valor_CSR.place(relx=0.575, rely=0.96, relwidth=0.03, relheight=0.03)
        self.Yxs_texto_CSR = Label(self.frame_CSR_MO, text="Rendimento de substrato em células (kg/kg):")
        self.Yxs_texto_CSR.place(relx=0.61, rely=0.96, relwidth=0.16, relheight=0.03)
        self.Yxs_str_CSR = str(round(self.parametros[2], 4))
        self.Yxs_valor_CSR = Label(self.frame_CSR_MO, text=self.Yxs_str_CSR)
        self.Yxs_valor_CSR.place(relx=0.77, rely=0.96, relwidth=0.03, relheight=0.03)
        self.a_texto_CSR = Label(self.frame_CSR_MO, text="Coeficiente de formação de produto (kg/kg):")
        self.a_texto_CSR.place(relx=0.805, rely=0.96, relwidth=0.16, relheight=0.03)
        self.a_str_CSR = str(round(self.parametros[3], 4))
        self.a_valor_CSR = Label(self.frame_CSR_MO, text=self.a_str_CSR)
        self.a_valor_CSR.place(relx=0.965, rely=0.96, relwidth=0.03, relheight=0.03)
        self.fig1, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.scatter(self.DE, self.XE, label="Células experimental", color="blue", marker="o", s=5)
        self.ax1.scatter(self.DE, self.SE, label="Substrato experimental", color="red", marker="o", s=5)
        self.ax1.scatter(self.DE, self.PE, label="Produto experimental", color="green", marker="o", s=5)
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[0], label="Células", color="cornflowerblue", linewidth=1,
                      linestyle="-")
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[1], label="Substrato", color="lightcoral", linewidth=1,
                      linestyle="-")
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[2], label="Produto", color="lightgreen", linewidth=1,
                      linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Concentração (kg/m³)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.ax1.legend(fontsize=15, edgecolor="black")
        self.grafico1 = FigureCanvasTkAgg(self.fig1, self.frame_CSR_MO)
        self.grafico1.get_tk_widget().place(relx=0.27, rely=0.05, relwidth=0.72, relheight=0.90)

    def modelar_CCRE(self):
        import pandas as pd
        import numpy as np
        from scipy.optimize import differential_evolution
        import matplotlib.pyplot as plt
        from tkinter import filedialog
        from tkinter import Label
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        self.planilha_MO = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        self.dados = pd.read_excel("Planilha Modelo.xlsx")
        self.DE = np.asarray(self.dados["Taxa de Diluição (1/h)"])
        self.XE = np.asarray(self.dados["Células (kg/m³)"])
        self.SE = np.asarray(self.dados["Substrato (kg/m³)"])
        self.PE = np.asarray(self.dados["Produto (kg/m³)"])
        self.Se = float(self.Se_valor_CCRE_MO.get())
        self.r = float(self.r_valor_CCRE_MO.get())
        self.c = float(self.c_valor_CCRE_MO.get())
        def modelo(D, p):
            self.S = (p[1] * D * (1 + self.r * (1 - self.c))) / (p[0] - D * (1 + self.r * (1 - self.c)))
            self.X = (self.Se - self.S) * p[2] / (1 + self.r * (1 - self.c))
            self.P = p[3] * p[2] * (self.Se - self.S)
            return (self.X, self.S, self.P)
        def objetiva(p):
            self.X_pred = modelo(self.DE, p)[0]
            self.S_pred = modelo(self.DE, p)[1]
            self.P_pred = modelo(self.DE, p)[2]
            residuo = np.sqrt((sum((self.XE - self.X_pred) ** 2) / len(self.XE)) + (sum((self.SE - self.S_pred) ** 2) / len(self.SE)) + (
                        sum((self.PE - self.P_pred) ** 2) / len(self.PE)))
            return residuo
        self.resultado = differential_evolution(objetiva, [(0.1, 0.6), (0, 1000), (0.01, 0.1), (0, 1000)],
                                           maxiter=2000, popsize=30)
        self.parametros = self.resultado.x
        self.mimax_texto_CCRE = Label(self.frame_CCRE_MO, text="Velocidade específica de crescimento (1/h):")
        self.mimax_texto_CCRE.place(relx=0.27, rely=0.96, relwidth=0.15, relheight=0.03)
        self.mimax_str_CCRE = str(round(self.parametros[0], 4))
        self.mimax_valor_CCRE = Label(self.frame_CCRE_MO, text=self.mimax_str_CCRE)
        self.mimax_valor_CCRE.place(relx=0.42, rely=0.96, relwidth=0.03, relheight=0.03)
        self.ks_texto_CCRE = Label(self.frame_CCRE_MO, text="Constante de saturação (kg/m³):")
        self.ks_texto_CCRE.place(relx=0.455, rely=0.96, relwidth=0.12, relheight=0.03)
        self.ks_str_CCRE = str(round(self.parametros[1], 4))
        self.ks_valor_CCRE = Label(self.frame_CCRE_MO, text=self.ks_str_CCRE)
        self.ks_valor_CCRE.place(relx=0.575, rely=0.96, relwidth=0.03, relheight=0.03)
        self.Yxs_texto_CCRE = Label(self.frame_CCRE_MO, text="Rendimento de substrato em células (kg/kg):")
        self.Yxs_texto_CCRE.place(relx=0.61, rely=0.96, relwidth=0.16, relheight=0.03)
        self.Yxs_str_CCRE = str(round(self.parametros[2], 4))
        self.Yxs_valor_CCRE = Label(self.frame_CCRE_MO, text=self.Yxs_str_CCRE)
        self.Yxs_valor_CCRE.place(relx=0.77, rely=0.96, relwidth=0.03, relheight=0.03)
        self.a_texto_CCRE = Label(self.frame_CCRE_MO, text="Coeficiente de formação de produto (kg/kg):")
        self.a_texto_CCRE.place(relx=0.805, rely=0.96, relwidth=0.16, relheight=0.03)
        self.a_str_CCRE = str(round(self.parametros[3], 4))
        self.a_valor_CCRE = Label(self.frame_CCRE_MO, text=self.a_str_CCRE)
        self.a_valor_CCRE.place(relx=0.965, rely=0.96, relwidth=0.03, relheight=0.03)
        self.fig1, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.scatter(self.DE, self.XE, label="Células experimental", color="blue", marker="o", s=5)
        self.ax1.scatter(self.DE, self.SE, label="Substrato experimental", color="red", marker="o", s=5)
        self.ax1.scatter(self.DE, self.PE, label="Produto experimental", color="green", marker="o", s=5)
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[0], label="Células", color="cornflowerblue", linewidth=1,
                      linestyle="-")
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[1], label="Substrato", color="lightcoral", linewidth=1,
                      linestyle="-")
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[2], label="Produto", color="lightgreen", linewidth=1,
                      linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Concentração (kg/m³)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.ax1.legend(fontsize=15, edgecolor="black")
        self.grafico1 = FigureCanvasTkAgg(self.fig1, self.frame_CCRE_MO)
        self.grafico1.get_tk_widget().place(relx=0.27, rely=0.05, relwidth=0.72, relheight=0.90)

    def modelar_CCRI(self):
        import pandas as pd
        import numpy as np
        from scipy.optimize import differential_evolution
        import matplotlib.pyplot as plt
        from tkinter import filedialog
        from tkinter import Label
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        self.planilha_MO = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        self.dados = pd.read_excel("Planilha Modelo.xlsx")
        self.DE = np.asarray(self.dados["Taxa de Diluição (1/h)"])
        self.XE = np.asarray(self.dados["Células (kg/m³)"])
        self.SE = np.asarray(self.dados["Substrato (kg/m³)"])
        self.PE = np.asarray(self.dados["Produto (kg/m³)"])
        self.Se = float(self.Se_valor_CCRI_MO.get())
        self.H = float(self.H_valor_CCRI_MO.get())
        self.f = float(self.f_valor_CCRI_MO.get())
        def modelo(D, p):
            self.S = (p[1] * D * (self.H * (1 - self.f) + self.f)) / (p[0] - D * (self.H * (1 - self.f) + self.f))
            self.X = (self.Se - self.S) * p[2] / (self.H * (1 - self.f) + self.f)
            self.P = p[3] * p[2] * (self.Se - self.S)
            return (self.X, self.S, self.P)
        def objetiva(p):
            self.X_pred = modelo(self.DE, p)[0]
            self.S_pred = modelo(self.DE, p)[1]
            self.P_pred = modelo(self.DE, p)[2]
            residuo = np.sqrt((sum((self.XE - self.X_pred) ** 2) / len(self.XE)) + (sum((self.SE - self.S_pred) ** 2) / len(self.SE)) + (
                        sum((self.PE - self.P_pred) ** 2) / len(self.PE)))
            return residuo
        self.resultado = differential_evolution(objetiva, [(0.1, 0.6), (0, 1000), (0.01, 0.1), (0, 1000)],
                                           maxiter=2000, popsize=30)
        self.parametros = self.resultado.x
        self.mimax_texto_CCRI = Label(self.frame_CCRI_MO, text="Velocidade específica de crescimento (1/h):")
        self.mimax_texto_CCRI.place(relx=0.27, rely=0.96, relwidth=0.15, relheight=0.03)
        self.mimax_str_CCRI = str(round(self.parametros[0], 4))
        self.mimax_valor_CCRI = Label(self.frame_CCRI_MO, text=self.mimax_str_CCRI)
        self.mimax_valor_CCRI.place(relx=0.42, rely=0.96, relwidth=0.03, relheight=0.03)
        self.ks_texto_CCRI = Label(self.frame_CCRI_MO, text="Constante de saturação (kg/m³):")
        self.ks_texto_CCRI.place(relx=0.455, rely=0.96, relwidth=0.12, relheight=0.03)
        self.ks_str_CCRI = str(round(self.parametros[1], 4))
        self.ks_valor_CCRI = Label(self.frame_CCRI_MO, text=self.ks_str_CCRI)
        self.ks_valor_CCRI.place(relx=0.575, rely=0.96, relwidth=0.03, relheight=0.03)
        self.Yxs_texto_CCRI = Label(self.frame_CCRI_MO, text="Rendimento de substrato em células (kg/kg):")
        self.Yxs_texto_CCRI.place(relx=0.61, rely=0.96, relwidth=0.16, relheight=0.03)
        self.Yxs_str_CCRI = str(round(self.parametros[2], 4))
        self.Yxs_valor_CCRI = Label(self.frame_CCRI_MO, text=self.Yxs_str_CCRI)
        self.Yxs_valor_CCRI.place(relx=0.77, rely=0.96, relwidth=0.03, relheight=0.03)
        self.a_texto_CCRI = Label(self.frame_CCRI_MO, text="Coeficiente de formação de produto (kg/kg):")
        self.a_texto_CCRI.place(relx=0.805, rely=0.96, relwidth=0.16, relheight=0.03)
        self.a_str_CCRI = str(round(self.parametros[3], 4))
        self.a_valor_CCRI = Label(self.frame_CCRI_MO, text=self.a_str_CCRI)
        self.a_valor_CCRI.place(relx=0.965, rely=0.96, relwidth=0.03, relheight=0.03)
        self.fig1, self.ax1 = plt.subplots(facecolor="white", edgecolor="black")
        self.ax1.scatter(self.DE, self.XE, label="Células experimental", color="blue", marker="o", s=5)
        self.ax1.scatter(self.DE, self.SE, label="Substrato experimental", color="red", marker="o", s=5)
        self.ax1.scatter(self.DE, self.PE, label="Produto experimental", color="green", marker="o", s=5)
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[0], label="Células", color="cornflowerblue", linewidth=1,
                      linestyle="-")
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[1], label="Substrato", color="lightcoral", linewidth=1,
                      linestyle="-")
        self.ax1.plot(self.DE, modelo(self.DE, self.parametros)[2], label="Produto", color="lightgreen", linewidth=1,
                      linestyle="-")
        self.ax1.set(xlabel="Taxa de Diluição (1/h)", ylabel="Concentração (kg/m³)")
        self.ax1.grid(color="gray", linestyle=":", linewidth=1)
        self.ax1.legend(fontsize=15, edgecolor="black")
        self.grafico1 = FigureCanvasTkAgg(self.fig1, self.frame_CCRI_MO)
        self.grafico1.get_tk_widget().place(relx=0.27, rely=0.05, relwidth=0.72, relheight=0.90)