from WildCatZoo import Lion, Tiger, Cheetah, Vet, Keeper, Caretaker
from WildCatZoo.animal import Animal
class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for el in self.workers:
            if el.name == worker_name:
                self.workers.remove(el)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        for el in self.workers:
            sum_salaries += el.salary
        if sum_salaries <= self.__budget:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_amount = 0
        for animal in self.animals:
            tend_amount += animal.money_for_care
        if tend_amount <= self.__budget:
            self.__budget -= tend_amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_list = []
        tigers_list = []
        cheetahs_list = []
        for el in self.animals:
            if isinstance(el, Lion): # type(el) == Lion
                lions_list.append(el)
            elif isinstance(el, Tiger):
                tigers_list.append(el)
            elif isinstance(el, Cheetah):
                cheetahs_list.append(el)

        result = f"You have {len(self.animals)} animals" + "\n" + f"----- {len(lions_list)} Lions:" + "\n"
        for el in lions_list:
            result += repr(el) + "\n"
        result += f"----- {len(tigers_list)} Tigers:" + "\n"
        for el in tigers_list:
            result += repr(el) + "\n"
        result += f"----- {len(cheetahs_list)} Cheetahs:"
        for el in cheetahs_list:
            result += "\n" + repr(el)
        return result

    def workers_status(self):
        caretaker_list = []
        keeper_list = []
        vet_list = []
        for el in self.workers:
            if isinstance(el, Caretaker):
                caretaker_list.append(el)
            elif isinstance(el, Keeper):
                keeper_list.append(el)
            elif type(el) == Vet:
                vet_list.append(el)

        result = f"You have {len(self.workers)} workers" + "\n"

        result += f"----- {len(keeper_list)} Keepers:" + "\n"
        for el in keeper_list:
            result += repr(el) + "\n"

        result += f"----- {len(caretaker_list)} Caretakers:" + "\n"
        for el in caretaker_list:
            result += repr(el) + "\n"

        result += f"----- {len(vet_list)} Vets:"
        for el in vet_list:
            result += "\n" + repr(el)
        return result