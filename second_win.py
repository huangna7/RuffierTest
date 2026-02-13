# write a code for the second screen of app

def timer_test(self):
    global time
    time = QTime(0, 0, 15)
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer1Event)
    self.timer.start(1000)
def timer_sits(self):
    global time
    time = QTime(0, 0, 30)
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer2Event)
    #one squat in 1.5 seconds
    self.timer.start(1500)
def timer_final(self):
    global time
    time = QTime(0, 1, 0)
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer3Event)
    #one squat in 1.5 seconds
    self.timer.start(1000)
