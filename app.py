#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_sre_demo.cdk_sre_demo_stack import CdkSreDemoStack


app = cdk.App()
CdkSreDemoStack(app, "CdkSreDemoStack",
    )

app.synth()
