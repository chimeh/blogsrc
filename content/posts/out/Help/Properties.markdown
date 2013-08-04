title: Properties
date: 2013-08-03
The dialog with notebook properties can be accessed with the menu item "*File*" -> "*Properties*". The following notebook properties can be configured:

The notebook **Name** is used in the "[Open Notebook](./Notebooks.markdown)" dialog and e.g. in the menu for the [Tray Icon](../Plugins/Tray_Icon.markdown). This name is also used for the window title.

The notebook **Interwiki keyword** can be used to link to this notebook for other notebooks. See "Interwiki" in [Links](./Links.markdown) for more info.

The **Home Page** is the first page to open in a notebook if you have no history yet. It can be accessed with the toolbar icon for the home page and the <Alt><Home> key binding. Typically the home page should be an index page linking to other pages.

The notebook **Icon** is an image that is used together with the name to identify the notebook.

The **Document Root** is a special folder which contains documents that can be linked from the notebook. To link files in this folder start the links with a "/" (see [Links](./Links.markdown) for more details). This folder is typically used for notebooks that are published as web page. When [exporting](./Export.markdown) the notebook to html the document root can be mapped to a special URL.

The **Profile** is an advanced property which allows having multiple sets of preferences. E.g. if you have two types of notebooks and each type you want different preferences, plugins, style, etc. you would assign notebooks different "profiles". Practically speaking this means that a separate set with config files is being used per profile.

The **Shared Notebook** setting tells zim that the notebook is on a shared file system, or is located somewhere where file access is slow. In this case cache files will be written to the user home directory cache instead of the cache directory in the notebook folder itself. 

Disadvantage of storing information about the notebook outside the notebook folder is that for example for encrypted notebooks this cache data is not encrypted anymore.

