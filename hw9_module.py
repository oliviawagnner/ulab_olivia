import numpy as np
import matplotlib.pyplot as plt

def plot_side_by_side():  # Plots h(x) and k(x) next to each other
    x = np.linspace(0, 2 * np.pi, 100)  # Domain from 0 to 2pi with 100 points
    h_x = np.cos(x)  # h(x)
    k_x = np.sin(x)  # k(x)

    fig, axs = plt.subplots(1, 2, figsize=(8, 12))  # Dimensions of the plot
    
    axs[0].plot(x, h_x, color='green', linestyle='-')  # Color and linestyle
    axs[0].set_title('h(x) = cos(x)', fontsize=14)  # Title
    axs[0].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[0].set_ylabel('h(x)', fontsize=12)  # Label y-axis

    axs[1].plot(x, k_x, color='blue', linestyle='--')  # Color and linestyle
    axs[1].set_title('k(x) = sin(x)', fontsize=14)  # Title
    axs[1].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[1].set_ylabel('k(x)', fontsize=12)  # Label y-axis

    plt.tight_layout()
    plt.show()  # Display

def plot_on_top_of_each_other():  # Plots h(x) and k(x) on top of each other
    x = np.linspace(0, 2 * np.pi, 100)  # Domain from 0 to 2pi with 100 points
    h_x = np.cos(x)  # h(x)
    k_x = np.sin(x)  # k(x)

    fig, axs = plt.subplots(2, 1, figsize=(8, 12)) # Dimensions of the plot

    axs[0].plot(x, h_x, color='green', linestyle='-')  # Color and linestyle
    axs[0].set_title('h(x) = cos(x)', fontsize=14)  # Title
    axs[0].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[0].set_ylabel('h(x)', fontsize=12)  # Label y-axis

    axs[1].plot(x, k_x, color='blue', linestyle='--')  # Color and linestyle
    axs[1].set_title('k(x) = sin(x)', fontsize=14)  # Title
    axs[1].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[1].set_ylabel('k(x)', fontsize=12)  # Label y-axis

    plt.tight_layout()
    plt.show()  # Display

def plot_side_by_side_big_domain():  # Plots h(x) and k(x) next to each other
    x = np.linspace(0, 4 * np.pi, 100)  # Domain from 0 to 2pi with 100 points
    h_x = np.cos(x)  # h(x)
    k_x = np.sin(x)  # k(x)

    fig, axs = plt.subplots(1, 2, figsize=(8, 12))  # Dimensions of the plot
    
    axs[0].plot(x, h_x, color='green', linestyle='-')  # Color and linestyle
    axs[0].set_title('h(x) = cos(x)', fontsize=14)  # Title
    axs[0].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[0].set_ylabel('h(x)', fontsize=12)  # Label y-axis

    axs[1].plot(x, k_x, color='blue', linestyle='--')  # Color and linestyle
    axs[1].set_title('k(x) = sin(x)', fontsize=14)  # Title
    axs[1].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[1].set_ylabel('k(x)', fontsize=12)  # Label y-axis

    plt.tight_layout()
    plt.show()  # Display

def plot_on_top_of_each_other_big_domain():  # Plots h(x) and k(x) on top of each other
    x = np.linspace(0, 4 * np.pi, 100)  # Domain from 0 to 2pi with 100 points
    h_x = np.cos(x)  # h(x)
    k_x = np.sin(x)  # k(x)

    fig, axs = plt.subplots(2, 1, figsize=(8, 12)) # Dimensions of the plot

    axs[0].plot(x, h_x, color='green', linestyle='-')  # Color and linestyle
    axs[0].set_title('h(x) = cos(x)', fontsize=14)  # Title
    axs[0].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[0].set_ylabel('h(x)', fontsize=12)  # Label y-axis

    axs[1].plot(x, k_x, color='blue', linestyle='--')  # Color and linestyle
    axs[1].set_title('k(x) = sin(x)', fontsize=14)  # Title
    axs[1].set_xlabel('x', fontsize=12)  # Label x-axis
    axs[1].set_ylabel('k(x)', fontsize=12)  # Label y-axis

    plt.tight_layout()
    plt.show()  # Display