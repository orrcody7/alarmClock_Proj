# create alarm_clock class

class Alarm_Clock:
    # ~~~~ PROPERTIES ~~~~
    def __init__(self):
        self.current_time = '8:00'
        self.clock_status = False
        self.alarm_time = '8:30'
        self.alarm_status = False


    # ~~~~ METHODS ~~~~
    def clock_time(self):
        print('the current time is' + (self.current_time))
        user_time = input('What time do you want to set the clock for?')
        print(f'the clock is now set to {user_time}')

    def alarm_toggle(self):
        if (self.alarm_status == False):
            self.alarm_status = True

        else:
            self.alarm_status = False


    def alarm_time(self):
        print('the alarm is set to' + (self.alarm_time))
