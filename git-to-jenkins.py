import argparse
import os
print("I am from git to jenkins pipeline")
print("I am latest version ")



parser = argparse.ArgumentParser(description='Process some strings.')

parser.add_argument('-I',help="please pass the input string")
parser.add_argument('-O',help="please pass the output string")
parser.add_argument('-awsp',help="please pass the output string")

args = parser.parse_args()

print(f"{args.I}{args.O}")

#print(f"aws configureation :{os.system("aws configure list")}")
#os.environ["AWS_ACCESS_KEY_ID"] = "AKIATYIPWP4CLF3G2ZVO"
#os.environ["AWS_SECRET_ACCESS_KEY"] = args.awsp


# Check if AWS_SECRET_ACCESS_KEY is provided
# if args.awsp is not None:
#     # Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
#     os.environ["AWS_ACCESS_KEY_ID"] = "AKIATYIPWP4CLF3G2ZVO"
#     os.environ["AWS_SECRET_ACCESS_KEY"] = args.awsp
#     print("Environment variables set successfully.")
# else:
#     print("AWS_SECRET_ACCESS_KEY not provided. Please provide a value.")

os.system("aws configure list")
os.system("aws s3 ls humanetics-bucket-nov-15")

