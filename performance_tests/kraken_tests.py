from locust import HttpUser, task, between


class KrakenTests(HttpUser):
    wait_time = between(1, 2)

    @staticmethod
    def validate_response_code(response, expected_response_code):
        if response.status_code == expected_response_code:
            response.success()
        else:
            response.failure(f"Response code was not {expected_response_code}.")

    @task(1)
    def get_server_time(self):  # Get the server's time.
        with self.client.get("/0/public/Time", name="Get Server Time", catch_response=True) as response:
            self.validate_response_code(response=response, expected_response_code=200)

    @task(1)
    def get_system_status(self):  # Get the current system status or trading mode.
        with self.client.get("/0/public/SystemStatus", name="Get System Status", catch_response=True) as response:
            self.validate_response_code(response=response, expected_response_code=200)

    @task(1)
    def get_assets_info(self):  # Get information about the assets.
        with self.client.get("/0/public/Assets", name="Get Asset Info", catch_response=True) as response:
            self.validate_response_code(response=response, expected_response_code=200)

    @task(1)
    def get_ohlc_data(self):  # OHLC
        with self.client.get("/0/public/OHLC?pair=XBTUSD", name="Get OHLC Data", catch_response=True) as response:
            self.validate_response_code(response=response, expected_response_code=200)
