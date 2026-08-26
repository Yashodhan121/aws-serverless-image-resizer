# AWS Serverless Image Resizer

## 1. Project Title and Objective

### Project Title
AWS Serverless Image Resizer using S3 and Lambda

### Objective
The objective of this project is to automatically resize images uploaded to an Amazon S3 bucket using AWS Lambda.

When an image is uploaded to the input S3 bucket, an S3 event triggers the Lambda function. The Lambda function downloads the image, resizes it using the Pillow library, and stores the resized image in an output S3 bucket.

This project demonstrates a serverless image-processing workflow using AWS services.

---

## 2. AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- AWS Lambda Layers

### Libraries Used

- Python
- Boto3
- Pillow

---

## 3. Architecture / Workflow

The workflow of the project is:

```text
User
  |
  | Upload Image
  v
S3 Input Bucket
image-resizer-input-yashodhan
  |
  | S3 Object Created Event
  v
AWS Lambda
image-resizer-lambda
  |
  | Download Image
  | Resize Image using Pillow
  |
  v
S3 Output Bucket
image-resizer-output-yashodhan
  |
  +----> large/
          |
          +---- Resized Images
