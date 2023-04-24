#!/usr/bin/env python3

# read text files and plot them

import matplotlib.pyplot as plt
import numpy as np
import sys
import math

# data files to read
file1 = "../data_files/q1.txt"
file2 = "../data_files/q2.txt"
file3 = "../data_files/q3.txt"
file4 = "../data_files/q4.txt"
file5 = "../data_files/q5.txt"
file6 = "../data_files/q6.txt"

q1_des = 90*np.pi/180
q3_des = 0
q4_des = -125*np.pi/180

traj1 = np.loadtxt(file1, skiprows=0)[:, [0, 2, 3, 7, 9, 10]]
traj2 = np.loadtxt(file2, skiprows=0)[:, [0, 2, 3, 7, 9, 10]]
traj3 = np.loadtxt(file3, skiprows=0)[:, [0, 2, 3, 7, 9, 10]]
traj4 = np.loadtxt(file4, skiprows=0)[:, [0, 2, 3, 7, 9, 10]]
traj5 = np.loadtxt(file5, skiprows=0)[:, [0, 2, 3, 7, 9, 10]]
traj6 = np.loadtxt(file6, skiprows=0)[:, [0, 2, 3, 7, 9, 10]]

time1 = np.arange(traj1.shape[0]) / 100
time2 = np.arange(traj2.shape[0]) / 100
time3 = np.arange(traj3.shape[0]) / 100
time4 = np.arange(traj4.shape[0]) / 100
time5 = np.arange(traj5.shape[0]) / 100
time6 = np.arange(traj6.shape[0]) / 100

# plotting
plt.figure(1)
plt.plot(time1, traj1[:, 0], 'b')
plt.plot(time1, traj1[:, 1], 'r')
plt.plot(time1, traj1[:, 2], 'g')
plt.axhline(y=q1_des, color='b', linestyle=':')
plt.axhline(y=q3_des, color='r', linestyle=':')
plt.axhline(y=q4_des, color='g', linestyle=':')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$q_1$, $q_3$, $q_4$ (rad) $\\rightarrow$')
plt.legend(['$q_1$', '$q_3$', '$q_4$', '$q_{1d}$', '$q_{3d}$', '$q_{4d}$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $q_1$, $q_3$, $q_4$ versus time')
plt.grid()
plt.savefig("Figure1.png", bbox_inches="tight")
plt.show()

plt.figure(2)
plt.plot(time1, traj1[:, 3], 'b')
plt.plot(time1, traj1[:, 4], 'r')
plt.plot(time1, traj1[:, 5], 'g')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ (rad/s) $\\rightarrow$')
plt.legend(['$\\dot{q}_1$', '$\\dot{q}_3$', '$\\dot{q}_4$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ versus time')
plt.grid()
plt.savefig("Figure2.png", bbox_inches="tight")
plt.show()

plt.figure(3)
plt.plot(time1, traj1[:, 0], 'b--', time2, traj2[:, 0], 'b')
plt.plot(time1, traj1[:, 1], 'r--', time2, traj2[:, 1], 'r')
plt.plot(time1, traj1[:, 2], 'g--', time2, traj2[:, 2], 'g')
plt.axhline(y=q1_des, color='b', linestyle=':')
plt.axhline(y=q3_des, color='r', linestyle=':')
plt.axhline(y=q4_des, color='g', linestyle=':')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$q_1$, $q_3$, $q_4$ (rad) $\\rightarrow$')
plt.legend(['$q_1$ from Q1', '$q_1$ from Q2', '$q_3$ from Q1', '$q_3$ from Q2', '$q_4$ from Q1', '$q_4$ from Q2', '$q_{1d}$', '$q_{3d}$', '$q_{4d}$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $q_1$, $q_3$, $q_4$ versus time')
plt.grid()
plt.savefig("Figure3.png", bbox_inches="tight")
plt.show()

plt.figure(4)
plt.plot(time1, traj1[:, 3], 'b--', time2, traj2[:, 3], 'b')
plt.plot(time1, traj1[:, 4], 'r--', time2, traj2[:, 4], 'r')
plt.plot(time1, traj1[:, 5], 'g--', time2, traj2[:, 5], 'g')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ (rad/s) $\\rightarrow$')
plt.legend(['$\\dot{q}_1$ from Q1', '$\\dot{q}_1$ from Q2', '$\\dot{q}_3$ from Q1', '$\\dot{q}_3$ from Q2', '$\\dot{q}_4$ from Q1', '$\\dot{q}_4$ from Q2'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ versus time')
plt.grid()
plt.savefig("Figure4.png", bbox_inches="tight")
plt.show()

plt.figure(5)
plt.plot(time2, traj2[:, 0], 'b--', time3, traj3[:, 0], 'b')
plt.plot(time2, traj2[:, 1], 'r--', time3, traj3[:, 1], 'r')
plt.plot(time2, traj2[:, 2], 'g--', time3, traj3[:, 2], 'g')
plt.axhline(y=q1_des, color='b', linestyle=':')
plt.axhline(y=q3_des, color='r', linestyle=':')
plt.axhline(y=q4_des, color='g', linestyle=':')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$q_1$, $q_3$, $q_4$ (rad) $\\rightarrow$')
plt.legend(['$q_1$ from Q2', '$q_1$ from Q3', '$q_3$ from Q2', '$q_3$ from Q3', '$q_4$ from Q2', '$q_4$ from Q3', '$q_{1d}$', '$q_{3d}$', '$q_{4d}$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $q_1$, $q_3$, $q_4$ versus time')
plt.grid()
plt.savefig("Figure5.png", bbox_inches="tight")
plt.show()

plt.figure(6)
plt.plot(time2, traj2[:, 3], 'b--', time3, traj3[:, 3], 'b')
plt.plot(time2, traj2[:, 4], 'r--', time3, traj3[:, 4], 'r')
plt.plot(time2, traj2[:, 5], 'g--', time3, traj3[:, 5], 'g')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ (rad/s) $\\rightarrow$')
plt.legend(['$\\dot{q}_1$ from Q2', '$\\dot{q}_1$ from Q3', '$\\dot{q}_3$ from Q2', '$\\dot{q}_3$ from Q3', '$\\dot{q}_4$ from Q2', '$\\dot{q}_4$ from Q3'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ versus time')
plt.grid()
plt.savefig("Figure6.png", bbox_inches="tight")
plt.show()

plt.figure(7)
plt.plot(time3, traj3[:, 0], 'b--', time4, traj4[:, 0], 'b')
plt.plot(time3, traj3[:, 1], 'r--', time4, traj4[:, 1], 'r')
plt.plot(time3, traj3[:, 2], 'g--', time4, traj4[:, 2], 'g')
plt.axhline(y=q1_des, color='b', linestyle=':')
plt.axhline(y=q3_des, color='r', linestyle=':')
plt.axhline(y=q4_des, color='g', linestyle=':')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$q_1$, $q_3$, $q_4$ (rad) $\\rightarrow$')
plt.legend(['$q_1$ from Q3', '$q_1$ from Q4', '$q_3$ from Q3', '$q_3$ from Q4', '$q_4$ from Q3', '$q_4$ from Q4', '$q_{1d}$', '$q_{3d}$', '$q_{4d}$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $q_1$, $q_3$, $q_4$ versus time')
plt.grid()
plt.savefig("Figure7.png", bbox_inches="tight")
plt.show()

plt.figure(8)
plt.plot(time3, traj3[:, 3], 'b--', time4, traj4[:, 3], 'b')
plt.plot(time3, traj3[:, 4], 'r--', time4, traj4[:, 4], 'r')
plt.plot(time3, traj3[:, 5], 'g--', time4, traj4[:, 5], 'g')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ (rad/s) $\\rightarrow$')
plt.legend(['$\\dot{q}_1$ from Q3', '$\\dot{q}_1$ from Q4', '$\\dot{q}_3$ from Q3', '$\\dot{q}_3$ from Q4', '$\\dot{q}_4$ from Q3', '$\\dot{q}_4$ from Q4'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ versus time')
plt.grid()
plt.savefig("Figure8.png", bbox_inches="tight")
plt.show()

plt.figure(9)
plt.plot(time4, traj4[:, 0], 'b--', time5, traj5[:, 0], 'b')
plt.plot(time4, traj4[:, 1], 'r--', time5, traj5[:, 1], 'r')
plt.plot(time4, traj4[:, 2], 'g--', time5, traj5[:, 2], 'g')
plt.axhline(y=q1_des, color='b', linestyle=':')
plt.axhline(y=q3_des, color='r', linestyle=':')
plt.axhline(y=q4_des, color='g', linestyle=':')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$q_1$, $q_3$, $q_4$ (rad) $\\rightarrow$')
plt.legend(['$q_1$ from Q4', '$q_1$ from Q5', '$q_3$ from Q4', '$q_3$ from Q5', '$q_4$ from Q4', '$q_4$ from Q5', '$q_{1d}$', '$q_{3d}$', '$q_{4d}$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $q_1$, $q_3$, $q_4$ versus time')
plt.grid()
plt.savefig("Figure9.png", bbox_inches="tight")
plt.show()

plt.figure(10)
plt.plot(time4, traj4[:, 3], 'b--', time5, traj5[:, 3], 'b')
plt.plot(time4, traj4[:, 4], 'r--', time5, traj5[:, 4], 'r')
plt.plot(time4, traj4[:, 5], 'g--', time5, traj5[:, 5], 'g')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ (rad/s) $\\rightarrow$')
plt.legend(['$\\dot{q}_1$ from Q4', '$\\dot{q}_1$ from Q5', '$\\dot{q}_3$ from Q4', '$\\dot{q}_3$ from Q5', '$\\dot{q}_4$ from Q4', '$\\dot{q}_4$ from Q5'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ versus time')
plt.grid()
plt.savefig("Figure10.png", bbox_inches="tight")
plt.show()

plt.figure(11)
plt.plot(time5, traj5[:, 0], 'b--', time6, traj6[:, 0], 'b')
plt.plot(time5, traj5[:, 1], 'r--', time6, traj6[:, 1], 'r')
plt.plot(time5, traj5[:, 2], 'g--', time6, traj6[:, 2], 'g')
plt.axhline(y=q1_des, color='b', linestyle=':')
plt.axhline(y=q3_des, color='r', linestyle=':')
plt.axhline(y=q4_des, color='g', linestyle=':')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$q_1$, $q_3$, $q_4$ (rad) $\\rightarrow$')
plt.legend(['$q_1$ from Q5', '$q_1$ from Q6', '$q_3$ from Q5', '$q_3$ from Q6', '$q_4$ from Q5', '$q_4$ from Q6', '$q_{1d}$', '$q_{3d}$', '$q_{4d}$'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $q_1$, $q_3$, $q_4$ versus time')
plt.grid()
plt.savefig("Figure11.png", bbox_inches="tight")
plt.show()

plt.figure(12)
plt.plot(time5, traj5[:, 3], 'b--', time6, traj6[:, 3], 'b')
plt.plot(time5, traj5[:, 4], 'r--', time6, traj6[:, 4], 'r')
plt.plot(time5, traj5[:, 5], 'g--', time6, traj6[:, 5], 'g')
plt.xlabel('time (sec) $\\rightarrow$')
plt.ylabel('$\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ (rad/s) $\\rightarrow$')
plt.legend(['$\\dot{q}_1$ from Q5', '$\\dot{q}_1$ from Q6', '$\\dot{q}_3$ from Q5', '$\\dot{q}_3$ from Q6', '$\\dot{q}_4$ from Q5', '$\\dot{q}_4$ from Q6'], bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('Plot of $\\dot{q}_1$, $\\dot{q}_3$, $\\dot{q}_4$ versus time')
plt.grid()
plt.savefig("Figure12.png", bbox_inches="tight")
plt.show()
