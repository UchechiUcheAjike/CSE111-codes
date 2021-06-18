#start of my code


from math import pi 

# Define the main function.
def main():
    
    # Create four variables to hold the name,radius, height and price.
    name = input("What is the name of the can?: ")
    radius = float(input("what is the radius of the can in centimeters?: "))
    height = float(input("what is the height of the can in centimeters?:"))
    price = float(input("what is the price of the can?:"))

    # Call the cylinder_volume and cylinder_surface_area functions and store
    # their return value in a variable to use later.
    volume = cylinder_volume(radius, height)
    surface_area = cylinder_surface_area(radius, height)
    
    

    storage_efficiency = pi * volume/surface_area
    print(storage_efficiency)


# Define a function that accepts two parameters.
def cylinder_volume(radius, height):
    volume = pi * radius ** 2 * height
    return volume




# Define a second function that accepts two parameters.
def cylinder_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area


# Start this program by
# calling the main function.
main()

#end of my code




#start of team activity

from math import pi

def main():
  biggest_storage = -1
  name_biggest_storage = ''
  lowest_cost = 99999999999
  name_lowest_cost = ''

  '''
  Name = "#1 Picnic"
  Radius = 6.83
  Height = 10.16
  Price = 0.28
  volume = compute_volume(Radius, Height)
  sArea = compute_surfaceArea(Radius, Height)
  stEfficiency = compute_storageEfficiency(volume, sArea)
  print(f"{Name} {stEfficiency:.1f}")

  Name = "#1 Tall"
  Radius = 7.78
  Height = 11.91
  Price = 0.43
  volume = compute_volume(Radius, Height)
  sArea = compute_surfaceArea(Radius, Height)
  stEfficiency = compute_storageEfficiency(volume, sArea)
  print(f"{Name} {stEfficiency:.1f}")
  '''
   
   
  with open('cans.txt') as the_file:
      for line in the_file:
          parts = line.strip()
          parts = parts.split(',')
          name = parts[0]
          radius = float(parts[1])
          height = float(parts[2])
          cost_per_can = float(parts[3])

          

          storage_efficiency = compute_storageEfficiency(radius, height)
          costF = cost_efficiency(radius, height, cost_per_can)
          print(f'name: {name}, storage efficiency: {storage_efficiency:.1f}, and the cost efficiency is: ${costF:.2f}')

          if storage_efficiency > biggest_storage:
            biggest_storage = storage_efficiency
            name_biggest_storage = name

          if costF < lowest_cost:
            lowest_cost = costF
            name_lowest_cost = name

      print(f"{name_biggest_storage} has the highest storage efficiency of {biggest_storage:.1f}")

      print(f"{name_lowest_cost} has the highest cost efficiency of {lowest_cost:.2f}")


def compute_volume(radius, height):
  volume = pi * radius ** 2 * height
  return volume

def compute_surfaceArea(radius, height):
  surfaceArea = 2 * pi * radius * (radius + height)
  return surfaceArea

def compute_storageEfficiency(radius, height):
  volume = compute_volume(radius, height)
  surface_area = compute_surfaceArea(radius, height)
  storageEfficiency = volume / surface_area
  return storageEfficiency

def cost_efficiency(radius, height, cost_per_can):
  volume = compute_volume(radius, height)
  cost_efficiency = volume / cost_per_can
  return cost_efficiency
main()

#end of team activity



