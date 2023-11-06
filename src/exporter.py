from .importer import Importer
from prometheus_client import Gauge

class PrometheusExporter:
    def __init__(self, importer):
        self.importer = importer

        self.g_cpuCount = Gauge('cpuCount', 'Physical CPU cores in the machine')
        self.g_cpuCountLogical = Gauge('cpuCountLogical', 'logical CPU cores in the machine')
        self.g_cpuCountUsable = Gauge('cpuCountUsable', 'Usable CPU cores in the machine')
        self.g_cpuPercent = Gauge('cpuPercent', 'percentage CPU usage')

        self.g_totalMemory = Gauge('totalMemory', 'Total memory')
        self.g_usedMemory = Gauge('usedMemory', 'Used memory')
        self.g_availableMemory = Gauge('availableMemory', 'Available memory')
        self.g_percentMemoryUsed = Gauge('percentMemoryUsed', 'percentage used memory')

        self.g_totalSwap = Gauge('totalSwap', 'Total swap memory')
        self.g_usedSwap = Gauge('usedSwap', 'Used swap memory')
        self.g_availableSwap = Gauge('availableSwap', 'Available swap memory')
        self.g_percentSwapUsed = Gauge('percentSwapUsed', 'percentage used swap')

        self.g_totalDisk = Gauge('totalDisk', 'Total disk space')
        self.g_usedDisk = Gauge('usedDisk', 'Used disk space')
        self.g_freeDisk = Gauge('freeDisk', 'free disk space')
        self.g_percentDiskUsed = Gauge('percentDiskUsed', 'percentage used disk space')

        self.g_bytesSent = Gauge('bytesSent', 'total bytes sent')
        self.g_bytesRecv = Gauge('bytesRecv', 'total bytes recv')
        self.g_packetsSent = Gauge('packetsSent', 'total packets sent')
        self.g_packetsRecv = Gauge('packetsRecv', 'packets received')
        self.g_errorIn = Gauge('errorIn', 'Total error in incoming packets')
        self.g_errorOut = Gauge('errorOut', 'total error in outgoing packets')
        self.g_dropIn = Gauge('dropIn', 'total incoming packets dropped')
        self.g_dropOut = Gauge('dropOut', 'total outgoing packets dropped')

        self.update_gauges()


    def update_gauges(self):
         
        self.g_cpuCount.set(self.importer.cpuCount)
        self.g_cpuCountLogical.set(self.importer.cpuCountLogical)
        self.g_cpuCountUsable.set(self.importer.cpuCountUsable)
        self.g_cpuPercent.set(self.importer.cpuPercent)
        self.g_totalMemory.set(self.importer.totalMemory)
        self.g_usedMemory.set(self.importer.usedMemory)
        self.g_availableMemory.set(self.importer.availableMemory)
        self.g_percentMemoryUsed.set(self.importer.memPercentUsed)

        self.g_totalDisk.set(self.importer.totalDisk)
        self.g_usedDisk.set(self.importer.usedDisk)
        self.g_freeDisk.set(self.importer.freeDisk)
        self.g_percentDiskUsed.set(self.importer.diskPercentUsed)

        self.g_totalSwap.set(self.importer.totalSwap)
        self.g_usedSwap.set(self.importer.usedSwap)
        self.g_availableSwap.set(self.importer.freeSwap)
        self.g_percentSwapUsed.set(self.importer.percentSwapUsed)

        self.g_bytesSent.set(self.importer.bytesSent)
        self.g_bytesRecv.set(self.importer.bytesRecv)
        self.g_packetsSent.set(self.importer.packetsSent)
        self.g_packetsRecv.set(self.importer.packetsRecv)
        self.g_errorIn.set(self.importer.errorIn)
        self.g_errorOut.set(self.importer.errorOut)
        self.g_dropIn.set(self.importer.dropIn)
        self.g_dropOut.set(self.importer.dropOut)