from Tkinter import *
import pandas as pd


def get_genre():
    global Hip_Hop
    Hip_Hop = False
    global Blends_Mash_ups
    Blends_Mash_ups = False
    global Electro
    Electro = False
    global Pop
    Pop = False
    global Alternative
    Alternative = False
    global Club
    Club = False
    global Country
    Country = False
    global Dance
    Dance = False
    global Electronica
    Electronica = False
    global House
    House = False
    global Intros
    Intros = False
    global Latin
    Latin = False
    global RandB
    RandB = False
    global Remix
    Remix = False
    global Rock
    Rock = False
    global Trap
    Trap = False
    global Twerk
    Twerk = False
    # global x
    # x = 0


    def hip_hop():
        global Hip_Hop
        Hip_Hop = True

    def blends_mash_ups():
        global Blends_Mash_ups
        Blends_Mash_ups = True

    def electro():
        global Electro
        Electro = True

    def pop():
        global Pop
        Pop = True

    def alternative():
        global Alternative
        Alternative = True

    def club():
        global Club
        Club = True

    def country():
        global Country
        Country = True

    def dance():
        global Dance
        Dance = True

    def electronica():
        global Electronica
        Electronica = True

    def house():
        global House
        House = True

    def intros():
        global Intros
        Intros = True


    def latin():
        global Latin
        Latin = True

    def randb():
        global RandB
        RandB = True

    def remix():
        global Remix
        Remix = True

    def rock():
        global Rock
        Rock = True

    def trap():
        global Trap
        Trap = True

    def twerk():
        global Twerk
        Twerk = True





    root = Tk()
    menu = Menu(root)

    Checkbutton(root, text='Hip Hop', command=hip_hop).grid(row=0, sticky=W)
    Checkbutton(root, text='Blends and Mashups', command=blends_mash_ups).grid(row=1, sticky=W)
    Checkbutton(root, text='Electro', command=electro).grid(row=2, sticky=W)
    Checkbutton(root, text='Pop', command=pop).grid(row=3, sticky=W)
    Checkbutton(root, text='Alternative', command=alternative).grid(row=4, sticky=W)
    Checkbutton(root, text='Club', command=club).grid(row=5, sticky=W)
    Checkbutton(root, text='Country', command=country).grid(row=6, sticky=W)
    Checkbutton(root, text='Dance', command=dance).grid(row=7, sticky=W)
    Checkbutton(root, text='Electronica', command=electronica).grid(row=8, sticky=W)
    Checkbutton(root, text='House', command=house).grid(row=9, sticky=W)
    Checkbutton(root, text='Intros', command=intros).grid(row=10, sticky=W)
    Checkbutton(root, text='Latin', command=latin).grid(row=11, sticky=W)
    Checkbutton(root, text='R&B', command=randb).grid(row=12, sticky=W)
    Checkbutton(root, text='Remix', command=remix).grid(row=13, sticky=W)
    Checkbutton(root, text='Rock', command=rock).grid(row=14, sticky=W)
    Checkbutton(root, text='Trap', command=trap).grid(row=15, sticky=W)
    Checkbutton(root, text='Twerk', command=twerk).grid(row=16, sticky=W)

    root.mainloop()

    genres_np = [str(Hip_Hop), str(Blends_Mash_ups), str(Electro), str(Pop), str(Alternative), str(Club), str(Country), str(Dance), str(Electronica), str(House), str(Intros), str(Latin), str(RandB), str(Remix), str(Rock), str(Trap), str(Twerk)]
    genres_df = pd.DataFrame(genres_np, columns=["True/False"])

    return genres_df
