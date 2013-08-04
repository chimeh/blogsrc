title: Ditaa Editor
date: 2013-08-03
ditaa is a small command-line utility written in Java, that can convert diagrams drawn using ascii art ('drawings' that contain characters that resemble lines like "``|" "/" "-"`` ), into proper bitmap graphics. This is best illustrated by the following example -- which also illustrates the benefits of using ditaa in comparison to other methods :)

Example
-------
	+--------+   +-------+    +-------+
	|        | --+ ditaa +--> |       |
	|  Text  |   +-------+    |diagram|
	|Document|   |!magic!|    |       |
	|     {d}|   |       |    |       |
	+---+----+   +-------+    +-------+
	    :                         ^
	    |       Lots of work      |
	    +-------------------------+


After conversion using ditaa, the above file becomes:
![](./Ditaa_Editor/ditaa.png)
ditaa interprets ascci art as a series of open and closed shapes, but it also uses special markup syntax to increase the possibilities of shapes and symbols that can be rendered.
ditaa is open source and free software (free as in free speech), since it is released under the GPL license.

See  <http://ditaa.sourceforge.net/> for more information about ditaa

