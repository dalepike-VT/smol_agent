```python
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from whisper_gpt import transcribe_audio, meeting_minutes
from docx_export import save_as_docx

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['audio_file']
        filename = secure_filename(file.filename)
        audio_file_path = os.path.join('/tmp', filename)
        file.save(audio_file_path)
        transcription = transcribe_audio(audio_file_path)
        minutes = meeting_minutes(transcription)
        docx_filename = filename.rsplit('.', 1)[0] + '.docx'
        save_as_docx(minutes, docx_filename)
        return render_template('result.html', minutes=minutes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```