title: Config Files
date: 2013-08-03
This page documents the various config files used. 
Also see [preferences](./Preferences.markdown) for documentation of the preferences dialog.

Paths
-----

### Freedesktop (Linux etc.)
Zim uses the scheme as laid down in the "XDG Base Directory Specification" as published by [freedesktop.org](http://freedesktop.org). The default paths are:

	XDG_CONFIG_HOME = HOME/.config/
	XDG_DATA_HOME   = HOME/.local/share/
	XDG_DATA_DIRS   = /usr/local/share/:/usr/share/

These can be overloaded with the coresponding environment variables.

When zim writes config files it always uses ``XDG_CONFIG_HOME``. Data files are read only and are searched for in ``XDG_DATA_HOME`` and ``XDG_DATA_DIRS``. The installation defaults for config files are also installed in ``XDG_DATA_DIRS``, but these are copied on first use to ``XDG_CONFIG_HOME``.

### Windows
On Windows the default paths are:

	XDG_CONFIG_HOME = APPDATA/zim/config/
	XDG_DATA_HOME   = 
``APPDATA/zim/data/``

Where ``APPDATA`` is the default Windows path to store application data, typically a path like "``USERPROFILE\Application Data``".

When there is no ``HOME`` environment parameter defined on Windows either the ``USERPROFILE`` parameter or ``HOMEDRIVE`` + ``HOMEPATH`` are used. Make sure to define ``HOME`` or ``USERPROFILE`` including a drive letter.



Global Config Files
-------------------

These config files determine various aspects of how zim behaves. They are global in the sense that they are not specific for one notebook.

### Main config file
The default config file is ``XDG_CONFIG_HOME/zim/preferences.conf``.

The config file is written automatically when you close zim. So if you want to change it manually you need to close all instances of zim first.

There is a hidden option here called "``autosave_timeout``" which gives the interval for autosaving in seconds, default is 10.

### Interwiki URL list
The file ``XDG_DATA/zim/urls.list`` gives a list of urls which are used for the [interwiki](./Links.markdown) function. All files in the XDG_DATA path are read when looking for an url, so you can use XDG_DATA_HOME to overload the installation defaults.

The format consist of one url per line, each line giving the key (which is the interwiki name), followed by whitespace, followed by the actual url. The url can conatin place holders "``{NAME}``" or "{URL}", the first will be replaced by the name of the interwiki page, the second by this name in url encoding. If no placeholder is found in the url the url encoded name is appended to the url.

Note that if you want interwiki page to include url syntax like a "#" to link to anchors in the target page, you should write your URLs with "``{NAME}``".

### Date format list
The file ``XDG_DATA/zim/dates.list`` gives a list of strftime formats, one on each line, to be used to populate the "Insert Date and Time" dialog. The first instance of this file that is found in the XDG_DATA path is used. 

See [this link](http://docs.python.org/library/time.html%23time.strftime) for documentation of the strftime formatting.

### GUI style config file
Zim has certain defaults on how to display styles. For example it displays links as blue text without underline. To change this style copy "``/usr/share/zim/style.conf``" to "``~/.config/zim/``" and edit it. Each style has it's own section which starts with the style name between square brackets and contains key value pairs for the various display properties.

**NOTE: **The display styles for the GUI are not used when exporting to HTML. If you want your HTML to show certain custom styles you should write a HTML [template](./Templates.markdown) with a CSS stylesheet.

Example:

	[TextView]
	tabs = 40
	font = Sans 10
	
	[Tag bold]
	weight = PANGO_WEIGHT_BOLD
	
	[Tag italic]
	style = italic

Known properties for TextView:

* **indent**: *integer*	- indenting step size in pixels
* **tabs**: *integer*	- tab size in pizels
* **linespacing**: *integer*	- line spacing in pixels
* **justify**: ``JUSTIFY_LEFT``, ``JUSTIFY_FILL``, ...
* **font**: *string*


Known style tags:

* **h1**, **h2**, **h3**, **h4**, **h5**, **h6**: various headings
* **emphasis**: emphasized or italic text
* **strong**: strong or bold text
* **mark**: highlighted or underlined text
* **strike**: strike-through text
* **code**: inline verbatim text
* **pre**: verbatim text as paragraph
* **sub**: subscript text
* **sup**: superscript text
* **link**: hyperlink text
* **indent**: indented lines
* **bullet-list**: lines in a bullet list
* **numbered-list**: lines in a numbered list
* **unchecked-checkbox**: lines with an open checkbox
* **checked-checkbox**: lines with a "v-checked" checkbox
* **xchecked-checkbox**: lines with a "x-checked" checkbox


Known properties for Tags:

* **family**: ``monospace``, ``sans``, ...
* **foreground**: ``grey``, ``blue``, ``#cccccc``, etc.
* **background**: ``yellow``, ``#cccccc``, etc.
* **weight**: ``PANGO_WEIGHT_BOLD``, ...
* **scale**: *integer*
* **style**: ``italic``, ...
* **underline**: ``single``, ...
* **striketrough**: ``true``, ``false``
* **wrap**_**mode**: "``none"``, ...
* **indent**: *integer*
* **linespacing**: *integer*


### GtkRC file
Gtk+ has it's own config file that allows you to customize how things look. This is the gtkrc file and it is typically saved as ``~/.gtkrc-2.0`` in the home directory. Some widgets have a name so you can set specific options for those widgets. Widgets that have a name in zim are:


* The textview showing the page: zim-pageview
* The treeview showing the page index: zim-pageindex


You can for example set the font used in the index by adding this to your gtkrc file:

	style "zim-pageindex-style"
	{
		font_name = "Sans 8"
	}
	widget "*.zim-pageindex" style "zim-pageindex-style"

or this example to make the treeview a bit more compact:

	style "gtkcompact" 
	{
		GtkTreeView::vertical-separator=0
		GtkTreeView::horizontal-separator=0
		GtkTreeView::expander-size=6
		GtkTreeView::fixed-height-mode=TRUE
		GtkWidget::focus_padding=0
	}
	class "GtkWidget" style "gtkcompact"

To change the base colors of the pageview widget use something like:

	style "mycolors" 
	{
		base: "#ccc"
		text: "#fff"
	}
	widget "*.zim-pageview" style "mycolors"


Check the internet for more examples.


Notebook config file
--------------------

There is a notebook specific config files called "``notebook.zim``" which should be in the notebook folder. This file contains a section "``[Notebook]``" which contains the properties that can be set in the [properties dialog](./Properties.markdown).

There is one hidden property, called "``end_of_line``" which determines the end-of-line convention for files written by zim within the scope of this notebook. The value can be either "``dos``" or "``unix``". For newly created notebooks this value is set depending on the platform on which zim is running. Main purpose of this property is to ensure that a notebook which is shared between e.g. linux and windows machines does not change the full file on every write. When desired the property can be changed manually, which will affect all pages edited after the change.

A second hidden option is "``disable_trash``" which defaults to ``False``. If enabled this will cause zim to avoid using the system trash for this notebook, see the section about deleting in [Pages](./Pages.markdown).

