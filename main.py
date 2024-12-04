
import pygame as pg

from assets import pixelResolution
from objects import Pixel
from scene import Scene

class VirtualMachine(Scene):
    def onInit(self):
        self.displayMap = {}
        for i in range(self.width//pixelResolution):
            for j in range(self.height//pixelResolution):
                self.displayMap[i, j] = Pixel(i*pixelResolution, j*pixelResolution)

        self.executionQue = []

        self.loadFile("VirtualMachineScript.txt")

    def loadFile(self, fileName: str):
        with open(fileName, "r") as file:
            data = file.read()
            file.close()

        for line in data.splitlines():
            if not line:
                continue

            statement = self.morphLine(line)
            self.executionQue.append(statement)

    def morphLine(self, line: str):
        statement = line
        args = line.lower().split()

        if args[0] == "set":

            if args[3] in ("on", 1):
                args[3] = True
            elif args[3] in ("off", 0):
                args = False

            statement = f"self.displayMap[{int(args[1]), int(args[2])}].state = {args[3]}"

        return statement

    def tick(self) -> None:
        if self.executionQue:
            exec(self.executionQue[0])
            self.executionQue.pop(0)

    def display(self) -> None:
        for pixel in self.displayMap:
            self.displayMap[pixel].display(self.window)

if __name__ == "__main__":
    instance = VirtualMachine((900, 500), "Virtual Machine")
    instance.start()