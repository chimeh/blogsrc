title: Attachments
date: 2013-08-03
Pages can have attachments, these are e.g. image files for images that are part of the page, but can also be documents that are referred to in the page.

Attachments are typically stored in the folder one level below the page with the text of the page. This folder can be opened with the menu item "*Tools → Open Attachments Folder*". To directly copy a file to the attachment folder and insert a link use the menu item "*Tools → Attach File*"

Attachments can be created, modified, and deleted with regular applications. To link them in a zim page, just drag and drop from the window manager to the editor.

**Note:** For images that are shown in the page, you may need to refresh the page before changes become visible. Use ``<ctrl>R`` or the menu item "*View → Reload*".

**See also:** [Plugins:Attachment Browser](../Plugins/Attachment_Browser.markdown)

File Templates
--------------
There is also a menu item "*Insert → New Attachment*". This item has a submenu that is based on a folder with file templates. Clicking any of the file templates will create a new attachment which is a copy of that file and insert a link to the new attachment, or, if it is an image, inserts it as an image. This is a convenient way to create new documents in the notebook and start editing them. The file is not opened directly, so to start editing you need to click the link or right click on the image.

By default the folder where the templates are located is ``~/Templates``, but you can change it in the [preferences](./Preferences.markdown). To manage the templates, click the last menu item ("*File Templates...*") to open the folder. Now create a new file that is a blank file of the file type that you would like to be able to insert into zim. Note that the file extension is removed in the menu, so give is a clear name, e.g an SVG file could be called "``SVG_Drawing.svg``".

Be aware that in order to edit the file, it usually must be a valid file of the specific file type. If you just create an empty text file and rename it to "``Image.png``" most image editing applications will not consider it a valid PNG image. So it is better to start an image editor and save a real blank image as template.

Of course it is perfectly fine to have multiple templates of the same file type.

Note that this feature tries to be compatible with the "*Create new document*" menu in the Gnome file browser.

