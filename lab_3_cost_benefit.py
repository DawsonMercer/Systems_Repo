import random
import time


def costs():
    cost_1 = 10000
    cost_2 = 250000
    cost_3 = 134000
    cost_4 = 1200000
    cost_5 = 40000
    cost_6 = 120000
    cost_7 = 4000000
    cost_list = [cost_1, cost_2, cost_3, cost_4, cost_5, cost_6, cost_7]
    return cost_list


def cost_probability_list():
    #             [min, max]
    cost_1_prob = [0.10, 0.30]
    cost_2_prob = [0.20, 0.90]
    cost_3_prob = [0.05, 0.40]
    cost_4_prob = [0.10, 1.0]
    cost_5_prob = [0.40, 0.75]
    cost_6_prob = [0.0, 0.50]
    cost_7_prob = [0.005, 0.50]
    cost_prob_list = [cost_1_prob,cost_2_prob, cost_3_prob, cost_4_prob, cost_5_prob, cost_6_prob, cost_7_prob]
    return cost_prob_list


def benefits():
    benefit_1 = 10000
    benefit_2 = 250000
    benefit_3 = 134000
    benefit_4 = 1200000
    benefit_5 = 400000
    benefit_6 = 120000
    benefit_7 = 4000000
    benefit_8 = 2000000
    benefit_list = [benefit_1, benefit_2, benefit_3, benefit_4, benefit_5, benefit_6, benefit_7, benefit_8]
    return benefit_list


def benefit_probability_list():
    benefit_1_prob = [0.10, 0.30]
    benefit_2_prob = [0.20, 0.90]
    benefit_3_prob = [0.05, 0.40]
    benefit_4_prob = [0.10, 1.0]
    benefit_5_prob = [0.10, 0.75]
    benefit_6_prob = [0.0, 0.50]
    benefit_7_prob = [0.50, 0.70]
    benefit_8_prob = [0.10, 0.80]
    benefit_prob_list = [benefit_1_prob, benefit_2_prob, benefit_3_prob, benefit_4_prob, benefit_5_prob, benefit_6_prob, benefit_7_prob, benefit_8_prob]
    return benefit_prob_list


def calculate_costs(cost_list, cost_prob_list, sim_max):
    # # for testing against Shavaji
    #
    # c1 = 75000
    # c2 = 10000
    # # For cost 1 .It means that the probability of cost element c1 could vary from 0.30 to 0.90
    # cp1_min = 0.30
    # cp1_max = 0.90
    # # cost 2
    # cp2_min = 0.20
    # cp2_max = 0.95
    # cost_list = [c1, c2]
    # cost_prob_list = [[cp1_min, cp1_max], [cp2_min, cp2_max]]

    overall_total_cost = 0
    total_average_cost = []
    for cost in cost_list:
        cost_total = 0
        for _ in range(0, sim_max-1):
            #using the cost as an index identifier, get the cost_min and cost_max, [min, max]
            cost_total = cost_total + cost * random.uniform(cost_prob_list[cost_list.index(cost)][0],
                                                            cost_prob_list[cost_list.index(cost)][1])
        average_cost = cost_total/sim_max
        # print(cost_total)
        # print(average_cost)
        # print(cost_prob_list[cost_list.index(cost)][0], cost_prob_list[cost_list.index(cost)][1])
        total_average_cost.append(average_cost)
    for average_cost in total_average_cost:
        overall_total_cost += average_cost

    print(f"Total cost is ${overall_total_cost}")
    return overall_total_cost


def calculate_benefits(benefit_list, benefit_prob_list, sim_max):
    overall_total_benefit = 0
    total_average_benefit = []
    for benefit in benefit_list:
        benefit_total = 0
        for _ in range(0, sim_max - 1):
            # using the cost as an index identifier, get the benefit_min and benefit_max, [min, max]
            benefit_total = benefit_total + benefit * random.uniform(benefit_prob_list[benefit_list.index(benefit)][0],
                                                            benefit_prob_list[benefit_list.index(benefit)][1])
        average_benefit = benefit_total / sim_max
        # print(cost_total)
        # print(average_cost)
        # print(cost_prob_list[cost_list.index(cost)][0], cost_prob_list[cost_list.index(cost)][1])
        total_average_benefit.append(average_benefit)
    for average_benefit in total_average_benefit:
        overall_total_benefit += average_benefit

    print(f"Total benefit is ${overall_total_benefit}")
    return overall_total_benefit

def calculate_costs_shavaji():
    # for testing against Shavaji
    sim_max = 100000
    c1 = 75000
    c2 = 10000
    # For cost 1 .It means that the probability of cost element c1 could vary from 0.30 to 0.90
    cp1_min = 0.30
    cp1_max = 0.90
    # cost 2
    cp2_min = 0.20
    cp2_max = 0.95
    cost_total_1 = 0
    cost_total_2 = 0

    for ind in range(0, sim_max - 1):

        cost_total_1 = cost_total_1 + c1 * random.uniform(cp1_min, cp1_max)
        cost_total_2 = cost_total_2 + c2 * random.uniform(cp2_min, cp2_max)

    average_cost_1 = cost_total_1 / sim_max
    average_cost_2 = cost_total_2 / sim_max
    total_cost = average_cost_1 + average_cost_2
    print("Total shavaji cost is $", total_cost)


def main():
    start_time = time.time()
    sim_max = 100000
    cost_list = costs()
    cost_prob_list = cost_probability_list()


    benefit_list = benefits()
    benefit_prob_list = benefit_probability_list()

    overall_total_cost = calculate_costs(cost_list, cost_prob_list, sim_max)
    overall_total_benefit = calculate_benefits(benefit_list, benefit_prob_list, sim_max)
    if (overall_total_cost <= overall_total_benefit):
        print("Project Approved")
    else:
        print("Project not approved")

    print("Time required for code to execute in milli-seconds", 1000*(time.time()-start_time))
    # calculate_costs_shavaji()


if __name__ == "__main__":
    main()
