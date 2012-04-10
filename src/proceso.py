import pygame

next_id = 0

class Proceso(object):

    def __init__(self,tiempo,memoria) :
        self.tiempo = tiempo
        self.memoria = memoria
        self.activo = True
        global next_id
        self.ID = next_id
        next_id += 1


    def cambiar_estado(self) :
        self.activo = not self.activo

    def ejecutar(self) :
        if(self.activo) : self.tiempo -= 1

    def display(self,screen,Rect):
        pygame.draw.rect(screen,(130,130,130),Rect,0)
        fontobject = pygame.font.Font(None,20)

        message1 = "ID : " + str(self.ID)
        message2 = "Tiempo : " + str(self.tiempo)
        message3 = "Memoria : " + str(self.memoria)
        if self.activo : message4 = "Estado : Activo"
        else : message4 = "Estado : Pausado"

        screen.blit(fontobject.render(message1,1,(255,255,255)),(Rect[0]+5,Rect[1]+5,Rect[2],Rect[3]))
        screen.blit(fontobject.render(message2,1,(255,255,255)),(Rect[0]+5,Rect[1]+20,Rect[2],Rect[3]))
        screen.blit(fontobject.render(message3,1,(255,255,255)),(Rect[0]+5,Rect[1]+35,Rect[2],Rect[3]))
        screen.blit(fontobject.render(message4,1,(255,255,255)),(Rect[0]+5,Rect[1]+50,Rect[2],Rect[3]))

def mostrar_memoria(screen, memoria) :
    fontobject = pygame.font.Font(None,18)
    pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width()) - 202,
                    (screen.get_height()/2) - 12,
                    168,24), 0)
    pygame.draw.rect(screen, (255,255,255),
                  ((screen.get_width()) - 202,
                    (screen.get_height() / 2) - 12,
                    168,24), 1)

    message = "Memoria disponible : " + str(memoria)

    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width()) - 200, (screen.get_height() / 2) - 10))
    pygame.display.flip()