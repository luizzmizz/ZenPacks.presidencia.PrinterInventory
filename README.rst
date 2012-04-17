==============================
ZenPacks.presidencia.PrinterInventory
==============================

.. contents::
   :depth: 3

This project is a Zenoss_ extension (ZenPack) that contains some custom 
printer specific modelers (to be grown)

Requirements & Dependencies
---------------------------
This ZenPack is known to be compatible with Zenoss versions 3.2

Installation
------------
There are no dependencies for installing this ZenPack.

Normal Installation (packaged egg)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copy it to your Zenoss server and run the following commands as the zenoss
user::

    zenpack --install <package.egg>
    zs restart

Developer Installation (link mode)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Copy it to your Zenoss server and run the following commands as the zenoss
user::
  
    zenpack --link --install <path.to.package.folder>
    zenoss restart

Usage
-----
Installing the ZenPack will add the following objects to your Zenoss system.

* Modeler plugin presidencia.snmp.PrinterDeviceMap

.. _Zenoss: http://www.zenoss.com/

