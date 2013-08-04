title: Key Bindings
date: 2013-08-03
See also [Menu Items](./Menu_Items.markdown).

### General

	F9		Toggle visibility of sidepane(s)
	<Ctrl>F9	Show all sidepanes
	<Ctrl><Space>	Toggle focus between index and buffer
	    		opens side pane if index is invisible
			(optional see preferences)
	<Ctrl><Tab>	Focus next inteface element (gtk default)
	<Ctrl><Shift><Tab> Focus previous interface element (gtk default)
	Esc		Close sidepane (when focus is on a side pane)


	<Alt><Home>	Go to the home page
	<Alt><Left>	Go one page back in history
	<Alt><Right>	Go one page forward in history
	<Alt><Up>	Go one page up in the namespace
	<Alt><Down>	Go one page down in the namespace
			(The actual page is chosen by the history)
	<Alt><PgUp>	Go to the previous page in the index
	<Alt><PgDown>	Go to the next page in the index
	<Alt>D		Go to today's page


	<Ctrl>Q		Quit the application
	<Ctrl>w		Close window


	<Ctrl>F		Find in the current page
	<Ctrl>G		Find next
	<Shift><Ctrl>G	Find previous
	<Shift><Ctrl>F  Search in all pages
	<Ctrl>H		Find and Replace


	<Ctrl>S		Save page        (forced)
	<Shift><Ctrl>S	Save version...
	<Ctrl>R		Reload page      (saves first)
	<Ctrl>J		Jump to page...  (either an existing or a new page)


	<Ctrl>L		Link selected text
			Follow selected text as link when read-only
	<Shift><Ctrl>L	Copy a link to the current page to the clipboard
			In the side pane copies a link to the selected page
			(Paste this link in a page with <Ctrl>V)
	<Ctrl>E		Show the "edit link" dialog
	<Ctrl>D		Inserts timestamp


	<Ctrl>1..<Ctrl>5 Make selected text a heading
	<Ctrl>9		Make selected text normal
	<Ctrl>B		Make selected text strong
	<Ctrl>I		Make selected text italic
	<Ctrl>U		Make selected text underline     (renders highlighted)
	<Ctrl>K		Make selected text strike-trough
	<Ctrl>T		Make selected text verbatim text (monospace font)


	<Ctrl>Z		Undo
	<Shift><Ctrl>Z	Redo
	<Ctrl>Y		Redo


	<Shift><Ctrl>D	Show the calendar dialog


	F1		Show the manual
	F2		Rename current page
	F3		Find next	(same as <Ctrl>G)
	<Shift>F3	Find previous	(same as <Ctrl>G)
	F5		Reload page	(same as <Ctrl>R)
	F12		Toggle checkbox item to 'OK'
	<Shift>F12	Toggle checkbox item to 'NOK'

Also all the usual keybindings apply for the gtk text edit widget, thus bindings like
``<Ctrl>C``, ``<Ctrl>X``, ``<Ctrl>V``, ``<Ctrl>A`` etc. work as expected.

### Side pane tree
The following key bindings works when the tree in the side pane is focussed:

	<Ctrl>L		Insert a link to the selected page
	<Shift><Ctrl>L	Copy the selected page to clipboard
	<Ctrl>C		Copy the selected page to clipboard
	<Ctrl>F		Search in the page list as shown
	*		Expand all
	\		Collapse all


### Text selections
For selected text the following keybindings are added:

	*		Toggle bullets for selected text
	>		Toggle email-style quoting for selected text
	<Tab>		Indent selected text
	<Shift><Tab>	Un-indents selected text
	<Backspace>	Un-indents selected text


Changing accelerators
---------------------
Gtk+ implements a feature that allows you to change accelerators (keybindings for menu items) interactively. To use this feature you need to either enable this setting in the settings manager of you desktop environment or add the line:

	gtk-can-change-accels = 1

to ``~/.gtkrc-2.0`` . Zim will remember any changes. If you ever want to reset to the default bindings just remove the "accelmap" file from ``~/.config/zim/``.

Emacs mode
----------
Zim does not support an emacs mode specifically, however Gtk+ does. When you set this option all Gtk+ programs will use emacs key bindings for text inputs. To use this feature you need to enable this setting in the settings manager of your desktop environment or add the line:

	gtk-key-theme-name = "Emacs"

to ``~/.gtkrc-2.0`` . Of course if you use this you will need to customize a number of accelerators as well which conflict with the emacs keybindings. See the section above.

