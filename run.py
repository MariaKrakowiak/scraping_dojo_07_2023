from dotenv import load_dotenv
from preparation.DataPreparation import browser_settings, data_preparation
from preparation.GenerateOutput import generate_output

# Load environmental variables
load_dotenv()

# Browser settings
browser_settings()

# Prepare data
data_preparation()

# Generate output
generate_output()



