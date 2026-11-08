import numpy as np

AVAILABLE_REGISTER_TYPES =  ["self-service", "cashier"]

class Register:
    def __init__(self, name : str, type : str):
        self.name = name
        assert type in AVAILABLE_REGISTER_TYPES
        self.type = type


class CustomerType:
    def __init__(self, name : str, available_register_types : list[str], time : int, part : float):
        self.name = name
        self.available_registers = available_register_types
        self.time = time
        self.part = part


class Simulation:
    def __init__(self, customer_types : list[CustomerType], registers : list[Register], check_N_next : int, skip_time_cost : int):
        sum_temp = 0
        for type in customer_types:
            sum_temp = sum_temp + type.part
        assert sum_temp == 1, "Customer types' parts need to sum up to 1"
        self.customers = customer_types
        self.registers = registers
        self.N = check_N_next
        self.skip_time_cost = skip_time_cost

    def run(self, iterations : str = 1000):
        # generate the customers in the queue
        customers = []
        for i in range(iterations):
            customers.append(np.random.choice(self.customers, p=[x.part for x in self.customers]))

        def check_if_customer_fits_register(customer : CustomerType, register : Register):
            return True if register.type in customer.available_registers else False

        def find_next_customer(customers : list[CustomerType], register : Register, wait_for_more_exlusive : bool = True):
            if len(customers) == 0:
                return None, customers, 0
            for i in range(len(customers)):
                if check_if_customer_fits_register(customers[i], register):
                    if wait_for_more_exlusive and len(customers[i].available_registers) > 1:
                        for n in range(self.N):
                            if check_if_customer_fits_register(customers[i+n+1], register) and len(customers[i].available_registers) == 1:
                                chosen = customers.pop(i+n+1)
                                print(n+1)
                                return chosen, customers, n+1
                    chosen = customers.pop(i)
                    return chosen, customers, 0
            return None, customers, 0

        total_time_elapsed = 0
        registers = {x : 0 for x in self.registers}

        while len(customers) > 0 or max(list(registers.values())) > 0:
            # find which registers are available
            available_registers = []
            for reg in self.registers:
                if registers[reg] <= 0:
                    available_registers.append(reg)
            # find the next customer for each available register
            for reg in available_registers:
                chosen_for_reg, customers, total_skips = find_next_customer(customers, reg)
            # add the time for what the register will be occupied
                if chosen_for_reg is not None:
                    registers[reg] = chosen_for_reg.time + total_skips
            # time-passing
            minimum_time_quant = min(x for x in registers.values() if x > 0)
            for reg in self.registers:
                if registers[reg] > 0:
                    registers[reg] -= minimum_time_quant
            total_time_elapsed += minimum_time_quant

        return total_time_elapsed
            

