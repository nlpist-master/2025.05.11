from datetime import datetime


class Timer:

    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration
        self.started_at = datetime.now()

    def __str__(self):
        custom_time = self.started_at.strftime("%H:%M:%S")
        return f"Timer {self.name} set for {self.duration} minutes (started at {custom_time})"

    def __repr__(self):
        return f"Timer('{self.name}', {self.duration})"

    def __del__(self):
        print(f"Timer '{self.name}' was deleted. Goodbye!")


if __name__ == '__main__':
    timer1 = Timer("sleep", 10)
    print(timer1)
    timers = [timer1]
    print(timers)
    del timer1
    timer2 = Timer("wakeup", 500)
    timer2.paused = False
    print(timer2.__dict__)
    del timer2.paused
    print(timer2.__dict__)
    timer3 = Timer('running', 20)
    timers = [timer2, timer3]
    print(timers)