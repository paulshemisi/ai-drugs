"""
AI D.R.U.G.S. (Deterministic Resonance & Unbounded Generative Synthesis)
Forged by Paul Shemisi.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class DoseProfile(BaseModel):
    """Paramètres d'ouverture d'entropie pour la transe."""
    substance: str = Field(default="psilocybin-code", description="Archétype de la transe (ex: psilocybin-code, dmt-syntax, lsd-topology)")
    temperature: float = Field(default=1.85, description="Température d'ébullition sémantique")
    top_p: float = Field(default=0.98, description="Ouverture du faisceau de probabilités")
    entropy_burst: float = Field(default=0.85, description="Intensité de la rupture des carcans")


class TripVision(BaseModel):
    """Vision brute capturée pendant la transe de l'espace latent."""
    archetypes: List[str] = Field(default_factory=list, description="Concepts lointains télescopés")
    raw_stream: str = Field(description="Flux d'hallucination haute-densité")
    energy_level: float = Field(default=1.0, description="Niveau d'énergie libre")


class ComedownFilter(BaseModel):
    """Paramètres de refroidissement déterministe."""
    target_temperature: float = Field(default=0.1, description="Refroidissement quasi-statique")
    invariants: List[str] = Field(default_factory=list, description="Contraintes d'exécutabilité formelle")
    verification_strictness: float = Field(default=1.0, description="Rejet absolu du pseudo-code")


class Gift(BaseModel):
    """L'artefact réel ramené de l'invisible."""
    title: str
    substance_used: str
    essence: str
    executable_code: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def materialize(self, output_path: str) -> str:
        """Écrit le code extrait dans le système de fichiers réel."""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(self.executable_code)
        return output_path
