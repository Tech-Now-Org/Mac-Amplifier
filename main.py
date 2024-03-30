import sounddevice as sd

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata * amplification_factor

if __name__ == "__main__":
    # Specify the desired amplification percentage here
    desired_percentage = 200  # Change this value to set the desired amplification percentage

    # Convert percentage to amplification factor
    amplification_factor = desired_percentage / 100.0

    samplerate = sd.query_devices(None, 'input')['default_samplerate']

    with sd.Stream(callback=callback, blocksize=0, device=None, channels=1, samplerate=samplerate):
        print(f"Recording with {desired_percentage}% amplification. Press Ctrl+C to stop.")
        try:
            sd.sleep(1000000)
        except KeyboardInterrupt:
            print("\nRecording stopped.")
