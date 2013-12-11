activemq-stomp-broker
=====================

Sample setup of ActiveMQ broker that uses STOMP.

To run the broker use maven

mvn activemq:run

The Openwire port is 61616
The STOMP port is 61613

The python client is in the python directory, and the sample MapMessage sender is part of the normal Maven project.

Articles
--------

http://blog.nigelsim.org/2013/12/11/using-mapmessage-with-activemq-with-a-python-stomp-py-consumer/
