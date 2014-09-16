===========
``gs.core``
===========
~~~~~~~~~~~~~~~~
Useful utilities
~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-02-24
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product contains some useful functions. They were originally written
as part of the GroupServer_ project, but they are totally independent of
GroupServer.

``curr_time``:
  Get the current time, in UTC, as a ``datetime.datetime``.


``to_ascii``:
  Convert a string to ASCII, with a reasonable chance of success.


``to_unicode_or_bust``:
  Convert a string instance to a Unicode instance, with
  reasonable chance of success.


``comma_comma_and``:
  Turn a list of strings into a single strings, with commas.

``to_id``:
  Create a random identifier, using a string as a seed.


``convert_int2b62``:
  Convert an integer to a base-62 encoded string.

Resources
=========

- Documentation: http://gscore.readthedocs.org/
- Code repository: https://source.iopen.net/groupserver/gs.core
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/
