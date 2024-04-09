#sal's Shipping - Project

#defining a weight variable to get from user or predefined (in lbs)

weight =4.8
cost=0 #ground shipping cost variable
cost_premium_ground_shipping =0 #premium ground shippping variable
cost_drone_shipping=0 #Drone shipping cost variable

#Ground Shipping

Flat_charge_ground_shipping=20.00
# for ground shipping cost = small flat charge of $20.00 + price_per_pound
if weight <= 2:
   cost=Flat_charge_ground_shipping+(1.50*weight)
   print("The cost of ground shipping the given weight",cost)
elif weight >2 and weight <=6:
    cost=Flat_charge_ground_shipping+(3.00*weight)
    print("The cost of ground shipping the given weight",cost)
elif weight >6 and weight <=10:
    cost=Flat_charge_ground_shipping+(4.00*weight)
    print("The cost of ground shipping the given weight",cost)
elif weight >10:
  cost=Flat_charge_ground_shipping+(4.75*weight)
  print("The cost of ground shipping the given weight",cost)
else:
  print("Ground shipping Error")

#premium Ground Shipping - does not change based on weights just flat rate.

cost_premium_ground_shipping = 125.00
print("The Cost of Premium ground shippping for the same weights is",cost_premium_ground_shipping)

#Drone Shipping calculator

#cost of drone shipping weight*price per pound

if weight<=2:
  cost_drone_shipping=weight*4.50
  print("The cost of drone shipping the same weight is",cost_drone_shipping)
elif weight>2 and weight<=6:
  cost_drone_shipping=weight*9.00
  print("The cost of drone shipping the same weight is",cost_drone_shipping)
elif weight>6 and weight <10:
  cost_drone_shipping=weight*4.50
  print("The cost of drone shipping the same weight is",cost_drone_shipping)
elif weight >10:
  cost_drone_shipping=weight*4.50
  print("The cost of drone shipping the same weight is",cost_drone_shipping)
else:
  print("Error Calculating the drone shipping price")

#Above we have given user the costs for different types of shipping methods, now to find the cheapest, we got to compare three variables.

#lets tell the user which is cheapest - smallest of three cost variables.
if(cost < cost_premium_ground_shipping and cost <cost_drone_shipping):
  print("Ground Shipping is the cheapest of all,and",cost,"would be your total cost to ship")
elif(cost_premium_ground_shipping <cost and cost_premium_ground_shipping < cost_drone_shipping):
  print("Premium Ground Shipping is the cheapest of all,and",cost_premium_ground_shipping, "would be your total cost to ship")
else:
  print("Drone is the cheapest of all,and ",cost_drone_shipping, "would be your total cost to ship")

#cheapest is found and cost and solution of the cheapest is given to the user.

