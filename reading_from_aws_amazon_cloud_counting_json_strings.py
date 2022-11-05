import base64
import gzip
import boto3
import io

aws_access_key_id = base64.b64decode("QUtJQTJEUlFGREdLMzM1UVVFSFc=".encode()).decode()
aws_secret_access_key = base64.b64decode("MFVmMEVyc1gyRE9QRGtGVmdGM3FWZmM4T1AwQVRtem9zdjFTcmNZRA==".encode()).decode()

bucket_name = "sample-log-data-028a9a4884211e5c6"
key = "example.log.gz"

# Your code here
s3 = boto3.resource('s3', aws_secret_access_key=aws_secret_access_key, aws_access_key_id=aws_access_key_id)
obj = s3.Object(bucket_name, key)
buf = io.BytesIO(obj.get()["Body"].read())  # Reads whole gz file into memory

json_strings = []
counter_curly_braces = 0  # Check for single json string using open and close curly brace counter
concatenate_str_json = ""
file = gzip.GzipFile(fileobj=buf)

for line in gzip.GzipFile(fileobj=buf):
    line = line.decode()
    line = ' '.join(line.split())  # As needed by assert

    for char_ in line:
        if char_ == "{":
            counter_curly_braces += 1

        elif char_ == "}":
            counter_curly_braces -= 1
            if counter_curly_braces == 0:
                concatenate_str_json += "}"
                json_strings.append(concatenate_str_json)
                concatenate_str_json = ""
        if counter_curly_braces > 0:
            concatenate_str_json += char_
            if char_ == ",":
                concatenate_str_json += ' '

# now instantiate the services
assert len(json_strings) == 21

first_json_string = json_strings[0]
assert first_json_string.startswith('{"FleetId": "fleet-xxx", "Errors": []')
assert first_json_string.endswith(', "RetryAttempts": 0}}')

last_json_string = json_strings[-1]
assert last_json_string.startswith('{"Resources": ["i-xxx"]')
assert last_json_string.endswith('"Value": "xxx-78"}]}')
