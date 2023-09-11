# Description
An AWS Lambda function written in Python that calculates the distance between a pair of coordinates and the football club San Lorenzo. It can be used with AWS API Gateway or other services.

# Installation
1. Install Python 3.11 or a newer version.
2. Create a directory named package and run `pip install --target ./package sympy`.
3. Copy the file `lambda_function.py` to the `package` directory.
4. Select all files in the directory and compress them into a .zip file. 
5. In AWS Lambda console create a new function and upload the .zip file.
6. Add the Layer `AWS SDK for pandas` to the Lambda function.