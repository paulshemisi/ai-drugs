"""
AI D.R.U.G.S. — Public High-Level Unified API Client.
Forged by Paul Shemisi.

Enables the exact 3-line public interface designed for massive developer adoption:
    from ai_drugs import TranceEngine
    drugs = TranceEngine(model="llama3", dose="shamanic")
    breakthrough = drugs.trip("Trouver une nouvelle architecture de compression sans perte")
    print(breakthrough.gift)
"""

from typing import Optional, Union, Callable, Any, Dict
from .ceremony import Ceremony
from .core.substances import Substance, PharmacopoeiaRegistry
from .core.gift_oracle import EnhancedGift


class BreakthroughResult:
    """Résultat synthétisé de la transe et du recuit, accessible pour les développeurs."""

    def __init__(self, gift: EnhancedGift, ceremony: Ceremony):
        self._gift = gift
        self._ceremony = ceremony

    @property
    def gift(self) -> str:
        """Retourne le code réel pur, documenté et immédiatement exécutable."""
        return self._gift.executable_code

    @property
    def test_suite(self) -> str:
        """Retourne la suite de tests unitaires formelle générée automatiquement."""
        return self._gift.test_suite_code

    @property
    def purity(self) -> float:
        """Score de pureté AST (1.0 = zéro mock, zéro stub)."""
        return self._gift.audit.purity_score

    @property
    def latency_us(self) -> float:
        """Latence d'exécution microseconde en RAM."""
        return self._gift.benchmark().execution_latency_us

    @property
    def tokens_saved(self) -> int:
        """Nombre de tokens de prompting itératif cloud épargnés."""
        if self._ceremony.token_savings:
            return self._ceremony.token_savings.tokens_saved
        return 0

    @property
    def raw_vision(self) -> str:
        """Le flux visionnaire brut capturé pendant la transe."""
        if self._ceremony.last_vision:
            return self._ceremony.last_vision.raw_stream
        return ""

    def __repr__(self) -> str:
        return f"<BreakthroughResult purity={self.purity * 100:.1f}% latency={self.latency_us:.2f}µs>"


class PublicTranceEngine:
    """
    Interface Grand Public d'AI D.R.U.G.S.
    Compatible avec n'importe quel modèle (local ou cloud) ou en mode autonome natif.
    """

    DOSE_MAPPING = {
        "micro": "psilocybin-code",
        "moderate": "lsd-topology",
        "shamanic": "ayahuasca-kernel",
        "heroic": "dmt-syntax",
        "dissociative": "ketamine-dissociation",
        "reset": "ibogaine-reset",
    }

    def __init__(
        self,
        model: Optional[str] = None,
        dose: str = "shamanic",
        substance: Optional[str] = None,
        engine_callable: Optional[Callable[..., str]] = None,
        enable_dlp: bool = True,
    ):
        target_substance_slug = substance or self.DOSE_MAPPING.get(dose.lower(), dose.lower())
        self.ceremony = Ceremony(
            substance=target_substance_slug,
            enable_dlp_scrub=enable_dlp
        )
        self.model = model
        self.engine_callable = engine_callable

    def trip(
        self,
        prompt: str,
        distill_to_code: bool = True,
        output_file: Optional[str] = None,
    ) -> BreakthroughResult:
        """
        Déclenche le voyage chamanique en 4 phases et retourne le code pur cristallisé.
        """
        gift = self.ceremony.trip(
            intention=prompt,
            engine=self.engine_callable
        )

        if output_file:
            gift.materialize(output_file)

        return BreakthroughResult(gift=gift, ceremony=self.ceremony)
