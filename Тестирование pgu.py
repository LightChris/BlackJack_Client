from pgu import gui

app = gui.Desktop()
app.connect(gui.QUIT, app.quit, None)

c = gui.Table(width=200, height=120)


def gg():
    print('hello')


e = gui.Button("hello")
e.connect(gui.CLICK, gg(), '')
c.add(e, 0, 0)

app.run(c)
