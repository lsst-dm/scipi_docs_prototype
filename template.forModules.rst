
From: https://dmtn-030.lsst.io/#module-topic-type

####################
Template For Modules
####################

lsst.module.name — Human Readable name
======================================

Since “module” is a Python-oriented term, the title should be formatted as: “python module name — Short description."

Summary paragraph
=================

This paragraph establishes the context of this module and lists key features.

See also
========

This component links to other parts of the documentation that do not otherwise follow from the topic type design.  For example, if the module is part of a framework, that framework’s page is linked from here. This component can also be used to disambiguate commonly-confused modules.

In Depth
========

This section lists and links to conceptual documentation pages for the module. Each conceptual documentation page focuses on a specific part of the API and dives into features while providing usage examples. The topics can also document architectural decisions.

Tasks
=====

This section lists and links to task topics for any tasks implemented by this module. 

Minimally, this section should be a simple list where the task name is included first as a link, followed by a short summary sentence.

Python and C++ API reference
============================

These sections list and link to reference pages for all Python and C++ API objects. Individual functions and classes are documented on separate pages.

Packaging
=========

This section is designed to help a user understand how to access a module, and understand how this module’s package relates to other packages in the Science Pipelines documentation by:

- Stating what package a module is part of.

- Linking to that package’s GitHub repository.

- Stating what top-level packages include this module’s package. 

- Stating what packages depend on this module’s package, distinguishing between direct and in-direct dependencies. 

- Stating what packages in the LSST Stack dependent on this package. 

The package dependencies can be expressed as both lists and graph diagrams.

Related documentation
=====================

This section consists of a listing of other documents related to this module, including:

- Design documentation.
- Technotes.
- RFCs.
- Community forum conversations.

For the last item, this will be done by an automatic service that can monitor https://community.lsst.org forum conversations.

