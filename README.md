# aws-glue-crawlflow

aws-glue-crawlflow helps you to run AWS Glue Crawler automatically.

## Description

AWS Services what to be called are below.

- AWS Lambda
- Amazon SQS
- AWS Step Functions
- AWS Glue

![aws-glue-crawlflow](https://github.com/tosh223/aws-glue-crawlflow/blob/master/drawio/aws-glue-crawlflow.svg)

## Install

This app is created to be deployed by AWS SAM(Serverless Application Model).

To install the AWS SAM CLI, see following pages.

[Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

```bash
git clone https://github.com/tosh223/aws-glue-crawlflow.git
cd ./aws-glue-crawlflow
sam build
sam deploy --guided
```

## Usage

Call a Lambda function 'enqueue_glue_crawlflow' with event like below.

```json
{
    "CrawlerName": "your-crawler-name",
    "WaitTime": "60",
    "CheckCount": "0"
}
```

## References

[Invoke Lambda with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-lambda.html)

[Glueの使い方的な⑦(Step Functionsでジョブフロー)](https://qiita.com/pioho07/items/f8a2fd946fc391f89c97)

