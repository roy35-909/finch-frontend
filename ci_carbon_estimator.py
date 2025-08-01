import time
import psutil
import argparse

# === CONFIG ===
CPU_POWER_WATTS = 15  # Adjust based on runner type
CARBON_INTENSITY = 475  # gCO2e per kWh

def get_avg_cpu_usage(duration):
    cpu_percentages = []
    print(f"Measuring CPU usage for {duration} seconds...")
    for _ in range(duration):
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_percentages.append(cpu_percent)
    avg_cpu = sum(cpu_percentages) / len(cpu_percentages)
    return avg_cpu

def estimate_energy_kwh(cpu_percent, duration):
    power_used = (cpu_percent / 100) * CPU_POWER_WATTS  # in Watts
    energy_kwh = (power_used * duration) / 3600 / 1000  # to kWh
    return energy_kwh

def estimate_carbon_grams(energy_kwh):
    return energy_kwh * CARBON_INTENSITY

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CI Carbon Footprint Estimator")
    parser.add_argument('--duration', type=int, required=True, help='CI run duration in seconds')
    args = parser.parse_args()

    avg_cpu = get_avg_cpu_usage(args.duration)
    energy_kwh = estimate_energy_kwh(avg_cpu, args.duration)
    carbon = estimate_carbon_grams(energy_kwh)

    print(f"\n=== Carbon Footprint Report ===")
    print(f"CI Run Duration: {args.duration}s")
    print(f"Avg CPU Usage: {avg_cpu:.2f}%")
    print(f"Energy Used: {energy_kwh:.6f} kWh")
    print(f"Estimated CO₂: {carbon:.2f} gCO₂e")
