def image_to_text_example(api_url: str) -> [str, str, str]:
    python_code = f"""
import requests

API_URL = "{api_url}"

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, data=data)
    return response.json()

output = query("cats.jpg")
print(output)
       """

    curl_code = f"""
curl  {api_url} \\
    -X POST \\
    --data-binary '@cats.jpg'
       """

    js_code = f"""
async function query(filename) {{
    const data = fs.readFileSync(filename);
    const response = await fetch(
        "{api_url}",
        {{
            method: "POST",
            body: data,
        }}
    );
    const result = await response.json();
    return result;
}}

query("cats.jpg").then((response) => {{
    console.log(JSON.stringify(response));
}});
       """

    return python_code, js_code, curl_code


def asr_example(api_url: str) -> [str, str, str]:
    python_code = f"""
import requests

API_URL = "{api_url}"
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, data=data)
    return response.json()

output = query("sample1.flac")
print(output)
       """

    curl_code = f"""
curl  {api_url}  \\
    -X POST \\
    --data-binary '@sample1.flac'
       """

    js_code = f"""
async function query(filename) {{
    const data = fs.readFileSync(filename);
    const response = await fetch(
        "{api_url}",
       {{
            method: "POST",
            body: data,
        }}
    );
    const result = await response.json();
    return result;
}}

query("sample1.flac").then((response) => {{
    console.log(JSON.stringify(response));
}});
       """

    return python_code, js_code, curl_code


def text_speech_example(api_url: str) -> [str, str, str]:
    python_code = f"""
import requests

API_URL = "{api_url}"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({{
    "inputs": "The answer to the universe is 42",
}})
print(output)
       """

    curl_code = f"""
curl {api_url} \\
    -X POST \\
    -d '{"inputs": "The answer to the universe is 42"}' \\
    -H 'Content-Type: application/json'
       """

    js_code = f"""
async function query(data)  {{
    const response = await fetch(
         "{api_url}",
        {{
            method: "POST",
            body: JSON.stringify(data),
        }}
    );
    const result = await response.json();
    return result;
}}

query({"inputs": "The answer to the universe is 42"}).then((response) =>  {{
    console.log(JSON.stringify(response));
}});
       """

    return python_code, js_code, curl_code


def text_generation_example(api_url: str) -> [str, str, str]:
    def python_test_case(api_url: str) -> str:
        import requests
        API_TOKEN = "HUGGINGFACE_API_TOKEN"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta" # example 
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        data = query({"inputs": "My name is Sarah Jessica Parker but you can call me Jessica"})
        output = data['generated_text']
        print(output)
    
    python_code = f"""
import requests

API_URL = {api_url}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query({"inputs": "My name is Sarah Jessica Parker but you can call me Jessica"})
output = data['generated_text']
print(output)
"""
    curl_code = f"""
    curl {api_url} \
        --header "Content-Type: application/json" \
        -X POST \
        -d '{"inputs":"My name is Sarah Jessica Parker but you can call me Jessica"}'
        """
    js_code = f"""
import fetch from "node-fetch";
async function query(data) {{
    const response = await fetch(
        {api_url},
        {{
            method: "POST",
            body: JSON.stringify(data),
        }}
    );
    const result = await response.json();
    return result;
}}
query({{inputs:"My name is Sarah Jessica Parker but you can call me Jessica"}}).then((response) => {{
    console.log(JSON.stringify(response));
}});
"""
    return python_code, js_code, curl_code

def summarization_example(api_url: str) -> [str, str, str]:
    def test_case():
        import requests
        API_TOKEN = "HUGGINGFACE_API_TOKEN"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        data = query(
            {
                "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
                "parameters": {"do_sample": False},
            }
        )
        result = data[0]['summary_text']
        print(result)
    
    python_code = f"""
        import requests
        
        API_URL = "{api_url}"
        def query(payload):
            response = requests.post(API_URL, json=payload)
            return response.json()
        data = query(
            {
                "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
                "parameters": {"do_sample": False},
            }
        )
        result = data[0]['summary_text']
        print(result)"""
    
    js_code = f"""
        import fetch from "node-fetch";
        
        async function query(data) {{
            const response = await fetch(
                "{api_url}",
                {{
                    method: "POST",
                    body: JSON.stringify(data),
                }}
            );
            const result = await response.json();
            return result;
        }}
        query({{inputs:"The answer to the universe is"}}).then((response) => {{
            console.log(JSON.stringify(response));
        }});"""
    
    curl_code = f"""
    curl {api_url} \
        -X POST \
        -d '{"inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.", "parameters": {"do_sample": false}}' \
        --header "Content-Type: application/json" """
        
    return python_code, js_code, curl_code