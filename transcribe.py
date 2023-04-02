import sys
import whisper
import torch

audio_data = whisper.load_audio(sys.argv[1])

model = whisper.load_model("medium", device="cuda")

_ = model.cuda()

with torch.no_grad():
    result = model.transcribe(
            audio_data, 
            verbose=False, 
            language="japanese",
            beam_size=1,
            fp16=True
    )
