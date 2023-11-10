from prometheus_client import start_http_server
from time import sleep
import threading
from traceback import print_exc
import argparse

from src.exporter import PrometheusExporter as Exporter
from src.importer import Importer as Importer

def PollHighFreq(importer, exporter,HighFreqPollingTime):

    while True:
        importer.measure()
        exporter.update_gauges()
        sleep(HighFreqPollingTime)

def PollLowFreq(importer, exporter,LowFreqPollingTime):

    while True:
        importer.measureLowFreq()
        exporter.update_gauges()
        sleep(LowFreqPollingTime)

import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Polling times and port for the program")

    # Add the arguments
    parser.add_argument('--HighFreqPoll', type=int, default=1, help='How frequently to measure very dynamic values, like CPU , memory, swap, network')
    parser.add_argument('--LowFreqPoll', type=int, default=10, help='How frequency to measure more slower changing values, like disk usage')
    parser.add_argument('--PrometheusPort', type=int, default=27020, help='Port for the prometheus server')

    # Parse the arguments
    args = parser.parse_args()

    try:
        start_http_server(args.PrometheusPort)

        importer = Importer()
        importer.measure()
        exporter = Exporter(importer)
        exporter.update_gauges()

        thread_HighFreq = threading.Thread(target=PollHighFreq, args=(importer, exporter, args.HighFreqPoll))
        thread_LowFreq = threading.Thread(target=PollLowFreq, args=(importer, exporter, args.LowFreqPoll))

        thread_HighFreq.daemon = True
        thread_LowFreq.daemon = True

        thread_HighFreq.start()
        thread_LowFreq.start()
    
        while True:
            sleep(1)

    except KeyboardInterrupt:
        print("Received KeyboardInterrupt, stopping threads...")

    except Exception as e:
        with open('error_log.txt', 'a') as f:
            f.write(f"An error occurred: {e}\n")
            f.write("Traceback (most recent call last):\n")
            print_exc(file=f)




if __name__ == "__main__":

    main()