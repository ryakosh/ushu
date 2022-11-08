import os
import sys

from dotenv import load_dotenv

load_dotenv()

try:
    USHU_HASHIDS_SALT = os.environ['USHU_HASHIDS_SALT']
    USHU_HASHIDS_MINLEN = int(os.environ['USHU_HASHIDS_MINLEN'])
    USHU_SHORTURL_MAXLEN = int(os.environ['USHU_SHORTURL_MAXLEN'])
except KeyError as key:
    print(f"ERR: {key} Not set", file=sys.stderr)
    sys.exit(1)
