import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28427872"))
    API_HASH = os.environ.get("API_HASH", "1b61c2213e7f9f26175fe0a77dec902e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5952944987:AAGmwWdwGyOzYi9aVDA8WhByGww1Pgimm4Q")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzQBu1WSQX6gsMCaxmu3nFELIb-ku5rbwgMOU7UAxTSxZaiih0b2bud61AvXqjmmGmd1mLZEaSbDpC4f1rEqTLbOcFn4UnKb2wYyMVMsRTyIX53UR1xKglc7VNy9v7YdNAi6qN5T-H-KLnDjQjmYE1hWrfMf_haDWSD7o8e7HIEpp0CJdy2JaOkH8eSN8smhh4t6THhEUW-5FV7Gx6tQUc1qihDeIgwlqDyudgRyySvyO2WNP-9vNVmepLcieavhl1HtssZqVDlA15ackeqYVlX46K91npk2HMDvfEvbf22beot2Ks06buOzIw-ghM5zijY7CK-Vp4j_3eLWOod2aXZs2H8=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MdzMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "gringomdz") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "mdzup") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5012010632", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
