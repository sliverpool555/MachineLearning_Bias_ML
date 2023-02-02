# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:51:26 2022

@author: 253364
"""

#plotting a graph 

import matplotlib.pyplot as plt
import pandas as pd


#### Dataset Adult


par_diff_avg = [-0.06106866503, -0.07828185694, -0.09685406114, -0.09852770801, -0.1004833963, -0.100884617, -0.09995630339, -0.09995630339, -0.09995630339]

ep_opp_avg = [-0.03273697358, -0.06890809587, -0.1702534871, -0.1740619642, -0.177944172, -0.1783952748, -0.1761391367, -0.1761391367, -0.1761391367]

avg_odds_avg = [-0.02974329513, -0.0547720339, -0.1084295296, -0.110813461, -0.1133993226, -0.1138220814, -0.1124619938, -0.1124619938, -0.1124619938]

fig, ax = plt.subplots()

plt.plot(par_diff_avg)
plt.plot(ep_opp_avg)
plt.plot(avg_odds_avg)

plt.legend(['par diff, avg', 'ep_opp_avg', 'avg_odds_avg'])
labels = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
ax.set_xticklabels(labels)
plt.title("Task 1 Fairness Matrix Adult Dataset Task2")
plt.xlabel("C")
plt.ylabel("Fairness Metrix")
plt.show()



par_diff_avg_A = [-0.01124052458,-0.008027376485,-0.01679938596,-0.01348978218,-0.01344393338,-0.01344393338,-0.0130111207,-0.0130111207,-0.0130111207]

ep_opp_avg_A = [0.002504301462, 0.009386418565,-0.02069119349,-0.01440009706,-0.01422536588,-0.01422536588,-0.01315009706,-0.01315009706,-0.01315009706]

avg_odds_avg_A = [-0.006617812776,-0.002145621499,-0.0182143271,-0.01388618662,-0.01379492859,-0.01379492859,-0.01314256265,-0.01314256265,-0.01314256265]

fig, ax = plt.subplots()

plt.plot(par_diff_avg)
plt.plot(ep_opp_avg)
plt.plot(avg_odds_avg)
plt.plot(par_diff_avg_A)
plt.plot(ep_opp_avg_A)
plt.plot(avg_odds_avg_A)

plt.legend(['par diff avg', 'ep_opp_avg', 'avg_odds_avg', 'par diff avg reweight', 'ep_opp_avg reweight', 'avg_odds_avg reweight'], loc='upper right')
labels = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
ax.set_xticklabels(labels)
plt.title("Fairness Parameters Adult Dataset ")
plt.xlabel("C")
plt.ylabel("Fairness Metrix")
plt.show()



###GERMAN dataset


par_diff_avg = [0.3749744931, 0.3749744931, 0.3994069255, 0.567272671, 0.5533741202, 0.5481567289, 0.5398233956, 0.4609828159, 0.4609828159]

ep_opp_avg = [0.2701364801, 0.2701364801, 0.2911891117, 0.4385352773,0.4357438159,0.4294280264,0.4294280264,0.3689017106,0.3689017106]

avg_odds_avg = [0.3553757797,0.3553757797,0.385382615,0.5795814915,0.5643329469,0.5611750522,0.5528417188,0.4709118943,0.4709118943]

fig, ax = plt.subplots()

plt.plot(par_diff_avg)
plt.plot(ep_opp_avg)
plt.plot(avg_odds_avg)

plt.legend(['par diff, avg', 'ep_opp_avg', 'avg_odds_avg'])
labels = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
ax.set_xticklabels(labels)
plt.title("Task 1 Fairness Matrix German Dataset Task2")
plt.xlabel("C")
plt.ylabel("Fairness Metrix")
plt.show()



par_diff_avg_A = [0.1862651009,0.1862651009,0.1815712234,-0.08344751804,-0.02160891914,-0.02187913155,-0.01608973245,-0.01344369032,-0.01344369032]

ep_opp_avg_A = [0.1533271572,0.1533271572,0.1533271572,-0.06607621707,-0.01051417797,-0.01051417797,-0.01051417797,-0.001992874707,-0.001992874707]

avg_odds_avg_A = [0.2179126767,0.2179126767,0.2107698196,-0.09515120377,-0.02946343819,-0.02738010486,-0.01790589851,-0.02364524688,-0.02364524688]

fig, ax = plt.subplots()

plt.plot(par_diff_avg)
plt.plot(ep_opp_avg)
plt.plot(avg_odds_avg)
plt.plot(par_diff_avg_A)
plt.plot(ep_opp_avg_A)
plt.plot(avg_odds_avg_A)

plt.legend(['par diff avg', 'ep_opp_avg', 'avg_odds_avg', 'par diff avg reweight', 'ep_opp_avg reweight', 'avg_odds_avg reweight'], loc='upper right')
labels = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]
ax.set_xticklabels(labels)
plt.title("Fairness Parameters German Dataset ")
plt.xlabel("C")
plt.ylabel("Fairness Metrix")
plt.show()







