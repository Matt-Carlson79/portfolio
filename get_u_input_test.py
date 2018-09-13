# import Tkinter
from Tkinter import *


# main fuunction
def get_genre():

    # define the genres array
    global genres
    genres = []

    # if user presses [Genre], and if it isn't already in the array, add to array
    def hip_hop():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Hip Hop':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Hip Hop')
        else:
            pass

    def blends_mash_ups():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Blends/Mash-ups':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Blends/Mash-ups')
        else:
            pass

    def electro():
        num = 0
        length = len(genres)
        for n in range(0,length, 1):
            if genres[n] == 'Electro':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Electro')
        else:
            pass

    def pop():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Pop':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Pop')
        else:
            pass

    def alternative():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Alternative':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Alternative')
        else:
            pass

    def club():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Club':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Club')
        else:
            pass

    def country():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Country':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Country')
        else:
            pass

    def dance():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Dance':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Dance')
        else:
            pass

    def electronica():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Electronica':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Electronica')
        else:
            pass

    def house():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'House':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('House')
        else:
            pass

    def intros():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Intros':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Intros')
        else:
            pass

    def latin():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Latin':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Latin')
        else:
            pass

    def randb():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'R&B':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('R&B')
        else:
            pass

    def remix():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Remix':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Remix')
        else:
            pass

    def rock():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Rock':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Rock')
        else:
            pass

    def trap():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Trap':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Trap')
        else:
            pass

    def twerk():
        num = 0
        length = len(genres)
        for n in range(0, length, 1):
            if genres[n] == 'Twerk':
                num += 1
            else:
                pass
        if num == 0:
            genres.append('Twerk')
        else:
            pass

    def stop():
        root.destroy()

        # define pop up
    root = Tk()

    # define check boxes
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
    Button(root, text='Enter', command=stop).grid(row=17, sticky=W)

    # run pop up
    root.mainloop()

    # return array of genres
    return genres

