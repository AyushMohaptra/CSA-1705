import time

env = {'A': 'dirty', 'B': 'dirty'}
loc = 'A'

print("Starting Vacuum Cleaner Simulation...")
while 'dirty' in env.values():
    print(f"Current state: {env}")
    print(f"Vacuum at {loc}.")
    if env[loc] == 'dirty':
        print(f"Cleaning {loc}...")
        env[loc] = 'clean'
        time.sleep(0.5)
    
    loc = 'B' if loc == 'A' else 'A'
    print(f"Moving to {loc}...")
    time.sleep(0.5)

print("\nAll rooms are clean. The job is done!")
