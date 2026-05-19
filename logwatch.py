import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="logwatch-py — analyseur de logs Linux orienté SOC"
    )
    parser.add_argument(
        "--file",
        required=True,
        help="Chemin vers le fichier de log à analyser"
    )
    return parser.parse_args()


def read_log(filepath: str) -> list:
    """Lit un fichier log et retourne une liste de lignes brutes."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        print(f"[+] {len(lines)} lignes lues dans {filepath}")
        return lines
    except FileNotFoundError:
        print(f"[!] Erreur : fichier '{filepath}' introuvable", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"[!] Erreur : permission refusée pour '{filepath}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    args = parse_args()
    lines = read_log(args.file)
    for line in lines[:20]: # affiche les 20 premières pour tester
        print(line.strip())