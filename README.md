# AWS CDK SRE Demo: Deploying a Lambda Function & S3 Bucket (Python)

This beginner-friendly project shows how to use **AWS CDK (Python)** to deploy:
- An S3 bucket with versioning enabled
- A simple Lambda function in Python

It’s designed for those new to cloud development, DevOps, or Infrastructure as Code (IaC). The full tutorial covers secure IAM setup, CDK bootstrapping, and troubleshooting a real Lambda deployment issue.
This project is designed for beginners and covers secure AWS setup, Infrastructure as Code (IaC), and troubleshooting a common Lambda packaging issue.
**[Read the full project write-up on my portfolio](https://your-portfolio-url.com/aws-cdk-lambda-s3)**

--

## What I Learned
This project builds introductory level hands-on skills that are essential for Cloud, DevOps, and SRE roles:
- Infrastructure as Code (IaC) using AWS CDK (Python)
- Packaging and deploying Lambda functions
- Secure IAM configuration (no root credentials)
- CloudFormation synthesis and asset management
- Troubleshooting CDK deployments and file staging

--

## Why This Project
I created this project to strengthen my portfolio for SRE, DevOps, and cloud engineering roles. With a strong background in Azure, I wanted to see how quickly I could transfer my skills to AWS — completing this in under 6 hours. This project demonstrates my ability to work with AWS CDK, implement security best practices, and troubleshoot infrastructure-as-code challenges—key skills for modern DevOps and SRE roles.

--

## Skills Demonstrated
- AWS CDK (Python)
- Serverless provisioning
- Infrastructure automation
- CloudFormation synthesis & deployment logic

--

## Prerequisites:
- AWS account
- AWS CLI v2
- Python 3.8+ (tested with 3.12)
- Node.js v14+ (tested with v22.16.0 and npm v10.9.2)
- AWS CDK v2 installed: `npm install -g aws-cdk`

--

## Deployment Steps
```bash
# 1. Create and enter project folder
mkdir cdk-sre-demo && cd cdk-sre-demo

# 2. Initialize CDK project in Python
cdk init app --language python

# 3. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Synthesize CloudFormation template (optional but recommended)
cdk synth --profile your-profile

# 6. Deploy stack to AWS using your profile
cdk bootstrap --profile your-profile
cdk deploy --profile your-profile
```

## Confirm Deployment
You can verify the S3 bucket and Lambda function through the AWS Console or CLI. 
Instructions for both are included in the [complete tutorial.]()

### S3 Bucket:
- Go to [S3 Console](https://s3.console.aws.amazon.com/s3/)
- Look for a bucket named `SreDemoBucket...`
- Confirm versioning is enabled

### Lambda Function:
- Go to [Lambda Console](https://console.aws.amazon.com/lambda/)
- Find and test the `HelloLambda` function
- OR run this in terminal:
```bash
  aws lambda list-functions
  aws lambda invoke --function-name <your-function-name> response.json
  cat response.json
```
-- 

## Clean Up
```bash
cdk destroy --profile your-profile
```