# logwatch-py

Analyseur de logs Linux en CLI, orienté détection SOC.
Développé dans un contexte de montée en compétences DevSecOps.

## Fonctionnalités
- Lecture et parsing de fichiers auth.log
- Détection de patterns suspects (bruteforce SSH, escalade sudo...)
- [à compléter au fil des features]

## Stack
Python 3.x — stdlib uniquement (argparse, dataclasses, re)

## Usage
```bash
python logwatch.py --file /var/log/auth.log
```

## Structure
├── logwatch.py     # point d'entrée CLI
├── logentry.py     # dataclass LogEntry
└── tests/

## Objectif
Projet pratique pour consolider Linux, parsing de logs et logique SOC