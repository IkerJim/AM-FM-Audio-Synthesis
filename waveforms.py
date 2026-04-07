import numpy as np
import sounddevice as sd

def sine_wave(
    size: int
    ) -> np.ndarray:

    angle_delta = 2 * np.pi / size

    angle = 0

    samples = np.zeros(size)

    for i in range(size):
        samples[i] = np.sin(angle)
        angle += angle_delta

    return samples

def oscillator(
    waveform: np.array, 
    frequency: float=440.0,
    duration: float=1.0,
    amplitude: float=0.5, 
    sample_rate: int=44100
    ) -> np.array:

    table_delta = frequency * len(waveform) / sample_rate

    current_index = 0

    total_len = int(sample_rate * duration)
    samples = np.zeros(total_len)

    for i in range(total_len):
        idx1 = int(current_index)
        idx2 = (idx1 + 1) % len(waveform)
        frac = current_index - idx1

        samples[i] = (1 - frac) * waveform[idx1] + frac * waveform[idx2]

        current_index += table_delta
        if current_index >= len(waveform):
            current_index -= len(waveform)

    max_amplitude = np.max(samples)
    samples *= amplitude / max_amplitude

    return samples

TABLE_SIZE = 1024

def main():
    sine = sine_wave(TABLE_SIZE)

    audio = oscillator(sine, frequency=220, duration=2.0, amplitude=0.25)

    sd.play(audio)
    sd.wait()

if __name__ == "__main__":
    main()