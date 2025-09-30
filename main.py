from gradio_client import Client, handle_file
from pathlib import Path

def clone_voice(audio_file_path, text, output_filename="result.wav"):
    """Clone a voice using the provided audio sample and generate speech with the given text."""
    client = Client("tonyassi/voice-clone")
    
    result = client.predict(
        text,
        handle_file(audio_file_path),
        api_name="/predict"
    )
    
    output_path = Path(output_filename)
    output_path.write_bytes(Path(result).read_bytes())
    
    return str(output_path)

if __name__ == "__main__":
    audio_path = "george.mp3"
    text = "Greetings from Intraamerican University of Puerto Rico, Metro campus"
    
    try:
        output_audio = clone_voice(audio_path, text)
        print(f"Voice cloning successful! Output saved to: {output_audio}")
    except Exception as e:
        print(f"Error during voice cloning: {e}")