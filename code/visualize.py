import matplotlib.pyplot as plt

def plot_trajectories(primary, simulated, conflicts=None):
    plt.figure(figsize=(10, 6))
    px = [wp['x'] for wp in primary['waypoints']]
    py = [wp['y'] for wp in primary['waypoints']]
    plt.plot(px, py, 'b-o', label='Primary Drone')

    for sim in simulated:
        sx = [wp['x'] for wp in sim['waypoints']]
        sy = [wp['y'] for wp in sim['waypoints']]
        plt.plot(sx, sy, '--', label=f"Simulated Drone {sim['drone_id']}")

    if conflicts:
        for c in conflicts:
            plt.plot(c['location']['x'], c['location']['y'], 'rx', markersize=10)
            plt.text(c['location']['x'], c['location']['y'], f"{c['time']}", fontsize=9)

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("UAV Trajectories & Conflicts")
    plt.legend()
    plt.grid(True)
    plt.savefig("visuals/trajectories.png")
    plt.close()