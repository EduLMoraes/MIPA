from cx_Freeze import setup, Executable

includes = [
    'tkinter',
    'src.views.window',
    'src.views.functions',
    'extract.extract',
    'PyPDF2',
    'gtts',
    'time',
    'PIL',
    'io',
    'requests'
]


setup(
    name = "MIPA",
    version = "1.0",
    description = "Esse aplicativo transforma os arquivos pdf do usuário em audio",
     options={
        'build_exe': {
            'includes': includes
        }
    },
    executables = [Executable('main.py')]
)