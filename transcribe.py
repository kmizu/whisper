import sys
import whisper

target_file=sys.argv[1]

model = whisper.load_model("large-v2")
result = model.transcribe(target_file, verbose=True, language="ja")
