"""
Suite de tests complète et exhaustive pour AI D.R.U.G.S.
Doctrine Zéro Simulation — Paul Shemisi.
"""

import ast
import os
import pytest
from ai_drugs.core.physics import LatentThermodynamics
from ai_drugs.core.substances import PharmacopoeiaRegistry, Substance
from ai_drugs.core.trance_engine import TranceEngine
from ai_drugs.core.comedown_annealer import ComedownAnnealer
from ai_drugs.core.gift_oracle import GiftOracle
from ai_drugs.commercial.enterprise_gate import EnterpriseGateway
from ai_drugs.commercial.dispensary import EnterpriseDispensary
from ai_drugs.lab.scientific_bench import ScientificBench
from ai_drugs.ceremony import Ceremony


# 1. Tests de la Physique de l'Espace Latent
def test_physics_thermodynamics():
    state_sub = LatentThermodynamics.compute_state(temperature=0.8)
    assert not state_sub.is_supercritical
    assert state_sub.fisher_rao_norm > 0.0

    state_super = LatentThermodynamics.compute_state(temperature=1.85)
    assert state_super.is_supercritical
    assert state_super.free_energy < state_sub.free_energy

    schedule = LatentThermodynamics.symplectic_annealing_schedule(initial_temperature=1.8, target_temperature=0.05, steps=5)
    assert len(schedule) == 5
    assert schedule[0] == 1.8
    assert schedule[-1] == 0.05
    assert schedule[1] < schedule[0]


def test_kolmogorov_proxy():
    simple_text = "AAAA" * 50
    complex_text = "The quick brown fox jumps over the lazy dog 1234567890 !@#$%^&*()" * 5
    d_simple = LatentThermodynamics.calculate_kolmogorov_complexity_proxy(simple_text)
    d_complex = LatentThermodynamics.calculate_kolmogorov_complexity_proxy(complex_text)
    assert d_complex > d_simple


# 2. Tests de la Pharmacopée Computationnelle
def test_substances_pharmacopoeia():
    subs = PharmacopoeiaRegistry.list_all()
    assert len(subs) >= 6
    dmt = PharmacopoeiaRegistry.get("dmt-syntax")
    assert dmt.temperature >= 1.9
    assert "hyper-monad" in dmt.archetypes

    aya = PharmacopoeiaRegistry.get("ayahuasca-kernel")
    assert "bare-metal" in aya.archetypes


# 3. Tests du Moteur de Transe
def test_trance_engine_local_vision():
    engine = TranceEngine(PharmacopoeiaRegistry.get("ayahuasca-kernel"))
    vision = engine.induce_trip("Buffer annulaire rapide")
    assert vision.thermodynamics.is_supercritical
    assert len(vision.archetypes) > 0
    assert "FastRingBuffer" in vision.raw_stream


# 4. Tests de l'Annealer et Assainissement AST
def test_comedown_annealer_purification():
    engine = TranceEngine(PharmacopoeiaRegistry.get("psilocybin-code"))
    vision = engine.induce_trip("Réseau mycélien")
    annealer = ComedownAnnealer(target_temperature=0.01)
    clean_code, audit = annealer.anneal(vision)

    assert audit.ast_valid is True
    assert audit.purity_score >= 0.8
    assert len(audit.classes_found) > 0
    # Vérification formelle AST
    tree = ast.parse(clean_code)
    assert tree is not None


# 5. Tests du Gift Oracle & In-RAM Benchmarking
def test_gift_oracle_and_benchmark():
    ceremony = Ceremony(substance="psilocybin-code")
    gift = ceremony.trip("Nœud mycélien distribué")

    assert gift.executable_code != ""
    assert gift.test_suite_code != ""
    assert gift.audit.ast_valid is True

    # Exécution du benchmark en RAM
    bench = gift.benchmark()
    assert bench.verified is True
    assert bench.execution_latency_us >= 0.0


# 6. Tests du Volet Commercial : Bouclier DLP In-RAM
def test_enterprise_dlp_scrub():
    sensitive_prompt = "Déployer avec sk-live99887766554433221100 sur 192.168.1.100 dans /Users/paulshemisi/vault"
    sanitized, report = EnterpriseGateway.in_ram_dlp_scrub(sensitive_prompt)

    assert "sk-live" not in sanitized
    assert "192.168.1.100" not in sanitized
    assert "/Users/paulshemisi" not in sanitized
    assert report.secrets_sanitized_count >= 2
    assert report.variables_anonymized_count >= 1
    assert report.is_safe_for_external_llm is True


# 7. Tests du Volet Commercial : Arbitrage de Tokens
def test_token_arbitrage():
    arb = EnterpriseGateway.calculate_token_arbitrage(code_lines=150, iterations_avoided=10)
    assert arb.tokens_saved > 0
    assert arb.local_execution_ratio > 70.0
    assert arb.cost_saved_usd > 0.0


# 8. Tests du Dispensaire d'Entreprise
def test_enterprise_dispensary(tmp_path):
    dispensary = EnterpriseDispensary()
    custom_sub = dispensary.craft_substance(
        name="Crypto Zero Knowledge Trance",
        slug="crypto-zk-trance",
        domain="Systèmes de preuves à divulgation nulle de connaissance",
        temperature=1.85,
        top_p=0.98,
        entropy_burst=0.92,
        induction_prompt="Pense en courbes elliptiques BN254...",
        anchor_prompt="Condense en circuits arithmétiques déterministes."
    )
    assert custom_sub.slug == "crypto-zk-trance"
    assert PharmacopoeiaRegistry.get("crypto-zk-trance").slug == "crypto-zk-trance"

    # Export / Import de recette
    recipe_file = tmp_path / "zk_recipe.json"
    dispensary.export_recipe("crypto-zk-trance", str(recipe_file))
    assert os.path.exists(recipe_file)


# 9. Tests du Banc de Métrologie Scientifique
def test_scientific_bench_diagnostics():
    ceremony = Ceremony(substance="dmt-syntax")
    gift = ceremony.trip("Hyper monade géométrique")
    report = ceremony.metrology_report

    assert report is not None
    assert report.recurrence_rate < 0.40  # Exploration saine sans boucle infinie
    assert report.regime in ("CRÉATIF_SUPERCRITIQUE_OPTIMAL", "CHAOS_STABLE")


# 10. Test de Matérialisation de Suite Complète (Code + Pytest)
def test_gift_materialize_suite(tmp_path):
    ceremony = Ceremony(substance="ayahuasca-kernel")
    gift = ceremony.trip("Anneau mémoire atomique")
    suite = gift.materialize_suite(str(tmp_path), prefix="atomic_ring")

    assert os.path.exists(suite["artifact"])
    assert os.path.exists(suite["test_suite"])
    with open(suite["artifact"], "r", encoding="utf-8") as f:
        code = f.read()
    assert len(code) > 0
    ast.parse(code)
