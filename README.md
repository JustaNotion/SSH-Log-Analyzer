# SSH-Log-Analyzer
A Python tool which parses SSH authentication logs, counts the log attempts, correctly formats the results, notifies
and provides a warning of multiple failed login attempts. Meant to be used as practice both for creating a script to
notify of brute-force attacks and also parsing through logs. 

The primary purpose of this project was two separate goals:
1. Create a project which would give me an introduction to critical tools within Python
2. Build something which can give me a starting place for any type of log parsing/log analysis.

This was of the earlier projects within my Python learning journey which took a step above basic/simple functions
(calculator, timer, number guesser, etc.). This was an introduction to .split(), indexing and dictionaries
all of which are demonstrated within the project as core components. 

The results are displayed by clearly and directly showing source IP addresses which have 5 failed attempts or more.
Both the attacking IP in addition to the specific number of failed attempts are displayed with a [WARNING] message.

The sample_auth.log included within the project is actually directly sourced from the AWS Serverless log parser project
which can be found here: 

This was one of the earlier projects which eventually became my AWS Serverless log parser. I realized that through the use of AWS services such as S3, DynamoDB and Lambda
I could simulate logs being input into an S3 bucket and displayed as attacking IPs, mimicking an environment and situation which I would encounter as a SOC Analyst.
