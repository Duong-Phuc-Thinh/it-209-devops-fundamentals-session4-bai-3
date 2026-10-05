import subprocess
import sys

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Lỗi: {e.stderr.strip()}"

def check_git_status():
    print("--- Kiểm tra Cấu hình Git ---:\n")
    
    remote_url = run_git_command(["git", "remote", "-v"])
    print("Remote URLs:")
    print(remote_url if remote_url else "Chưa cấu hình remote repository.")
    print("\n")
    
    status = run_git_command(["git", "status"])
    print("Trạng thái Git:")
    print(status)

if __name__ == "__main__":
    print("Bắt đầu kiểm tra cấu hình dự án GitHub SSH...\n")
    check_git_status()
