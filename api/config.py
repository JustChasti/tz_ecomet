import os


# basic configuration

parser_host = 'http://parser:5000'

my_host = '0.0.0.0'

test_mode = True

# db cofiguration
base_user = os.getenv('BASE_USER')
base_pass = os.getenv('BASE_PASSWORD')
base_name = os.getenv('BASE_NAME')
base_host = os.getenv('BASE_HOST')
base_port = os.getenv('BASE_PORT')
