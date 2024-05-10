
from openai import AzureOpenAI, OpenAI

client_args = {
            "api_key": "api_key",
            "organization": None,
            "api_version": None,
            "azure_endpoint": None,
            "base_url": "base_url"
        }

client_args = {k: v for k, 
               v in client_args.items() if v is not None}

print(OpenAI(**client_args))