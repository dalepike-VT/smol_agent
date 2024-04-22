```python
import openai

openai.api_key = 'your-api-key'

def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe(file=audio_file)
    return response.data['text']

def abstract_summary_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following meeting transcription: {transcription}"}
        ]
    )
    return response['choices'][0]['message']['content']

def key_points_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Extract key points from the following meeting transcription: {transcription}"}
        ]
    )
    return response['choices'][0]['message']['content']

def action_item_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Identify action items from the following meeting transcription: {transcription}"}
        ]
    )
    return response['choices'][0]['message']['content']

def sentiment_analysis(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Analyze the sentiment of the following meeting transcription: {transcription}"}
        ]
    )
    return response['choices'][0]['message']['content']

def meeting_minutes(audio_file_path):
    transcription = transcribe_audio(audio_file_path)
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    action_items = action_item_extraction(transcription)
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }
```