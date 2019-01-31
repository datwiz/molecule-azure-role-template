*******
Azure driver installation guide
*******

Requirements
============

* An Azure credentials rc file
* azure sdk
* env var AZURE_RESOURCE_GROUP set to an exiting resource group name

Install
=======

.. code-block:: bash

    $ sudo pip install 'ansible[azure]'
    $ export AZURE_RESOURCE_GROUP=<resource_group_name>
