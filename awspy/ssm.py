import boto3


class ssm:
    def __init__(self) -> None:
        cli = boto3.client('ssm')
        self.cli = cli

    def getParameter(self, name):
        res = self.cli.get_parameter(
            Name=name,
            WithDecryption=True
        )
        return res
