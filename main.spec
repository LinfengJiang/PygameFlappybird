# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['read_ini.py', './Mulitplayer/database.py', './Mulitplayer/high_score.py', './Mulitplayer/IDgenerate.py', './Mulitplayer/last_score.py', './Mulitplayer/register.py', 'C:\\Users\\MC\\Desktop\\PygameTest'],
             binaries=[],
             datas=[('resource','resource')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='resource\\icon.ico')
