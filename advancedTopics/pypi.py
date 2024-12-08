"""
    Modules ->
        - single file with .py extension
        - contains definitions and statements
        - imported using 'import moduleName'
    Packages ->
        - collection of related modules
        - imported using 'import moduleName'
        - distributable with PyPi
            cmd command to show what can I do: pip
            cmd command to install new package: pip install somePackageName
            cmd command to show witch packages I have: pip list
            packages site: pypi.org
"""
import pulsar
import requests

response = requests.get("https://www.google.com")
print(response)

pulsar_client = pulsar.Client("pulsar://localhost:6650")
