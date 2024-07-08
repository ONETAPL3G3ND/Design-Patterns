class Engine:
    def __init__(self, HP, MaxSpeed):
        self.HP = HP
        self.MaxSpeed = MaxSpeed

    def Start(self):
        ...

    def Stop(self):
        ...


class Transmission:
    def SetDrive(self):
        ...

    def SetReverse(self):
        ...

    def SetNeutral(self):
        ...


class Auto:
    def __init__(self):
        self.engine = Engine(100, 210)
        self.IsEngineStarted = False
        self.Transmission = Transmission()

    def StartEngine(self):
        self.engine.Start()
        self.IsEngineStarted = True

    def StopEngine(self):
        self.engine.Stop()
        self.IsEngineStarted = False

    def MoveForward(self):
        if self.IsEngineStarted:
            self.Transmission.SetDrive()

    def MoveBackward(self):
        if self.IsEngineStarted:
            self.Transmission.SetReverse()
