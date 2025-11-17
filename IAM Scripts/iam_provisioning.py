# iam_provisioning.py
import json

users = [
    {"username": "alice", "role": "Admin"},
    {"username": "bob", "role": "Developer"},
    {"username": "carol", "role": "Analyst"}
]

print("Starting provisioning...\n")
for user in users:
    print(f"Provisioning {user['username']} with role {user['role']}")

print("\nProvisioning complete! Users provisioned:")
print(json.dumps(users, indent=4))

