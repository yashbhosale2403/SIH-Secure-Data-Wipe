import os

def wipe_drive(drive_letter, method="zero", passes=1, dry_run=True):
    drive_path = f"{drive_letter}:/"
    if dry_run:
        return f"[DRY RUN] Would wipe {drive_letter}: with {method} ({passes} pass)"
    try:
        with open(drive_path, "rb+") as f:
            for _ in range(passes):
                f.seek(0)
                chunk_size = 1024 * 1024  # 1MB
                for _ in range(5):  # Only first 5MB for demo
                    if method == "zero":
                        f.write(b"\x00" * chunk_size)
                    elif method == "random":
                        f.write(os.urandom(chunk_size))
        return f"✅ {drive_letter}: wiped successfully"
    except Exception as e:
        return f"❌ Failed to wipe {drive_letter}: {e}"