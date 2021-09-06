# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:43:31 2021

@author: Alexander Urbina
"""
from numpy import pi
import matplotlib.pyplot as plt

def squared(x: float) -> float:      
    return x**2
"""
Takes x as a float and returns its square
:param x: float
:return x**2
"""
def knots_to_ftpersec(speed): # Speed is the user input and is in knots
    return speed*1.68781

def thrust_required(rho_inf, v_inf, s, cd0_, k, w):
    cl = 2 * w / (rho_inf * v_inf ** 2 * s)
    return 0.5 * rho_inf * v_inf **2 *s * (cd0_ + k * cl ** 2)

"""
This function calculated thrust required based on this equation:
             2 * weight
    CL = -------------------
        rho_inf* V_inf^2 * S
"""

weight = 200000 # Ib
wing_area = 1318 # ft
wing_span = 117.4166
cd0 = 0.0185
thrust = 66000 #Ib of thrust total
aspect_ratio = wing_span**2/ wing_area
e = 0.92
K = 1/ (pi * e * aspect_ratio)
rho_sl = 23.77E-4 # in slugs/ft^3

x_vals_sl = [ i for i in range(80, 750, 10)]

tr_sl = [] 
for airspeed in x_vals_sl:
    airspeed_fps = knots_to_ftpersec(airspeed)
    thrust_calculated = thrust_required(rho_sl, knots_to_ftpersec(airspeed),
    wing_area, cd0, K, weight)
    
    tr_sl.append(thrust_calculated)

TA_sl = 0.7 * thrust
y_coords_sl = [TA_sl for _ in x_vals_sl]

takeoff_vel_sl = [180, 180]
cruise_velocity_fl350_values = [11000, 46500]

rho_fl100 = 17.56E-4 # in slug s/ft^3
x_vals_fl100 = [i for i in range(110, 745, 10)]
tr_fl100 = [thrust_required(rho_fl100, knots_to_ftpersec(x),
                            wing_area, cd0, K, weight) for x in x_vals_fl100]
TA_fl100 = 0.7 * thrust * rho_fl100 /  rho_sl
cruise_velocity = [ 250, 250]
cruise_velocity_fl100_values = [10000, 34130]
y_coords_fl100 = [TA_fl100 for _ in x_vals_fl100]

print(airspeed)
print(tr_sl)
print(y_coords_sl)
print("Thrust calculated = ",thrust_calculated)
plt.subplot(3, 1, 1)
plt.plot(x_vals_sl, tr_sl, 'g-', label=r"$T_R$ at Sea Level")
plt.plot(x_vals_sl, y_coords_sl, 'k--',
         label = '$T_A$ at Sea Level({:,.0f} Ib)'.format(TA_sl))
plt.plot(takeoff_vel_sl, cruise_velocity_fl350_values, 'b-.', 
         label = "Takeoff Velocity ({} knots)".format(takeoff_vel_sl[0]))

plt.ylim(5000, 50000)
plt.xlim(50,1550)
plt.ylabel('Thrust (Ib)')

plt.title('Thrust Required & Thrust Available Curves')
plt.legend(loc = 'lower right')
#plt.show()

plt.subplot(3, 1, 2)
plt.plot(x_vals_fl100, tr_fl100, 'k-', label=r"$T_R$ at FL100")
plt.plot(x_vals_fl100, y_coords_fl100, 'k--',
         label= "$T_A$ at FL100 ({:,.0f} lb)".format(cruise_velocity[0]))
plt.plot(cruise_velocity, cruise_velocity_fl100_values, 'b-.', 
         label= "Cruise Velocity ({} knots)".format(cruise_velocity[0]))
plt.ylabel('Thrust (Ib)')
plt.ylim(5000, 38000)
plt.xlim(50,1550)
plt.legend(loc = 'lower right')
plt.subplot(3, 1, 3)
rho_fl350 = 7.38E-4 # in slugs/ft^3
cruise_velocity_fl350 = [450, 450]
cruise_velocity_fl350_values = [9900, 14200]
x_vals_fl350 = [i for i in range(280, 695, 10)]
TA_fl350 = 0.7 * thrust * rho_fl350/ rho_sl
tr_fl350 = [thrust_required(rho_fl350, knots_to_ftpersec(x), 
                            wing_area, cd0, K, weight) for x in x_vals_fl350 ]
plt.plot(x_vals_fl350, tr_fl350, 'k-', label=r"$T_R$ at FL350")
y_coords_fl350 = [TA_fl350 for _ in x_vals_fl350]
plt.plot(x_vals_fl350, tr_fl350, 'k-', 
         label=r"$T_A$ at FL350 ({:,.0f} lb)".format(TA_fl350))
plt.plot(cruise_velocity_fl350, cruise_velocity_fl350_values, 'b-.',
         label= "Cruise Velocity ({} knots)".format(cruise_velocity_fl350_values[0]))
plt.xlabel('Velocity(knots)')
plt.ylabel('Thrust (lb)')
plt.xlim(50, 1550)
plt.legend(loc = 'lower right' )
plt.subplots_adjust(hspace=0.50)
plt.show()

"""   
a= 5
y = squared(a)
print(y)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
end_list = []
for number in numbers:
    if number % 2 == 0:
        end_list.append(number)
print(end_list)
 """   
