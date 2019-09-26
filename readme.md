########################################################################

The application is developed using python and mongodb.
The application is built using two docker containers.
1. The container takes http input string and append "last_name" to it and send the input string, appended string and 
timestamp is sent to mongodb.
2. The second container has mongodb.

command to build and run the application:


docker-compose up
