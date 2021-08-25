from tkinter import *
from tkinter.ttk import *
import pandas as pd
from pandastable import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

#The main window with a resolution of 700x600
master = Tk()
master.geometry("700x600")

def openTop():
    # Información de la ventana principal de tops
    topWindow = Toplevel(master)
    topWindow.iconbitmap("imagenes/Poke-ball.ico")

    # Titulo de la nueva ventana
    topWindow.title("Top de Pokémons")

    # Tamaño predefinido
    topWindow.geometry("720x550")

    # Imagen:
    labelImagen1 = Label(topWindow, image=imagenTops).grid(row=0, column=1)

    textoTops = Label(topWindow,
                      text="Esta sección sirve para mostrar los tres mejores pokemon de cada tipo. Ordenados según su Total, Vida (HP), Ataque, Defensa, \n"
                           "Ataque especial, Defensa especial y Velocidad.").grid(row=1, column=1)

    def openStats():
        topWindow = Toplevel(master)
        topWindow.iconbitmap("imagenes/Poke-ball.ico")

        # Titulo de la nueva ventana
        topWindow.title("Top de Pokémons")

        # Tamaño predefinido
        topWindow.geometry("770x130")

        # Venanas interiores para Total
        def openTotal():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón
            def totalNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def totalFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def totalAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def totalElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico, showtoolbar=False, showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def totalPlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def totalHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def totalLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def totalVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def totalTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def totalPsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def totalBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def totalRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=totalNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=totalFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=totalAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=totalElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=totalPlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=totalHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=totalLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=totalVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=totalTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=totalPsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=totalBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=totalRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        # Ventanas interiores para Vida:
        def openVida():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón de tops vida
            def vidaNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal_vida, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def vidaFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego_vida, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def vidaAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua_vida, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def vidaElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico_vida, showtoolbar=False,
                                       showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def vidaPlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta_vida, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def vidaHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo_vida, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def vidaLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha_vida, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def vidaVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno_vida, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def vidaTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra_vida, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def vidaPsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico_vida, showtoolbar=False,
                                      showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def vidaBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho_vida, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def vidaRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca_vida, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=vidaNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=vidaFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=vidaAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=vidaElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=vidaPlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=vidaHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=vidaLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=vidaVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=vidaTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=vidaPsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=vidaBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=vidaRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        # Ventanas interiores para Ataque:
        def openAtaque():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón de tops vida
            def ataqueNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal_ataque, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def ataqueFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego_ataque, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def ataqueAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua_ataque, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def ataqueElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico_ataque, showtoolbar=False,
                                       showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def ataquePlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta_ataque, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def ataqueHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo_ataque, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def ataqueLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha_ataque, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def ataqueVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno_ataque, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def ataqueTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra_ataque, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def ataquePsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico_ataque, showtoolbar=False,
                                      showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def ataqueBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho_ataque, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def ataqueRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca_ataque, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=ataqueNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=ataqueFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=ataqueAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=ataqueElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=ataquePlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=ataqueHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=ataqueLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=ataqueVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=ataqueTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=ataquePsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=ataqueBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=ataqueRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        # Ventanas interiores para Defensa:
        def openDefensa():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón de tops vida
            def defensaNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal_defensa, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def defensaFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego_defensa, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def defensaAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua_defensa, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def defensaElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico_defensa, showtoolbar=False,
                                       showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def defensaPlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta_defensa, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def defensaHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo_defensa, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def defensaLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha_defensa, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def defensaVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno_defensa, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def defensaTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra_defensa, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def defensaPsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico_defensa, showtoolbar=False,
                                      showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def defensaBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho_defensa, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def defensaRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca_defensa, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=defensaNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=defensaFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=defensaAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=defensaElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=defensaPlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=defensaHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=defensaLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=defensaVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=defensaTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=defensaPsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=defensaBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=defensaRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        # Ventanas interiores para Ataque especial:
        def openAes():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón de tops vida
            def aesNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal_aes, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def aesFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego_aes, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def aesAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua_aes, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def aesElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico_aes, showtoolbar=False,
                                       showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def aesPlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta_aes, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def aesHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo_aes, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def aesLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha_aes, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def aesVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno_aes, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def aesTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra_aes, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def aesPsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico_aes, showtoolbar=False,
                                      showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def aesBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho_aes, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def aesRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca_aes, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=aesNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=aesFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=aesAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=aesElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=aesPlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=aesHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=aesLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=aesVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=aesTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=aesPsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=aesBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=aesRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        # Ventanas interiores para Defensa especial:
        def openDes():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón de tops vida
            def desNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal_des, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def desFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego_des, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def desAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua_des, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def desElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico_des, showtoolbar=False,
                                       showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def desPlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta_des, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def desHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo_des, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def desLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha_des, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def desVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno_des, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def desTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra_des, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def desPsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico_des, showtoolbar=False,
                                      showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def desBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho_des, showtoolbar=False, showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def desRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca_des, showtoolbar=False, showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=desNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=desFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=desAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=desElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=desPlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=desHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=desLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=desVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=desTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=desPsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=desBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=desRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        # Ventanas interiores para Defensa especial:
        def openVelocidad():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            # Titulo de la nueva ventana
            topWindow.title("Tipos de Pokémons")

            # Tamaño predefinido
            topWindow.geometry("1085x310")

            # Funciones para cada botón de tops vida
            def velocidadNormal():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo normal")
                topWindow.geometry("1065x135")

                # Para crear una tabla que muestre el dataFrame
                normalTable = Table(topWindow, dataframe=mejores_normal_velocidad, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                normalTable.show()

            def velocidadFuego():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fuego")
                topWindow.geometry("1065x135")

                fuegoTable = Table(topWindow, dataframe=mejores_fuego_velocidad, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                fuegoTable.show()

            def velocidadAgua():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo agua")
                topWindow.geometry("1065x135")

                aguaTable = Table(topWindow, dataframe=mejores_agua_velocidad, showtoolbar=False,
                                  showstatusbar=True,
                                  editable=False)
                aguaTable.show()

            def velocidadElectrico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo eléctrico")
                topWindow.geometry("1065x135")

                electricoTable = Table(topWindow, dataframe=mejores_electrico_velocidad, showtoolbar=False,
                                       showstatusbar=True,
                                       editable=False)
                electricoTable.show()

            def velocidadPlanta():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo planta")
                topWindow.geometry("1065x135")

                plantaTable = Table(topWindow, dataframe=mejores_planta_velocidad, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                plantaTable.show()

            def velocidadHielo():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo hielo")
                topWindow.geometry("1065x135")

                hieloTable = Table(topWindow, dataframe=mejores_hielo_velocidad, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                hieloTable.show()

            def velocidadLucha():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo lucha")
                topWindow.geometry("1065x135")

                luchaTable = Table(topWindow, dataframe=mejores_lucha_velocidad, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                luchaTable.show()

            def velocidadVeneno():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo veneno")
                topWindow.geometry("1065x135")

                venenoTable = Table(topWindow, dataframe=mejores_veneno_velocidad, showtoolbar=True,
                                    showstatusbar=True,
                                    editable=False)
                venenoTable.show()

            def velocidadTierra():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo tierra")
                topWindow.geometry("1065x135")

                tierraTable = Table(topWindow, dataframe=mejores_tierra_velocidad, showtoolbar=False,
                                    showstatusbar=True,
                                    editable=False)
                tierraTable.show()

            def velocidadPsiquico():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo psiquico")
                topWindow.geometry("1065x135")

                psiquicoTable = Table(topWindow, dataframe=mejores_psiquico_velocidad, showtoolbar=False,
                                      showstatusbar=True,
                                      editable=False)
                psiquicoTable.show()

            def velocidadBicho():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo bicho")
                topWindow.geometry("1065x135")

                bichoTable = Table(topWindow, dataframe=mejores_bicho_velocidad, showtoolbar=False,
                                   showstatusbar=True,
                                   editable=False)
                bichoTable.show()

            def velocidadRoca():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo roca")
                topWindow.geometry("1065x135")

                rocaTable = Table(topWindow, dataframe=mejores_roca_velocidad, showtoolbar=False,
                                  showstatusbar=True,
                                  editable=False)
                rocaTable.show()

            def totalFantasma():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo fantasma")
                topWindow.geometry("1065x135")

                fantasmaTable = Table(topWindow, dataframe=mejores_fantasma, showtoolbar=False, showstatusbar=True,
                                      editable=False)
                fantasmaTable.show()

            def totalDragon():
                topWindow = Toplevel(master)
                topWindow.iconbitmap("imagenes/Poke-ball.ico")
                topWindow.title("Top 3 tipo dragon")
                topWindow.geometry("1065x135")

                dragonTable = Table(topWindow, dataframe=mejores_dragon, showtoolbar=False, showstatusbar=True,
                                    editable=False)
                dragonTable.show()

            # Botones para los tipos
            btnNormal = Button(topWindow, image=normal0, command=velocidadNormal).grid(row=0, column=0)
            btnFuego = Button(topWindow, image=fuego0, command=velocidadFuego).grid(row=0, column=1)
            btnAgua = Button(topWindow, image=agua0, command=velocidadAgua).grid(row=0, column=2)
            btnElectrico = Button(topWindow, image=electrico0, command=velocidadElectrico).grid(row=0, column=3)
            btnPlanta = Button(topWindow, image=planta0, command=velocidadPlanta).grid(row=0, column=4)
            btnHielo = Button(topWindow, image=hielo0, command=velocidadHielo).grid(row=0, column=5)
            btnLucha = Button(topWindow, image=lucha0, command=velocidadLucha).grid(row=0, column=6)
            btnVeneno = Button(topWindow, image=veneno0, command=velocidadVeneno).grid(row=1, column=0)
            btnTierra = Button(topWindow, image=tierra0, command=velocidadTierra).grid(row=1, column=1)
            btnPsiquico = Button(topWindow, image=psiquico0, command=velocidadPsiquico).grid(row=1, column=2)
            btnBicho = Button(topWindow, image=bicho0, command=velocidadBicho).grid(row=1, column=3)
            btnRoca = Button(topWindow, image=roca0, command=velocidadRoca).grid(row=1, column=4)
            btnFantasma = Button(topWindow, image=fantasma0, command=totalFantasma).grid(row=1, column=5)
            btnDragon = Button(topWindow, image=dragon0, command=totalDragon).grid(row=1, column=6)

        btnTot = Button(topWindow, text = "Total",image=total_icon, command=openTotal, compound="top").grid(row=0, column=0)
        btnHp = Button(topWindow, text = 'Vida', image=hp_icon, command=openVida, compound="top").grid(row=0, column=1)
        btnAtk = Button(topWindow, text = 'Ataque', image=atk_icon, command=openAtaque, compound="top").grid(row=0, column=2)
        btnDef = Button(topWindow,text = 'Defensa', image=def_icon, command=openDefensa, compound="top").grid(row=0, column=3)
        btnAes = Button(topWindow,text = 'At. Esp', image=aes_icon, command=openAes, compound="top").grid(row=0, column=4)
        btnDes = Button(topWindow,text = 'Df. Esp', image=des_icon, command=openDes, compound="top").grid(row=0, column=5)
        btnSpd = Button(topWindow,text = 'Velocidad', image=spd_icon, command=openVelocidad, compound="top").grid(row=0, column=6)

    btnEmpezar = Button(topWindow, image=imagenBotonMapaStats, command=openStats).grid(row=2, column=1)


#----------------------------------------------------------------------------------------------------------------------#

def openMaps():

    topWindow = Toplevel(master)
    topWindow.iconbitmap("imagenes/Poke-ball.ico")

    topWindow.title("Mapas de calor Pokémon")
    topWindow.geometry("720x550")

    labelImagen1 = Label(topWindow, image=imagenMapas).grid(row=0, column=1)

    textoTops = Label(topWindow,
                      text="Esta sección sirve para mostrar mapas de calor por tipos para comprobar los puntos flojos y fuertes de cada tipo.").grid(row=1, column=1)

# Ventanas interiores para Defensa especial:
    def openMapas():
        topWindow = Toplevel(master)
        topWindow.iconbitmap("imagenes/Poke-ball.ico")

        # Titulo de la nueva ventana
        topWindow.title("Tipos de Pokémons (Mapas de calor)")

        # Tamaño predefinido
        topWindow.geometry("1085x310")

        # Funciones para cada botón de tops vida
        def mapaNormal():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: normal")
            topWindow.geometry("450x280")

            #Insertar mapa de calor para el tipo normal:
            labelImagen = Label(topWindow, image=imagenNormalMapa).grid(row=0, column=1)

        def mapaFuego():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: fuego")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo fuego:
            labelImagen = Label(topWindow, image=imagenFuegoMapa).grid(row=0, column=1)

        def mapaAgua():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: agua")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo agua:
            labelImagen = Label(topWindow, image=imagenAguaMapa).grid(row=0, column=1)

        def mapaElectrico():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: eléctrico")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo electrico:
            labelImagen = Label(topWindow, image=imagenElectricoMapa).grid(row=0, column=1)

        def mapaPlanta():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: planta")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo planta:
            labelImagen = Label(topWindow, image=imagenPlantaMapa).grid(row=0, column=1)

        def mapaHielo():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: hielo")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo hielo:
            labelImagen = Label(topWindow, image=imagenHieloMapa).grid(row=0, column=1)

        def mapaLucha():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: lucha")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo lucha:
            labelImagen = Label(topWindow, image=imagenLuchaMapa).grid(row=0, column=1)

        def mapaVeneno():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: veneno")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo veneno:
            labelImagen = Label(topWindow, image=imagenVenenoMapa).grid(row=0, column=1)

        def mapaTierra():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: tierra")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo tierra:
            labelImagen = Label(topWindow, image=imagenTierraMapa).grid(row=0, column=1)

        def mapaPsiquico():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: psíquico")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo psíquico:
            labelImagen = Label(topWindow, image=imagenPsiquicoMapa).grid(row=0, column=1)

        def mapaBicho():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: bicho")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo bicho:
            labelImagen = Label(topWindow, image=imagenBichoMapa).grid(row=0, column=1)

        def mapaRoca():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: roca")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo roca:
            labelImagen = Label(topWindow, image=imagenRocaMapa).grid(row=0, column=1)

        def mapaFantasma():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: fantasma")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo fantasma:
            labelImagen = Label(topWindow, image=imagenFantasmaMapa).grid(row=0, column=1)

        def mapaDragon():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Mapa de calor: dragón")
            topWindow.geometry("450x280")

            # Insertar mapa de calor para el tipo dragón:
            labelImagen = Label(topWindow, image=imagenDragonMapa).grid(row=0, column=1)

        # Botones para los tipos
        btnNormal = Button(topWindow, image=normal0, command=mapaNormal).grid(row=0, column=0)
        btnFuego = Button(topWindow, image=fuego0, command=mapaFuego).grid(row=0, column=1)
        btnAgua = Button(topWindow, image=agua0, command=mapaAgua).grid(row=0, column=2)
        btnElectrico = Button(topWindow, image=electrico0, command=mapaElectrico).grid(row=0, column=3)
        btnPlanta = Button(topWindow, image=planta0, command=mapaPlanta).grid(row=0, column=4)
        btnHielo = Button(topWindow, image=hielo0, command=mapaHielo).grid(row=0, column=5)
        btnLucha = Button(topWindow, image=lucha0, command=mapaLucha).grid(row=0, column=6)
        btnVeneno = Button(topWindow, image=veneno0, command=mapaVeneno).grid(row=1, column=0)
        btnTierra = Button(topWindow, image=tierra0, command=mapaTierra).grid(row=1, column=1)
        btnPsiquico = Button(topWindow, image=psiquico0, command=mapaPsiquico).grid(row=1, column=2)
        btnBicho = Button(topWindow, image=bicho0, command=mapaBicho).grid(row=1, column=3)
        btnRoca = Button(topWindow, image=roca0, command=mapaRoca).grid(row=1, column=4)
        btnFantasma = Button(topWindow, image=fantasma0, command=mapaFantasma).grid(row=1, column=5)
        btnDragon = Button(topWindow, image=dragon0, command=mapaDragon).grid(row=1, column=6)

    btnVel = Button(topWindow, image = imagenBotonMapaSecundario, command=openMapas).grid(row=8, column=1)

#----------------------------------------------------------------------------------------------------------------------#

def openCrear():

    topWindow = Toplevel(master)
    topWindow.iconbitmap("imagenes/Poke-ball.ico")

    topWindow.title("Crear equipos Pokémon")
    topWindow.geometry("720x550")

    labelImagen1 = Label(topWindow, image=imagenEquipos).grid(row=0, column=1)

    textoTops = Label(topWindow, text="Esta sección sirve para crear equipos de 3 pokémons aleatorios.").grid(row=1, column=1)

    def crearEquipo():
        topWindow = Toplevel(master)
        topWindow.iconbitmap("imagenes/Poke-ball.ico")
        topWindow.title("Equipo Aleatorio")
        topWindow.geometry("270x625")

        lista = []

        for x in range(3):
            randompoki = np.random.randint(0, 151)
            lista.append(pokemon.iloc[randompoki])
            lista.append("--------------------------")

        label = Label(topWindow, text="\n".join(map(str, lista))).grid(row=0,column=1)

    #Botones:
    botonRandomize = Button(topWindow, image = imagenBotonRandom,command=crearEquipo).grid(row=3, column=1)

#----------------------------------------------------------------------------------------------------------------------#

def openComparativas():

    topWindow = Toplevel(master)
    topWindow.iconbitmap("imagenes/Poke-ball.ico")

    topWindow.title("Totales por tipo")
    topWindow.geometry("720x550")

    labelImagen1 = Label(topWindow, image=imagenComparativas).grid(row=0, column=1)

    def openCorrelacion():
        topWindow = Toplevel(master)
        topWindow.iconbitmap("imagenes/Poke-ball.ico")

        topWindow.title("Correlación del Total con los Stats")
        topWindow.geometry("660x130")

        def openCorrelacionVida():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Correlación entre el Total y la vida")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['HP'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_ylabel('Vida de los pokémon')
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Correlación entre el Total y la vida')

            topWindow.title("Correlación del Total con la vida")
            topWindow.geometry("500x450")

            # Para mostrar la correlación usamos la función pearson_r que está definida al final del código
            Label(topWindow, text=pearson_r(pokemon["Total"], pokemon["HP"])).grid(row=1, column=0)

        def openCorrelacionAtaq():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Correlación del Total con el ataque")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['Attack'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_ylabel('Ataque de los pokémon')
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Correlación entre el Total y el ataque')

            topWindow.geometry("500x450")

            Label(topWindow, text=pearson_r(pokemon["Total"], pokemon["Attack"])).grid(row=1, column=0)

        def openCorrelacionDef():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")
            topWindow.title("Correlación del Total con la defensa")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['Defense'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_ylabel('Defensa de los pokémon')
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Correlación entre el Total y la defensa')

            Label(topWindow, text=pearson_r(pokemon["Total"], pokemon["Defense"])).grid(row=1, column=0)

        def openCorrelacionAes():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Correlación del Total con el ataque especial")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['Sp. Atk'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_ylabel('Ataque Especial de los pokémon')
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Correlación entre el Total y el ataque especial')

            Label(topWindow, text=pearson_r(pokemon["Total"], pokemon["Sp. Atk"])).grid(row=1, column=0)

        def openCorrelacionDes():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Correlación del Total con la defensa especial")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['Sp. Def'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_ylabel('Defensa especial de los pokémon')
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Correlación entre el Total y la defensa especial')

            Label(topWindow, text=pearson_r(pokemon["Total"], pokemon["Sp. Def"])).grid(row=1, column=0)

        def openCorrelacionSpd():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Correlación del Total con la velocidad")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['Speed'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_ylabel('Velocidad de los pokémon')
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Correlación entre el Total y la velocidad')

            Label(topWindow, text=pearson_r(pokemon["Total"], pokemon["Speed"])).grid(row=1, column=0)

        btnHp = Button(topWindow, text='Vida', image=hp_icon, command=openCorrelacionVida, compound="top").grid(row=0, column=1)
        btnAtk = Button(topWindow, text='Ataque', image=atk_icon, command=openCorrelacionAtaq, compound="top").grid(row=0,column=2)
        btnDef = Button(topWindow, text='Defensa', image=def_icon, command=openCorrelacionDef, compound="top").grid(row=0,column=3)
        btnAes = Button(topWindow, text='At. Esp', image=aes_icon, command=openCorrelacionAes, compound="top").grid(row=0,column=4)
        btnDes = Button(topWindow, text='Df. Esp', image=des_icon, command=openCorrelacionDes, compound="top").grid(row=0,column=5)
        btnSpd = Button(topWindow, text='Velocidad', image=spd_icon, command=openCorrelacionSpd, compound="top").grid(row=0,column=6)

    def openMapasPuntos():
        topWindow = Toplevel(master)
        topWindow.iconbitmap("imagenes/Poke-ball.ico")

        topWindow.title("Mapas puntos")
        topWindow.geometry("770x130")

        def openMapaTotal():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos del Total por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Total'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Total de los pokémon')
            ax3.set_title('Mapa de puntos del Total por Tipos')

        def openMapaHP():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos de la vida por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['HP'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Vida de los pokémon')
            ax3.set_title('Mapa de puntos de la vida por Tipos')

        def openMapaAtaque():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos del Ataque por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Attack'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Ataque de los pokémon')
            ax3.set_title('Mapa de puntos del Ataque por Tipos')

        def openMapaDefensa():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos de la defensa por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Defense'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Defensa de los pokémon')
            ax3.set_title('Mapa de puntos de la defensa por Tipos')

        def openMapaAes():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos del ataque especial por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Sp. Atk'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Ataque especial de los pokémon')
            ax3.set_title('Mapa de puntos del ataque especial por Tipos')

        def openMapaDes():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos de la defensa especial por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Sp. Def'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Defensa especial de los pokémon')
            ax3.set_title('Mapa de puntos de la defensa especial por Tipos')

        def openMapaVel():
            topWindow = Toplevel(master)
            topWindow.iconbitmap("imagenes/Poke-ball.ico")

            topWindow.title("Mapa de puntos de la velocidad por Tipos")
            topWindow.geometry("500x450")

            figure3 = plt.Figure(figsize=(5, 4), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.scatter(pokemon['Speed'], pokemon['Type 1'], color='r')
            scatter3 = FigureCanvasTkAgg(figure3, topWindow)
            scatter3.get_tk_widget().grid(row=0, column=0)
            ax3.set_xlabel('Velocidad de los pokémon')
            ax3.set_title('Mapa de puntos de la velocidad por Tipos')


        btnTot = Button(topWindow, text='Total', image=total_icon, command=openMapaTotal, compound="top").grid(row=0,column=0)
        btnHp = Button(topWindow, text='Vida', image=hp_icon, command=openMapaHP, compound="top").grid(row=0,column=1)
        btnAtk = Button(topWindow, text='Ataque', image=atk_icon, command=openMapaAtaque, compound="top").grid(row=0, column=2)
        btnDef = Button(topWindow, text='Defensa', image=def_icon, command=openMapaDefensa, compound="top").grid(row=0, column=3)
        btnAes = Button(topWindow, text='At. Esp', image=aes_icon, command=openMapaAes, compound="top").grid(row=0, column=4)
        btnDes = Button(topWindow, text='Df. Esp', image=des_icon, command=openMapaDes, compound="top").grid(row=0, column=5)
        btnSpd = Button(topWindow, text='Velocidad', image=spd_icon, command=openMapaVel, compound="top").grid(row=0, column=6)

    #Botones:
    botonCorrelaciones = Button(topWindow, image = imagenBotonCorrelaciones,command=openCorrelacion).grid(row=1, column=1)
    botonMapasPuntos = Button(topWindow, image = imagenBotonMapasTipos, command=openMapasPuntos).grid(row=2,column=1)

#----------------------------------------------------------------------------------------------------------------------#

#Insertar fotos para los botones del menú principal:
imagenBotonTop = PhotoImage(file="imagenes/tops-boton.gif")
imagenBotonMapas = PhotoImage(file="imagenes/mapas-boton.gif")
imagenBotonEquipos = PhotoImage(file="imagenes/equipos-boton.gif")
imagenBotonComparativas = PhotoImage(file="imagenes/comparativas-boton.gif")

# Para otros botones
imagenBotonRandom = PhotoImage(file="imagenes/boton-random.gif")
imagenBotonMapaSecundario = PhotoImage(file="imagenes/boton-mapa-secundario.gif")
imagenBotonMapaStats = PhotoImage(file="imagenes/boton-stats.gif")
imagenBotonCorrelaciones = PhotoImage(file="imagenes/correlaciones-boton.gif")
imagenBotonMapasTipos = PhotoImage(file="imagenes/mapa-puntos-boton.gif")

# Los botones para acceder a las categorias:
btnTops = Button(master,image = imagenBotonTop ,command=openTop).grid(row=1,column=1)
btnMaps = Button(master,image = imagenBotonMapas, command = openMaps).grid(row=2,column=1)
btnCrear = Button(master,image = imagenBotonEquipos,command=openCrear).grid(row=3,column=1)
btnComp = Button(master,image = imagenBotonComparativas,command=openComparativas).grid(row=4,column=1)

master.title("Pokemon")

#Para modificar el icono de la ventana:
master.iconbitmap("imagenes/Poke-ball.ico")

#Para insertar foto
miImagen = PhotoImage(file="imagenes/principal.gif")
labelImagen = Label(master, image = miImagen).grid(row = 0,column = 1)

#Insertar fotos en otras ventanas:
imagenTops = PhotoImage(file="imagenes/tops.gif")
imagenEquipos = PhotoImage(file="imagenes/equipo.gif")
imagenCovarianza = PhotoImage(file="imagenes/covarianzas.gif")
imagenMapas = PhotoImage(file="imagenes/mapas.gif")
imagenComparativas = PhotoImage(file="imagenes/comparativas.gif")

#Fotos para los botones de tipos
normal0 = PhotoImage(file="imagenes/normal0.gif")
fuego0 = PhotoImage(file="imagenes/fuego0.gif")
agua0 = PhotoImage(file="imagenes/agua0.gif")
electrico0 = PhotoImage(file="imagenes/electrico0.gif")
planta0 = PhotoImage(file="imagenes/planta0.gif")
hielo0 = PhotoImage(file="imagenes/hielo0.gif")
lucha0 = PhotoImage(file="imagenes/lucha0.gif")
veneno0 = PhotoImage(file="imagenes/veneno0.gif")
tierra0 = PhotoImage(file="imagenes/tierra0.gif")
psiquico0 = PhotoImage(file="imagenes/psiquico0.gif")
bicho0 = PhotoImage(file="imagenes/bicho0.gif")
roca0 = PhotoImage(file="imagenes/roca0.gif")
fantasma0 = PhotoImage(file="imagenes/fantasma0.gif")
dragon0 = PhotoImage(file="imagenes/dragon0.gif")

# Botones para los stats:
total_icon = PhotoImage(file="imagenes/icon-total.gif")
hp_icon = PhotoImage(file="imagenes/icon-hp.gif")
atk_icon = PhotoImage(file="imagenes/icon-ataque.gif")
aes_icon = PhotoImage(file="imagenes/icon-ataque-especial.gif")
def_icon = PhotoImage(file="imagenes/icon-defensa.gif")
des_icon = PhotoImage(file="imagenes/icon-defensa-especial.gif")
spd_icon = PhotoImage(file="imagenes/icon-velocidad.gif")

#Fotos para los mapas de calor:
imagenNormalMapa = PhotoImage(file="imagenes/mapa-normal.gif")
imagenFuegoMapa = PhotoImage(file="imagenes/mapa-fuego.gif")
imagenAguaMapa = PhotoImage(file="imagenes/mapa-agua.gif")
imagenElectricoMapa = PhotoImage(file="imagenes/mapa-electrico.gif")
imagenPlantaMapa = PhotoImage(file="imagenes/mapa-planta.gif")
imagenHieloMapa = PhotoImage(file="imagenes/mapa-hielo.gif")
imagenLuchaMapa = PhotoImage(file="imagenes/mapa-lucha.gif")
imagenVenenoMapa = PhotoImage(file="imagenes/mapa-veneno.gif")
imagenTierraMapa = PhotoImage(file="imagenes/mapa-tierra.gif")
imagenPsiquicoMapa = PhotoImage(file="imagenes/mapa-psiquico.gif")
imagenBichoMapa = PhotoImage(file="imagenes/mapa-bicho.gif")
imagenRocaMapa = PhotoImage(file="imagenes/mapa-roca.gif")
imagenFantasmaMapa = PhotoImage(file="imagenes/mapa-fantasma.gif")
imagenDragonMapa = PhotoImage(file="imagenes/mapa-dragon.gif")

#TRATADO DE DATOS
#Tomamos un csv
pokemon = pd.read_csv('pokemon.csv', index_col = 0)

#Pasamos a crear una dataFrames para cada tipo de pokemon
agua = pokemon["Type 1"] == 'Water'
bicho = pokemon["Type 1"] == "Bug"
dragon = pokemon["Type 1"] == "Dragon"
electrico = pokemon["Type 1"] == "Electric"
fantasma = pokemon["Type 1"] == "Ghost"
fuego = pokemon["Type 1"] == "Fire"
hielo = pokemon["Type 1"] == "Ice"
lucha = pokemon["Type 1"] == "Fighting"
normal = pokemon["Type 1"] == "Normal"
planta = pokemon["Type 1"] == "Grass"
psiquico = pokemon["Type 1"] == "Psychic"
roca = pokemon["Type 1"] == "Rock"
tierra = pokemon["Type 1"] == "Ground"
veneno = pokemon["Type 1"] == "Poison"

#dataFrames para los tops totales:
mejores_normal = pokemon[normal].sort_values('Total', ascending = False).head(3)
mejores_fuego = pokemon[fuego].sort_values('Total', ascending = False).head(3)
mejores_agua = pokemon[agua].sort_values('Total', ascending = False).head(3)
mejores_electrico = pokemon[electrico].sort_values('Total', ascending = False).head(3)
mejores_planta = pokemon[planta].sort_values('Total', ascending = False).head(3)
mejores_hielo = pokemon[hielo].sort_values('Total', ascending = False).head(3)
mejores_lucha = pokemon[lucha].sort_values('Total', ascending = False).head(3)
mejores_veneno = pokemon[veneno].sort_values('Total', ascending = False).head(3)
mejores_tierra = pokemon[tierra].sort_values('Total', ascending = False).head(3)
mejores_psiquico = pokemon[psiquico].sort_values('Total', ascending = False).head(3)
mejores_bicho = pokemon[bicho].sort_values('Total', ascending = False).head(3)
mejores_roca = pokemon[roca].sort_values('Total', ascending = False).head(3)
mejores_fantasma = pokemon[fantasma].sort_values('Total', ascending = False).head(3)
mejores_dragon = pokemon[dragon].sort_values('Total', ascending = False).head(3)

#dataFrames para los tops de vida:
mejores_normal_vida = pokemon[normal].sort_values('HP', ascending = False).head(3)
mejores_fuego_vida = pokemon[fuego].sort_values('HP', ascending = False).head(3)
mejores_agua_vida = pokemon[agua].sort_values('HP', ascending = False).head(3)
mejores_electrico_vida = pokemon[electrico].sort_values('HP', ascending = False).head(3)
mejores_planta_vida = pokemon[planta].sort_values('HP', ascending = False).head(3)
mejores_hielo_vida = pokemon[hielo].sort_values('HP', ascending = False).head(3)
mejores_lucha_vida = pokemon[lucha].sort_values('HP', ascending = False).head(3)
mejores_veneno_vida = pokemon[veneno].sort_values('HP', ascending = False).head(3)
mejores_tierra_vida = pokemon[tierra].sort_values('HP', ascending = False).head(3)
mejores_psiquico_vida = pokemon[psiquico].sort_values('HP', ascending = False).head(3)
mejores_bicho_vida = pokemon[bicho].sort_values('HP', ascending = False).head(3)
mejores_roca_vida = pokemon[roca].sort_values('HP', ascending = False).head(3)

#dataFrames para los tops ataque:
mejores_normal_ataque = pokemon[normal].sort_values('Attack', ascending = False).head(3)
mejores_fuego_ataque = pokemon[fuego].sort_values('Attack', ascending = False).head(3)
mejores_agua_ataque = pokemon[agua].sort_values('Attack', ascending = False).head(3)
mejores_electrico_ataque = pokemon[electrico].sort_values('Attack', ascending = False).head(3)
mejores_planta_ataque = pokemon[planta].sort_values('Attack', ascending = False).head(3)
mejores_hielo_ataque = pokemon[hielo].sort_values('Attack', ascending = False).head(3)
mejores_lucha_ataque = pokemon[lucha].sort_values('Attack', ascending = False).head(3)
mejores_veneno_ataque = pokemon[veneno].sort_values('Attack', ascending = False).head(3)
mejores_tierra_ataque = pokemon[tierra].sort_values('Attack', ascending = False).head(3)
mejores_psiquico_ataque = pokemon[psiquico].sort_values('Attack', ascending = False).head(3)
mejores_bicho_ataque = pokemon[bicho].sort_values('Attack', ascending = False).head(3)
mejores_roca_ataque = pokemon[roca].sort_values('Attack', ascending = False).head(3)

#dataFrames para los tops defensa:
mejores_normal_defensa = pokemon[normal].sort_values('Defense', ascending = False).head(3)
mejores_fuego_defensa = pokemon[fuego].sort_values('Defense', ascending = False).head(3)
mejores_agua_defensa = pokemon[agua].sort_values('Defense', ascending = False).head(3)
mejores_electrico_defensa = pokemon[electrico].sort_values('Defense', ascending = False).head(3)
mejores_planta_defensa = pokemon[planta].sort_values('Defense', ascending = False).head(3)
mejores_hielo_defensa = pokemon[hielo].sort_values('Defense', ascending = False).head(3)
mejores_lucha_defensa = pokemon[lucha].sort_values('Defense', ascending = False).head(3)
mejores_veneno_defensa = pokemon[veneno].sort_values('Defense', ascending = False).head(3)
mejores_tierra_defensa = pokemon[tierra].sort_values('Defense', ascending = False).head(3)
mejores_psiquico_defensa = pokemon[psiquico].sort_values('Defense', ascending = False).head(3)
mejores_bicho_defensa = pokemon[bicho].sort_values('Defense', ascending = False).head(3)
mejores_roca_defensa = pokemon[roca].sort_values('Defense', ascending = False).head(3)

#dataFrames para los tops velocidad:
mejores_normal_velocidad = pokemon[normal].sort_values('Speed', ascending = False).head(3)
mejores_fuego_velocidad = pokemon[fuego].sort_values('Speed', ascending = False).head(3)
mejores_agua_velocidad = pokemon[agua].sort_values('Speed', ascending = False).head(3)
mejores_electrico_velocidad = pokemon[electrico].sort_values('Speed', ascending = False).head(3)
mejores_planta_velocidad = pokemon[planta].sort_values('Speed', ascending = False).head(3)
mejores_hielo_velocidad = pokemon[hielo].sort_values('Speed', ascending = False).head(3)
mejores_lucha_velocidad = pokemon[lucha].sort_values('Speed', ascending = False).head(3)
mejores_veneno_velocidad = pokemon[veneno].sort_values('Speed', ascending = False).head(3)
mejores_tierra_velocidad = pokemon[tierra].sort_values('Speed', ascending = False).head(3)
mejores_psiquico_velocidad = pokemon[psiquico].sort_values('Speed', ascending = False).head(3)
mejores_bicho_velocidad = pokemon[bicho].sort_values('Speed', ascending = False).head(3)
mejores_roca_velocidad = pokemon[roca].sort_values('Speed', ascending = False).head(3)

#dataFrames para los tops Ataque especial:
mejores_normal_aes = pokemon[normal].sort_values('Sp. Atk', ascending = False).head(3)
mejores_fuego_aes = pokemon[fuego].sort_values('Sp. Atk', ascending = False).head(3)
mejores_agua_aes = pokemon[agua].sort_values('Sp. Atk', ascending = False).head(3)
mejores_electrico_aes = pokemon[electrico].sort_values('Sp. Atk', ascending = False).head(3)
mejores_planta_aes = pokemon[planta].sort_values('Sp. Atk', ascending = False).head(3)
mejores_hielo_aes = pokemon[hielo].sort_values('Sp. Atk', ascending = False).head(3)
mejores_lucha_aes = pokemon[lucha].sort_values('Sp. Atk', ascending = False).head(3)
mejores_veneno_aes = pokemon[veneno].sort_values('Sp. Atk', ascending = False).head(3)
mejores_tierra_aes = pokemon[tierra].sort_values('Sp. Atk', ascending = False).head(3)
mejores_psiquico_aes = pokemon[psiquico].sort_values('Sp. Atk', ascending = False).head(3)
mejores_bicho_aes = pokemon[bicho].sort_values('Sp. Atk', ascending = False).head(3)
mejores_roca_aes = pokemon[roca].sort_values('Sp. Atk', ascending = False).head(3)

#dataFrames para los tops defensa especial:
mejores_normal_des = pokemon[normal].sort_values('Sp. Def', ascending = False).head(3)
mejores_fuego_des = pokemon[fuego].sort_values('Sp. Def', ascending = False).head(3)
mejores_agua_des = pokemon[agua].sort_values('Sp. Def', ascending = False).head(3)
mejores_electrico_des = pokemon[electrico].sort_values('Sp. Def', ascending = False).head(3)
mejores_planta_des = pokemon[planta].sort_values('Sp. Def', ascending = False).head(3)
mejores_hielo_des = pokemon[hielo].sort_values('Sp. Def', ascending = False).head(3)
mejores_lucha_des = pokemon[lucha].sort_values('Sp. Def', ascending = False).head(3)
mejores_veneno_des = pokemon[veneno].sort_values('Sp. Def', ascending = False).head(3)
mejores_tierra_des = pokemon[tierra].sort_values('Sp. Def', ascending = False).head(3)
mejores_psiquico_des = pokemon[psiquico].sort_values('Sp. Def', ascending = False).head(3)
mejores_bicho_des = pokemon[bicho].sort_values('Sp. Def', ascending = False).head(3)
mejores_roca_des = pokemon[roca].sort_values('Sp. Def', ascending = False).head(3)

#DataFrames para correlaciones realizamos la función siguiente:
def pearson_r(x, y):
    # Introducimos dos matrices, las cuales mediante una función de numpy muestra la correlación
    corr_mat = np.corrcoef(x, y)

    # Devuelve valor entre [0,1]
    return corr_mat[0, 1]


# mainloop, runs infinitely
mainloop()
