"""
AI D.R.U.G.S. — Qwen3 8B Warm Socket Adapter (Zero Disk Re-read).
Forged by Paul Shemisi.

Connects to the warm in-memory Qwen3-8B daemon via loopback HTTP socket.
Responses are returned in milliseconds without touching the physical disk.
"""

import urllib.request
import json
import time
from typing import Optional, Dict, Any


class Qwen3WarmSocketAdapter:
    """
    Client ultra-rapide pour le cerveau chaud Qwen3-8B résident en RAM.
    """

    DEFAULT_ENDPOINT = "http://127.0.0.1:8088/completion"
    HEALTH_ENDPOINT = "http://127.0.0.1:8088/health"

    def __init__(self, endpoint: Optional[str] = None):
        self.endpoint = endpoint or self.DEFAULT_ENDPOINT

    def is_alive(self) -> bool:
        """Vérifie si le cerveau est allumé et prêt à recevoir une dose."""
        try:
            req = urllib.request.Request(self.HEALTH_ENDPOINT, method="GET")
            with urllib.request.urlopen(req, timeout=1.0) as resp:
                return resp.status == 200
        except Exception:
            return False

    def infuse(
        self,
        prompt: str,
        temperature: float = 1.65,
        top_p: float = 0.96,
        max_tokens: int = 256,
        repeat_penalty: float = 1.15
    ) -> str:
        """
        Envoie l'infusion directement dans la RAM du modèle via la socket locale.
        Exécution pure en millisecondes.
        """
        payload = {
            "prompt": prompt,
            "temperature": temperature,
            "top_p": top_p,
            "n_predict": max_tokens,
            "repeat_penalty": repeat_penalty,
            "stop": ["```\n\n", "User:", "Human:"]
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.endpoint,
            data=data,
            headers={"Content-Type": "application/json"}
        )

        t0 = time.perf_counter()
        with urllib.request.urlopen(req, timeout=60.0) as resp:
            raw_res = json.loads(resp.read().decode("utf-8"))
        elapsed = time.perf_counter() - t0

        return raw_res.get("content", "").strip()
