""" from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) """

#!/usr/bin/env python3
import sys
print(sys.path)

import docker
print(docker.__version__)


client = docker.from_env()

client.containers.run(
    "gitlab/gitlab-ce:latest",
    detach=True,
    hostname="gitlab.example.com",
    ports={
        '443/tcp': 443,
        '80/tcp': 80,
        '22/tcp': 22
    },
    name="gitlab",
    restart_policy={"Name": "always"},
    volumes={
        "C:/Users/steve/gitlab/config": {'bind': '/etc/gitlab', 'mode': 'rw'},
        "C:/Users/steve/gitlab/logs": {'bind': '/var/log/gitlab', 'mode': 'rw'},
        "C:/Users/steve/gitlab/data": {'bind': '/var/opt/gitlab', 'mode': 'rw'}
    }
)

print("GitLab container started")