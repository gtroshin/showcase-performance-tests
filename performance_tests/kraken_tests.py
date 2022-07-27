from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def get_server_time(self):  # Get the server's time.
        self.client.get("/0/public/Time", name="Get Server Time")

    @task(1)
    def get_system_status(self):  # Get the current system status or trading mode.
        self.client.get("/0/public/SystemStatus", name="Get System Status")

    @task(1)
    def get_assets_info(self):  # Get information about the assets.
        self.client.get("/0/public/Assets", name="Get Asset Info")

    @task(1)
    def get_ohlc_data(self):  # OHLC
        self.client.get("/0/public/OHLC?pair=XBTUSD", name="Get OHLC Data")
