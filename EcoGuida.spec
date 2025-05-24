# main.spec
# -*- mode: python ; coding: utf-8 -*-

import sys
import os
block_cipher = None

# Funzione per gestire il path anche in runtime
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

a = Analysis(
    ['src/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('GUI/*.ui', 'GUI'),                # Include i file .ui
        ('images/*.png', 'images'),        # Include le immagini
    ],
    hiddenimports=[
        'src.text'                          # Import nascosto di text.py
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EcoGuida',                      # Nome del file .exe generato
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                             # Comprime il file finale
    console=False,                        # Metti True se vuoi vedere la console durante l’esecuzione
    icon=resource_path("images/Logo_EcoGuidaNoBG.ico") if os.path.exists(resource_path("images/Logo_EcoGuidaNoBG.ico")) else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='EcoGuida'
)
