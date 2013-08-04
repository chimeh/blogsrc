title: Exporting
date: 2013-08-03
Zim will be able to export content to various formats. At the moment exporting to [HTML](./Export/HTML.markdown) and [LaTeX](./Export/LaTeX.markdown) is supported, as well as the Markdown and RST text formats.

Export dialog
-------------
To open op the export dialog in zim use the "*File*->*Export*" menu item. This dialog asks for a number of input fields before you can start exporting.

### Step1: Select the pages to export
The option **Complete Notebook** will export all pages in the current notebook. 

The option **Single page** allows to select you a single page to export.

### Step 2: Select the export format
The **Format** allows the choice of the output format.

The **Template** field asks you to select a template file (see below). When you select "``Other...``" in the combo box you can browse for another file in the input field below the combo box.

If your notebook has a Document Root (see [Properties](./Properties.markdown))  you can select what to do with links to files under that document root. Either **Link files under document root with full file path**, which means files will be linked by their absolute file path, or **Map document root to URL**, which will result in links with the given URL as prefix. This can be useful when you [publish](../Usage/Publishing.markdown) pages as part of a larger website.

### Step 3: Select the output file or folder
Here you can select the **output folder** (if you are exporting multiple pages) or the **output file** (if you export a single page).

If you specify an **Index page** a page will be generated that contains a list with links to all pages that were exported. This can e.g. be used as a site map.


Attachments
-----------
Files and images that live inside the notebook directory ([attachments](./Attachments.markdown), equations etc.) will always be copied to the new output directory when you export a notebook.

Templates
---------
The export code only produces the tags that represent the content of the page. [Templates](./Templates.markdown) are used to create complete output. A few standard templates are packaged  with zim, see the pages for the output formats for a list and descriptions. You can also make your own.

Exporting from the commandline
------------------------------
Try something like:

	$ zim --export --output=./html \
	  --format=html --template=./foo.html ~/Notes

See "``zim --help``" for all options.


