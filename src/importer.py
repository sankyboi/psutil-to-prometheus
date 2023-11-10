import psutil

class Importer:
    def __init__(self):
        self.prevNetwork = psutil.net_io_counters(pernic=False, nowrap=True)
        self.measureStatic()
        self.measure()
        self.measureLowFreq()

    
    def measure(self):

        self.measureCPU()
        self.measureMemory()
        self.measureSwap()
        self.measureNetwork()

    def measureLowFreq(self):

        self.measureDisk() 
        


    def measureNetwork(self):

        network = psutil.net_io_counters(pernic=False, nowrap=True)
        self.bytesSent = network.bytes_sent
        self.bytesRecv = network.bytes_recv
        self.packetsSent = network.packets_sent
        self.packetsRecv = network.packets_recv
        self.errorIn = network.errin
        self.errorOut = network.errout
        self.dropIn = network.dropin
        self.dropOut = network.dropout
        self.dlSpeed = network.bytes_recv - self.prevNetwork.bytes_recv
        self.ulSpeed = network.bytes_sent - self.prevNetwork.bytes_sent
        self.packetsSentRate = network.packets_sent - self.prevNetwork.packets_sent
        self.packetsRecvRate = network.packets_recv - self.prevNetwork.packets_recv
        self.errorInRate = network.errin - self.prevNetwork.errin
        self.errorOutRate = network.errout - self.prevNetwork.errout
        self.dropInRate = network.dropin - self.prevNetwork.dropout
        self.dropOutRate = network.dropout - self.prevNetwork.dropout
        self.prevNetwork = network      

    def measureDisk(self):

        if not psutil.WINDOWS:
            #single tree file directory systems, all drives would be under this
            disk = psutil.disk_usage("/")
            self.totalDisk = disk.total
            self.usedDisk = disk.used
            self.freeDisk = disk.free
            self.diskPercentUsed = disk.percent

        else:
            diskParts = psutil.disk_partitions()
            self.totalDisk = 0
            self.usedDisk = 0
            self.freeDisk = 0
            # "/" path in windows only has C drive under it, other hard drives will be under their own directory. Gotta add 'em all!
            for i in range(len(diskParts)):
                disk = psutil.disk_usage(diskParts[i].mountpoint)
                self.totalDisk += disk.total
                self.usedDisk += disk.used
                self.freeDisk += disk.free
            
            self.diskPercentUsed = ((self.usedDisk / self.totalDisk ) * 100)

    def measureSwap(self):

        swap = psutil.swap_memory()
        self.totalSwap = swap.total
        self.usedSwap = swap.used
        self.freeSwap = swap.free
        self.percentSwapUsed = swap.percent

    def measureMemory(self):

        mem = psutil.virtual_memory()
        
        self.usedMemory = mem.used
        self.availableMemory = mem.available
        self.memPercentUsed = mem.percent

    def measureCPU(self):
 
        self.cpuPercent = psutil.cpu_percent()


    def measureStatic(self):

        self.cpuCountLogical = psutil.cpu_count() #the number of physical cores multiplied by the number of threads that can run on each core 
        self.cpuCount = psutil.cpu_count(logical=False) #physical corees
        mem = psutil.virtual_memory()
        self.totalMemory = mem.total