import boto3
from moto import mock_aws
def main():
    # Use mock IAM as a context manager
    with mock_aws():
        iam = boto3.client("iam", region_name="us-east-1")

        users = ["alice", "bob", "carol"]

        for user in users:
            try:
                iam.create_user(UserName=user)
                print(f"Created user: {user}")
            except Exception as e:
                print(f"Error creating user {user}: {e}")

        # List users to simulate AWS Console view
        response = iam.list_users()
        print("\nCurrent IAM Users:")
        for u in response['Users']:
            print(f"- {u['UserName']}")

if __name__ == "__main__":
    main()
