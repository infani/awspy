import boto3


def discover_instances(namespace: str, service: str):
    client = boto3.client('servicediscovery')
    res = client.discover_instances(
        NamespaceName=namespace,
        ServiceName=service,
    )
    return res