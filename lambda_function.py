```python
import boto3
import urllib.parse
import os
from PIL import Image

s3 = boto3.client("s3")

OUTPUT_BUCKET = "image-resizer-output-yashodhan"
OUTPUT_FOLDER = "large"

# Resize dimensions
MAX_WIDTH = 800
MAX_HEIGHT = 800


def lambda_handler(event, context):

    try:
        # Get bucket and object information from S3 event
        source_bucket = event["Records"][0]["s3"]["bucket"]["name"]
        source_key = urllib.parse.unquote_plus(
            event["Records"][0]["s3"]["object"]["key"]
        )

        print(f"Source bucket: {source_bucket}")
        print(f"Source image: {source_key}")

        # Get file name
        file_name = os.path.basename(source_key)

        # Temporary files in Lambda
        input_path = f"/tmp/{file_name}"
        output_path = f"/tmp/resized_{file_name}"

        # Download original image
        print("Downloading image from S3...")
        s3.download_file(
            source_bucket,
            source_key,
            input_path
        )

        # Open image using Pillow
        print("Opening image...")
        image = Image.open(input_path)

        # Convert image if necessary
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Resize image while maintaining aspect ratio
        image.thumbnail((MAX_WIDTH, MAX_HEIGHT))

        # Save resized image
        print("Resizing image...")
        image.save(output_path, quality=85)

        # Output object key
        output_key = f"{OUTPUT_FOLDER}/{file_name}"

        # Upload resized image
        print("Uploading resized image...")
        s3.upload_file(
            output_path,
            OUTPUT_BUCKET,
            output_key,
            ExtraArgs={
                "ContentType": "image/jpeg"
            }
        )

        print(
            f"Successfully uploaded resized image: "
            f"s3://{OUTPUT_BUCKET}/{output_key}"
        )

        return {
            "statusCode": 200,
            "body": "Image resized successfully"
        }

    except Exception as e:

        print(f"Error processing image: {str(e)}")

        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
```
