class Character:
    def __init__(self, hp, stamina, damage):
        self.hp = hp
        self.stamina = stamina
        self.damage = damage

    # Метод 1: сколько ударов нанесет персонаж, пока не кончится выносливость.
    # Допустим, 1 удар тратит 10 единиц выносливости.
    def calculate_stamina_hits(self) -> int:
        return self.stamina // 10

    def __add__(self, other):
        if type(other) == type(self):
            return f"Оба объекта принадлежат одному классу '{self.__class__.__name__}'"
        return f"Объекты принадлежат разным классам: '{self.__class__.__name__}' и '{other.__class__.__name__}' соответственно"


class WeakEnemy(Character):
    def __init__(self, hp, stamina, damage, exp):
        super().__init__(hp, stamina, damage)
        self.exp = exp  # Уникальное поле: сколько опыта дают за убийство

    # Метод 2: сколько ударов нужно до смерти этого врага
    def hits_to_kill(self, attacker_damage) -> int:
        hits = 0
        current_hp = self.hp
        while current_hp:
            current_hp -= attacker_damage
            hits += 1
        return hits


class Boss(Character):
    def __init__(self, hp, stamina, damage, armor):
        super().__init__(hp, stamina, damage)
        self.armor = armor  # Уникальное поле: защита (броня)

    # Метод 2: сколько ударов нужно до смерти босса (учитываем броню)
    def hits_to_kill(self, attacker_damage):
        real_damage = attacker_damage - self.armor

        if real_damage <= 0:
            return "Босса невозможно убить!"

        hits = 0
        current_hp = self.hp
        while current_hp > 0:
            current_hp -= real_damage
            hits += 1
        return hits


if __name__ == '__main__':
    # hero = Character(100, 50, 15)
    # hero2 = Character(100, 50, 15)
    # slime = WeakEnemy(30, 10, 5, 15)
    # dragon = Boss(100, 100, 30, 5)
    # print(hero + slime)
    # print(hero + hero2)
    pass
