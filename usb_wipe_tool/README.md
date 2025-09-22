# USB Wipe Tool

A minimal Django demo for safely wiping and formatting removable USB drives on Windows.

## Features
- Detects connected removable USB drives (psutil)
- Lists drive letter, size, filesystem, type
- Dry Run Wipe, Permanent Wipe, Format (FAT32)
- Safety: confirmation required, system drive protected, dry_run default
- Tailwind CSS UI

## Installation
```sh
pip install django psutil
```

## Usage
```sh
python manage.py runserver
```

## WARNING
**Only run on removable drives, NOT system drives!**
- System drive (C:) is protected
- Always confirm drive letter before wiping/formatting
- Demo only wipes first few MB for safety
