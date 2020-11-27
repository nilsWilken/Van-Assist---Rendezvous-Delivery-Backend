import docker

client = docker.from_env()

containers = client.containers.list(all="true", filters={"ancestor": "vanassistwebservice:1.0"})
for container in containers:
    container.stop()
    container.remove()

client.containers.prune()


vanassistubuntu_found = False

images = client.images.list()
for img in images:
    if len(img.tags) < 1:
        continue
    elif img.tags[0] == "vanassistubuntu:1.0":
        vanassistubuntu_found = True

if vanassistubuntu_found == False:
    client.images.build(path="./VanAssistUbuntu", tag="vanassistubuntu:1.0", rm="true")

client.images.build(path=".", tag="vanassistwebservice:1.0", rm="true")

client.containers.run(image="vanassistwebservice:1.0", ports={"8000/tcp":"8000"}, detach="false", mem_limit="6g", restart_policy={"Name":"on-failure", "MaximumRetryCount":5})

images = client.images.list()
for img in images:
    if len(img.tags) < 1:
        client.images.remove(image=img.id)