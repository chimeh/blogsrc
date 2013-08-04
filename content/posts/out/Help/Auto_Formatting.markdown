title: Auto Formatting
date: 2013-08-03
Auto-formatting means that zim parses text while you type. Be aware that the syntax for auto-formatting isn't the same as the [wiki syntax](./Wiki_Syntax.markdown) for the source formatting (the wiki format as it is saved to the files). If you typed in source syntax and you want to have it rendered you should reload the page (press ^R).

If auto-formatting does something you didn't intend you can reverse it by pressing ``<ctrl>Z``.

Headings
--------
Typing:

	== Heading 1 <ENTER>

gives you a heading 1 and typing:

	=== Heading 2<ENTER>

gives you a heading 2. But in the corresponding text file these headings are marked as follows:

	====== Heading 1 ======
	===== Heading 2 =====


Links
-----
When you type a word in "CamelCase" it will be considered a link. Once again this auto-formatting is done by the editor, your source format does not have to support CamelCase.

This feature can be turned off in the [Preferences](./Preferences.markdown).

Also when you type a internet url like <http://perl.org> it will automatically be identified as a link.

Bullets and Checkboxes
----------------------
Another example of auto-formatting is that "* " at the beginning of a line gets converted to a bullet automatically. Typing either "[] ", "[*] ", "[x] " or "() ", "(*) ", "(x) " will give your different kinds of [Check Boxes](./Check_Boxes.markdown).

