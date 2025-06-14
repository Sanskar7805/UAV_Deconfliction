from utils import load_missions, check_conflicts
from visualize import plot_trajectories

if __name__ == "__main__":
    primary_mission, simulated_missions = load_missions("data/primary_mission.json", "data/simulated_missions.json")
    status, details = check_conflicts(primary_mission, simulated_missions)
    print("Mission Status:", status)
    if details:
        print("Conflict Details:", details)
    plot_trajectories(primary_mission, simulated_missions, details)