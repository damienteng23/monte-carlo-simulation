import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def mc_pi(num_points):
    # Generate random points in a unit square
    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)

    # Check if points fall inside the unit circle
    inside_circle = x**2 + y**2 <= 1
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    error_percent = abs(pi_estimate - np.pi) / np.pi * 100

    # Plot setup
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_title(f"Estimated π ≈ {pi_estimate:.8f} using {num_points} points")

    # Plot square boundary
    square = plt.Rectangle((-1, -1), 2, 2, edgecolor='black', facecolor='none')
    ax.add_patch(square)

    # Plot circle boundary
    circle = plt.Circle((0, 0), 1, edgecolor='blue', facecolor='none')
    ax.add_patch(circle)

    # Plot points
    ax.scatter(x[inside_circle], y[inside_circle], color='green', s=1, label='Inside Circle')
    ax.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside Circle')
    ax.legend(loc='upper right')

    # Display plot
    st.pyplot(fig)

    return error_percent