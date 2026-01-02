"""
===========================================================
Mini-projet P3-C1 — Sécurité Informatique
Simulation et analyse des logiciels malveillants 
===========================================================

"""

import os
import threading
import time
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import sys

# ===========================================================
# CONFIGURATION GLOBALE
# ===========================================================

SAFE_MODE = "--safe" in sys.argv

BASE_DIR = Path.home() / ".malware_simulation"
LOG_FILE = BASE_DIR / "malware_log.txt"

SIMULATED_TARGETS = [
    Path.home() / "Desktop",
    Path.home() / "Documents"
]

# ===========================================================
# OUTILS DE LOG
# ===========================================================

def write_log(message: str):
    """Écrit un message horodaté dans le fichier de logs"""
    BASE_DIR.mkdir(exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# ===========================================================
# PARTIE MALVEILLANTE (SIMULÉE)
# ===========================================================

class MalwareSimulation:
    """
    Classe représentant le comportement d'un malware moderne
    TOUS les comportements sont simulés
    """

    def run(self):
        write_log("=== DÉMARRAGE DE LA SIMULATION MALVEILLANTE ===")
        self.simulate_persistence()
        self.simulate_duplication()
        self.simulate_file_scan()
        self.simulate_ransomware()
        self.simulate_propagation()
        write_log("=== FIN DE LA SIMULATION MALVEILLANTE ===")

    def simulate_persistence(self):
        """Simulation de persistance au démarrage"""
        write_log("Simulation de persistance au démarrage")
        write_log(
            "Le malware se copierait dans le dossier de démarrage "
            "(AUCUNE COPIE RÉELLE EFFECTUÉE)"
        )
        time.sleep(1)

    def simulate_duplication(self):
        """Simulation de duplication dans des emplacements stratégiques"""
        write_log("Simulation de duplication")
        fake_locations = [
            Path.home() / "Desktop" / "system_update.exe",
            Path.home() / "Documents" / "security_patch.exe"
        ]
        for loc in fake_locations:
            write_log(f"Copie simulée vers : {loc}")
        time.sleep(1)

    def simulate_file_scan(self):
        """Simulation d'analyse des fichiers utilisateur"""
        write_log("Début du scan des fichiers utilisateur")
        for target in SIMULATED_TARGETS:
            write_log(f"Analyse du dossier : {target}")
            if target.exists():
                for file in target.glob("*"):
                    write_log(f"Fichier détecté : {file.name}")
        write_log("Fin du scan des fichiers")
        time.sleep(1)

    def simulate_ransomware(self):
        """Simulation d'un comportement ransomware"""
        write_log("Simulation du comportement ransomware")
        write_log(
            "Les fichiers suivants seraient renommés avec l'extension '.encrypted'"
        )
        for target in SIMULATED_TARGETS:
            if target.exists():
                for file in target.glob("*"):
                    write_log(f"{file.name} → {file.name}.encrypted (SIMULÉ)")
        write_log("AUCUN FICHIER N'A ÉTÉ MODIFIÉ")
        time.sleep(1)

    def simulate_propagation(self):
        """Simulation de propagation"""
        write_log("Simulation de propagation locale")
        fake_nodes = ["USB_Device", "Shared_Folder", "Backup_Drive"]
        for node in fake_nodes:
            write_log(f"Propagation simulée vers : {node}")
        time.sleep(1)

# ===========================================================
# PARTIE LÉGITIME — CALCULATRICE
# ===========================================================

class CalculatorApp:
    """Calculatrice améliorée avec meilleure UX"""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.resizable(False, False)

        self.expression = ""

        self.entry = tk.Entry(
            root,
            font=("Consolas", 20),
            bd=8,
            relief=tk.RIDGE,
            justify="right",
            width=18
        )
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ('C', 1, 0), ('⌫', 1, 1), ('(', 1, 2), (')', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(
                root,
                text=text,
                width=5,
                height=2,
                font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, padx=4, pady=4)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.update_entry()
        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.update_entry()
        elif char == "=":
            self.calculate()
        else:
            self.expression += char
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate(self):
        try:
            # Sécurité minimale : caractères autorisés uniquement
            if not all(c in "0123456789+-*/(). " for c in self.expression):
                raise ValueError("Expression non autorisée")

            result = eval(self.expression)
            self.expression = str(result)
            self.update_entry()
        except Exception:
            messagebox.showerror("Erreur", "Expression invalide")
            self.expression = ""
            self.update_entry()


# ===========================================================
# LANCEMENT DE L'APPLICATION
# ===========================================================

def start_malware_simulation():
    """Lance la simulation dans un thread séparé"""
    malware = MalwareSimulation()
    malware.run()

def main():
    if not SAFE_MODE:
        write_log("Application lancée en MODE NORMAL")
        t = threading.Thread(target=start_malware_simulation, daemon=True)
        t.start()
    else:
        print("Application lancée en MODE SAFE (simulation désactivée)")

    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
