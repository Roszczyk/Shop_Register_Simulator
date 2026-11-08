from simulation import Simulation, CustomerType, Register, AVAILABLE_REGISTER_TYPES

if __name__ == "__main__":
    regular_customer = CustomerType("regular", AVAILABLE_REGISTER_TYPES, 10, 0.7)
    hotdog_customer = CustomerType("hotdog", ["cashier"], 40, 0.15)
    alcohol_customer = CustomerType("alcohol", ["cashier"], 10, 0.15)

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
        simulation_results[N] = simulations[N].run(10000)

    print(simulation_results)