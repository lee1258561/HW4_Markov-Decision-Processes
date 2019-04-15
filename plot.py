import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def create_path(*arg, filename=None):
    path = os.getcwd()
    for directory in arg:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            print('%s doesn\'t exist, creating...' % path)
            os.mkdir(path)

    if filename:
        path = os.path.join(path, filename)
    return path

def plot_and_save(x, ys, labels, title, x_axis, y_axis, axis_range='auto', ylim=None, fig_path='fig', format='png'):
    if axis_range is None:
        plt.axis([x[0], x[-1], 0, 1])
    elif type(axis_range) == type(list()):
        plt.axis(axis_range)
    elif axis_range == 'auto':
        pass

    if ylim is not None:
        plt.ylim(*ylim)

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)

    lines = []
    for y in ys:
        l, = plt.plot(x, y)
        lines.append(l)
    if len(labels) == len(ys):
        plt.legend(lines, labels, loc="best")
    plt.grid(True, linestyle = "-.", color = '0.3')

    plt.savefig(fig_path + '.' + format, format=format)
    plt.clf()

def experiment_plot(mdp_name, plot_range=500, fig_path='fig'):
    if mdp_name == 'easyGridWorld':
        import easyGridData as data
    else: 
        import hardGridData as data

    file_path = create_path(fig_path, mdp_name, filename='reward')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [data.reward['vi'][:plot_range], data.reward['pi'][:plot_range], data.reward['ql'][:plot_range]],
                  ['Value Iteration', 'Policy Iteration', 'Q Learning'],
                  'Reward v.s. Iteration',
                  'iterations',
                  'reward',
                  fig_path=file_path)

    file_path = create_path(fig_path, mdp_name, filename='timeEachIter')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [data.runtime['vi'][:plot_range], data.runtime['pi'][:plot_range], data.runtime['ql'][:plot_range]],
                  ['Value Iteration', 'Policy Iteration', 'Q Learning'],
                  'Runtime v.s. Iteration',
                  'iterations',
                  'milisecond',
                  fig_path=file_path)

    file_path = create_path(fig_path, mdp_name, filename='step')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [data.step['vi'][:plot_range], data.step['pi'][:plot_range], data.step['ql'][:plot_range]],
                  ['Value Iteration', 'Policy Iteration', 'Q Learning'],
                  'Step v.s. Iteration',
                  'iterations',
                  'steps',
                  fig_path=file_path)

    file_path = create_path(fig_path, mdp_name, filename='qLR')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [data.q_e01_lr08['step'][:plot_range], data.q_e01_lr05['step'][:plot_range], data.q_e01_lr02['step'][:plot_range]],
                  ['0.8', '0.5', '0.2'],
                  'Step v.s. Iteration - Learning Rate',
                  'iterations',
                  'step',
                  #ylim=[0, 10000],
                  fig_path=file_path)
    file_path = create_path(fig_path, mdp_name, filename='qLR_reward')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [data.q_e01_lr08['reward'][:plot_range], data.q_e01_lr05['reward'][:plot_range], data.q_e01_lr02['reward'][:plot_range]],
                  ['0.8', '0.5', '0.2'],
                  'Reward v.s. Iteration - Learning Rate',
                  'iterations',
                  'reward',
                  #ylim=[-10000, 100],
                  fig_path=file_path)

    file_path = create_path(fig_path, mdp_name, filename='qStratagyStep')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [
                    data.q_b01_lr02['step'][:plot_range], 
                    data.q_b02_lr02['step'][:plot_range], 
                    data.q_b05_lr02['step'][:plot_range], 
                    data.q_e01_lr02['step'][:plot_range], 
                    data.q_e02_lr02['step'][:plot_range], 
                    data.q_e05_lr02['step'][:plot_range]
                  ],
                  ['0.1 T', '0.2 T', '0.5 T', '0.1 E', '0.2 E', '0.5 E'],
                  'Step v.s. Iteration - Strategy',
                  'iterations',
                  'step',
                  #ylim=[0, 10000],
                  fig_path=file_path)
    file_path = create_path(fig_path, mdp_name, filename='qStratagyReward')
    plot_and_save(list(range(data.numIter)[:plot_range]), 
                  [
                    data.q_b01_lr02['reward'][:plot_range], 
                    data.q_b02_lr02['reward'][:plot_range], 
                    data.q_b05_lr02['reward'][:plot_range], 
                    data.q_e01_lr02['reward'][:plot_range], 
                    data.q_e01_lr02['reward'][:plot_range], 
                    data.q_e05_lr02['reward'][:plot_range]
                  ],
                  ['0.1 T', '0.2 T', '0.5 T', '0.1 E', '0.2 E', '0.5 E'],
                  'Reward v.s. Iteration - Strategy',
                  'iterations',
                  'reward',
                  #ylim=[-10000, 100],
                  fig_path=file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['easyGridWorld', 'hardGridWorld']:
        print("Usage: python plot.py [easyGridWorld|hardGridWorld]")
        exit(1)

    experiment_plot(sys.argv[1], plot_range=100)


