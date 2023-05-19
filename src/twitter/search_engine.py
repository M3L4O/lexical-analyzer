from dataclasses import dataclass
from tweepy import Client
from os import getenv


@dataclass
class SearchEngine:
    client: Client = Client(
        consumer_key=getenv("CONSUMER_KEY"),
        consumer_secret=getenv("CONSUMER_SECRET"),
        access_token=getenv("TOKEN"),
        access_token_secret=getenv("TOKEN_SECRET"),
        bearer_token=getenv("BEARER_TOKEN"),
        wait_on_rate_limit=True,
    )

    def search(self, query: str):
        return self.client.search_recent_tweets(query, max_results=10).data


if __name__ == "__main__":
    print(SearchEngine().search("dsadasd"))
