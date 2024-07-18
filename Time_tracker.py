import time
import json
class TimeTracker:
    def __init__(self):
        self.session_start_time = time.time()
        self.total_time = 0
        self.session_times = []
        self.load_time_data()
    
    def load_time_data(self):
        try:
            with open('time_data.json', 'r') as file:
                data = json.load(file)
                self.total_time = data.get('total_time', 0)
                self.session_times = data.get('session_times', [])
        except FileNotFoundError:
            self.total_time = 0
            self.session_times = []

    def save_time_data(self):
        data = {
            'total_time': self.total_time,
            'session_times': self.session_times
        }
        with open('time_data.json', 'w') as file:
            json.dump(data, file)

    def end_session(self):
        session_time = time.time() - self.session_start_time
        self.session_times.append(session_time)
        self.total_time += session_time
        self.total_time += session_time
        self.save_time_data()

    def get_current_session_time(self):
        return time.time() - self.session_start_time
    
    def get_average_sesion_time(self):
        if len(self.session_times) == 0:
            return 0
        return sum(self.session_times) / len(self.session_times)
    
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours}h {minutes}m {seconds}s"



    