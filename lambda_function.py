import json
import requests

def lambda_handler(event, context):
    try:
        # Example GET request
        response_get = requests.get('https://api.example.com/resource')
        data_get = response_get.json()
        print("GET request response:", data_get)

        # Example POST request
        payload_post = {'key1': 'value1', 'key2': 'value2'}
        response_post = requests.post('https://api.example.com/resource', json=payload_post)
        data_post = response_post.json()
        print("POST request response:", data_post)

        # Example PUT request
        payload_put = {'key1': 'new_value1'}
        response_put = requests.put('https://api.example.com/resource/1', json=payload_put)
        data_put = response_put.json()
        print("PUT request response:", data_put)

        # Example DELETE request
        response_delete = requests.delete('https://api.example.com/resource/1')
        data_delete = response_delete.json() if response_delete.content else {"message": "Resource deleted"}
        print("DELETE request response:", data_delete)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'get_response': data_get,
                'post_response': data_post,
                'put_response': data_put,
                'delete_response': data_delete
            })
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
