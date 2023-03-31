import logging
from typing import Optional

import polars as pl


class ExploratoryDataAnalysis:

    def __init__(self) -> None:
        super().__init__()

    def get_word_transcription(self) -> str:
        try:
            return self.parser.get_transcription()
        except:
            logging.exception("api error")
            return ""
            # raise DictionaryApiError


    def load_dataset(self) -> any:
        try:
            # df =
            return pl.read_csv("https://j.mp/iriscsv")
        except:
            logging.exception("error loading dataset")
            return "False"
