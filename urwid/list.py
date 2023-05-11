import urwid as u

PALETTE = [("normal", "black", "white"),
           ("highlighted", "black", "dark cyan")]

l = "abcdefghijklmnopqrstuvwxyz"

contents = [u.AttrMap(u.Button(x), "normal", "highlighted") for x in l]

walker = u.SimpleFocusListWalker(contents)

listbox = u.ListBox(walker)

box_adapter = u.BoxAdapter(listbox, height=10)

filler = u.Filler(box_adapter, 'top')

loop = u.MainLoop(filler, PALETTE)

loop.run()
