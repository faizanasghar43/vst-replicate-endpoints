from flask import Flask, request
import replicate

app = Flask(__name__)


@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    print("request received")

    if 'audio' not in request.files:
        return 'No audio file provided', 400

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return 'No selected audio file', 400

    # You can now process the audio file as needed
    # For example, save it to a specific directory
    audio_file.save('upload/' + audio_file.filename)
    output = replicate.run(
        "zsxkib/realistic-voice-cloning:0a9c7c558af4c0f20667c1bd1260ce32a2879944a0b9e44e1398660c077b1550",
        input={"song_input": open(f"/home/faizi/PycharmProjects/vst-cpp-api/upload/{audio_file.filename}", "rb")}
    )

    return output


if __name__ == '__main__':
    app.run(debug=True)
