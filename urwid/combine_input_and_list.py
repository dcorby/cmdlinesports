import urwid

# placeholder
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'),]
placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.widget = urwid.AttrMap(placeholder, 'bg')
loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

# pile
pile = loop.widget.base_widget

# text
def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

txt = urwid.Text(u"Hello World")
#fill = urwid.Filler(txt, 'top')
pile.contents.append((txt, pile.options()))

# list
PALETTE = [("normal", "black", "white"),
           ("highlighted", "black", "dark cyan")]
l = "abcdefghijklmnopqrstuvwxyz"
contents = [urwid.AttrMap(urwid.Button(x), "normal", "highlighted") for x in l]
walker = urwid.SimpleFocusListWalker(contents)
listbox = urwid.ListBox(walker)
box_adapter = urwid.BoxAdapter(listbox, height=10)
#fill = urwid.Filler(box_adapter, 'bottom')
#loop = urwid.MainLoop(box_adapter, PALETTE)
pile.contents.append((box_adapter, pile.options()))

loop.run()

