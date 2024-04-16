# Wykop API Client

This is a Python client library for accessing the Wykop API v3. It simplifies the process of making HTTP requests to the Wykop API and handles authentication and token management.

## Getting Started

Before you can use this library, you need to obtain your API credentials (app key and secret) from Wykop.

### Obtaining API Credentials

1. Go to the Wykop Developer Dashboard: [Wykop API Dashboard](https://dev.wykop.pl/dashboard/app)
2. Create a new application if you haven't done so already.
3. Note down the `app_key` and `secret` provided after the application registration process.

## Installation

Install the package via pip:

```bash
pip install wykop
```

## Usage

Here's how you can use the `WykopAPI` client in your Python projects:

### Importing the library

```python
from wykop import WykopAPI
```

### Initializing the client

To start making requests to the Wykop API, you need to instantiate the client with your credentials:

```python
api = WykopAPI(app_key='your_app_key', secret='your_secret')
```

### Authenticating

To perform authenticated requests, first call the `authenticate` method:

```python
api.authenticate()
```

### Making requests

After authenticating, you can make requests to the API. For example, to fetch data from a specific endpoint:

```python
response = api.make_request('/some_endpoint', method='GET')
print(response)
```

### Closing the client

It's important to close the HTTP client when you're done:

```python
api.close()
```

## Example

Here is a full example of using the Wykop API client:

```python
def main():
    app_key = 'your_app_key'
    secret = 'your_secret'
    api = WykopAPI(app_key, secret)
    try:
        api.authenticate()
        response = api.make_request('/tags/popular-user-tags', method='GET')
        print(response)
    finally:
        api.close()

if __name__ == "__main__":
    main()
```


## output
```bash
{'data': [{'name': 'misteriusowybot'}, {'name': 'kuponynazywo'}, {'name': 'gearbestkupony'},
{'name': 'anonimowemirkowyznania'}, {'name': 'mirkoanonim'}, {'name': 'chinskacebulakupony'},
{'name': 'pustulkowelaptopy'}, {'name': 'grzewczy'}, {'name': 'otwartywykopmobilny'}, 
{'name': 'lowcychin'}]}
```
## Support

For issues, questions, or contributions, please use the GitHub repository associated with this package.

