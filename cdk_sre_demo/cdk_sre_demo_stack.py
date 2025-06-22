from aws_cdk import (
    Stack,
    aws_s3 as s3, 
    aws_lambda as _lambda,
)
from constructs import Construct

class CdkSreDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "SreDemoBucket", versioned=True)

        _lambda.Function(
            self, "HelloLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="hello_lambda.handler",
            code=_lambda.Code.from_asset("hello_lambda.zip")
        )