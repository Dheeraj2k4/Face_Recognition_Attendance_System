import redis

# Connect to Redis Client
# hostname = 'redis-18195.c301.ap-south-1-1.ec2.redns.redis-cloud.com'
# portnumber = 18195
# password = 'XThqqtHKksOod1ICKRkhPoeVAufi0DUB'
hostname = 'redis-18549.c322.us-east-1-2.ec2.redns.redis-cloud.com'
portnumber = 18549
password = '0CMhOIkl2gHDzNWiMnIvPgEtDpDhBheB'
r = redis.StrictRedis(host=hostname,
                      port=portnumber,
                      password=password)

# Simulated Logs
with open('simulated_logs.txt', 'r') as f:
    logs_text = f.read()

encoded_logs = logs_text.split('\n')

# Push into Redis database
r.lpush('attendance:logs', *encoded_logs)
