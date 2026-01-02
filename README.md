# 🛡️ Simulation et analyse des logiciels malveillants

Mini-projet réalisé dans le cadre du cours **Sécurité Informatique (P3-C1)**.  
Ce projet a pour objectif de **simuler de manière pédagogique, locale et inoffensive** le comportement d’un malware moderne, tout en conservant une application légitime pleinement fonctionnelle.

---

## 🎯 Objectif du projet

L’objectif principal est de montrer qu’un logiciel malveillant ne commence généralement pas par attaquer directement, mais par **se faire passer pour une application normale et utile**.

Dans ce projet :
- L’application visible est une **calculatrice fonctionnelle**
- En arrière-plan, des **comportements malveillants sont simulés**
- Aucune action réelle dangereuse n’est effectuée
- Tout est journalisé pour analyse

---

## 🧩 Fonctionnalités

### ✅ Partie légitime
- Calculatrice simple avec interface graphique (Tkinter)
- Fonctionnement normal et fluide pour l’utilisateur
- Indépendante de la partie malveillante simulée

### ⚠️ Partie malveillante (simulation uniquement)
Les comportements suivants sont **simulés** et **journalisés** :

- **Simulation de persistance**  
  Indique où le programme se relancerait au démarrage du système

- **Simulation de duplication**  
  Copie fictive vers des emplacements stratégiques

- **Simulation de scan des fichiers utilisateur**  
  Analyse des dossiers Desktop et Documents (lecture des noms uniquement)

- **Simulation de ransomware**  
  Liste des fichiers qui seraient renommés avec l’extension `.encrypted`  
  (aucune modification réelle)

- **Simulation de propagation**  
  Propagation fictive vers des nœuds comme :
  - USB_Device
  - Shared_Folder
  - Backup_Drive

- **Journalisation complète**  
  Toutes les actions sont enregistrées avec timestamp dans un fichier de logs
---
## 📄 Fichier de logs

Un fichier `malware_log.txt` est créé dans un dossier dédié.  
```bash
~/.malware_simulation/malware_log.txt
Il contient :
- La date et l’heure de chaque action simulée
- Le détail des étapes du scénario d’attaque
- Aucune donnée sensible ni modification réelle

Ce fichier permet une **analyse pédagogique et forensic** du comportement simulé.

---

## 🔐 Mode sécurisé

Le projet intègre un **mode sécurisé** permettant d’exécuter uniquement la calculatrice.

```bash
python calculatrice.py --safe


## 📁 Structure du projet

