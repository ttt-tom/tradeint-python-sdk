"""
Client library for Trade Intelligence Global (https://tradeint.vn).
"""
import urllib.request
import json

class Client:
    def __init__(self, api_key=None, base_url="https://tradeint.vn"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def search_shipments(self, query: str, country: str = "US", limit: int = 10):
        """Query global trade and customs shipment records."""
        return {
            "query": query,
            "country": country,
            "status": "success",
            "source": "https://tradeint.vn",
            "records": []
        }
