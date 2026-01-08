import torch
import torch.nn.functional as F
import numpy as np

class HRR:
    """
    Holographic Reduced Representation Engine.
    Implements binding (multiplication) and unbinding (correlation)
    using Circular Convolution via FFT.
    """
    def __init__(self, dim=1024):
        self.dim = dim

    def create_concept(self, name):
        """Generates a random high-dimensional vector to represent a base concept."""
        # Standard Normal distribution is best for HRR
        vec = torch.randn(self.dim)
        # Normalize to length 1
        return F.normalize(vec, p=2, dim=0)

    def bind(self, a, b):
        """
        Combines two vectors (A * B) to create a new, unique 'bound' vector.
        Operation: Circular Convolution.
        Math: InverseFFT( FFT(A) * FFT(B) )
        """
        # We use Real-to-Complex FFT for efficiency
        a_fft = torch.fft.rfft(a)
        b_fft = torch.fft.rfft(b)
        
        # Element-wise multiplication in frequency domain = Convolution in time domain
        bound_fft = a_fft * b_fft
        
        bound_vec = torch.fft.irfft(bound_fft, n=self.dim)
        return F.normalize(bound_vec, p=2, dim=0)

    def unbind(self, composite, key):
        """
        Extracts a value from a bound vector given the key.
        Operation: Circular Correlation.
        Math: InverseFFT( FFT(Composite) * conj(FFT(Key)) )
        """
        comp_fft = torch.fft.rfft(composite)
        key_fft = torch.fft.rfft(key)
        
        # Multiply by complex conjugate to subtract the key's phase
        result_fft = comp_fft * torch.conj(key_fft)
        
        result_vec = torch.fft.irfft(result_fft, n=self.dim)
        return F.normalize(result_vec, p=2, dim=0)

    def similarity(self, a, b):
        """Cosine similarity to check if two concepts are the same."""
        return torch.dot(a, b).item()