title: Spell Checker
date: 2013-08-03
This plugin adds inline spell checking for zim. It has a preference setting to determine the language used for spell checking. If this is not set, the system default is used.

**Dependencies:** This plugin requires the "gtkspell" library to be installed as well as the Python language bindings for this library. 


* On Ubuntu or Debian systems installing the package "python-gtkspell" (or "python-gnome2-extras" on older releases) will meet these dependencies.
* On Fedora systems, installing the package "gnome-python2-gtkspell" will meet these dependencies.


Options
-------
The options **Default Language** specifies the language to use for the spell checking. Languages should be specified as language codes, e.g. for Dutch you would set "nl" or "nl_NL". If the option is not set, the system default will be used.

Dictionaries
------------
The gtkspell library does not always come with all dictionaries installed. If no dictionary is found for your language zim will give an error when loading this plugin. For most Linux flavors the  "aspell" dictionaries are used, so for example to install the English language dictionaries install the "aspell-en" package. If you can not find these packages, please refer to the documentation for your specific Linux flavor.

