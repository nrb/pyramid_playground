This is a simple project meant to illustrate app customization via Pyramid includes.

Concept
=======

This app is meant to illustrate an extensible Pyramid application (``base.py``) that can be used by a 'customization package' (``customized.py``) in order to override the default behavior **without** using something like ZCML.

To Install
==========

Make a virtualenv, then run ``pip install -r requirements.txt``

To Run the Base App
===================

``python base.py``

To Run the Customized App
=========================

``python customized.py``
