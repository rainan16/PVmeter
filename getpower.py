import asyncio
import os
import logging

from meross_iot.controller.mixins.electricity import ElectricityMixin
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

EMAIL = os.environ.get('MEROSS_EMAIL')
PASSWORD = os.environ.get('MEROSS_PASSWORD')


async def load_current_value():
    power = 0

    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.async_from_user_password(email=EMAIL, password=PASSWORD)
    if http_api_client:
        logging.info("login okay")
    else:
        logging.info('login failed')


    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Retrieve all the devices that implement the electricity mixin
    await manager.async_device_discovery()
    devs = manager.find_devices(device_class=ElectricityMixin)

    if len(devs) < 1:
        return "No electricity-capable device found."
    else:
        dev = devs[0]

        # Update device status: this is needed only the very first time we play with this device (or if the
        #  connection goes down)
        await dev.async_update()

        # Read the electricity power/voltage/current
        power = await dev.async_get_instant_metrics()

    # Close the manager and logout from http_api
    manager.close()
    await http_api_client.async_logout()

    return power.toJSON()