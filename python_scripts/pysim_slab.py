import numpy as np
import simpy 
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1500)

no_of_iterations = 1000             
vec_x = np.arange(no_of_iterations)
in_angle  = np.pi*25.0/180.0                                 #incident angle
in_height = 10                             #The value of y co-ordinate where the ray hits the medium
vec_y = np.zeros(no_of_iterations)
r_index = np.ones(no_of_iterations)

for i in range(1,1000) :
	r_index[i] = r_index[i]/(1+ float(i)/1000.0)      #set the refractive index function here. 
	
	
r_index[0] = 1                               #refractive index of outer medium 


def ang_of_incidence(n):                     #decides the angle of refraction for the next iteration step 
    if n == 1:
    	incident_ang = np.sin(in_angle)*(r_index[0]/r_index[1]) 
        return incident_ang
    else:
    	incident_ang = (r_index[n-1]/r_index[n])*ang_of_incidence(n-1) 
        return  incident_ang

def path_eq(n):                               #trajectory of ray 
	
	if n  == 0:
		vec_y[n] = in_height
		return vec_y
		
	else:
		vec_y[n] = path_eq(n-1)[n-1] + np.tan(np.arcsin(ang_of_incidence(n))) 
		return vec_y

def get_slope(n):                              
    print('slope : ' , (180/np.pi)*np.arcsin(ang_of_incidence(n)))

get_slope(50)


plt.plot(vec_x, path_eq(no_of_iterations-1))
plt.xlabel('x')
plt.ylabel('y')
plt.show()
