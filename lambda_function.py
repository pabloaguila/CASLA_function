import json
import sympy as sp
import numpy as np
#from sklearn.metrics.pairwise import haversine_distances

# Define the necessary symbols
p, t = sp.symbols("phi theta")
p0, t0 = sp.symbols("phi0 theta0")


# Define the rotation matrices to turn the first vector into the z-axis
Rxy = sp.Matrix([[sp.cos(p),sp.sin(p),0],[-sp.sin(p),sp.cos(p),0],[0,0,1]])
Rxz = sp.Matrix([[sp.cos(t),0,-sp.sin(t)],[0,1,0],[sp.sin(t),0,sp.cos(t)]])

# Define the other vector 
V = sp.Matrix([[sp.cos(p0)*sp.sin(t0)],[sp.sin(p0)*sp.sin(t0)],[sp.cos(t0)]])

# Obtain the second vector in the new coordinates
W = sp.simplify(Rxz*Rxy*V)

# Calculate the new theta and lambdify it
theta = sp.lambdify([p,t,p0,t0], sp.acos(W[2]),"numpy")

R = 6371 # Earth radius in km
distance = lambda p,t,p0,t0: R*theta(p,t,p0,t0)

def distance_to_CASLA(lat, lon):
    CASLA_theta = np.pi*(90-(-34.63447654700209))/180
    CASLA_phi = np.pi*(180-58.4241211330751)/180
    theta = np.pi*(90-lat)/180
    phi = np.pi*(180+lon)/180
    return distance(CASLA_phi, CASLA_theta, phi, theta)
    
def lambda_handler(event, context):
    latitude = float(event.get('latitude'))
    longitude = float(event.get('longitude'))
    distance = distance_to_CASLA(latitude, longitude)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'You are {distance:.2f} km away from San Lorenzo.')
    }
    