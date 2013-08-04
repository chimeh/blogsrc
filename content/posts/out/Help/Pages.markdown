title: Pages
date: 2013-08-03
Each [notebook](./Notebooks.markdown) consists of a set of pages. Each page can contain, text, images and links to other pages. The pages can be arranged in a hierarchical index. 

Page names use a ":" as a path separator for pages that are nested in the hierarchy. So the name "Foo:Bar" refers to a page names "Bar" that is nested below a page "Foo".

	+ Foo
	`--- Bar

The parent page is sometimes also referred to as the "namespace" of the page. So in this case the page "Bar" is said to belong to the namespace "Foo". Namespaces can be used to organize notebooks in sections of pages. Also sometimes namespaces are used for special purposes, for example the [Journal plugin](../Plugins/Journal.markdown) uses a namespace like ":Journal:" to contain all journal pages.

There are various ways to refer to other pages, either by absolute or relevant links. E.g. the page "``Foo:Bar``" can be linked from "``Foo``" as "``:Foo:Bar``" but also as "``+Bar``". For more details see [Links](./Links.markdown). The editor tries to automatically turn page names into links, as a special case you can use "CamelCase" to make page names more recognizable and make the auto-formatting easier. See [Auto Formatting](./Auto_Formatting.markdown) and [Preferences](./Preferences.markdown).

There are a number of characters that are forbidden in page names, these are: "?", "#", "/", "\\", "*", '"', "<", ">", "|" and "%". These are forbidden because they have a special meaning in the zim wiki syntax or because they can not be encoded on common file systems.

Pages can have attachments, for example images, data files, related documents etc. See [Attachments](./Attachments.markdown) for more details.

New Page Dialog
---------------
The New Page dialog prompts for a page name and then creates a new page with the specified name. To create a page that is nested in the hierarchy, specify it with a ":" in between the parts of the hierarchy.

New Sub Page Dialog
-------------------
This dialog is similar to the New Page dialog, but it creates a new child page of the current page. So no need to specify the full hierarchy path.

Jump To Dialog
--------------
This dialog is intended to jump to a specified page. It is actually hardly different from the New Page dialog except that it resolves page names relative to the current page and does not immediately create a new page. However you can always create new pages by jumping to a page that does not yet exist and start editing.

Deleting pages
--------------
When you select "Delete Page" by default zim will try to trash the page and all it's sub pages and attachments - **that means all files that are in the folder below the text file for the page**. If you deleted something on accident you should be able to recover the data from your system's trash can. After recovering data you probable need to run "Re-build Index" from the "Tools" menu to make sure zim indexes the data again.

If zim is not able to move data to the trash can it will offer to delete the data permanently. In this case a dialog is shown to ask for confirmation which includes a detailed list of files to be deleted.

If you don't like to use the trash by default (e.g. for notebooks that contain sensitive data) there is an option in the notebook [config file](./Config_Files.markdown) to disable the trash. In this case the confirmation dialog will always be shown on "delete page".

