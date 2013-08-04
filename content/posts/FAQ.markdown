title: FAQ_test
date: 2013-08-03
lang: zh
author: jim
category: faq
tags: zim faq
Tags: 测试Tags
# FAQ_test_title

Mail [me](mailto:jaap.karssenberg@gmail.com) if you have questions that you would like to see answered below.

How do I create a new page?
---------------------------
You can just link non-existing pages. If you follow such a link the page will be created automatically when needed.

How do you close these "tabs" ?
-------------------------------
Uhm, if you mean the buttons above your page, technically that are not tabs but a path bar keeping track of your history or recent pages. The buttons in this bar map to pages in your browse history, not to open pages or something like that. You can not "close" something that is in your history. To change the style of this bar, or hide it completely, go to the "*View"* -> "*Pathbar*" menu item.

How do I organize my pages in a tree structure?
-----------------------------------------------
You can use "namespaces" to organize your pages. A "namespace" is similar to a directory for files, it is a named group of pages. Namespaces are separated by the "``:``" character in the page name. Thus if you link to "``foo:bar``" you will link to the page called "bar" in the namespace "foo". Just link a non-existing page and follow the link to create it. See [Pages](./Help/Pages.markdown) for more information.

Why are some pages in the index grayed out?
-------------------------------------------
These are pages that are linked by other pages but do not (yet) contain text. You can edit them to make them regular pages or check the pages linking them.

Why do some pages not disappear from the index after deleting them?
-------------------------------------------------------------------
The index keeps pages that are linked by other pages even if you delete them. To completely remove them you also need change any page linking them.

I would like zim to hide in the system tray.
--------------------------------------------
There is a [Tray Icon plugin](./Plugins/Tray_Icon.markdown) which can be enabled from the Preferences dialog.

I would like to start zim hidden in the system tray.
----------------------------------------------------
You can call the [Tray Icon plugin](./Plugins/Tray_Icon.markdown) with the command "``zim --plugin trayicon``"

Can I make zim appear with a global keybinding?
-----------------------------------------------
By default zim will  only run a single instance of each notebook. Trying to open the same notebook again will just pop the corresponding window to the foreground. So you can set a default notebook (see [Notebooks](./Help/Notebooks.markdown)) and just make a global key binding run the command "``zim``". 

How do I publish content from zim to my webpage?
------------------------------------------------
See [Usage:Publishing](./Usage/Publishing.markdown) for some tips

Can I change the colors used for links, underline etc. ?
--------------------------------------------------------
Yes. Copy "``/usr/share/zim/style.conf``" to "``~/.config/zim/``" and edit as you see fit. See the [Config Files](./Help/Config_Files.markdown) page for the syntax of this file.

Can I have encrypted notebooks?
-------------------------------
Zim notebooks do not support encryption or password protection natively. However you can use for example [encfs](http://www.arg0.net/encfs) to encrypt your notebooks.

Can I have full calendaring in zim?
-----------------------------------
Well, if you really want to, you can use zim as your agenda. However, the Calendar feature is more intended to keep various kinds of journals or logbooks. I'm very hesitant to add calendaring features because these are usually tied to email applications. I admit that it would be really cool to link notes, emails and appointments, but I have no plans to extend zim to become an email reader.

How do I change the font size of the side pane
----------------------------------------------
You can change this by modifying the ``gtkrc`` file, see [Config Files](./Help/Config_Files.markdown) for details.

Does it run on Windows?
-----------------------
Yes it does. See the download page on the website for more notes on installing on the win32 platform.

Does it run on OS X?
--------------------
Yes it does. You can install the dependencies using [Mac Ports](http://www.macports.org/).

I want to move/backup/synchronize a zim notebook. Which files do I need to take care of?
----------------------------------------------------------------------------------------
The visible files in the notebook folder contain all data of notes and [attachments](./Help/Attachments.markdown).

What is the hidden .zim folder in my notebook folder?
-----------------------------------------------------
The hidden .zim folder contains only caches and GUI state. It doesn't contain any information that can not be recreated on the fly.

How can I synchronize a zim notebook?
-------------------------------------
By synchronizing all visible files in the notebook. E.g. by putting the zim notbook in a dropbox share.

Can multiple people collaborate using a zim notebook ?
------------------------------------------------------
Zim is written as a "single user" program, so it is not intended for multiple people using the same notebook. However it can be used with version control like Bazaar, Git or Mercurial. This way multiple users can work on the same notebook and merge their changes. See the [Version Control plugin](./Plugins/Version_Control.markdown).

I have a useful trick or tip. How can I share it with other users?
------------------------------------------------------------------
You can have a look at the [zim documentation wiki](http://www.zim-wiki.org/wiki/doku.php). It has a section dedicated to [tricks and tips](http://www.zim-wiki.org/wiki/doku.php?id=tips_and_tricks). Or write a mail to the mailing list, see the [team page](https://launchpad.net/~zim-wiki) on launchpad


