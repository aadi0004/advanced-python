# 🐘 1.1 Setup RDS PostgreSQL
# Go to AWS RDS → Create PostgreSQL instance.

# Note the following:

# Endpoint = host

# Username, Password, DB Name

# Allow public access (0.0.0.0/0) in RDS security group (temporarily) for connection testing.

# Enable port 5432 in EC2 security group too.

# ☁️ 5.2 Setup EC2 instance
# Launch EC2 (Ubuntu)

# SSH into EC2

# Install Docker:


# sudo apt-get update 
# sudo apt-get install docker.io -y
# sudo usermod -aG docker $USER && newgrp docker


# 🧱 Step 6: Deploy Docker App to EC2

# git clone <your_repo>
# git clone https://github.com/1602saurab/poster.git


# 🐳 6.2 Build and run Docker image

# cd your-project-folder
# docker build -t query_bot_app .
# docker run -d -p 8501:8501 --env-file .env query_bot_app


# 🌍 Step 7: Access App from Browser
# Open browser and go to:
# http://<EC2-PUBLIC-IP>:8501


#### but how i check my data is stored in postgresql or not ?????????

# In EC2 Server 

# sudo apt install postgresql-client -y
# psql -h database-1.cwdmo62sqr3o.us-east-1.rds.amazonaws.com -U postgres -d postgres -p 5432

# Enter your password : 


#### SQL query to list databases(This will give you a clean list of all available databases)

# SELECT datname FROM pg_database;


###To switch to a database:

# \c your_database_name


#### Then list tables:
# \dt

##### Describe Table Structure (See Columns)
# \d query_logs

#### Then view your data:
# SELECT * FROM query_logs;


#### Count Total Number of Queries Stored
# SELECT COUNT(*) FROM query_logs;

#### View Most Recent Queries(This shows the 5 most recent entries.)
# SELECT * FROM query_logs ORDER BY created_at DESC LIMIT 5;


### Exit PostgreSQL
# \q
