title: Journal
date: 2013-08-03
The Journal Plugin turns a specific namespace ("Journal" by default, but this is configurable) into a journal. It can either have a page per day, organized by year and month, or a page per week or per month. The plugin also adds a calendar widget to zim. By default this is done by adding a dialog, but optionally it can also be put in the side pane above the page index. In this calendar each date is linked to a page for that date.

This plugin is intended to help organize notes by date like you would do for a journal. Another use case is e.g. to put minutes of meetings or class notes on the page for the date of the meeting - possibly to work them out later in pages for the specific subject.

**Dependencies:** This plugin has no additional dependencies. The python module "``babel``" is an optional dependency to determine the weekday conventions.

**See also:** [Usage:Daily Journal](../Usage/Daily_Journal.markdown)

Options
-------
This plugin has the following options:

The option **Show calendar in sidepane instead of as dialog** does just that; if enabled the calendar widget is embedded at the top of the side pane. Otherwise the calendar is shown in a separate dialog when you click the toolbar button. If the calendar is embedded in the side pane, the option **Position in the window** determines in which side pane the calendar is shown.

The option **Use a page for each: ...** allows you to set the calendar to either use a separate page for each day, each week, each month or even each year.

The **Namespace** controls where the calendar pages are stored.

Keybindings
-----------

* ``<Alt>D``  - navigate to the calendar date for today


Tasks per day
-------------
The [Task List plugin](./Task_List.markdown) has an option to automatically set the due date for tasks that are defined on calendar pages. When this is enabled you can put tasks on the correct calendar page and they will show up in the task list with this implicit due date.

Template Properties
-------------------
The Calendar plugin adds the following properties to the template for calendar pages:

**calendar_plugin.date**
Date covered by this page

**calendar_plugin.start_date**
First date covered by this page (same as 'calendar_plugin.date')

**calendar_plugin.end_date**
Last date covered by this page

**calendar_plugin.days()**
A function that returns a list of all days in the week, month, year covered by this page

All these dates can be used with the templates ``strftime()`` function to format the date as text. See [Templates](../Help/Templates.markdown) for details.


