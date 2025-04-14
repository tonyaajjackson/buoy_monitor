# Arctic Buoy Monitoring System

A monitoring system that simulates data from Arctic buoys, sends it to a Graphite database, and visualizes it in Grafana. Made in connection with the [Buoy Demo project](https://tonyaajjackson.com/Portfolio/Buoy-Demo/Buoy-Demo).

## Quick Start

1. Clone this repository
2. Copy `template.env` to `.env` and configure credentials if needed
3. Start the containers: `docker-compose up -d`
4. Run the buoy simulator: `./fake_buoy_monitoring.sh`
5. Access Grafana at `http://localhost` (default credentials: admin/admin)

## Components

- **Simulator Script**: Generates fake buoy data with location information
- **Graphite**: Time-series database for storing buoy metrics
- **Grafana**: Visualization platform with world map plugin for displaying buoy locations

## How It Works

The system simulates 10 Arctic buoys (buoy_0 through buoy_9) positioned at 58.232067°N with varying longitudes. Each buoy sends data to Graphite every second, with a 5-second pause after each complete cycle.

```bash
# Example data flow
Simulator → Graphite (port 2004) → Grafana Dashboard
```

## Configuration

### Docker Setup
- Graphite container exposes ports 2004 (carbon) and 8080 (web interface)
- Grafana container exposes port 80 (web UI)
- Persistent storage for both services via Docker volumes

### Dependencies
- Python 3.8
- Docker and Docker Compose
- Grafana with worldmap panel plugin (auto-installed)

## Customization

To modify buoy parameters, edit `fake_buoy_monitoring.sh`:
- Change the number of buoys by adjusting the range `{0..9}`
- Modify latitude/longitude values to simulate different locations
- Adjust sleep intervals to change data transmission frequency

## Dashboard Setup

1. Log into Grafana (http://localhost) using credentials from `.env` file
2. Add Graphite as a data source (URL: http://graphite:8080)
3. Import or create a dashboard with the worldmap panel
4. Configure the worldmap to use buoy latitude/longitude data

## Development

This project uses pipenv for dependency management:
```bash
pipenv install
pipenv shell
python ./monitor/monitor.py --help
```

## Troubleshooting

- If no data appears in Grafana, check that the simulator script is running
- Verify Graphite is receiving data by checking its web interface at http://localhost:8080
- Ensure the Grafana worldmap plugin is installed correctly

## License

This project is licensed under the MIT License - see the LICENSE file for details.
