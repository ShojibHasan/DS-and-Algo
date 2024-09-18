import boto3

def lambda_handler(event, context):
    source_bucket = event['source_bucket']
    prefix = event['processed_prefix']
    target_bucket = event['target_bucket']
    target_key = event['target_key']

    s3 = boto3.client('s3')

    response = s3.list_objects_v2(Bucket=source_bucket, Prefix=prefix)
    files = sorted([obj['Key'] for obj in response['Contents']], key=lambda x: x)

    combined_file_path = '/tmp/combined_file'
    with open(combined_file_path, 'wb') as combined_file:
        for file_key in files:
            obj = s3.get_object(Bucket=source_bucket, Key=file_key)
            combined_file.write(obj['Body'].read())

    s3.upload_file(Filename=combined_file_path, Bucket=target_bucket, Key=target_key)

    return {
        'statusCode': 200,
        'body': f"Successfully combined files into {target_key} in {target_bucket}"
    }