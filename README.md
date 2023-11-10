# psutil to Prometheus

![Sample dashboard screenshot](./Sample%20Grafana%20Dashboard/image.png)

Monitor multiple systems with Prometheus and Grafana

psutil-to-prometheus gathers some (as of now) psutil stats, calculates some rates, and prepares them to be collected by Prometheus. 

## How to run 

Clone the repo, then run

```
pip install -r requirements.txt

```
subsequently, you can simply start the program using

```
python main.py 
```

or if you're on a Windows machine, double click on `start_script.bat`

### Arguments 

You can define the frequency of measurements and the port used using arguments. To know more, run 

```
python main.py --help
```

## Using Docker 

Add the following to your docker compose :

```
version: '3'
services:
  system-monitor:
    container_name: psutil-to-prometheus
    build: /path/to/directory/psutil-to-prometheus
    ports:
      - 27020:27020
```

then run 

```
sudo docker compose build --no-cache psutil-to-prometheus  
```

Finally, start the docker compose 

```
docker compose up -d psutil-to-prometheus
```

### Warning 
psutil on Docker for windows will only return resources available to the docker container. Therefore for accurate readings, I recommend running without Docker on windows, using the .bat script.  Docker works fine on Linux. 

## Sample Dashboard 

Once you have your prometheus reading from psutil-to-prometheus and your prometheus is set up as a datasource on Grafana, you can use the JSON model in the Sample Grafana Dashboard folder for a dashboard which shows stats per device (instanceName)