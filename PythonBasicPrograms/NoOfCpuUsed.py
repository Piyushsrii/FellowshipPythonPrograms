import multiprocessing
class CpuUsed:
    def checkCpu(self):
        print("No. Of CPU use are : ", multiprocessing.cpu_count())

cpuObj = CpuUsed()
cpuObj.checkCpu()