import csv
import random
import time


class Simulation:
    def __init__(self, sim_max: int, cost_file: str, benefit_file: str):
        self.__cost_file = cost_file
        self.__benefit_file = benefit_file
        self.__sim_max = sim_max
        self.__cost_list = []
        self.__cost_prob_list = []

        self.__benefit_list = []
        self.__benefit_prob_list = []

    @property
    def cost_file(self):
        return self.__cost_file

    @property
    def benefit_file(self):
        return self.__benefit_file

    def read_costs_file(self):
        with open(self.cost_file, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                min_max_list = []
                self.__cost_list.append(int(row[0]))
                min_max_list.extend([float(row[1]), float(row[2])])
                self.__cost_prob_list.append(min_max_list)


    def read_benefit_file(self):
        with open(self.benefit_file, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                min_max_list = []
                self.__benefit_list.append(int(row[0]))
                min_max_list.extend([float(row[1]), float(row[2])])
                self.__benefit_prob_list.append(min_max_list)

    def run_simulation(self):
        start_time = time.time()
        overall_total_cost = self.calculate_costs()
        overall_total_benefit = self.calculate_benefits()
        if (overall_total_cost <= overall_total_benefit):
            print("Project Approved")
        else:
            print("Project not approved")

        print("Time required for code to execute in milli-seconds", 1000 * (time.time() - start_time))


    def calculate_costs(self):
        overall_total_cost = 0
        total_average_cost = []
        for cost in self.__cost_list:
            cost_total = 0
            for _ in range(0, self.__sim_max - 1):
                # using the cost as an index identifier, get the cost_min and cost_max, [min, max]
                cost_total = cost_total + cost * random.uniform(self.__cost_prob_list[self.__cost_list.index(cost)][0],
                                                                self.__cost_prob_list[self.__cost_list.index(cost)][1])
            average_cost = cost_total / self.__sim_max
            total_average_cost.append(average_cost)
        for average_cost in total_average_cost:
            overall_total_cost += average_cost

        print(f"Total cost is ${overall_total_cost}")
        return overall_total_cost

    def calculate_benefits(self):
        overall_total_benefit = 0
        total_average_benefit = []
        for benefit in self.__benefit_list:
            benefit_total = 0
            for _ in range(0, self.__sim_max - 1):
                # using the cost as an index identifier, get the benefit_min and benefit_max, [min, max]
                benefit_total = benefit_total + benefit * random.uniform(
                    self.__benefit_prob_list[self.__benefit_list.index(benefit)][0],
                    self.__benefit_prob_list[self.__benefit_list.index(benefit)][1])
            average_benefit = benefit_total / self.__sim_max
            total_average_benefit.append(average_benefit)
        for average_benefit in total_average_benefit:
            overall_total_benefit += average_benefit

        print(f"Total benefit is ${overall_total_benefit}")
        return overall_total_benefit


def main():
    simulation1 = Simulation(100000, "Costs - Sheet1.csv", "Benefits - Sheet1.csv")
    simulation1.read_costs_file()
    simulation1.read_benefit_file()
    simulation1.run_simulation()


if __name__ == "__main__":
    main()
