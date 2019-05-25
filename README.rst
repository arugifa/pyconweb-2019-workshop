PyConWeb 2019 Terraform Workshop
================================

Introduction to Terraform for managing web infrastructures.


Getting Started
===============

Before trying to go further, you first need to install a couple of requirements:

- `Docker`_, `Docker Compose`_ and `Terraform`_,
- `Python-OpenStackClient`_ (recommended, to check you can connect to OpenStack),
- `Kubectl`_ (optional, only if we have enough time to play with Kubernetes...).

.. _Docker: https://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/
.. _Kubectl: https://github.com/kubernetes/kubectl
.. _Python-OpenStackClient: https://pypi.org/project/python-openstackclient/
.. _Terraform: https://www.terraform.io/

After what, you will be able to set-up the project with::

   docker-compose build


Running the Demo
================

First, run the demo server in the foreground::

   docker-compose up

You can now access to the web API on ``http://localhost:5000/``

If you prefer to run the server on a different port, try that instead::

   DEMO_PORT=<WHATEVER> docker-compose up


Running Tests
=============

To run the tests::

   docker-compose -f docker-compose.test.yml run sut


What To Do Next?
================

It depends on what you want, and how fast we will be:

1. Deploy the demo application on OpenStack.
2. Deploy the demo application on Kubernetes.

But for now, just raise your hand and say "Я закончил!".
