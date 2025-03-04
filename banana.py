def max_bananas(initial_bananas, distance, carry_capacity, consumption_rate):
    bananas = initial_bananas
    position = 0
    
    while bananas > 0 and position < distance:
        trips_required = (bananas // carry_capacity) + (1 if bananas % carry_capacity > 0 else 0)
        total_cost = trips_required * consumption_rate

        if bananas <= total_cost:
            break  # No more bananas left after transport
        
        bananas -= total_cost
        position += 1
    
    return bananas

# Parameters
initial_bananas = 3000
distance = 1000
carry_capacity = 1000
consumption_rate = 1

# Compute max bananas delivered
remaining_bananas = max_bananas(initial_bananas, distance, carry_capacity, consumption_rate)
print("Maximum bananas that can reach the market:", remaining_bananas)
