import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket']
    directory = event['body']['directory']
    file_name = event['body']['file_name']
    
    s3 = boto3.client('s3')
    with open(directory, 'rb') as fileu:
        s3.upload_fileobj(fileu, bucket_name, file_name)
    
    return {
        'statusCode': 200,
        'mensaje': f'Archivo {file_name} subido al bucket {bucket_name}'
    }
