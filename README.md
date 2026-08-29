# 🖼️ AWS Serverless Image Resizer

An automated, serverless image-processing application built using **Amazon S3, AWS Lambda, Python, Boto3, and Pillow**.

The application automatically resizes images whenever a new image is uploaded to an Amazon S3 input bucket. An S3 event triggers an AWS Lambda function, which downloads the image, processes it using the Pillow library, and stores the resized image in a separate S3 output bucket.

---

## 📌 Project Overview

The **AWS Serverless Image Resizer** demonstrates how serverless AWS services can be used to build an event-driven image-processing application without managing traditional servers.

Instead of manually resizing images, the system automatically processes uploaded images.

### Basic workflow

```text
User
 │
 │ Upload Image
 ▼
Amazon S3
Input Bucket
 │
 │ Object Created Event
 ▼
AWS Lambda
 │
 │ Download Image
 │
 │ Resize using Pillow
 ▼
Amazon S3
Output Bucket
 │
 ▼
Resized Image
```

---

# 🎯 Objectives

The main objectives of this project are:

* Automatically process images uploaded to Amazon S3.
* Use S3 events to trigger AWS Lambda.
* Perform image resizing using Python.
* Use the Pillow library for image processing.
* Store processed images in a separate S3 bucket.
* Build a completely serverless image-processing workflow.
* Demonstrate event-driven architecture on AWS.
* Implement appropriate IAM permissions.
* Monitor Lambda execution using Amazon CloudWatch.

---

# ☁️ AWS Services Used

| AWS Service           | Purpose                            |
| --------------------- | ---------------------------------- |
| **Amazon S3**         | Stores original and resized images |
| **AWS Lambda**        | Executes image-resizing logic      |
| **AWS IAM**           | Provides permissions to Lambda     |
| **Amazon CloudWatch** | Monitors Lambda execution and logs |
| **AWS Lambda Layers** | Provides the Pillow dependency     |

---

# 🛠️ Technologies & Libraries

* **Python**
* **Boto3**
* **Pillow (PIL)**
* **Amazon S3**
* **AWS Lambda**
* **AWS IAM**
* **Amazon CloudWatch**

---

# 🏗️ System Architecture

```text
                         👤 USER
                           │
                           │ Upload Image
                           ▼
                ┌─────────────────────┐
                │      Amazon S3      │
                │    Input Bucket     │
                │                     │
                │ image-resizer-      │
                │ input-yashodhan     │
                └──────────┬──────────┘
                           │
                           │ Object Created
                           │ Event
                           ▼
                ┌─────────────────────┐
                │     AWS Lambda      │
                │                     │
                │ image-resizer-      │
                │ lambda              │
                │                     │
                │ Python + Boto3      │
                │ Pillow              │
                └──────────┬──────────┘
                           │
                           │ Resize Image
                           ▼
                ┌─────────────────────┐
                │      Amazon S3      │
                │    Output Bucket    │
                │                     │
                │ image-resizer-      │
                │ output-yashodhan    │
                └──────────┬──────────┘
                           │
                           ▼
                     Resized Image
```

---

# 🔄 Detailed Workflow

## 1. Upload Image

The user uploads an image to the input S3 bucket.

Example:

```text
image-resizer-input-yashodhan
│
└── photo.jpg
```

---

## 2. S3 Event Trigger

When the image is uploaded, Amazon S3 generates an **Object Created** event.

The event invokes the configured AWS Lambda function.

```text
S3 Object Created
        ↓
AWS Lambda Trigger
```

---

## 3. Lambda Receives Event

The Lambda function receives information about:

* S3 bucket name
* Object key
* Uploaded file

The function extracts the bucket and image name from the S3 event.

---

## 4. Download Original Image

Lambda uses **Boto3** to download the image from the input S3 bucket.

```text
S3 Input Bucket
      ↓
   Boto3
      ↓
Lambda temporary storage
```

---

## 5. Resize Image

The Lambda function uses **Pillow** to open and resize the uploaded image.

Conceptually:

```text
Original Image
     ↓
Pillow
     ↓
Resize
     ↓
Processed Image
```

The resizing operation is performed inside the Lambda function.

---

## 6. Upload Resized Image

After processing, the resized image is uploaded to the output S3 bucket.

Example:

```text
image-resizer-output-yashodhan
│
└── large/
    └── photo.jpg
```

---

## 7. Monitor Execution

Amazon CloudWatch automatically records Lambda execution logs.

CloudWatch can be used to verify:

* Lambda execution
* Successful processing
* Errors
* Execution messages
* Function activity

---

# 📂 S3 Bucket Structure

## Input Bucket

```text
image-resizer-input-yashodhan
│
├── image1.jpg
├── image2.png
└── image3.jpeg
```

The input bucket contains the original uploaded images.

---

## Output Bucket

```text
image-resizer-output-yashodhan
│
└── large/
    ├── image1.jpg
    ├── image2.png
    └── image3.jpeg
```

The output bucket stores the processed/resized images.

---

# ⚡ AWS Lambda Function

The Lambda function is responsible for the main image-processing logic.

### Function

```text
image-resizer-lambda
```

### Runtime

```text
Python
```

### Main responsibilities

1. Receive S3 event.
2. Identify uploaded image.
3. Download image from S3.
4. Open image using Pillow.
5. Resize image.
6. Save processed image.
7. Upload resized image to output S3 bucket.
8. Generate execution logs.

---

# 🧩 Pillow Lambda Layer

The **Pillow** library is used because standard AWS Lambda Python runtimes do not necessarily include Pillow by default.

A Lambda Layer is therefore used to provide the required image-processing dependency.

```text
AWS Lambda
     │
     ├── Python Function
     │
     └── Pillow Layer
             │
             ▼
       Image Processing
```

This keeps the Lambda function code separate from the external dependency.

---

# 🔐 IAM Permissions

The Lambda execution role requires appropriate permissions to interact with Amazon S3 and CloudWatch.

The permissions should follow the **principle of least privilege**.

Typical permissions include:

### Input Bucket

```text
s3:GetObject
```

Allows Lambda to read uploaded images.

### Output Bucket

```text
s3:PutObject
```

Allows Lambda to upload resized images.

### CloudWatch Logs

```text
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
```

Allows Lambda to create execution logs.

---

# 📊 Monitoring

Amazon CloudWatch is used for monitoring the Lambda function.

The Lambda execution logs can be inspected through:

```text
AWS Lambda
    ↓
Monitor
    ↓
CloudWatch Logs
```

Example log flow:

```text
Lambda execution started
        ↓
S3 event received
        ↓
Image downloaded
        ↓
Image resized
        ↓
Resized image uploaded
        ↓
Lambda execution completed
```

---

# 🧪 Testing

The project was tested using an image upload to the S3 input bucket.

### Test Procedure

#### Step 1

Upload an image:

```text
photo.jpg
```

to:

```text
image-resizer-input-yashodhan
```

#### Step 2

S3 generates the Object Created event.

#### Step 3

Lambda is automatically triggered.

#### Step 4

Lambda processes the image using Pillow.

#### Step 5

The resized image is uploaded to:

```text
image-resizer-output-yashodhan/large/
```

#### Step 6

Verify the processed image in the output bucket.

#### Step 7

Check CloudWatch logs to confirm successful Lambda execution.

---

# 📸 Screenshots

The repository contains a `screenshots/` folder containing project evidence.

Recommended screenshots include:

### 1. Input S3 Bucket

Shows the input bucket created for uploading original images.

### 2. Uploaded Image

Shows an image uploaded to the input bucket.

### 3. Lambda Function

Shows the configured `image-resizer-lambda` function.

### 4. Lambda Trigger

Shows the S3 Object Created trigger configured for Lambda.

### 5. Lambda Layer

Shows the Pillow dependency configured through a Lambda Layer.

### 6. Output S3 Bucket

Shows the processed image in the output bucket.

### 7. Resized Image

Shows the resulting resized image.

### 8. CloudWatch Logs

Shows successful Lambda execution and image-processing logs.

These screenshots provide evidence that the complete event-driven workflow is working.

---

# 📁 Repository Structure

```text
aws-serverless-image-resizer/
│
├── screenshots/
│   ├── s3-input-bucket.png
│   ├── lambda-function.png
│   ├── lambda-trigger.png
│   ├── lambda-layer.png
│   ├── s3-output-bucket.png
│   ├── resized-image.png
│   └── cloudwatch-logs.png
│
└── README.md
```

> The exact screenshot filenames may differ from the final files uploaded to the repository.

---

# 💰 Why Serverless?

This project uses a serverless architecture instead of a continuously running EC2 server.

### Traditional Architecture

```text
User
 ↓
EC2 Server
 ↓
Application
 ↓
Image Processing
 ↓
Storage
```

This requires managing a server even when there are no image-processing requests.

### Serverless Architecture

```text
User
 ↓
S3
 ↓
Lambda
 ↓
S3
```

Lambda executes only when the event occurs.

### Benefits

* No server management
* Event-driven execution
* Automatic scaling
* Reduced infrastructure management
* Suitable for occasional workloads
* Easy integration with AWS services

---

# 🔒 Security Considerations

AWS resources should be configured using the minimum permissions required.

Important security practices:

* Do not hard-code AWS access keys.
* Do not upload AWS credentials to GitHub.
* Use IAM roles for Lambda.
* Follow least-privilege permissions.
* Restrict S3 access appropriately.
* Enable logging for troubleshooting.
* Avoid unnecessary public access to S3 buckets.

---

# ⚠️ Important S3 Event Consideration

The input and output buckets are separated intentionally.

```text
Input Bucket
     ↓
Lambda
     ↓
Output Bucket
```

This helps prevent the Lambda function from repeatedly triggering itself when it uploads the processed image.

If the same bucket is used for both input and output without appropriate filtering, an upload performed by Lambda could generate another S3 event and potentially create a recursive invocation loop.

---

# 🚀 Future Enhancements

The project can be extended with additional functionality.

### 1. Multiple Image Sizes

Generate different versions:

```text
small/
medium/
large/
```

---

### 2. API Integration

Add Amazon API Gateway:

```text
Client
  ↓
API Gateway
  ↓
Lambda
  ↓
S3
```

---

### 3. CloudFront

Add Amazon CloudFront for faster global delivery of processed images.

---

### 4. Automatic Image Optimization

The application could automatically:

* Compress images
* Convert formats
* Optimize JPEG/PNG files
* Generate thumbnails

---

### 5. Infrastructure as Code

The AWS infrastructure could be automated using:

* AWS CloudFormation
* Terraform
* AWS SAM

---

### 6. CI/CD

GitHub Actions could be added to automatically deploy Lambda code when changes are pushed to the repository.

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

* AWS Lambda
* Amazon S3
* S3 Event Notifications
* IAM roles and policies
* Lambda Layers
* Python
* Boto3
* Pillow
* CloudWatch
* Serverless architecture
* Event-driven architecture
* Image processing
* AWS cloud deployment

---

# 📈 Project Architecture Summary

```text
                 ┌──────────────┐
                 │     User     │
                 └──────┬───────┘
                        │
                        │ Upload Image
                        ▼
              ┌────────────────────┐
              │   S3 Input Bucket  │
              └─────────┬──────────┘
                        │
                  Object Created
                        │
                        ▼
              ┌────────────────────┐
              │    AWS Lambda     │
              │                    │
              │ Python + Boto3     │
              │ Pillow Layer       │
              └─────────┬──────────┘
                        │
                   Resize Image
                        │
                        ▼
              ┌────────────────────┐
              │  S3 Output Bucket │
              │                    │
              │      /large/       │
              └─────────┬──────────┘
                        │
                        ▼
                 Resized Image

                        │
                        ▼
              ┌────────────────────┐
              │   CloudWatch Logs  │
              └────────────────────┘
```

---

# 📌 Project Status

| Component             | Status       |
| --------------------- | ------------ |
| S3 Input Bucket       | ✅ Completed  |
| S3 Output Bucket      | ✅ Completed  |
| Lambda Function       | ✅ Completed  |
| S3 Event Trigger      | ✅ Completed  |
| Pillow Layer          | ✅ Completed  |
| IAM Permissions       | ✅ Configured |
| Image Processing      | ✅ Completed  |
| Output Image Storage  | ✅ Completed  |
| CloudWatch Monitoring | ✅ Configured |
| Testing               | ✅ Completed  |
| Screenshots           | ✅ Added      |
| GitHub Documentation  | ✅ Completed  |

---

# 👨‍💻 Author

**Yashodhan Kolhe**

---
