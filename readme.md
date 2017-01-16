# Python and mysql

In this repository we can see a general things about the connection of python with mysql.

The requiremnts are:
* python
* mysql
* mySQL connecto


## python 
In most of GNU/Linux systems python is installed by default. In this small guide this topic is not aborded. 

## mySQL
   You should download the properly version of mySQL for your system. For some GNU/Linux systems this guide can help [https://www.if-not-true-then-false.com/2010/install-mysql-on-fedora-centos-red-hat-rhel/](https://www.if-not-true-then-false.com/2010/install-mysql-on-fedora-centos-red-hat-rhel/)


## mySQL connector 

At first is necesary check the version of python and mySQL

> python --version

> mysql --version

In order to know what version of the mySQL we need the next table would help:

Connector/Python Version | 	MySQL Server Versions |	Python Versions | 	Connector Status
------------------------ | ---------------------- | --------------- | -------------------- 
2.2 |5.7, 5.6, 5.5 	| 3.3 and higher, 2.7  |	Developer Milestone
2.1 |5.7, 5.6, 5.5 	| 3.3 and higher, 2.7, | 2.6 	Recommended version
2.0 |5.7, 5.6, 5.5  | 3.3 and higher, 2.7, 2.6 | GA, Supported
1.2 |5.7, 5.6, 5.5 (5.1, 5.0, 4.1) | 3.1 and higher, 2.7, 2.6 |	GA, Supported

from site [mysql](https://dev.mysql.com/doc/connector-python/en/connector-python-versions.html) 

