import boto3
import base64

def lambda_handler(event, context):
    bucket_name = event['body']['bucket']
    file_name = event['body']['file_name']
    file_content = base64.b64decode(event['body']['file_content'])
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    
    return {
        'statusCode': 200,
        'mensaje': f'Archivo {file_name} subido al bucket {bucket_name}'
    }
