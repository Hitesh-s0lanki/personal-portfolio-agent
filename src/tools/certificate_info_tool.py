import json
import os

def certificate_info_tool():
    """
    Helps in Certificates-related queries by reading JSON data from 'project.json'
    and returning it as a stringified JSON.
    """
    path = os.path.join(os.getcwd(), 'src/public/certificates.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Convert back to a JSON-formatted string
    return json.dumps(data)
