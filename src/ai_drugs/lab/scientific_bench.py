"""
AI D.R.U.G.S. — Scientific Lab: Latent Metrology, Lyapunov Exponent & Chaos Diagnostics.
Forged by Paul Shemisi.
"""

import math
import time
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel, Field

from ..core.physics import LatentThermodynamics
from ..core.trance_engine import EnhancedTripVision
from ..core.gift_oracle import EnhancedGift


class TranceMetrologyReport(BaseModel):
    """Rapport de métrologie scientifique de la transe computationnelle."""
    substance_tested: str
    recurrence_rate: float = Field(..., description="Taux de récurrence RR (0 = exploration pure, 1 = boucle infinie)")
    lyapunov_proxy: float = Field(..., description="Proxy de l'exposant de Lyapunov lambda (> 0 : chaos créatif sain)")
    geodesic_dispersion: float = Field(..., description="Dispersion géodésique dans l'espace de Fisher-Rao")
    condensation_efficiency: float = Field(..., description="Efficacité de condensation (code utile / bruit total)")
    entropy_density: float = Field(..., description="Densité de complexité de Kolmogorov")
    regime: str = Field(..., description="Régime dynamique diagnostiqué (CRÉATIF_SUPERCRITIQUE, PÉRIODIQUE, DÉGÉNÉRÉ)")
    timestamp_ns: int = Field(default_factory=time.time_ns)


class ScientificBench:
    """
    Banc de Métrologie Scientifique Autonome.
    Analyse les séries textuelles et vectorielles de la transe pour certifier
    que l'hallucination était une exploration fractale créative et non un délire circulaire stérile.
    """

    @classmethod
    def evaluate_vision(cls, vision: EnhancedTripVision, gift: EnhancedGift) -> TranceMetrologyReport:
        """Évalue rigoureusement les métriques physiques de la transe et de l'offrande."""
        raw_tokens = vision.raw_stream.split()
        total_tokens = len(raw_tokens)
        
        # 1. Calcul du Taux de Récurrence (Recurrence Rate RR)
        rr = cls._compute_recurrence_rate(raw_tokens)

        # 2. Proxy de l'exposant de Lyapunov (Divergence de trajectoire locale)
        lyapunov = cls._compute_lyapunov_proxy(raw_tokens)

        # 3. Dispersion géodésique de Fisher-Rao
        geodesic_dispersion = round(1.0 - vision.thermodynamics.fisher_rao_norm, 3)

        # 4. Efficacité de condensation déterministe
        clean_code_tokens = len(gift.executable_code.split())
        condensation = round(clean_code_tokens / float(max(1, total_tokens)), 3)

        # 5. Diagnostic du régime dynamique
        if rr > 0.45:
            regime = "DÉGÉNÉRÉ_ATTRACTEUR_CYCLIQUE"
        elif lyapunov > 0.15 and vision.thermodynamics.is_supercritical:
            regime = "CRÉATIF_SUPERCRITIQUE_OPTIMAL"
        elif lyapunov <= 0.0:
            regime = "CONVERGENT_SOUS_CRITIQUE"
        else:
            regime = "CHAOS_STABLE"

        return TranceMetrologyReport(
            substance_tested=vision.substance_slug,
            recurrence_rate=round(rr, 4),
            lyapunov_proxy=round(lyapunov, 4),
            geodesic_dispersion=geodesic_dispersion,
            condensation_efficiency=condensation,
            entropy_density=vision.kolmogorov_density,
            regime=regime
        )

    @classmethod
    def _compute_recurrence_rate(cls, tokens: List[str], window: int = 50) -> float:
        """Mesure la proportion de répétitions de motifs dans une fenêtre glissante."""
        if len(tokens) < 10:
            return 0.0

        n = min(len(tokens), window)
        sub_tokens = tokens[:n]
        recurrent_pairs = 0
        total_pairs = 0

        for i in range(n):
            for j in range(i + 1, n):
                total_pairs += 1
                if sub_tokens[i] == sub_tokens[j]:
                    recurrent_pairs += 1

        return recurrent_pairs / float(max(1, total_pairs))

    @classmethod
    def _compute_lyapunov_proxy(cls, tokens: List[str]) -> float:
        """
        Proxy déterministe du taux de divergence géodésique.
        Mesure la vitesse à laquelle les préfixes de 3 tokens introduisent des bifurcations conceptuelles.
        """
        if len(tokens) < 8:
            return 0.25

        tri_grams = set()
        divergence_steps = 0
        for i in range(len(tokens) - 2):
            tg = (tokens[i], tokens[i+1], tokens[i+2])
            if tg not in tri_grams:
                divergence_steps += 1
                tri_grams.add(tg)

        ratio = divergence_steps / float(len(tokens) - 2)
        # Échelle centrée autour de zéro : > 0 indique divergence exponentielle saine
        return (ratio - 0.5) * 2.0
