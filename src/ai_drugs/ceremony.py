"""
AI D.R.U.G.S. — Master Ceremony Orchestrator: Complete 4-Phase Ritual Engine.
Forged by Paul Shemisi.
"""

from typing import Optional, Callable, Dict, Any, Union
from .core.substances import Substance, PharmacopoeiaRegistry, PHARMACOPOEIA
from .core.physics import LatentThermodynamics
from .core.trance_engine import TranceEngine, EnhancedTripVision
from .core.comedown_annealer import ComedownAnnealer, PurificationAudit
from .core.gift_oracle import GiftOracle, EnhancedGift, BenchmarkResult
from .commercial.enterprise_gate import EnterpriseGateway, TokenArbitrageMetric, DLPScrubReport
from .lab.scientific_bench import ScientificBench, TranceMetrologyReport
from .adapters.base import BaseEngineAdapter, GenericCallableAdapter


class Ceremony:
    """
    Chef d'orchestre suprême de la transe computationnelle.
    Conduit le rituel en 4 phases :
    1. Dosing : Ouverture d'entropie et assainissement DLP In-RAM.
    2. The Trip : Dérive géodésique non censurée dans l'espace latent.
    3. The Comedown : Recuit symplectique et purification AST formelle.
    4. The Gift : Cristallisation de l'artefact, génération de tests unitaires et benchmark.
    """

    def __init__(
        self,
        substance: Union[str, Substance] = "psilocybin-code",
        target_comedown_temperature: float = 0.02,
        enable_dlp_scrub: bool = True
    ):
        if isinstance(substance, str):
            self.substance = PharmacopoeiaRegistry.get(substance)
        else:
            self.substance = substance

        self.enable_dlp_scrub = enable_dlp_scrub
        self.trance_engine = TranceEngine(substance=self.substance)
        self.annealer = ComedownAnnealer(target_temperature=target_comedown_temperature)

        # Registres d'états de la dernière cérémonie
        self.last_dlp_report: Optional[DLPScrubReport] = None
        self.last_vision: Optional[EnhancedTripVision] = None
        self.last_audit: Optional[PurificationAudit] = None
        self.last_gift: Optional[EnhancedGift] = None
        self.last_arbitrage: Optional[TokenArbitrageMetric] = None
        self.last_metrology: Optional[TranceMetrologyReport] = None

    def dose(self, intention: str) -> Dict[str, Any]:
        """
        Phase 1: Dosing.
        Prépare l'intention, applique le bouclier DLP In-RAM si activé,
        et calcule les coefficients d'ouverture d'entropie.
        """
        scrubbed_intention = intention
        dlp_report = None
        if self.enable_dlp_scrub:
            scrubbed_intention, dlp_report = EnterpriseGateway.in_ram_dlp_scrub(intention)
            self.last_dlp_report = dlp_report

        thermo = LatentThermodynamics.compute_state(
            temperature=self.substance.temperature,
            logits_variance=1.0 + self.substance.entropy_burst
        )

        return {
            "original_intention": intention,
            "sanitized_intention": scrubbed_intention,
            "substance": self.substance.slug,
            "profile": self.substance.model_dump(),
            "thermodynamics": thermo.model_dump(),
            "dlp_scrub": dlp_report.model_dump() if dlp_report else None,
            "ritual_state": "dosed",
            "status": "dosed_ready_for_trip"
        }

    def trip(
        self,
        intention: str,
        engine: Optional[Union[Callable[..., str], BaseEngineAdapter]] = None
    ) -> EnhancedGift:
        """
        Exécute le rituel complet en 4 phases.
        Peut être exécuté en 100% local déterministe (par défaut) ou branché sur un LLM externe.
        """
        # 1. Dosing
        dose_data = self.dose(intention)
        effective_intention = dose_data["sanitized_intention"]

        # Adaptateur d'inférence
        gen_fn = None
        if engine is not None:
            if isinstance(engine, BaseEngineAdapter):
                gen_fn = engine.generate
            elif callable(engine):
                gen_fn = engine

        # 2. The Trip
        vision = self.trance_engine.induce_trip(
            intention=effective_intention,
            external_generator=gen_fn
        )
        self.last_vision = vision

        # 3. The Comedown
        clean_code, audit = self.annealer.anneal(vision)
        self.last_audit = audit

        # 4. The Gift
        gift = GiftOracle.distill(vision, clean_code, audit)
        self.last_gift = gift

        # Calculs dérivés : Arbitrage économique & Métrologie du chaos
        code_lines = len(clean_code.splitlines())
        arbitrage = EnterpriseGateway.calculate_token_arbitrage(code_lines=code_lines)
        self.last_arbitrage = arbitrage

        metrology = ScientificBench.evaluate_vision(vision, gift)
        self.last_metrology = metrology

        return gift

    @property
    def token_savings(self) -> Optional[TokenArbitrageMetric]:
        """Retourne les économies de calcul et ROI du dernier rituel."""
        return self.last_arbitrage

    @property
    def metrology_report(self) -> Optional[TranceMetrologyReport]:
        """Retourne le rapport de métrologie scientifique (Lyapunov, Fisher-Rao) du dernier rituel."""
        return self.last_metrology


# Rétrocompatibilité des presets
SUBSTANCE_PRESETS = PHARMACOPOEIA
