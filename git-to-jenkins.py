import argparse
#import os
print("I am from git to jenkins pipeline")
print("I am latest version ")



parser = argparse.ArgumentParser(description='Process some strings.')

parser.add_argument('-I',help="please pass the input string")
parser.add_argument('-O',help="please pass the output string")

args = parser.parse_args()

print(f"{args.I}{args.O}")

#print(f"aws configureation :{os.system("aws configure list")}")
#os.system("aws configure list")
#os.system("aws s3 ls humanetics-bucket-nov-15")

