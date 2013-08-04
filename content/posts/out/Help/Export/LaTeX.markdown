title: LaTeX
date: 2013-08-03
The [Equation Editor](../../Plugins/Equation_Editor.markdown) plugin is supported, equations entered with this plugin are automatically placed inside math environments. Embedded Images of types that are not supported by the TeX Engine of your choice may lead to compilation errors. For ``pdflatex`` the supported types are PDF, JPG, JBIG2, and PNG, for ``latex`` it is EPS. Index creation is currently not working.

Dependencies
------------
All templates depend on several LaTeX packages

* ``inputenc`` package to use utf8 as input encoding.
* ``hyperref`` to realize links (or another appropriate definition for ``\href)``
* ``graphicx`` for including images
* ``amsmath, amssymb, color`` are needed for support of the equationeditor plugin
* ``ulem`` is used for underlines and strikeouts


Templates
---------
The following templates are supplied:

**"Report"**

This templates is based (and depends) on the KOMA-Script Report Class ``scrreprt``. It generates a title page and a table of contents and is therefore more suitable for longer pages. To display checkboxes it depends on the ``wasysym`` package.

**"Article"**

This templates is based (and depends) on the KOMA-Script Report Class ``scrartcl``. It omits the lowest heading and is therefore not suitable for deeply structured documents.  To display checkboxes it depends on the ``wasysym`` package.

**"Part"**

The result from this template can not be compiled on its own, it is designed to be one part of a larger document and be included (``\include{}``) in a master document.

Template Options
----------------

#### document_type

Possible values: 'report', 'article', 'book'
Default: 'report'

The exported LaTeX code will use only commands suitable for the given document class (e.g. sectioning commands).




 



