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
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product contains some useful functions. They were originally written
as part of the GroupServer_ project, but they are totally independent of
GroupServer.

``curr_time``
=============

Get the current time, in UTC, as a ``datetime.datetime``.

Synopsis
--------

::

   gs.core.curr_time()

Description
-----------

This function returns the current time, with a timezone, as a standard
Python ``datetime.datetime`` instance [#datetime]_. It saves quite a few
imports!

.. [#datetime] See <http://docs.python.org/library/datetime.html>

Arguments
---------

None.

Returns
-------

The current time, as a ``datetime.datetime`` instance, with the timezone
set to UTC.

``to_ascii``
=============

Convert a string to ASCII, with a reasonable chance of success.

Synopsis
--------

::

  gs.core.to_ascii(stringOrUnicode)

Description
-----------

The ``to_ascii`` function, ultimately, calls ``unicode.encode('ascii',
'ignore')``, but it has a couple of advantages.

#. It takes up less space.
#. If passed a string then the string will be decoded as UTF-8, before
   being re-encoded as ASCII.

The second point may seem to be redundant, but it avoids the dreaded
**Unicode Decode Error** from occurring.

Arguments
---------

``stringOrUnicode``:
  The sting instance, or Unicode instance, to convert.

Returns
-------

An ASCII string.

Example
-------

::

  filename = to_ascii('{0}-members.csv'.format(self.groupInfo.id))

``to_unicode_or_bust``
======================

Convert a string instance to a Unicode instance, with reasonable chance of
success.

Synopsis
--------

::

  gs.core.to_unicode_or_bust(stringOrUnicode, encoding='utf-8')

Description
-----------

Sometimes text-input has… uncertain… origins, and it is hard to know
encoding it is. The ``to_unicode_or_bust`` has a good stab at converting
the input to a Unicode instance.

Arguments
---------

``stringOrUnicode``:
  The sting instance, or Unicode instance, to convert.

``encoding``:
  The encoding for the string. Defaults to UTF-8.

Returns
-------

A Unicode instance.

Example
-------

::

  filename = gs.core.to_unicode_or_bust(someInput)

Acknowledgements
----------------

Taken from an excellent presentation on `Unicode in Python by Kumar
McMillan <http://farmdev.com/talks/unicode/>`_.


``to_id``
=========

Create a random identifier, using a string as a seed.

Synopsis
--------

::

  gs.core.to_id(s)

Description
-----------

Many things require unique identifiers, such as users, posts, topics,
password-reset links, and email-verification links. The ``to_id`` function
takes a string and converts it to a fixed-length base-62 encoded string
that can be used as an ID.

Arguments
---------

``s``:
  The string to be used as a seed.

Returns
-------

A base-62 encoded string, 22 characters long.

Example
-------

::

    email = emailUser.get_delivery_addresses()[0]
    verificationId = to_id(email)

``convert_int2b62``
===================

Convert an integer to a base-62 encoded string.

Synopsis
--------

::

  gs.core.convert_int2b62(num)

Arguments
---------

``num``:
  The number to convert

Returns
-------

A base-62 encoded string.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.core
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
