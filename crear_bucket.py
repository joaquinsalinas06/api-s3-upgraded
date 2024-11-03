import boto3

def lambda_handler(event, context):
    bucket_name = event['body']['bucket']

    
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)


    
    return {
        'statusCode': 200,
        'mensaje': f'Bucket {bucket_name} creado exitosamente',
        'response': str(response)
    }
