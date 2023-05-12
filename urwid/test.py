import urwid

# Pile - A pile of widgets stacked vertically from top to bottom

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

# text
pile = urwid.Pile([urwid.Text('heey'),urwid.Text("There")])

# list
contents = [urwid.AttrMap(urwid.Button(x), "normal", "highlighted") for x in ["foo", "bar", "baz"]]
walker = urwid.SimpleFocusListWalker(contents)
listbox = urwid.ListBox(walker)
box_adapter = urwid.BoxAdapter(listbox, height=3)
pile.contents.append((box_adapter, pile.options()))

body = urwid.Frame(body=urwid.Filler(pile, valign="top"))
loop = urwid.MainLoop(body, unhandled_input=exit_on_q)

print(pile.focus_position)
pile.focus_position = 2
print(pile.focus_position)
print(pile.contents)

loop.run()

