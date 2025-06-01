import requests
import os
from typing import Dict, Any

def api_get_response(
    endpoint:str,
    headers:Dict[str, Any] = None,
    params:Dict[str, Any] = None,
):
    try:
        response = requests.get(endpoint, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Warning: Could not get response successfully, {response}")
        return response.json()
    except Exception as e:
        raise Exception(f"Error: {e}") 