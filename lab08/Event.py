class Event:
    def __init__(self, day, time, location):
        self.day = day
        self.time = time
        self.location = location.upper()

    def __eq__(self, other):
        return self.day == other.day and self.time == other.time and self.location == other.location
    
    def __str__(self):
        def format(time):
            return f"{time[0]//100:0>2}:{time[0]%100:0>2} - {time[1]//100:0>2}:{time[1]%100:0>2}"
        
        start_time = str(self.time[0])
        start_time = start_time[:2] + ':' + start_time[2:]
        end_time = str(self.time[1])
        end_time = end_time[:2] + ':' + end_time[2:]
        return f"{self.day} {format(self.time)}, {self.location}"