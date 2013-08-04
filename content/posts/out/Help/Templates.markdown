title: Templates
date: 2013-08-03
[Attachments](./Attachments.markdown)

Template Editor Dialog
----------------------

The Template Editor Dialog can be accessed with the menu item "*Edit*" -> "*Templates*". It will show a list of templates that are available, and allows you to view and edit them.

Templates can either be system defaults, or custom templates in your home folder. When you edit them, a copy is made of the default to your home folder, and this copy is than edited. The remove function again deletes this custom version, but does not touch the default template.

**Note:** if you try to edit for example a HTML template, and it opens in the web browser instead of in your default text editor, the cause is most likely that you did not explicitly configure a text editor in the preferences. Go to the [Preferences Dialog](./Preferences.markdown) and specify your text editor.

Templates for export
--------------------

For a list of templates for exporting see [Export](./Export.markdown) and subpages.

Template options
----------------

Templates can also set template options that influence the generated output, by setting key-value pairs like in the example below. A list of available template options for a output format can be found at [Export](./Export.markdown) and subpages.

Special templates
-----------------

**wiki/Default.txt**
This template is used to initialize new pages. The default contains a header with the page name and the date at which the page was created.

**wiki/Journal.txt**
This template is used to initialize new pages in the Journal namespace.

Customizing
-----------

Templates are located in ``/usr/share/zim/templates/`` and ``~/.local/share/zim/templates`` by default. You can add templates you use more often there. To modify a template copy it to the ``~/.local/...`` directory and edit it.

Template syntax:

	[% var %]	# interpolates a variable
	[%- var %]	# + strip line break before the expression
	[% var -%]	# + strip line break after the expression
	[%- var -%]	# + strip line breaks on both sides
	
	[% IF expr %] ... [% END %]	# conditionals
	
	[% IF expr %]
		...
	[% ELSIF expr %]
		...
	[% ELSE %]
		...
	[% END %]
	
	[% FOREACH name = var ]		# loop
	... [% name %] ...
	[% END %]
	
	[% strftime("%c") %]		# current time stamp
	[% strftime("%c", var) %]	# date from variable
	
	
	[% options.option_name = value %] # set the template option option_name to value
	
	[% page.properties["Creation-Date"] %] # access dict


For the ``IF`` and ``ELIF`` statements the expression can be either just a variable, in which case it is evaluated boolean, or an equality expression with "==". For example "``[% IF page.name == 'foo' %]``" is understood. More complex expressions are not supported.

Available variables:

	zim.version		# version of zim
	notebook.name		# name of the notebook
	notebook.interwiki	# interwiki key of the notebook if any
	
	page.name		# complete page name
	page.namespace		# namespace
	page.basename		# last part of the page name
	page.properties		# dict with page properties
	page.title		# first heading in the page or the basename
	page.heading		# first heading in the page
	page.body		# content of the page without the leading heading
	page.content	# content of the page including the leading heading
	page.has_links	# True if the page has links to other pages
	page.links		# list of page objects for pages linked in this page
	page.has_backlinks	# True if the page is linked by other pages
	page.backlinks		# list of page objects for pages linking to this page
	page.has_attachments	# True if the page has attachments
	page.attachments	# list of file objects for attachments
	
	# These special pages have the same properties as the 'page' object
	pages.index		# the index page generated when exporting
	pages.home		# the home page
	pages.next		# the next page in the index (if any)
	pages.previous		# the previous page in the index (if any)
	
	options			# dict where format specific options can be set


File objects returned by page.attachments have the following attributes:

	file.path		# (relative) path as a string
	file.basename	# file basename
	file.mtime		# file mtime, to be used with strftime()
	file.size		# file size as human readable string


Functions available:

``url(link)``
Turns a zim link or file object into an URL

``resource(filename)``
Returns an URL for a template resource (see below)

``strftime(template, date)``
Format a date, see standard library for codes
		
strfcal(template, date)
Format a week number, accepts:
		
%w for day of week according to locale
%W for weeknumber according to locale
%Y for the year to which the week belongs

pageindex``(namespace, collapse, ignore_empty)``
Creates a page index of a given namespace or the whole notebook

``namespace``: the starting root - defaults to the top level (":")
``collapse:`` if ``TRUE`` only branches related to the current page are visible*, * if ``FALSE`` all branches are visible - defaults to TRUE
``ignore_empty:`` if ``TRUE`` empty pages are ignored — defaults to TRUE.

*Example*:	``menu(page.namespace,  TRUE, FALSE)``


See also the [Journal Plugin](../Plugins/Journal.markdown) for some properties available for journal pages

### Template Resources
To add ad



ional files to the template, create a folder of the same name as the template. Any files in the folder (like style sheets, images, javascript files, etc.) will be copied along when this template is used to export data in zim. There is a function "``resource(filename)``" to refer to these files in the template.

Zim always includes some images when exporting for the checkboxes used in checkbox lists. To customize these there should be template resources named "``checked-box.png``", "``unchecked-box.png``" and "``xchecked-box.png``" in this folder.

For the web interface the resources can also contain a "``favicon.ico``" to serve as the favicon of the website.


