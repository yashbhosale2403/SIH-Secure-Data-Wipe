import os
import psutil
from django.shortcuts import render, redirect
from .secure_wipe import wipe_drive
from .format_device import format_drive

SYSTEM_DRIVE = 'C:'

def index(request):
    drives = []
    for part in psutil.disk_partitions():
        if 'removable' in part.opts or part.fstype == '':
            try:
                usage = psutil.disk_usage(part.mountpoint)
                drives.append({
                    'letter': part.device[:2],
                    'mountpoint': part.mountpoint,
                    'size': usage.total,
                    'filesystem': part.fstype,
                    'type': 'Removable' if 'removable' in part.opts else 'Unknown',
                })
            except Exception:
                continue
    return render(request, 'index.html', {'drives': drives})

def wipe(request):
    if request.method == 'POST':
        drive_letter = request.POST.get('drive_letter')
        confirm = request.POST.get('confirm')
        method = request.POST.get('method', 'zero')
        dry_run = request.POST.get('dry_run', 'true') == 'true'
        passes = int(request.POST.get('passes', 1))
        if drive_letter.upper() == SYSTEM_DRIVE:
            msg = '❌ Cannot wipe system drive!'
        elif confirm != drive_letter:
            msg = '❌ Confirmation does not match drive letter.'
        else:
            msg = wipe_drive(drive_letter, method=method, passes=passes, dry_run=dry_run)
        return render(request, 'result.html', {'message': msg})
    return redirect('index')

def format_view(request):
    if request.method == 'POST':
        drive_letter = request.POST.get('drive_letter')
        confirm = request.POST.get('confirm')
        fs = request.POST.get('fs', 'FAT32')
        if drive_letter.upper() == SYSTEM_DRIVE:
            msg = '❌ Cannot format system drive!'
        elif confirm != drive_letter:
            msg = '❌ Confirmation does not match drive letter.'
        else:
            msg = format_drive(drive_letter, fs=fs)
        return render(request, 'result.html', {'message': msg})
    return redirect('index')