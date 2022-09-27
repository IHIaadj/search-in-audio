import whisper
import datetime
model = whisper.load_model("base")

result = model.transcribe("reading_session.mp3")

search = "transformers"
start = 0
seek = 0
id = 0
for segment in result["segments"]:
    if search in segment["text"]:
        id = segment["id"]
        start = segment["start"]
        seek = segment["seek"]
        break

print('You may want to listen from', str(datetime.timedelta(seconds=start-20)))