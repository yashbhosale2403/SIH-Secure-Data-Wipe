import subprocess

def format_drive(drive_letter, fs="FAT32"):
    try:
        cmd = ["format", f"{drive_letter}:", f"/FS:{fs}", "/Q", "/Y"]
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return f"✅ {drive_letter}: formatted successfully"
        else:
            return f"❌ Format failed: {result.stderr}"
    except Exception as e:
        return f"❌ Exception: {e}"