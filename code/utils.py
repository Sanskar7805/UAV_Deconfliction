import json
import math

def load_missions(primary_path, simulated_path):
    with open(primary_path) as f:
        primary = json.load(f)
    with open(simulated_path) as f:
        simulated = json.load(f)
    return primary, simulated

def euclidean(p1, p2):
    return math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)

def check_conflicts(primary, simulated, safety_radius=5.0):
    conflicts = []
    for sim in simulated:
        for i, wp1 in enumerate(primary["waypoints"]):
            for j, wp2 in enumerate(sim["waypoints"]):
                if wp1["time"] == wp2["time"]:
                    if euclidean(wp1, wp2) < safety_radius:
                        conflicts.append({
                            "time": wp1["time"],
                            "location": {"x": wp1["x"], "y": wp1["y"]},
                            "with": sim["drone_id"]
                        })
    if conflicts:
        return "conflict detected", conflicts
    return "clear", None