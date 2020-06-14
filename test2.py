from tkinter import *                                                      #1

                                                                           #2

fen = Tk()                                                                 #3

fen.title("Fenêtre composée à l'aide de frames")                           #4

fen.geometry("300x300")                                                    #5

                                                                           #6

f1 = Frame(fen, bg = '#80c0c0')                                            #7

f1.pack(side =LEFT, padx =5)                                               #8

                                                                           #9

fint = [0]*6                                                               #10

for (n, col, rel, txt) in [(0, 'grey50', RAISED, 'Relief sortant'),        #11

                           (1, 'grey60', SUNKEN, 'Relief rentrant'),       #12

                           (2, 'grey70', FLAT, 'Pas de relief'),           #13

                           (3, 'grey80', RIDGE, 'Crête'),                  #14

                           (4, 'grey90', GROOVE, 'Sillon'),                #15

                           (5, 'grey100', SOLID, 'Bordure')]:              #16

    fint[n] = Frame(f1, bd =2, relief =rel)                                #17

    e = Label(fint[n], text =txt, width =15, bg =col)                      #18

    e.pack(side =LEFT, padx =5, pady =5)                                   #19

    fint[n].pack(side =TOP, padx =10, pady =5)                             #20

                                                                           #21

f2 = Frame(fen, bg ='#d0d0b0', bd =2, relief =GROOVE)                      #22

f2.pack(side =RIGHT, padx =5)                                              #23

                                                                           #24

can = Canvas(f2, width =80, height =80, bg ='white', bd =2, relief =SOLID) #25

can.pack(padx =15, pady =15)                                               #26

bou =Button(f2, text='Bouton')                                             #27

bou.pack()                                                                 #28

                                                                           #29

fen.mainloop() 