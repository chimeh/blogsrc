title: Version Control
date: 2013-08-03
Zim's default installation ships with a Version Control Plugin. To enable it, go to ``Edit -> Preferences -> Plugins`` and check the box next to Version Control. Zim supports [Bazaar](http://bazaar.canonical.com/),  [Git](http://git-scm.com/), and [Mercurial](http://mercurial.selenic.com/) as backends.

**Dependencies:** This plugin requires one of the supported version control systems to be installed. Currently Bazaar, Git and Mercurial are supported, so one of these applications is required. In specific the "``bzr``", "``git``" or "``hg``" command should be available in the system path.

Options
-------
If the option **Autosave version on regular intervals** is enabled zim will save (or "commit") a new version every time you close zim or when opening zim if new changes are detected.

Usage
-----
If you want to keep track of your changes or if you want to collaborate on a Zim notebook as a team, version control is the best way to go. Zim integrates very well with existing version control software because all relevant data is stored in plain text files.

To save the current state of the Notebook, choose ``File -> Save Version...`` from the Main Menu and confirm that you want to enable Version Control. In the next window add a comment describing the changes (probably something like "yeah, first version" at this point) and confirm by clicking Save.

You can browse the complete history of saved versions by selecting ``File -> Versions...`` from the Main Menu. You can view and restore previous versions of your Notebook and view all your changes between two versions in the window that open.

Sharing
-------
TODO here should be documented how to share the newly created repository with your collaborators... (Depends on the backend chosen)

See the [Bazaar](http://bazaar.canonical.com/) user manual for various scenarios of collaboration (follow the "documentation" link on their website).

Technical Details
-----------------
Technically speaking a local repository is created when enabling Version Control, depending on the backend you choose, this repository is managed by  [Bazaar](http://bazaar.canonical.com/),  [Git](http://git-scm.com/), or [Mercurial](http://mercurial.selenic.com/). Every time you save a version, another revision is checked in. Zim just uses standard version control systems as backend, so you can always view and export your history using standard tools.

On startup zim tries to detect the version control system used for a specific notebook, and use it if supported. So you can manually initialize repository (e.g. by branching) and then open them with zim. No need to tell Zim that the notebook is managed explicitly.

Manual Version Control
----------------------
This is for advanced users that have to use another Version Control System or have other reasons not to use the included plugin.

To manually manage revisions of your notebook, the following files should be added to your repository:

* The "``notebook.zim``" file in the notebook folder
* All your pages (*.txt files in the notebook folder and subfolders)
* All files linked/embedded from/into your pages ([attachments](../Help/Attachments.markdown) etc.)


All files created by Zim are in plain text format and only change when you explicitly change them so you should get readable, reasonable diffs and merges in case of conflicts.

You can and should ignore the following items however:

* The complete "``.zim``" folder - this is a local cache that will be regenerated
* Anything you manually put into or below the root folder you do not want to be in your repository


The files in the "``.zim``" folder are caches of the index and some client configuration (window sizes, scroll position etc.) and some of it is in binary format, so you do not need or want it in your repository.

If you want for some reason stop using version control and throw away all history, you can do the following:

* Disable the version control plugin
* Quit zim
* Remove from your notebook folder:
	* the .bzr folder and .bzrignore file in case of Bazaar,
	* the .hg folder and the .hgignore file in case of Mercurial,
	* the .git folder and the .gitignore file in case of Git.


