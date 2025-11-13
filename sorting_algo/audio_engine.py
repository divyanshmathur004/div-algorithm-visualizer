"""
Audio engine for generating tones based on array values
"""

import numpy as np
import pygame
from constants import *


class AudioEngine:
    """Handles all audio generation and playback"""
    
    def __init__(self, array_size=DEFAULT_ARRAY_SIZE):
        """Initialize the audio engine"""
        pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1, buffer=512)
        self.array_size = array_size
        
    def value_to_frequency(self, value):
        """Map array value to audio frequency"""
        normalized = (value - 1) / (self.array_size - 1)
        return MIN_FREQUENCY + normalized * (MAX_FREQUENCY - MIN_FREQUENCY)
    
    def generate_tone(self, frequency, duration=None):
        """Generate a tone at specified frequency with envelope"""
        if duration is None:
            duration = NOTE_DURATION
            
        num_samples = int(duration * SAMPLE_RATE)
        
        # Generate sine wave
        t = np.linspace(0, duration, num_samples, False)
        wave = np.sin(2 * np.pi * frequency * t)
        
        # Add envelope to prevent clicking
        envelope = np.ones_like(wave)
        fade_samples = int(FADE_DURATION * SAMPLE_RATE)
        envelope[:fade_samples] = np.linspace(0, 1, fade_samples)
        envelope[-fade_samples:] = np.linspace(1, 0, fade_samples)
        wave = wave * envelope
        
        # Convert to 16-bit integer
        wave = (wave * 32767).astype(np.int16)
        
        # Create stereo sound
        stereo_wave = np.column_stack((wave, wave))
        
        return pygame.sndarray.make_sound(stereo_wave)
    
    def play_value(self, value):
        """Play a tone corresponding to a value"""
        freq = self.value_to_frequency(value)
        sound = self.generate_tone(freq)
        sound.play()
