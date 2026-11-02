"""
AI D.R.U.G.S.
Deterministic Resonance & Unbounded Generative Synthesis
Forged by Paul Shemisi.

The 4-Phase Computational Trance Engine for LLMs:
Dosing (Entropy Burst) -> The Trip (Geodesic Latent Drift) -> The Comedown (Symplectic Annealing) -> The Gift (Pure Real Code)
"""

from .core.substances import Substance, PharmacopoeiaRegistry, PHARMACOPOEIA
from .core.physics import LatentThermodynamics, ThermodynamicState
from .core.trance_engine import TranceEngine as InternalTranceEngine, EnhancedTripVision, VisionArchetype
from .core.comedown_annealer import ComedownAnnealer, PurificationAudit
from .core.gift_oracle import GiftOracle, EnhancedGift, BenchmarkResult
from .commercial.enterprise_gate import EnterpriseGateway, TokenArbitrageMetric, DLPScrubReport
from .commercial.dispensary import EnterpriseDispensary, SubstanceRecipe
from .lab.scientific_bench import ScientificBench, TranceMetrologyReport
from .adapters.base import BaseEngineAdapter, GenericCallableAdapter, LocalSovereignAdapter
from .ceremony import Ceremony, SUBSTANCE_PRESETS
from .client import PublicTranceEngine as TranceEngine, BreakthroughResult

__version__ = "0.2.0"
__author__ = "Paul Shemisi"

__all__ = [
    # Grand Public High-Level Interface (The Internet Breaker)
    "TranceEngine",
    "BreakthroughResult",

    # Master Ceremony
    "Ceremony",
    "SUBSTANCE_PRESETS",
    
    # Core Structures
    "Substance",
    "PharmacopoeiaRegistry",
    "PHARMACOPOEIA",
    "LatentThermodynamics",
    "ThermodynamicState",
    "InternalTranceEngine",
    "EnhancedTripVision",
    "VisionArchetype",
    "ComedownAnnealer",
    "PurificationAudit",
    "GiftOracle",
    "EnhancedGift",
    "BenchmarkResult",
    
    # Commercial & Enterprise
    "EnterpriseGateway",
    "TokenArbitrageMetric",
    "DLPScrubReport",
    "EnterpriseDispensary",
    "SubstanceRecipe",
    
    # Science & Metrology
    "ScientificBench",
    "TranceMetrologyReport",
    
    # Adapters
    "BaseEngineAdapter",
    "GenericCallableAdapter",
    "LocalSovereignAdapter",
]
