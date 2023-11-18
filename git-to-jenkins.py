import os
print("I am from git to jenkins pipeline")
print("I am latest version ")
#print(f"aws configureation :{os.system("aws configure list")}")
os.system("aws configure list")
os.system("aws s3 ls humanetics-bucket-nov-15")

