def ground_cost(weight):
  if weight <= 2.0:
    price_per_pound = 1.50
  elif weight > 2.0 and weight <= 6.0:
    price_per_pound = 3.00
  elif weight > 6.0 and weight <= 10.0:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (weight * price_per_pound)
print(ground_cost(8.4))

premium_cost = 125.00

def drone_cost(weight):
  if weight <= 2.0:
    price_per_pound = 4.50
  elif weight <= 6.0:
    price_per_pound = 9.00
  elif weight <= 10.0:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return weight * price_per_pound
print(drone_cost(1.5))

def print_cheapest_method(weight):
  ground = (ground_cost(weight))
  drone = (drone_cost(weight))
  premium = premium_cost
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone shipping"
    cost = drone
    
  print(
  "The cheapest option is $%.2f with %s shipping"
    % (cost, method)
  )
print_cheapest_method(4.8)
print_cheapest_method(41.5)
