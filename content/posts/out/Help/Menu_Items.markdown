title: Menu Items
date: 2013-08-03
File
----

**New Page <Ctrl><N>**
Prompt for a page name and create a new page.

**New Sub Page**
Prompt for a page name and create a new page as a child of the current page.

**Open Another Notebook <Ctrl><O>**
Prompt a list of known notebooks for opening another notebook. This dialog will also allow you to specify a file path for a new notebook.

**Import Page**
Prompts for a file path for a text file to import into this notebook. The text file is assumed to be already using the wiki formatting used by the notebook. Files saved using "Save A Copy" can be imported again by this function. The basename of the imported file will be used as the page name.

**Open in New Window**
Open the current page in a separate window. The new window will be readonly and any links clicked will open in the main window.

**Save <Ctrl><S>**
Save the current page. This function is included to not scare users that do not feel comfortable with only auto-save. However pages are being saved continuously, save there is hardly any need to explicitly save them.

**Save A Copy**
This function is intended for saving a copy of the current page outside of the notebook as a text file using the wiki syntax of the notebook. These files can later be imported again with the "Import Page" function.

**Save Version <Shift><Ctrl><S>**
Prompt for entering a comment and save a new version. This is a snapshot of the notebook that can later be restored or used to compare changes. If no version control is enabled yet for this notebook this function will ask you to enable version control.

Only available if the [Version Control plugin](../Plugins/Version_Control.markdown) is enabled.

**Versions**
Shows a list of saved versions and includes tools to compare versions.

Only available if the [Version Control plugin](../Plugins/Version_Control.markdown) is enabled.

**Export**
Show the [export dialog](./Export.markdown). 

**Print to Browser <Ctrl><P>**
Export the current page to a temporary file and open it with the browser. This is a work around for the lack of printing support in zim. You can print the page from the browser, so pressing <ctrl><P> twice will print the current page.

**Send To**
Open a new email with the current page as the email text using your email application. 

**Rename Page**
Prompt for a new name for the current page. Optionally the page heading is also changed on the fly. Links to this page can be updated automatically.

**Move Page**
Prompt for a new namespace for the current page. Alternatively you can move pages by drag and drop in the side pane. Moving a page also moves all of it's child pages as well as any [attachments](./Attachments.markdown). Links to this page can be updated automatically.

**Delete Page**
Delete the current page and all of it's child pages and [attachments](./Attachments.markdown). Unless the current page has been stored in a saved version this can not be undone.

**Properties**
Show the [properties dialog](./Properties.markdown).

**Close <Ctrl><W>**
Close the current notebook. In most cases this is identical to "Quit". However when the [TrayIcon plugin](../Plugins/Tray_Icon.markdown) is enabled closing the notebook only hides the window.

**Quit <Ctrl><Q>**
Quit the current notebook.


Edit
----

**Undo <Ctrl><Z>**
Undo the last edit for the current page. The undo stack tries to be intelligent and undo edits by word or by logical action. If you start typing after an undo step the undo step itself will also be folded into the list of edits. This means you can actually undo an undo step. Pressing undo after an [auto formatting](./Auto_Formatting.markdown) triggered will first undo the automatic formatting and the next undo will undo the actual editing.

**Redo <Shift><Ctrl><Z>**
Opposite of Undo. Only works if the page was not edited after the undo step. If it was edited the previous state is reachable by Undo, as described above.

**Cut <Ctrl><X>**
Cut selection and put it on the clipboard.

**Copy <Ctrl><C>**
Copy selection and put it on the clipboard.

**Paste <Ctrl><V>**
Paste content from the clipboard.

**Delete**
Delete selection or next character in the editor.

**Toggle Checkbox 'V' <F12>**
Toggle a [checkbox](./Check_Boxes.markdown) using the "OK" checkmark.

**Toggle Checkbox 'X' <Shift><F12>**
Toggle a [checkbox](./Check_Boxes.markdown) using the "NOK" checkmark.

**Edit Link or Object <Ctrl><E>**
Prompt a dialog to edit the properties of a link or other object. This also shows the property editor for an image when the cursor is next to an image.

**Remove Link**
Remove a link at the cursor.

**Copy Location <Shift><Ctrl><L>**
Copy the page name for the current page on the clipboard.

**Preferences**
Show the [preferences dialog](./Preferences.markdown).


View
----

**Notebook Editable**
This toggle allows switching between editing and read-only mode. In read-only mode the notebook can not be modified. This feature is intended to prevent accidental edits while browsing pages.

**Toolbar**
Toggle the visibility of the toolbar.

**Statusbar**
Toggle the visibility of the statusbar.

**Side Panes <F9>**
Toggle the visibility of the side pane(s).

You can also use the <Alt><Space> (or <Ctrl><Space>) [keybinding](./Key_Bindings.markdown) to switch focus between the editor and the side pane. Even if the side pane is hidden, this key binding will show it temporarily.

**All Side Panes <Ctrl><F9>**
This action will show all side panes that are being used.

**Pathbar**
Toggle the pathbar visibility and style. Options are **None**, **Recent** **Pages**, **History** and **Namespace**. Obviously "None" will hide the pathbar. "Recent Pages" shows a summary of the history. This summary only shows unique pages and tries to not re-order them too often. Setting "History" shows the full history list. "Namespace" will show the page path to the current page, showing all it's parents.

**Toolbar**
Toggle toolbar style, overriding the system defaults. The same submenu is available as a context menu on the toolbar itself.

**Fullscreen <F11>**
Toggle fullscreen display, mainly intended for small screens where it makes sense to use the whole screen for the editor. Visibility of the toolbar, pathbar and statusbar is configured separately for the fullscreen mode and the normal mode. 

( Users who really prefer to use the whole screen can even decide to hide the menubar in fullscreen mode. See the hidden option in the notebook state file. )

**Task List**
Show the task list dialog.

Only available if the [Task List plugin](../Plugins/Task_List.markdown) is enabled.

**Show Link Map**
Show the relations between the current page and other pages in this notebook in a graph.

Only available if the [Link Map plugin](../Plugins/Link_Map.markdown) is enabled.

**Calendar**
Show the calendar dialog.

Only available if the [Journal plugin](../Plugins/Journal.markdown) is enabled.

**Reload <Ctrl><R>**
Reload the current page. This means the page is saved and then reloaded from source. Any wiki formatting in the page that is not yet rendered will be rendered after reloading.


Insert
------

**Date and Time <Ctrl><D>**
Insert a date or a date and timestamp. If the [Journal plugin](../Plugins/Journal.markdown) is enabled the date can be linked automatically to the journal page. 

**Image**
Insert an image.

**Screenshot**
Prompt with options to take a screenshot and insert it as an image. 

Only available if the [Insert Screenshot plugin](../Plugins/Insert_Screenshot.markdown) is enabled.

**Equation**
Prompt for an equation written in latex and insert it as an image.

Only available if the [Equation Editor plugin](../Plugins/Equation_Editor.markdown) is enabled.

**Diagram**
Prompt for an diagram defined in the dot language and insert it as an image.

Only available if the [Diagram Editor plugin](../Plugins/Diagram_Editor.markdown) is enabled.

**Text From File**
Prompt for a text file and insert the text from that file into the current page.

**New Attachment (submenu)**
This submenu shows a number of file templates for new attachments, see [Attachments](./Attachments.markdown) for details.

**Link <Ctrl><L>**
Prompt for a link and insert it in the current page. Selected text will be used as default value.


Format
------

**Heading 1 <Ctrl><1>**
**Heading 2 <Ctrl><2>**
**Heading 3 <Ctrl><3>**
**Heading 4 <Ctrl><4>**
**Heading 5 <Ctrl><5>**
Toggle formatting used while typing. Selected text will also be formatted. If the "auto select" [preference](./Preferences.markdown) is set toggling the will automatically select the current line and turn it in a heading.

**Strong <Ctrl><B>**
**Emphasis <Ctrl><I>**
**Mark <Ctrl><U>**
**Strike <Ctrl><K>**
**Verbatim <Ctrl><T>**
Toggle formatting used while typing. Selected text will also be formatted. If the "auto select" [preference](./Preferences.markdown) is set toggling the format while the cursor is in the middle of a word will automatically select the word and format it.

**Clear Formatting <Ctrl><0>**
Remove all formatting from the selected text.


Search
------

**Find <Ctrl><F>**
**Find Next <Ctrl><G>**
**Find Previous <Shift><Ctrl><G>**
**Replace <Ctrl><H>**
**Search <Shift><Ctrl><F>**
**Search Backlinks**
Search for pages linking this page. Uses the standard Search dialog.


Tools
-----

**Check Spelling <F7>**
Turn on spell checking.

Only available if the [Spell Checker plugin](../Plugins/Spell_Checker.markdown) is enabled.

**Attach File**
Attach a file to the current page. Will prompt for a file, the file will then be copied to the notebook folder and a link inserted in the current page.

**Open Attachments Folder**
Open the folder with [attachments](./Attachments.markdown) for the current page in a file browser. Typically this will be a folder below the notebook folder.

**Open Notebook Folder**
Open the folder for the current notebook in a file browser.

**Cleanup Attachments**
Starts a dialog to search for orphaned files.  When an [attachment](./Attachments.markdown) link is removed, the file still exists in the attachment directory. From time to time it may be useful do find and delete this "orphaned" files.

**Start Web Server**
Start a stand-alone web server to make the current notebook available as a web page. Can be used to check the html formatting live, or to quickly share the current notebook with others on the same network.

**Open Document Root**
Open the document root folder in a file browser.

**Update Index**
Double check the page index against the folder contents of the notebook. This can be used when the index is by accident out of sync with the notebook contents.


Go
--

**Back <Alt><Left>**
Go to the previous page in the history.

**Forward <Alt><Right>**
Go to the next page in the history.

**Parent <Alt><Up>**
Go to the parent page.

**Child <Alt><Down>**
Go to a child page. If there is a recent child page in the history that page will opened, otherwise the first child in the index is opened.

**Next in Index <Alt><PgDn>**
Go to the next page in the index. This traverses all children of pages recursively and only goes to the next page on the same level after the last child.

**Previous in Index <Alt><PgUp>**
Go to the next page in the index. This traverses all children of pages recursively and only goes to the next page on the same level after the last child.

**Today <Alt><D>**
Go to the Journal page for today.
Only available if the [Journal Plugin](../Plugins/Journal.markdown) is enabled.

**Home <Alt><Home>**
Go to the home page of this notebook. You can change the home page in the [properties dialog](./Properties.markdown).

**Jump to <Ctrl><J>**
Prompt for a page name and jump to that page. The page name is resolved relative to the current page. You can also use this to open pages that do not yet exist. In contrast to "New Page" opening a page that does not exist will not directly create the page, it will only be saved after you edit it.


Help
----

**Contents <F1>**
Show this user manual

**FAQ**
Show the [FAQ](../FAQ.markdown) page in this manual.

**Keybindings**
Show the [Key Bindings](./Key_Bindings.markdown) page in this manual.

**Bugs**
Show the [Bugs](../Bugs.markdown) page in this manual.

**About**
Show the About dialog with license terms and credits.

