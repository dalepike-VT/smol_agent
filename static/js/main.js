```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const uploadButton = document.getElementById('upload-button');
    const audioFileInput = document.getElementById('audio-file');
    const resultContainer = document.getElementById('result-container');

    uploadButton.addEventListener('click', () => {
        const audioFile = audioFileInput.files[0];
        if (!audioFile) {
            alert('Please select an audio file first.');
            return;
        }

        const formData = new FormData();
        formData.append('audio_file', audioFile);

        fetch('/transcribe', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'transcription-complete') {
                displayResult(data.minutes);
            } else {
                alert('An error occurred during transcription.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function displayResult(minutes) {
        resultContainer.innerHTML = `
            <h2>Meeting Minutes</h2>
            <h3>Abstract Summary</h3>
            <p>${minutes.abstract_summary}</p>
            <h3>Key Points</h3>
            <p>${minutes.key_points}</p>
            <h3>Action Items</h3>
            <p>${minutes.action_items}</p>
            <h3>Sentiment Analysis</h3>
            <p>${minutes.sentiment}</p>
        `;
    }
});
```