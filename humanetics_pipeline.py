import boto3
import argparse
import sagemaker
from sagemaker import get_execution_role
from sagemaker.processing import ProcessingInput, ProcessingOutput, ScriptProcessor
from sagemaker.estimator import Estimator
from sagemaker.workflow.parameters import ParameterInteger, ParameterString
from sagemaker.workflow.steps import ProcessingStep, TrainingStep
from sagemaker.workflow.pipeline import Pipeline



def pipeline(role_arn=None,bucket=None,processing_script=None,utils_folder=None,processing_image=None,training_image=None,pipeline_name=None,raw_data=None,processing_instance=None,training_instance=None,training_data=None,model_name=None,feature_name=None):
    # Set up SageMaker session and role
    sagemaker_session = sagemaker.Session()

    # Set the SageMaker execution role ARN
    #role_arn = "arn:aws:iam::258267840260:role/service-role/SageMaker-sagemaker_custom_nov10_v1"

    # Define parameters for your pipeline
    input_data = ParameterString(name="InputData", default_value=raw_data)
    #output_model = ParameterString(name="OutputModel", default_value="s3://humanetics-bucket-nov-15/model_logs/")
    instance_type = ParameterString(name="InstanceType", default_value=training_instance)
    training_instance_count = ParameterInteger(name="InstanceCount", default_value=1)

    # Step 1: Data Preprocessing
    processing_repository_uri = processing_image
    script_processor = ScriptProcessor(
        command=["python3"],
        image_uri=processing_repository_uri,
        role=role_arn,  # Specify the SageMaker execution role ARN here
        instance_count=1,
        instance_type=processing_instance,
    )

    processing_step = ProcessingStep(
        name="DataPreprocessing",       
        code=processing_script,
        processor=script_processor,
        inputs=[ProcessingInput(source=input_data, destination="/opt/ml/processing/input"),
                ProcessingInput(source=utils_folder, destination="/opt/ml/processing/input/code/utils")],
        outputs=[ProcessingOutput(output_name="train_data", source="/opt/ml/processing/output")],        
        job_arguments=[
        "--bucket_name",bucket, 
            ],
    )

    # Step 2: Model Training
    training_image_uri = training_image
    estimator = Estimator(
        image_uri=training_image_uri,
        role=role_arn,  # Specify the SageMaker execution role ARN here
        instance_count=training_instance_count,
        instance_type=instance_type,
        hyperparameters={
        "bucket": bucket,
        "model_name": model_name,
        "feature": feature_name
    }
    )

    training_step = TrainingStep(
        name="ModelTraining",
        estimator=estimator,
        inputs={"training": f"{training_data}"},
        depends_on=[processing_step.name]
    )

    # Create the SageMaker pipeline
    pipeline = Pipeline(
        name=pipeline_name,
        #parameters=[input_data, output_model, instance_type, training_instance_count],
        parameters=[input_data, instance_type, training_instance_count],
        steps=[processing_step, training_step],
    )

    # Execute the pipeline
    pipeline.upsert(role_arn=role_arn)
    execution = pipeline.start(
        parameters=dict(
            InputData=raw_data,
            #OutputModel="s3://humanetics-bucket-nov-15/model_logs/",
            InstanceType=training_instance,
            InstanceCount=1,
        )
    )

    # Wait for the pipeline execution to complete
    execution.wait()

if __name__=="__main__":
    arguments=argparse.ArgumentParser(description='Process some strings.')
    arguments.add_argument('-s3_bucket',help="please give you valid bucket name")
    arguments.add_argument('-p',help="please give you valid processing script ")
    arguments.add_argument('-u',help="please give you valid utils path ")
    arguments.add_argument('-r',help="please give you valid role arn")
    arguments.add_argument('-pu',help="please give you valid processing uri ")
    arguments.add_argument('-tu',help="please give you valid train uri ")
    arguments.add_argument('-pn',help="please give you valid pipeline  name")
    arguments.add_argument('-rd',help="please give you valid raw data path ")
    arguments.add_argument('-pi',help="please give you valid processing instance name") 
    arguments.add_argument('-ti',help="please give you valid training instance ")
    arguments.add_argument('-prd',help="please give you valid training data ")
    arguments.add_argument('-f',help="please give you feature training data ")
    arguments.add_argument('-m',help="please give you model name")

    args=arguments.parse_args()
    pipeline(args.r,args.s3_bucket,args.p,args.u,args.pu,args.tu,args.pn,args.rd,args.pi,args.ti,args.prd,args.f,args.m)


