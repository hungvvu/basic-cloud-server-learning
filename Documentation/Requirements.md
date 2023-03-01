# Cloud Prototyping Goals and Requirements
(As defined during the team meeting)

1. Learn to receive and store sensor data from the device

	1.1. The cloud system must provide a way to submit sensor data
2. Learn to design an effective database

    2.1. The database should uphold standard designing principles and practices, such as BCNF
3. Learn to send data as requested from the database to the app

	3.1. The system must have a way for the app to request data  
	3.2. The system must be able to send the data to the app reliably
4. Learn how to host and run a simple remotely accessible cloud server
	
	4.1. Server should be accessible over internet
5. Learn to store passwords on the server side with some form of encryption
	 
	5.1. The password must be stored securely in the database  
	5.2. The service can authenticate connection according to entered username and password  
6. Learn to make the cloud infrastructure fault tolerance (with backups and recovery methods)
	
	6.1. The service are resistant to failure and should still be useable after disasters
