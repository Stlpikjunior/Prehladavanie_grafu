import tkinter as tk
import time

root = tk.Tk()
width_can = 1000
height_can = 500
canvas = tk.Canvas(root, width = width_can, height = height_can, bg = 'black')
canvas.pack()


fr_v = open('vrcholy.txt', 'r', encoding ='UTF8')
fr_h = open('hrany.txt', 'r', encoding ='UTF8')

cities = {}
neighbour = {}
spots = {}
lines = []

def city_draw(cities):
    global spots
    for row in fr_v:
        row = row.split(';')
        x = int(row[1])
        y = int(row[2])
        spots[row[0]] = (canvas.create_oval(x-5, y-5, x+5, y+5, fill = 'red'))
        canvas.create_text(x, y-10, text = row[0], font='Arial 8', fill='yellow')
        cities[row[0]] = [x,y]
def hrany_draw(sused):
    global lines
    dic_keys = []
    for row in fr_h:
        row = row.strip().split(';')
        m_1 = row[0]
        m_2 = row[1]
        lines.append(canvas.create_line(cities[row[0]][0],cities[row[0]][1], cities[row[1]][0], cities[row[1]][1], fill = 'red' ))
        if m_1 in dic_keys:
            sused[m_1][m_2] =0
        else:
            sused[m_1] = {m_2:0}
            dic_keys.append(m_1)
        if m_2 in dic_keys:
            sused[m_2][m_1] =0
        else:
            sused[m_2] = {m_1:0}
            dic_keys.append(m_2)






city_draw(cities)
hrany_draw(neighbour)
canvas.update()


visited_d = []
def into_the_deep(mesto):
    visited_d.append(mesto)
    canvas.itemconfig(spots[mesto], fill = 'lime')
    canvas.update()
    time.sleep(0.0000000001)
    for i in neighbour[mesto]:
        if i not in visited_d:
            into_the_deep(i)

vis = []
visited_w = []
def into_the_width(mesto):
    global visited_w, vis
    vis.append(mesto)
    visited_w.append(mesto)
    while len(vis)>0:
        kiki = vis[0]
        for sused in neighbour[kiki]:
            if sused not in visited_w:
                vis.append(sused)
                visited_w.append(sused)
        vis.remove(vis[0])


into_the_width('Bratislava')

into_the_deep('Martin')
print(len(visited_d)) #pocet miest pri prehliadani do hlbky
print(len(visited_w))#poce tmiest pri prehlaidani do sirky - sedia



root.mainloop()





