Question = [
    ["Which of the following is a key benefit of using Amazon S3 for storing data?", "Unlimited storage capacity", "Low-latency data retrieval", "Automatic data encryption", "Real-time data analytics", "3"],
    ["Which AWS service is used to launch and manage virtual servers in the cloud?", "Amazon S3", "AWS Lambda", "Amazon EC2", "Amazon RDS", "3"],
    ["What does the \"R\" stand for in the AWS service \"Amazon RDS\"?", "Reliable", "Redundant", "Real-time", "Remote", "1"],
    ["Which AWS service can be used to distribute content globally and improve website performance?", "Amazon CloudFront", "AWS Glacier",  "AWS Snowball", "Amazon Route 53", "1"],
    ["What does the acronym \"IAM\" stand for in AWS?", "Internet Access Management", "Identity and Access Management", "Infrastructure Authentication Model", "Intelligent Authorization Mechanism", "2"],
    ["Which AWS service provides a fully managed, scalable, and serverless data warehouse?", "Amazon S3", "Amazon RDS", "AWS Redshift", "AWS Glue", "3"],
    ["What AWS service is used to create and manage virtual private networks (VPNs) in the cloud?", "Amazon VPC", "Amazon EC2", "AWS Direct Connect", "Amazon Route 53", "1"],
    ["Which AWS service is designed for building, training, and deploying machine learning models at scale?", "Amazon S3", "AWS Lambda", "Amazon Redshift", "Amazon SageMaker", "4"],
    ["What is the primary purpose of AWS CloudTrail?", "Monitoring CPU utilization of EC2 instances", "Analyzing network traffic patterns", "Auditing and tracking API activity", "Managing database backups", "3"],
    ["Which AWS service can be used to automatically scale EC2 instances based on demand?", "AWS Lambda", "Amazon EC2 Auto Scaling", "AWS Elastic Beanstalk", "Amazon Route 53", "2"]
]
Level = [ "10,00,000", "20,00,000", "30,00,000", "40,00,000", "50,00,000", "60,00,000", "70,00,000", "80,00,000", "90,00,000", "1,00,00,000",]
# Level = "10,00,000"
num = 1
Money = 0
print("Welcome in KBC...")

for i in range(0, len(Question)):
    question = Question[i]
    print(f"\n\nQ{num}. {question[0]}")
    reply = input(f"1. {question[1]}\n2. {question[2]}\n3. {question[3]}\n4. {question[4]}\nEnter your answer (1-4) or 0 to quit: ")
    num = num + 1
    if reply == question[5]:
        print(f"Answer is correct. And you have won Rs. {Level[i]}")
        if i == 2:
            Money = Level[i]
        elif i == 6:
            Money = Level[i]
        elif i == 9:
            print(f"\n\nCongratulations....!, your take home money is Rs. {Level[i]}")
    elif reply == "0":
        print(f"You quit now and Your take home money is Rs. {Level[i-1]} ")
        break
    else:
        print(f"Wrong Answer. And your take home money is Rs. {Money}")
        break
    