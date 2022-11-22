from cx_Freeze import setup, Executable
base = None
# Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("Algorithme version finale.py", base=base)]
# Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna","itertools","random","tkinter","copy","functools","time","tkinter.ttk"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
# Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Omptim\'flot",
    options = options,
    version = "1.0",
    description = 'Programme d\'optimisation de flot de linge d\'hopital',
    executables = executables
)