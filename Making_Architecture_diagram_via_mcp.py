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



