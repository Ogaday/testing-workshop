from datetime import datetime
from urllib.parse import urljoin

import pandas as pd
import requests


def save_intensity_data(start: datetime, end: datetime, destination: str) -> None:
    base_url = "https://api.carbonintensity.org.uk"
    path = "/intensity/{from}/{to}".format(
        **{
            "from": start.strftime("%Y-%m-%dT%H:%MZ"),
            "to": end.strftime("%Y-%m-%dT%H:%MZ"),
        }
    )
    url = urljoin(base_url, path)
    r = requests.get(url)
    data = []
    for row in r.json()["data"]:
        data.append(
            {
                "from_": row["from"],
                "to": row["to"],
                "intensity_forecast": row["intensity"]["forecast"],
                "intensity_actual": row["intensity"]["actual"],
                "intensity_index": row["intensity"]["index"],
            }
        )
    df = pd.DataFrame(data)
    df.to_csv(destination, index=False, quoting=1)


import tempfile
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest
import vcr


@pytest.fixture
def directory():
    with tempfile.TemporaryDirectory() as dir:
        # Note the yield here instead of return:
        yield dir


@vcr.use_cassette("cassettes/intensity.yaml")
def test_save_intensity_data(directory):
    filepath = Path(directory) / "test.txt"
    start = datetime(2024, 7, 1, tzinfo=ZoneInfo("UTC"))
    end = datetime(2024, 7, 2, tzinfo=ZoneInfo("UTC"))

    save_intensity_data(start=start, end=end, destination=filepath)
