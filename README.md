# 🛡️ TP POO Fighters - Simulation de combat

Ce projet est une implémentation en Python d’un jeu de combat tour par tour orienté objet, développé dans le cadre du TP de Programmation Orientée Objet (POO).

## 📚 Objectif

Faire s'affronter des personnages (guerriers et magiciens) en simulant un combat automatisé. Le projet illustre les principes de l'héritage, du polymorphisme, de l'encapsulation et de la surcharge.

## ⚔️ Règles du jeu

- Un combat commence avec au moins 2 personnages.
- À chaque tour :
  - L'ordre des personnages est mélangé.
  - Chaque personnage vivant attaque tous les autres.
- Le combat se termine si :
  - Tous les combattants sont morts.
  - Un seul survivant reste (il gagne).
- Un personnage meurt s’il atteint 0 point de vie.

## 👥 Personnages

Chaque personnage hérite de la classe `Character` et possède :
- `vie` : 100 points (base)
- `attaque` : 20 points (base)
- `défense` : 10 % (base)

### 🛡️ Guerrier (Warrior)

- Vie ×1.5, Défense ×1.2
- Peut s’équiper d’une `arme` (attaque bonus)
- Entre en état de **rage** si sa vie < 20 % → +20 % d’attaque

### 🔮 Magicien (Magician)

- Vie ×0.8, Attaque ×2
- 1 chance sur 3 d’activer un **bouclier magique** bloquant tous les dégâts

## 🗡️ Armes (`Weapon`)

- Possèdent un nom et une puissance d’attaque
- Si non précisée, une arme par défaut "Wood stick" (1 dégât) est utilisée

## 🧪 Lancer la simulation

```bash
python EXO2_final_TP.py
