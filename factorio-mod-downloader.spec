# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['src\\factorio_mod_downloader\\__main__.py'],
    pathex=[],
    binaries=[],
    datas=[('factorio_downloader.ico', '.')],
    hiddenimports=[
        'customtkinter',
        'playwright',
        'playwright.sync_api',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='factorio-mod-downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['factorio_downloader.ico'],
)