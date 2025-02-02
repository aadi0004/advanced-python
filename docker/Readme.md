and on vs code terminal write docker build -t saurabhbrd/database_infra . 
and on vs code terminal write docker build -t docker_hub_username/image_name .

<!-- if you want to see your all images  -->
docker images 

If you want to run your docker image 
docker run -p 5000:5000 saurabhbrd/database_infra 


docker ps    ### this will show how many  containers are running 

docker stop container-id  ### for stopping the container 

docker hub ---> login ---> save passwrod 

on the terminal 
docker login 
Username : fill your username
Pasword: fill your password 

docker push saurabhbrd/database_infra:latest

docker pull saurabhbrd/database_infra:latest


