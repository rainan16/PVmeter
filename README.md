# ☀️ PVmeter for balcony power plant using a Merros Smart Plug 🔌

## Azure Serverless Function to monitor plugged in balcony power plant
Azure Functions are a great choice for a serverless service collecting data from the Meross Smart Plug. 

This projects monitors the power produced by a balcony power plant, stores them in a CosmosDB and finally display the last two days on a static web site (e.g. also hosted in Azure).

## Meross IoT library
This project is heavily based on Albertor Geniola's "Meross IoT library".

See *Meross IoT library* on Github: [MerossIot Python Library](https://github.com/albertogeniola/MerossIot/tree/0.4.X.X/meross_iot)
