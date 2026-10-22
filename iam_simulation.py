
users = {
    "user-1": "S3-Support",
    "user-2": "EC2-Support",
    "user-3": "EC2-Admin"
}

permissions = {
    "S3-Support": [
        "s3:ListAllMyBuckets",
        "s3:ListBucket",
        "s3:GetObject"
    ],
    "EC2-Support": [
        "ec2:DescribeInstances"
    ],
    "EC2-Admin": [
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances"
    ]
}

tests = [
    "s3:ListAllMyBuckets",
    "ec2:DescribeInstances",
    "ec2:StartInstances",
    "ec2:StopInstances"
]

for user, group in users.items():
    print(f"\n{user} ({group})")

    for action in tests:
        status = (
            "ALLOWED"
            if action in permissions[group]
            else "DENIED"
        )
        print(f"{action}: {status}")
