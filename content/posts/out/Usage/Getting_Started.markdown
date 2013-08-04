title: Getting started
date: 2013-08-03
When you run Zim for the first time, the first thing you need to do is to add a [notebook](../Help/Notebooks.markdown). This means that you need to tell Zim in which directory you want to store your pages.

When you open a newly created notebook you get an empty page titled "**Home**". You can just start typing on this page. Do not worry about saving, this is done automatically.

Now you can use the items in the *Format* menu or their corresponding [keybindings](../Help/Key_Bindings.markdown) to make text **bold** or *italic*. A special format type is "Link" which highlights a word as a hyperlink. Try selecting a word in your text and press ``<ctrl>L`` this will make the word a link. Now when you click on this word (or press ``<Enter>`` while the cursor is on the link) you go to a new page. You will notice that this new page is generated on the fly.

Once you have several pages you can navigate them like you would in a browser. There are buttons and keybindings for going Back, Forward or Home.

It is also possible to order your pages into namespaces. The namespace separator is the colon ":" character. So when you use this character as part of a page name the name will be split at that point. The tree in the side pane will show a hierarchy of namespaces when you use this.

After you have edited some pages you might want to have a look at how they are saved. Use your file browser to open the notebook directory. As you will see there is a simple text file corresponding to each page. These text files are formatted with [wiki format](../Help/Wiki_Syntax.markdown) to preserve markup. This "raw" markup can also be used in Zim, try entering some raw syntax in your page and press ``<ctrl>R`` to reload the page; your formatting codes are now parsed into markup. Apart from the raw wiki syntax there are also a number of formats that are parsed as you type them, this is called [autoformatting](../Help/Auto_Formatting.markdown) and can be very useful to speed up your typing.

Some tips
---------

Zim has a lot of little features to make often performed routines quicker. Some of these are highlighted below. Just try out some ways to work with Zim and see what suits you.

#### Use the "Jump to.." dialog
If you want to start a new page without linking to it you can popup the *Jump to..* dialog using "``<Ctrl>J``" and type the name of the page you want. The page you jump to does not have to exist, if it doesn't it will be created on the fly when you start editing. This routine can be used to make notes of thought unrelated to what you are working on when they popup in your mind. You can use "``<Alt>Left``" or the "Back" button to return to what you were doing.

#### Use CamelCase
CamelCase is a way of to mark page names that is often used in wikis. The idea is that a page name always is a contraction of two words both starting with a capital (like for example the word "CamelCase"). The wiki recognizes these words and highlights them as links. Zim formats these CamelCase words as links on the fly when you type them. Thus you do not have to explicitly create links as long as you choose your page names to match this format.

If you do not like CamelCase it can be turned off in the preferences menu (*Edit*->*Preferences*) under the "Editing" tab.

#### Use backlinks
You can use [backlinks](../Help/Links.markdown) to trace all pages that link to a certain page. This can be used to create wiki-style categories. Since link relations are stored in a cache backlinks are an efficient way to find relations between pages.

#### Drag and Drop from your file browser
You can insert images and links to files very easily by dragging them into the page. For images the image will be embedded while for other file types a link will be inserted. In the same way you can drag urls from you web browser. If you want to include the image files in the notebook try the menu item "*Tools* -> *Document Folder*". This will open a folder in the notebook directory that corresponds to the current page. You can also use a document root for this, see [properties](../Help/Properties.markdown) for that.

#### Use the <ctrl><space> keybinding
The ``<ctrl><space>`` keybinding is used to switch focus between the text area and the tree in the side pane. This allows you to switch pages using the keyboard instead of needing to grab the mouse. As an extra feature the ``<ctrl><space>`` keybinding pops open the side pane when it was hidden but closes it as soon as you have selected a page. This is very useful when you do not want to have the side pane open all the time but instead use it occasionally to find another page.


