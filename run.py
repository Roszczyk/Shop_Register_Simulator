from simulation import Simulation, CustomerType, Register, AVAILABLE_REGISTER_TYPES
from visualise import plot_simulation_results

if __name__ == "__main__":
    regular_customer = CustomerType("regular", AVAILABLE_REGISTER_TYPES, 10, 0.7)
    hotdog_customer = CustomerType("hotdog", ["cashier"], 40, 0.15)
    alcohol_customer = CustomerType("alcohol", ["cashier"], 10, 0.15)

    TEST_SAMPLE = 10000
    REPEAT_EXPERIMENT = 10

    customers = [regular_customer, hotdog_customer, alcohol_customer]

    registers = [
        Register("cashier", "cashier"),
        Register("self-service", "self-service")
    ]

    simulations = {}

    for N in range(11):
        simulations[N] = Simulation(customers, registers, N, 1)
        

    simulation_results = {}

    for N in simulations.keys():
        temp_sum = 0
        for i in range(REPEAT_EXPERIMENT):
            temp_sum += simulations[N].run(TEST_SAMPLE)
        simulation_results[N] = temp_sum / REPEAT_EXPERIMENT

    plot_simulation_results(simulation_results, TEST_SAMPLE)