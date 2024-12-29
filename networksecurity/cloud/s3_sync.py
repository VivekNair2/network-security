import os


class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command=f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)
        
    def sync_folder_to_s3(self,folder,aws_bucket):
        command=f"aws s3 sync {folder} {aws_bucket}"
        os.system(command)