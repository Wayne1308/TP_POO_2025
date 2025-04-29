import logging
import random
from typing import Optional

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""
    pass


class Character:
    def __init__(self, name: str):
        self._name = name
        self._life = 100.0  # Vie de base
        self._attack = 20.0  # Dégâts de base
        self._defense = 0.1  # Réduction de dégâts (10%)

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_dead(self) -> bool:
        return self._life <= 0

    def _compute_attack_power(self) -> float:
        """Calcule la puissance d'attaque du personnage"""
        return self._attack

    def _compute_damage_reduction(self, damage_value: float) -> float:
        """Applique la réduction de dégâts liée à la défense"""
        return damage_value * (1 - self._defense)

    def take_damages(self, damage_value: float):
        """Applique les dégâts au personnage en tenant compte de sa défense"""
        damage_taken = self._compute_damage_reduction(damage_value)
        self._life -= damage_taken
        log.info(f"{self.name} took {damage_taken:.2f} damage. Remaining life: {self._life:.2f}")

    def attack(self, target: 'Character'):
        """Attaque une cible et inflige des dégâts"""
        damage = self._compute_attack_power()
        target.take_damages(damage)

    def __str__(self) -> str:
        """Affiche le nom et les points de vie restants du personnage"""
        return f"{self.name} <{self._life:.3f}>"


class Weapon:
    def __init__(self, name: str, attack: float):
        self._name = name
        self._attack = attack

    @property
    def name(self) -> str:
        return self._name

    @property
    def attack_power(self) -> float:
        return self._attack

    @classmethod
    def default(cls) -> 'Weapon':
        """Constructeur alternatif créant une arme par défaut ('Wood stick')"""
        return cls("Wood stick", 1.0)


class Warrior(Character):
    def __init__(self, name: str, weapon: Optional[Weapon] = None):
        super().__init__(name)
        self._life *= 1.5  # Vie x1.5
        self._defense *= 1.2  # Défense x1.2
        self._weapon = weapon if weapon else Weapon.default()

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @property
    def is_raging(self) -> bool:
        """Retourne True si le guerrier a moins de 20% de sa vie de base"""
        return self._life < (100.0 * 0.2 * 1.5)

    def _compute_attack_power(self) -> float:
        """Calcule l'attaque totale (arme + rage éventuelle)"""
        base_attack = self._attack + self._weapon.attack_power
        if self.is_raging:
            base_attack *= 1.2  # Bonus de 20% si en rage
        return base_attack


class Magician(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self._life *= 0.8  # Vie -20%
        self._attack *= 2.0  # Attaque x2

    def _activate_magical_shield(self) -> bool:
        """1 chance sur 3 d'activer un bouclier magique bloquant tous les dégâts"""
        return random.randint(1, 3) == 1

    def take_damages(self, damage_value: float):
        if self._activate_magical_shield():
            log.info(f"{self.name} activated magical shield! No damage taken.")
        else:
            super().take_damages(damage_value)