from proceso import Proceso
import pygame
from pygame.locals import *
from sys import exit
from button import *
from proceso import *
import inputbox

__author__="marioyc"
__date__ ="$Jun 6, 201 4:50:20 PM$"

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sistemas Operativos - Simulador de Procesos")

    # Informacion del Fondo
    background_image_filename = 'SO.png'
    screen = pygame.display.set_mode((1024,720),0,32)
    background = pygame.image.load(background_image_filename).convert()

    # Informacion del mouse
    pygame.mouse.set_visible(False)
    mouse_image = pygame.image.load("mousecursor.png").convert_alpha()

    # Informacion de los botones
    x = 100
    y = 150
    button_height = 200

    buttons = {}
    buttons["nuevo"]    = Button("nuevo.png",(x,y))
    buttons["pausar/reanudar"]   = Button("pausa.png",(x,y+button_height*1))
    buttons["eliminar"] = Button("eliminar.png",(x,y+button_height*2))

    #Informacion de los procesos
    MAX_PROC = 30
    cola_procesos = []

    #Memoria del sistema
    screen.blit(background, (0,0))
    TOT_MEM = inputbox.ask(screen, "Memoria Total")
    MEM_LIBRE = TOT_MEM

    while True :
        button_pressed = None

        for event in pygame.event.get() :
            if event.type == QUIT : exit()
            elif event.type == MOUSEBUTTONDOWN :
                # Find the pressed button
                for button_name, button in buttons.iteritems() :
                    if button.is_over(event.pos):
                        print button_name, "pressed"
                        button_pressed = button_name
                        break

        if button_pressed is not None :
            if button_pressed == "nuevo" and len(cola_procesos)<36 :
                tiempo = inputbox.ask(screen, "Tiempo del proceso")
                memoria = inputbox.ask(screen, "Memoria del proceso")
                if(memoria<=MEM_LIBRE) :
                    cola_procesos.append(Proceso(tiempo,memoria))
                    MEM_LIBRE -= memoria
            
            elif button_pressed == "pausar/reanudar" :
                ID = inputbox.ask(screen, "ID del proceso que desea pausar/reanudar")
                found = False
                ind = 0;

                for p in cola_procesos :
                    if p.ID == ID :
                        found = True
                        break
                    else : ind += 1
                
                if found : cola_procesos[ind].activo = not cola_procesos[ind].activo

            elif button_pressed == "eliminar" :
                ID = inputbox.ask(screen, "ID del proceso que desea eliminar")
                found = False
                ind = 0;

                for p in cola_procesos :
                    if p.ID == ID :
                        found = True
                        break
                    else : ind += 1

                if found :
                    MEM_LIBRE += cola_procesos[ind].memoria
                    cola_procesos.pop(ind)

        #Los procesos activos avanzan
        eliminar = []

        for i in xrange(len(cola_procesos)) :
            p = cola_procesos[i]

            if p.activo :
                p.tiempo -= 1
                if p.tiempo==0 :
                    MEM_LIBRE += p.memoria
                    eliminar.append(i)

        for i in xrange(len(eliminar)) :
            cola_procesos.pop(eliminar[i])

        #Actualizar pantalla
        screen.blit(background, (0,0))

        for button in buttons.values():
            button.render(screen)


        for k in xrange(0,len(cola_procesos)) :
            if   k<9*1 : Rect = ((screen.get_width()/2)-300,20+75*k,130,70)
            elif k<9*2 : Rect = ((screen.get_width()/2)-150,20+75*(k-9*1),130,70)
            elif k<9*3 : Rect = ((screen.get_width()/2),20+75*(k-9*2),130,70)
            elif k<9*4 : Rect = ((screen.get_width()/2)+150,20+75*(k-9*3),130,70)
            
            cola_procesos[k].display(screen, Rect)

        #Mostrar memoria disponible
        mostrar_memoria(screen,MEM_LIBRE)

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(mouse_image, mouse_pos)
        
        pygame.display.update()
        
        t = 0
        while t<=500000 : t += 1
