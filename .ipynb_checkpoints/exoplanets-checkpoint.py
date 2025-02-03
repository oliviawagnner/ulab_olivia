# Data from Q2 Indexing and Coding
radii = [1.2, 0.8, 1.5, 2.0, 1.0, 0.6] # Radii
temperatures = [300, 400, 350, 280, 500, 450] # Temps

def exoplanets(radii, temperatures): # Function with inputs of radii and temperatures
    for i in range(len(radii)): # Loop that goes through the radii 
        if temperatures[i] < 350: # If statement to find the radii associated with temps under 350 K
            print(radii[i])  # Prints the radii