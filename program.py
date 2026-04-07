import numpy as np
import sounddevice as sd

def am_synthesis(
    carrier_frequency: float,
    modulator_wave: np.array,
    modulation_index: float=0.5,
    amplitude: float=0.5,
    sample_rate: int=44100
    ) -> np.array:
    """
    Generates an AM Synthesis waveform
    """

    # Primero calcular el número de muestras requeridas
    total_len = len(modulator_wave)

    # Generar un array de puntos temporales
    time_points = np.arange(total_len) / sample_rate

    # Generar la onda portadora
    carrier_wave = np.sin(2 * np.pi * carrier_frequency * time_points)

    # Aplicar la fórmula de AM Synthesis
    am_wave = (1 + modulation_index * modulator_wave) * carrier_wave

    # Normalizar a la amplitud específica
    max_amplitude = np.max(am_wave)
    am_wave = amplitude * (am_wave / max_amplitude)

    return am_wave

def fm_synthesis(
    carrier_frequency: float,
    modulator_wave: np.array,
    modulation_index: float=3.0,
    amplitude: float=0.5,
    sample_rate: int=44100
) -> np.array:
    """
    Generates an PM Synthesis waveform
    """

    # Primero calcular el número de muestras requeridas
    total_len = len(modulator_wave)

    # Generar un array de puntos temporales
    time_points = np.arange(total_len) / sample_rate

    # Generar la onda FM utilizando la frecuencia instantánea
    fm_wave = np.sin(2 * np.pi * carrier_frequency * time_points + modulation_index * modulator_wave)

    # Normalizar a la amplitud específica
    max_amplitude = np.max(fm_wave)
    fm_wave = amplitude * (fm_wave / max_amplitude)

    return fm_wave

def sine_tone(
    frequency: int=440,
    duration: float=1.0,
    amplitude:float=0.5,
    sample_rate:int=44100
    ) -> np.array:
    """
    Generate a sine tone
    """

    # Calcular el número de muestras requeridas
    total_len = duration * sample_rate

    # Generar un array de puntos temporales
    time_points = np.arange(total_len) / sample_rate

    # Generar la onda sinusiodal
    sine_wave = np.sin(2 * np.pi * frequency * time_points)

    # Normalizar a la amplitud específica
    sine_wave = sine_wave * amplitude

    return sine_wave

def main():

    # Crear una onda moduladora
    my_modulator = sine_tone(500, 3)

    # Apply frequency modulation
    fm_sound = fm_synthesis(220, my_modulator, modulation_index=1.0, amplitude=0.1)

    # Play the sound
    sd.play(fm_sound)
    sd.wait()

if __name__ == "__main__":
    main()
