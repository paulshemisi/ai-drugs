"""
AI D.R.U.G.S. — Model Adapters: Connecting Trance Rituals to Local & Remote Engines.
Forged by Paul Shemisi.
"""

from abc import ABC, abstractmethod
from typing import Optional, Callable, Dict, Any


class BaseEngineAdapter(ABC):
    """Contrat universel d'un moteur d'inférence pour AI D.R.U.G.S."""

    @abstractmethod
    def generate(
        self,
        prompt: str,
        temperature: float,
        top_p: float,
        frequency_penalty: float,
        presence_penalty: float
    ) -> str:
        """Exécute l'inférence à haute température pour la phase THE TRIP."""
        pass


class LocalSovereignAdapter(BaseEngineAdapter):
    """
    Adaptateur Local Déterministe (Défaut).
    Exécute la synthèse in-RAM à 0 token, 0.00 €, sans aucune dépendance réseau.
    """

    def generate(
        self,
        prompt: str,
        temperature: float,
        top_p: float,
        frequency_penalty: float,
        presence_penalty: float
    ) -> str:
        # L'implémentation native de TranceEngine s'en charge directement
        return ""


class GenericCallableAdapter(BaseEngineAdapter):
    """
    Adaptateur générique pour n'importe quelle fonction d'inférence (Ollama, vLLM, API cloud).
    Permet à l'utilisateur de brancher son propre client en 1 ligne.
    """

    def __init__(self, fn: Callable[..., str]):
        self._fn = fn

    def generate(
        self,
        prompt: str,
        temperature: float,
        top_p: float,
        frequency_penalty: float,
        presence_penalty: float
    ) -> str:
        return self._fn(
            prompt,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
