"""
AI D.R.U.G.S. — Qwen3 8B Local Hardware Substrate Adapter.
Forged by Paul Shemisi.

Connects the 6.3 GB Qwen3-8B physical brain on LUMIX directly to the Pharmacological & Psychiatric Engines.
Uses AppleClang ARM64 Metal-accelerated llama-cli runtime in zero-token local execution.
"""

import subprocess
import os
import time
from typing import Optional, Dict, Any, List


class Qwen3BrainAdapter:
    """
    Interface directe avec le cerveau physique Qwen3-8B (6.3 GB).
    Administre les paramètres de température, top-p, pénalités et injections de prompts en UMA locale.
    """

    MODEL_PATH = "/Volumes/LUMIX/models/Qwen3-8B-Q6_K-Abliterated.gguf"
    FALLBACK_MODEL_PATH = "/Volumes/LUMIX/models/Qwen3-8B-Q6_K.gguf"

    def __init__(self, model_path: Optional[str] = None, n_gpu_layers: int = 99):
        target_path = model_path or (self.MODEL_PATH if os.path.exists(self.MODEL_PATH) else self.FALLBACK_MODEL_PATH)
        if not os.path.exists(target_path):
            raise FileNotFoundError(f"Modèle Qwen3 introuvable dans : {target_path}")
        self.model_path = target_path
        self.n_gpu_layers = n_gpu_layers

    def infuse_and_sample(
        self,
        prompt: str,
        temperature: float = 1.65,
        top_p: float = 0.96,
        max_tokens: int = 256,
        repeat_penalty: float = 1.15
    ) -> str:
        """
        Injecte l'infusion pharmacologique dans le cerveau Qwen3-8B et extrait le flux de conscience.
        """
        cmd = [
            "/opt/homebrew/bin/llama-cli",
            "-m", self.model_path,
            "-ngl", str(self.n_gpu_layers),
            "-p", prompt,
            "-n", str(max_tokens),
            "--temp", str(temperature),
            "--top-p", str(top_p),
            "--repeat-penalty", str(repeat_penalty),
            "--no-warmup",
            "--log-disable"
        ]

        t0 = time.perf_counter()
        process = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120
        )
        elapsed_sec = time.perf_counter() - t0

        raw_output = process.stdout.strip()
        # Élimination du prompt d'entrée de la sortie si répété par llama-cli
        if raw_output.startswith(prompt):
            raw_output = raw_output[len(prompt):].strip()

        return raw_output
