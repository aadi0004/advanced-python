# MCP Server ---> Memory Control Protocol 

# LLM(Large Language Model) --> ChatGPT , Groq , Gemini  ....

# GPT ---> Generative Pre-training transformers ----> information (2023) 
# MCP + LLM Model  --> Response return 




# Application ---> 
# Frontend 
# Backend    -----> deployment , service , pv , pvc . 
# DataBase 





# LLM  ----> Agent(Amazon Q Cli)


# Create an ec2 server ---> 

# sudo apt-get update 
# sudo apt install libfuse2 

#####Install the deb file for Amazon Q

# curl --proto '=https' --tlsv1.2 -sSf https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb -o amazon-q.deb


##### Install Amazon Q debian file

# sudo apt install -y ./amazon-q.deb


# q  login 
# Use for free builder ID ----> 

#### this is the link 
# https://community.aws/builderid?trk=529c4ce9-0395-4c42-915a-d70bf060ef3c&sc_channel=el

### from where we can create builder id . 
# 


#### In ec2 sever  , we will select or write  'Use for Free with Builder ID' and click enter 

### Now we wil see a url copy this url and paste it into another tab of browser ---> Now we will AWS Developer q click 'confirm and continue' ---> Now click on 'Allow Access' . 


### Now we will see in our ec2 server login successfully messafe is here . 

### Now write 'q' in ec2 server then we will see Amazon Q is present there .

# /quit    
# ### for exit 

#### Now we will setup mcp in our ec2 server 

# cd .aws/amazonq 
# ls    ####We will see profiles folder is here .

### Now we will create a mcp server file in which we will put all configurations .

# vim mcp.json
# 
# ### paste these details 
# --------------------------------------------
# {

# 	"mcpServers" : {
    
#  "awslabs.cdk-mcp-server": {
#         "command": "uvx",
#         "args": ["awslabs.cdk-mcp-server@latest"],
#         "env": {
#            "FASTMCP_LOG_LEVEL": "ERROR"
#         }
#    },
#  "awslabs.aws-diagram-mcp-server": {
#  		"command": "uvx",
#  		"args": ["awslabs.aws-diagram-mcp-server"],
#  		"env": {
#  			"FASTMCP_LOG_LEVEL": "ERROR"
#  		},
#  		"autoApprove": [],
#  		"disabled": false
#  	}
# }

# }

#---------------------------------------------------------------
### Now write 'q' 
### It will represent failed . 
## Now write 
# /quit 
# cd .. 
######You need uv to install and Run MCP Servers

# sudo snap install astral-uv --classic

### Now write 
# uvx 

### Now write 'q'   and we will see that our both mcp servers are initialized. 

### Now I will ask 'can you create architecture digrams?'  press enter .

### Now write 't' 
### Now write 't' 

#### Now it will automatically install some packages that is important to create diagram . 

# /quit 

### Now again press 'q' and 
# Now I will ask  'can you create an architecture diagram for s3 website Hosting , with ssl and web security 


### if you are getting error then again copy and paste your question , it will work.


# Now I will ask  'can you create a three tier application architecture diagram with ECS , RDS , VPC and security features in place . 



# If you want to install it into vs code then go to vs code and ---> Extension(amazon q) ---> Install and Restart Extension  --->> Now we will see ... in left mid side click on it and sleect Amazon Q. 


# Install amazonq in ec2 server 

# mkdir kubernetes-mcp
# cd kubernetes-mcp
# q 


## Now if i ask what is kubernetes in one line ?

### Can you tell me what pods are running ? 

### but he didi not which is cluster, pod ?

### So , we have to add mcp server.

# /quit

# cd .aws/amazonq 
# vim mcp.json 

# ### paste these details 
# --------------------------------------------
# {

# 	"mcpServers" : {
    
#  "kubernetes-mcp-server": {
#         "command": "uvx",
#         "args": ["kubernetes-mcp-server@latest"],
#         "env": {
#            "FASTMCP_LOG_LEVEL": "ERROR"
#         }
#    }


# }
# }

#---------------------------------------------------------------

# /quit 

####Now we have to restart it . 

# q 


#####Now we will see servers are loading . Now if you want to see servers then you can use this command .

# /tools 

# !uvx kubernetes-mcp-server@latest 

####Now we will see failed to initialize . Now we will do troubleshoot. 


# Can you make sure the KUBERNETES_MASTER environment is set to run uvx kubernetes-mcp-server@latest


# Can you install kubectl for me .

# yes, please set the ENVIRONMENT_VARIABLE and see if kubernetes-mcp-server works 


####Now we will see our one mcp tool is initialized . 

# /quit 

### Again Restart 

# q 


### Now we will see that our mcp server is initialized . 

# /tools 


### Now we will ask questions 

# which pods are running  in my default namespace 

# Can you create an nginx pod in namespace nginx ?

# Can you ensure the pod is running 

### Now we will see that our Nginx pod is fully running. 


#Can you make sure I can access the pod nginx via browser . 

#### Now we have to add port in our security group which it provides us .
# 



#### Now go to browser and clone this repo. 

# https://github.com/LondheShubham153/online_shopping_app.git


### Create a docker image  otherwise you can use docer image traiwithshubhum/online_shop_app 

### Now on ec2 server 

# Can you create a namespace called online-shop , in that create deployment with 3 replicas and image trainwithshubhum/online_shop_app , the port for container is 80 , make sure to have service as well , deploy the app for me in my kubernetes cluster . 


### Now we will open our application on a new browser . 





