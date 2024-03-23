import subprocess

def install_requirements():
    try:
        subprocess.check_call(["pip", "install", "-r", "public/requirements.txt"])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing requirements:", e)
        raise

if __name__ == "__main__":
    install_requirements()