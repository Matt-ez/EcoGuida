# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import os
from PyInstaller.utils.hooks import collect_data_files

base_path = os.getcwd()

datas = [
    (os.path.join(base_path, 'GUI', '*.ui'), 'GUI'),      # Include tutti i .ui
    (os.path.join(base_path, 'images', '*.png'), 'images'),  # Include le immagini png
    (os.path.join(base_path, 'images', '*.jpg'), 'images'),  # Include le immagini jpg
    (os.path.join(base_path, 'images', '*.ico'), 'images'),  # Include le icone
]

a = Analysis(
    ['app.py'],
    pathex=[base_path],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='EcoGuida',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Lascia True per vedere errori in console
    icon=os.path.join(base_path, 'images', 'Logo_EcoGuida.ico'),
)
