title: Diagram Editor
date: 2013-08-03
The diagram editor allows you to insert and edit diagrams based on GraphViz. GraphViz (or "dot" as the program is also referred to) uses a basic script language to define diagrams. This plugin adds a dialog where one can define a diagram in this script. The dialog shows a preview of the rendered diagram and when the diagram is finished it can be inserted in a zim page as an image. You can always edit it later again by selecting "Edit Diagram" from the context menu (right-mouse-click on the diagram will show the context menu).

**Dependencies:** This plugin requires GraphViz to be installed. In specific the "dot" command should be available in the system path.

Example
-------

For example a diagram like:

![](./Diagram_Editor/diagram.png)

Can be created by entering the following definition in the dialog:

	digraph G {
	  foo -> bar
	  bar -> baz
	  baz -> foo
	}

For full documentation of the script language see: <http://www.graphviz.org/>


