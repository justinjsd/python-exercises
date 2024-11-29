# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name, password):
        super().__init__(name)
        self.__password = password

    def check__password(self, password):
        if password != self.__password:
            raise ValueError("Wrong Password")

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        self.check__password(password)
        super().add_ingredient(ingredient, amount)
        
    def print_recipe(self, password: str):
        self.check__password(password)
        super().print_recipe()

if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")
    diminuendo.print_recipe("Random Password")