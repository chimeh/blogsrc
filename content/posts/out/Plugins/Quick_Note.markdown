title: Quick Note
date: 2013-08-03
The "Quick Note" plugin offers a dialog for inserting quick notes into a notebook. It can be invoked from the commandline and can therefore easily be bound to keyboard shortcuts or used in scripts.

**Dependencies:** This plugin has no additional dependencies.

**Commandline: **``zim`` --plugin quicknote [OPTIONS]

**Options:**

* notebook=URI    Select the notebook in the dialog
* namespace=STRING    Fill in the namespace in the dialog
* basename=STRING    Fill in the page name in the dialog
* text=TEXT    Provide the text directly
* input=stdin    Provide the text on stdin
* input=clipboard    Take the text from the clipboard
* encoding=url	url encoded utf-8 text
* encoding=base64	base64 encoded utf-8 text
* option:url=STRING  Set template parameter


