from prometheus_client import start_http_server
from time import sleep


from src.exporter import PrometheusExporter as Exporter
from src.importer import Importer as Importer

def main():

    start_http_server(27020)

    importer = Importer()
    importer.measure()
    exporter = Exporter(importer)
    exporter.update_gauges()

    while True:
        importer.measure()
        exporter.update_gauges()
        sleep(10)

if __name__ == "__main__":

    main()