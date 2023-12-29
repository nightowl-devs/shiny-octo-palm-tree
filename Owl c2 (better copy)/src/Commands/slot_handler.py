import os
import time
import json
def is_attack_running():
    try:
        with open('slots.json', 'r') as file:
            attack_info = json.load(file)
            if attack_info['status'] == 'attack':
                start_time = int(attack_info['start_time'])
                duration = int(attack_info['duration'])
                elapsed_time = time.time() - start_time
                remaining_time = duration - elapsed_time
                if remaining_time > 0:
                    return True, remaining_time  # Return True if an attack is running
    except FileNotFoundError:
        pass
    return False, 0
def set_attack(duration):
    start_time = int(time.time())
    attack_info = {
        'status': 'attack',
        'start_time': start_time,
        'duration': duration
    }
    with open('slots.json', 'w') as file:
        json.dump(attack_info, file)
        file.flush()
