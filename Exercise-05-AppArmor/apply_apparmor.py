import docker

client = docker.from_env()

print("Building image from Dockerfile...")
client.images.build(path=".", tag="flask-apparmor")

print("\nChecking Docker AppArmor support...")
info = client.info()
print("Security options:", info.get("SecurityOptions", []))

print("\nStarting container with requested AppArmor profile...")
container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5003},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
        name="flask-apparmor-sdk-test",
    )

    container.reload()
    details = client.api.inspect_container(container.id)
    print("Container started:", container.short_id)
    print("Configured security options:",
          details["HostConfig"].get("SecurityOpt"))
    print("Actual process AppArmor profile:",
          details["AppArmorProfile"])

except docker.errors.APIError as exc:
    print("Docker could not start the container with the requested profile.")
    print("Reason:", exc)

finally:
    if container is not None:
        try:
            container.stop()
        finally:
            container.remove()
        print("Test container cleaned up.")
