import numpy as np
import matplotlib.pyplot as plt
def simulate_wright_fisher(p0, N, T, dt):
    """
    Simulates genetic drift using the Wright-Fisher SDE via Euler-Maruyama.
    p0: Initial allele frequency
    N: Effective population size
    T: Total time units
    dt: Time step size
    """
    steps = int(T / dt)
    p = np.zeros(steps)
    p[0] = p0
    for t in range(1, steps):
        curr = max(0, min(1, p[t-1])) 
        diffusion = np.sqrt((curr * (1 - curr)) / (2 * N))
        dW = np.random.normal(0, np.sqrt(dt))
        p[t] = curr + (diffusion * dW)
        if p[t] <= 0:
            p[t:] = 0
            break
        if p[t] >= 1:
            p[t:] = 1
            break
    return p
if __name__ == "__main__": 
    p0 = 0.5
    N = 50      
    T = 10.0    
    dt = 0.01
    time_axis = np.linspace(0, T, int(T/dt))
    plt.figure(figsize=(10, 6), dpi=500)
    for i in range(5):
        trajectory = simulate_wright_fisher(p0, N, T, dt)
        plt.plot(time_axis, trajectory, label=f"Path {i+1}")
    plt.title(f"Wright-Fisher Diffusion (N={N}, T={T})")
    plt.xlabel("Time (Generations)")
    plt.ylabel("Allele Frequency (p)")
    plt.axhline(1, color='red', linestyle='--', alpha=0.3, label="Fixation")
    plt.axhline(0, color='blue', linestyle='--', alpha=0.3, label="Extinction")
    plt.ylim(-0.05, 1.05)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.show()
