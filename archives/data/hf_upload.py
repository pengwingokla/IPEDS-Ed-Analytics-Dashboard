from huggingface_hub import HfApi
import os
api = HfApi(token=os.getenv("HF_TOKEN"))

def upload_enrollment_data():
    ENRL_PATH = "data/processed/enrollment.csv"
    ENRL_FILE = "enrollment.csv"
    
    api.upload_file(
        path_or_fileobj=ENRL_PATH,
        path_in_repo=ENRL_FILE,
        repo_id="chloecodes/IPEDS_ENROLLMENT",
        repo_type="dataset"
    )

def upload_graduation_data():
    GRAD_PATH = "data/processed/graduation.csv"
    GRAD_FILE = "graduation.csv"
    
    api.upload_file(
        path_or_fileobj=GRAD_PATH,
        path_in_repo=GRAD_FILE,  # Specifies where to save the file in the HuggingFace repo
        repo_id="chloecodes/IPEDS_GRADUATION",
        repo_type="dataset"
    )

if __name__ == "__main__":
    upload_enrollment_data()
    # upload_graduation_data()