from pathlib import Path
import subprocess
import sys

EXTENSION = "autd"
SEPARATOR = ";"
GLOBAL = True
BASE_DIR = Path.cwd()

if (GLOBAL == True):
    BASE_DIR = Path(__file__).resolve().parent

def list_autd():
    ficheros = Path(BASE_DIR).iterdir()

    out = f"All saved .{EXTENSION}: \n\t"

    for i in ficheros:
        if i.is_file() and i.name.endswith("." + EXTENSION):
            out += i.name[:-5] + "\n\t"
            
    if out.endswith("\n\t"):
        print(out[:-2])
    else:
        print("Empty")

def add(autd_name, sequence): # Añade y modifica
    archivo = Path(BASE_DIR / f"{autd_name}.{EXTENSION}")

    with archivo.open("w", encoding="utf-8") as f:
        f.write(sequence)

def remove(autd_name):
    archivo = Path(BASE_DIR / f"{autd_name}.{EXTENSION}")

    if archivo.exists():
        archivo.unlink()
    else:
        print(f"{EXTENSION} not found. Use list to list all the saved {EXTENSION}.")

def execute(autd_name):
    archivo = Path(BASE_DIR / f"{autd_name}.{EXTENSION}")

    if archivo.exists():
        with archivo.open("r", encoding="utf-8") as f:
            contenido = f.read()
        
        comandos_separados = contenido.split(SEPARATOR)

        for i in comandos_separados:
            cmd = i.strip()
            subprocess.run(cmd, shell=True, check=True)
    else:
        print("Autd not found. Use list to list all the saved autd.")

def printStructureError(): 
    print(f"Bad command structure. Use this instead: this_command [add/remove/list/exec] [name_of_the_{EXTENSION}] [sequence]", file=sys.stderr)

if __name__ == "__main__":
    args: list[str] = sys.argv
    del args[0]
    args_lenght: int = len(args)

    # print(f"Numero argumentos: {args_lenght}")

    if args_lenght >= 1:
        match args[0]:
            case "list":
                list_autd()
            case "add":
                if args_lenght >= 3:
                    add(autd_name=args[1], sequence=args[2])
                else:
                    printStructureError()
            case "remove":
                remove(autd_name=args[1])
            case "exec":
                execute(autd_name=args[1])

    else:
        printStructureError()