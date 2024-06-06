#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:22:24 2024

@author: fmohebbi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

    
def draw_rp(shs,buffer,color, tools):
    fig, axes = plt.subplots(figsize=(7, 8))
    legend_handles1 = []
    for i in range(0,len(tools)):
        sh_perc = shs[i]
        pos = np.arange(len(sh_perc))+buffer[i]
        col = color[i]
        box = axes.boxplot(sh_perc, positions = pos,
                        boxprops=dict(facecolor=col, alpha = 0.5), widths = 0.13, vert=True, patch_artist=True)
        # for i, data in enumerate(sh_perc):
        #     x = [pos[i] for t in range(len(data)) ]
        #     axes.scatter(x, data, color='black', marker='.', alpha=0.5)
        legend_handles1.append(box['boxes'][0])
    axes.legend(legend_handles1, tools, loc='lower right', bbox_to_anchor=(1.1, 0.0), fancybox=True, shadow=True) #loc='lower right') #'upper left'
    # axes.set_title('Technical replicates')
    axes.set_ylabel('percentage of consistency %')
    axes.set_ylim([20,100])
    axes.set_xlabel('Threshold')
    #axes.set_xticklabels(['exact match','integer','within 1%','within 10%'])
    num_ticks = 3
    xtick_pos = np.linspace(0, len(sh_perc) - 1, num_ticks)
    axes.set_xticks(xtick_pos)

    axes.set_xticklabels(['Exact match','0.01','0.1'])
    for pos in xtick_pos[1:]:
        axes.axvline(x=pos - 0.5, linestyle='--', color='gray', alpha=0.7)

    xtick_pos = np.arange(len(sh_perc))
    axes.set_xticks(xtick_pos)


def boxplot_treshold_based_consistency(consistencies, tools, lable, dir_):
    # Adjust colors and buffers based on the number of tools
    num_tools = len(tools)
    basic_colors = list(mcolors.TABLEAU_COLORS.values())
    color = basic_colors[:num_tools]
    buffer = np.linspace(-0.3, 0.3, num_tools)

    buffer = buffer + np.arange(num_tools) * 0.005  # Adjust the buffer for better visualization
    # print(rps)
    draw_rp(consistencies, buffer, color, tools)

    # plt.suptitle("Percentage of consistency (gene count) between simulated replicates and their reversed complement", wrap=True)
    plt.suptitle("Percentage of consistency (gene count) ", wrap=True)
    plt.savefig(dir_+"boxplot_"+lable+".png", dpi=199)
    plt.show()
    
    
