title: Plugins
date: 2013-08-03
The following plugins are standard included with zim:


* [Arithmetic](./Plugins/Arithmetic.markdown)
* [Attachment Browser](./Plugins/Attachment_Browser.markdown)
* [Automount](./Plugins/Automount.markdown)
* [BackLinks Pane](./Plugins/BackLinks_Pane.markdown)
* [Diagram Editor](./Plugins/Diagram_Editor.markdown)
* [Distraction Free Editing](./Plugins/Distraction_Free_Editing.markdown)
* [Ditaa Editor](./Plugins/Ditaa_Editor.markdown)
* [Equation Editor](./Plugins/Equation_Editor.markdown)
* [GNU R Plot Editor](./Plugins/GNU_R_Plot_Editor.markdown)
* [Gnuplot Editor](./Plugins/Gnuplot_Editor.markdown)
* [Insert Screenshot](./Plugins/Insert_Screenshot.markdown)
* [Insert Symbol](./Plugins/Insert_Symbol.markdown)
* [Inline Calculator](./Plugins/Inline_Calculator.markdown)
* [Journal](./Plugins/Journal.markdown)
* [Link Map](./Plugins/Link_Map.markdown)
* [Line Sorter](./Plugins/Line_Sorter.markdown)
* [Log events with Zeitgeist](./Plugins/Log_events_with_Zeitgeist.markdown)
* [Print to Browser](./Plugins/Print_to_Browser.markdown)
* [Quick Note](./Plugins/Quick_Note.markdown)
* [Score Editor](./Plugins/Score_Editor.markdown)
* [Spell Checker](./Plugins/Spell_Checker.markdown)
* [Table Of Contents](./Plugins/Table_Of_Contents.markdown)
* [Tags](./Plugins/Tags.markdown)
* [Task List](./Plugins/Task_List.markdown)
* [Tray Icon](./Plugins/Tray_Icon.markdown)
* [Version Control](./Plugins/Version_Control.markdown)


Plugins can be enabled and configured in the [preferences dialog](./Help/Preferences.markdown). A number of plugins have additional dependencies, like specific external programs, that are not required for the core functionality of zim. If one or more dependencies of a plugin are not fulfilled, these are marked red.

Installing Plugins
------------------
If a plugin is distributed as a separate python module, it should be installed such that zim can find it. For use specific plugins you can install them Python's "per user site-package directory".

For example for python 2.6 this folder is:
Unix (including Mac OS X): ``~/.local/lib/python2.6/site-packages``
Windows: ``%APPDATA%/Python/Python26/site-packages``

See <http://www.python.org/dev/peps/pep-0370/> for details.

Writing Plugins
---------------
If you are looking for information on **writing plugins** please download the source package and have a look at the notes included in the "HACKING" folder.


