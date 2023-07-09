import os
import pandas as pd
import settings


def generate_output():
    """
    Generate final jsonl file with all quotes, authors and tags
    :return:
    """
    df = pd.DataFrame(settings.overall_dict)
    df.to_json(str(os.getenv('OUTPUT_FILE')), orient='records', lines=True)
