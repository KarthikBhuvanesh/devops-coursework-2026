import docker

client = docker.from_env()
container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        detach=True,
        name="flask-apparmor-restriction-test",
        security_opt=["apparmor=my-apparmor-profile"],
    )

    container.reload()
    details = client.api.inspect_container(container.id)

    print("Container started:", container.short_id)
    print("Configured security options:",
          details["HostConfig"].get("SecurityOpt"))
    print("Actual AppArmor profile:",
          details["AppArmorProfile"] or "(not reported)")

    for description, command in [
        ("Read /etc/passwd", ["cat", "/etc/passwd"]),
        ("Execute /bin/bash", ["/bin/bash", "-c", "echo bash-executed"]),
    ]:
        result = container.exec_run(command)
        print(f"\n{description}")
        print("Exit code:", result.exit_code)
        print("Output:", result.output.decode(errors="replace").strip())

    print("\nNote: These results do not prove AppArmor enforcement.")

except docker.errors.APIError as exc:
    print("Docker API error:", exc)

finally:
    if container is not None:
        try:
            container.stop()
        finally:
            container.remove()
        print("\nTest container cleaned up.")
