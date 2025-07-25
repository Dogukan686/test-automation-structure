
import os
import concurrent.futures
import glob

def run_feature(file):
    print(f"Running {file}")
    os.system(f"behave {file}")

if __name__ == "__main__":
    feature_files = glob.glob("features/*.feature")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_feature, feature_files)
