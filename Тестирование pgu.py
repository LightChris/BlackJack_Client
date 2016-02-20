from pgu import gui

app = gui.Desktop()
app.connect(gui.QUIT, app.quit, None)

c = gui.Table(width=200, height=120)

e = gui.Button("Quit")
e.connect(gui.CLICK, app.quit, None)
c.add(e, 0, 0)

app.run(c)