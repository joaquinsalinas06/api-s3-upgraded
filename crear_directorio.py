import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket']
    dir_name = event['body']['directory']
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=f'{dir_name}/')
    
    return {
        'statusCode': 200,
        'mensaje': f'Directorio {dir_name} creado en el bucket {bucket_name}'
    }
