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
        
    sim_0 = Simulation(customers, registers, 0, 1)

    total_time = sim_0.run(1000)

    print(total_time)