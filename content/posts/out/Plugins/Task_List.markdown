title: Task List
date: 2013-08-03
The Task List plugin adds a dialog that lists open items across all pages of the current notebook. In a way it is a specialized search function. An open item or task is defined by a single line and can have tags and a priority.

**Dependencies:** This plugin has no additional dependencies.

**See also:** [Usage:Getting Things Done](../Usage/Getting_Things_Done.markdown)

Options
-------
This plugin has two options that can be configured:

If the option "**Consider all checkboxes as tasks**" is enabled any checkboxes found will appear in the task list. If it is disabled only checkboxes that have a task label (like "FIXME" or "TODO") will appear in the list.

If **Turn page name into tags for task items** is enabled, each task will be tagged with the path components of the page name. E.g. a task defined in the page "``Projects:ProjectA:Phase1``"  will get the tags "``Projects``", "``ProjectA``", and "``Phase``1". This is useful because it allows selecting tasks from a sub-tree of pages at once using the proper tags. Also pages with similar names in diffent parts of the tree can easily be shown in this way.

If **Implicit due date for task items in calendar pages** is enabled, tasks found in pages that belong to the [Journal plugin](./Journal.markdown) will get that calendar date as due date. If the calendar page covers multiple days (e.g. a weekly page) the last day of the period will be taken as the due date.

If **Flag tasks due on Monday or Tuesday before the weekend** is enabled the highlighting of due dates assumes a Monday to Friday work week. This means that tasks due on Monday will already be highlighted on Thursday and Friday.

The option **Labels marking tasks** gives a comma separated list of labels that are used to flag tasks. By default these are "TODO" and "FIXME" but this can be customized.

The option **Label for next task** sets a label to start tags that depend on the previous task. The default is "Next:", but you can also customize it. If a tasks depends on the previous task it will not be "**actionable**" until the previous task is marked as done. This is particularly useful if you want to breakdown a task in serial steps, but not put all steps in the task list at once. Tasks that are not yet actionable are grayed out in the list.

The option **Tags for non-actionable tasks** allows you to specify tags that will flag tasks as non-actionable. This is for example useful when working with a [GTD](../Usage/Getting_Things_Done.markdown) method to flag delegated tasks that are not actionable right now, but may need to be reviewed again later. A tag like "``@delegated``" or "``@waiting``" could be used for this. Multiple tags can be given separated by a "``,``".

The options **Subtree(s) to index** and **Subtree(s) to ignore** can be used to limit the namespaces that are indexed for tasks. By default the whole notebook is used, but if either of these options or both these options are set, only a limited set is indexed. Multiple namespaces can be given separated by a "``,``".

Usage
-----

### Using Checkboxes
The first way to use the task list is to define open items by checkboxes. A list like this will be interpreted as a task list and each individual line will appear in the task list dialog.


* ☐ Buy rice @groceries
* ☐ Call Susan to invite for diner [d: 5/1] !
* ☐ Print menu @desk


In this example the second item will have the highest **priority** because of the "!", the more exclamation marks the higher the priority. Also the words with an "@" will be considered **tags**, so the dialog will show the tags "groceries" and "desk" which can be used for filtering the task list.

A **due date** can be added by putting a date in between "[d: ]". Zim parses a couple of date formats:

	dd/mm		dd-mm
	dd/mm/yy	dd-mm-yy
	dd/mm/yyyy	dd-mm-yyyy
	yyyy/mm/dd	yyyy-mm-dd

So you can use e.g. "[d: 5/1]", "[d: 2010-1-5]" or "[d: 5/1/10]". (Any other separator character to separate year, month, and day will also work, as long as it is not a number or a letter.)

**Note: **dates are parse in European notation, so "dd/mm", not as "mm/dd" as is customary in the US. Unfortunately there is no way to resolve these unambiguously.

A task in a checkbox list can also have sub-items. This can help enormously to split up a complex task in step by step action items. For example:


* ☐ Organize party [d: 19/8] !
	* ☐ Send invitations [d: 1/8] !!
	* ☐ Cleanup living room
		* ☐ Get rid of moving boxes [d: 10/8]
		* ☐ Buy vacuum cleaner [d: 15/8]
	* ☐ Buy food & drinks


Such sub-items will also show up in the tasklist as sub-items below the main task in a hierarchic tree. Note that sub-items that do not have an explicit due date or priority set will inherit these from the main task. So in this example the "*send invitations*" action an earlier due date and a higher priority, while the "*cleanup living room*" and "*buy food & drinks*" items inherit due date and priority from the main task.

### Using labels
The second way to use the task list is by using labels like "TODO" or "FIXME" in your notes. Labels can appear at the start of a line or directly after a checkbox. The rest of the lines is parsed the same as a task description after a checkbox. So the following will also be considered a task:

FIXME: finish the previous paragraph

Different labels can be used similar to tags to distinguish different categories of tasks.

As a special case labels can be used to flag a whole list being a task list. In that case the tag needs to start a new paragraph and be on a line by itself before the first checkbox. This usage is especially useful when the option "Consider all checkboxes as tasks" is turned off. Any tags on this first line will be applied to the whole list. However no other words should appear as that would make this first line a regular item and cause the list to be ignored. An example of this usage is as follows:

TODO: @home

* ☐ Call Susan to invite for diner [d: 5/1] !
* ☐ Print menu @desk


Now both items will get the tag "@home" appended.

### Non-actionable tasks
Non-actionable tasks are tasks that you can not (yet) act on. For example tasks that can only start after a previous tasks has finished, or tasks that you are waiting for someone else. The tasklist dialog by default shows such tasks grayed out, but you can also hide all non-actionable tasks.

There are two configuration to help flagging non-actionable tasks. The first option is the "Next" label. This flags that a task depends on the previous task being completed. This is useful when you write down an action plan, but don't want to see all at once in the task list. The "Next" label can be used at the start of a line like this:

Clean up the garage:

* ☐ Make space by bringing old stuff to the dump
* ☐ Next: buy new shelves @shopping
* ☐ Next: setup new shelves in the back of the garage
* ☐ Next: move stuff from side wall to the new shelves


etc. Assuming each of these tasks will end up being done on different days, it helps to write them down step by step. But the tasklist will only show the next one coming up

Another way to flag non-actionable tasks is using special tags. E.g. a generic tag @waiting could be used to flag when you wait for someone else, or @review for plans that are not agreed yet. You can define your own depending on your own work flow.



