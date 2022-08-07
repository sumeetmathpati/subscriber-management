import motor

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["mongodb://localhost:27017"])
db = client.college
