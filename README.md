# 🖼️ AWS Serverless Image Resizer

## 📌 Project Overview

**AWS Serverless Image Resizer** is an event-driven image-processing application built using **Amazon S3, AWS Lambda, Python, Boto3, and Pillow**.

The system automatically resizes images whenever a new image is uploaded to an Amazon S3 input bucket. An S3 event triggers the Lambda function, which processes the image and stores the resized version in a separate output bucket.

This project demonstrates the practical use of **serverless computing and event-driven architecture on AWS**.

---

## 🎯 Objectives

* Automatically resize images uploaded to Amazon S3.
* Trigger AWS Lambda using an S3 Object Created event.
* Process images using Python and Pillow.
* Store processed images in a separate S3 bucket.
* Use IAM for secure AWS resource access.
* Monitor Lambda execution using CloudWatch.

---

## ☁️ AWS Services Used

| AWS Service           | Purpose                            |
| --------------------- | ---------------------------------- |
| **Amazon S3**         | Stores original and resized images |
| **AWS Lambda**        | Performs image resizing            |
| **AWS IAM**           | Provides required permissions      |
| **Amazon CloudWatch** | Monitoring and execution logs      |
| **AWS Lambda Layers** | Provides the Pillow library        |

### Technologies & Libraries

* Python
* Boto3
* Pillow
* Git & GitHub

---

## 🏗️ Architecture

```text
                    User
                     |
                     | Upload Image
                     ↓
          ┌──────────────────────┐
          │   S3 Input Bucket    │
          │ image-resizer-input- │
          │      yashodhan       │
          └──────────┬───────────┘
                     |
                     | Object Created Event
                     ↓
          ┌──────────────────────┐
          │     AWS Lambda       │
          │ image-resizer-lambda │
          │                      │
          │ Python + Boto3       │
          │ Pillow Layer         │
          └──────────┬───────────┘
                     |
                     | Resize Image
                     ↓
          ┌──────────────────────┐
          │   S3 Output Bucket   │
          │ image-resizer-output-│
          │      yashodhan       │
          └──────────┬───────────┘
                     |
                     ↓
                Resized Image

                     |
                     ↓
              CloudWatch Logs
```

---

## 🔄 How It Works

### 1. Upload Image

The user uploads an image to the S3 input bucket:

```text
image-resizer-input-yashodhan
```

### 2. S3 Event Trigger

When the image is uploaded, Amazon S3 generates an **Object Created event**.

### 3. Lambda Execution

The event automatically invokes:

```text
image-resizer-lambda
```

The Lambda function receives the S3 bucket and object information.

### 4. Image Processing

Lambda downloads the image using **Boto3** and uses the **Pillow** library to resize it.

### 5. Store Resized Image

The processed image is uploaded to:

```text
image-resizer-output-yashodhan
```

For example:

```text
image-resizer-output-yashodhan/
└── large/
    └── photo.jpg
```

### 6. Monitoring

Lambda execution information and errors are recorded in **Amazon CloudWatch Logs**.

---

## 🔐 IAM & Security

The Lambda function uses an IAM execution role with permissions required to:

* Read objects from the input S3 bucket.
* Upload objects to the output S3 bucket.
* Create and write CloudWatch logs.

AWS credentials should never be hard-coded or committed to the GitHub repository.

The project follows the **principle of least privilege** wherever possible.

---

## 🧩 Pillow Lambda Layer

The **Pillow** library is used for image processing.

A **Lambda Layer** is configured to provide the Pillow dependency to the Lambda function.

```text
AWS Lambda
     |
     ├── Python Function
     |
     └── Pillow Layer
             |
             ↓
       Image Processing
```

---

## 🧪 Testing

The project was tested using the following workflow:

1. Upload an image to the input S3 bucket.
2. Verify that the S3 event triggers Lambda.
3. Check Lambda execution.
4. Verify that the image is resized successfully.
5. Check the resized image in the output bucket.
6. Verify execution details in CloudWatch Logs.

---

## 📸 Screenshots

The `screenshots/` folder contains project implementation evidence, including:

* S3 input bucket
* Uploaded image
* Lambda function
* S3 event trigger
* Pillow Lambda Layer
* S3 output bucket
* Resized image
* CloudWatch logs

---

## 📂 Repository Structure

```text
aws-serverless-image-resizer/
│
├── screenshots/
│   ├── s3-input-bucket.png
│   ├── lambda-function.png
│   ├── lambda-trigger.png
│   ├── lambda-layer.png
│   ├── s3-output-bucket.png
│   └── cloudwatch-logs.png
│
└── README.md
```

---

## ⭐ Key Features

* ⚡ Fully serverless image processing
* 📤 Automatic S3 event triggering
* 🖼️ Image resizing using Pillow
* 🔄 Automated S3-to-S3 processing
* 🔐 IAM-based access control
* 📊 CloudWatch monitoring
* 💰 No continuously running server required

---

## 🚀 Future Enhancements

* Generate multiple image sizes such as thumbnail, medium, and large.
* Add image compression and format conversion.
* Integrate Amazon API Gateway.
* Use Amazon CloudFront for faster image delivery.
* Add automated deployment using GitHub Actions.
* Implement infrastructure using AWS SAM or Terraform.

---

## 📚 Learning Outcomes

This project provided practical experience with:

**Amazon S3 • AWS Lambda • IAM • CloudWatch • Lambda Layers • Python • Boto3 • Pillow • Serverless Computing • Event-Driven Architecture**

---

## 👨‍💻 Author

**Yashodhan Kolhe**

---
