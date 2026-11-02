"""
AI D.R.U.G.S. — Commercial Enterprise Compliance & Zero-Simulation Verification Suite.
Validates the full enterprise readiness:
1. Zero-Mock formal guarantee (AST validation and assertion execution)
2. In-RAM DLP privacy scrub (zero leak of keys, ips, or filepaths)
3. Cryptographic sealing and benchmark reproducibility
4. Token arbitrage and enterprise ROI calculation
"""

import ast
import os
import json
import pytest
from ai_drugs.ceremony import Ceremony
from ai_drugs.commercial.enterprise_gate import EnterpriseGateway
from ai_drugs.core.substances import PharmacopoeiaRegistry


def test_zero_mock_formal_guarantee():
    """Vérifie que chaque substance produit un code 100% exécutable sans aucun stub ni mock."""
    for slug in ["ayahuasca-kernel", "psilocybin-code", "dmt-syntax"]:
        ceremony = Ceremony(substance=slug)
        gift = ceremony.trip(intention=f"Production enterprise pipeline for {slug}")
        
        # 1. Vérification formelle AST
        tree = ast.parse(gift.executable_code)
        assert tree is not None
        assert gift.audit.ast_valid is True
        assert gift.audit.purity_score == 1.0
        assert gift.audit.purged_mocks_count == 0
        
        # 2. Exécution réelle et assertions in-RAM
        bench = gift.benchmark()
        assert bench.verified is True
        assert bench.execution_latency_us > 0.0
        assert bench.execution_latency_us < 500.0  # Moins de 500 microsecondes


def test_in_ram_dlp_zero_leak():
    """Garantit l'étanchéité absolue des secrets avant tout traitement."""
    secret_prompt = (
        "Connecter la base de données avec sk-proj-1234567890abcdef1234567890 "
        "sur l'hôte interne 10.0.1.42 avec clé GitHub ghp_99887766554433221100aabbccdd "
        "dans le volume /Users/paulshemisi/Documents/secret_vault"
    )
    sanitized, report = EnterpriseGateway.in_ram_dlp_scrub(secret_prompt)
    
    assert "sk-proj-" not in sanitized
    assert "10.0.1.42" not in sanitized
    assert "ghp_" not in sanitized
    assert "/Users/paulshemisi" not in sanitized
    assert report.is_safe_for_external_llm is True
    assert report.secrets_sanitized_count >= 3


def test_commercial_audit_receipt(tmp_path):
    """Vérifie la génération d'un livrable enterprise avec suite de tests et quittance."""
    ceremony = Ceremony(substance="psilocybin-code")
    gift = ceremony.trip(intention="Architecture P2P d'échange d'état sans serveur")
    
    dist_dir = tmp_path / "enterprise_delivery"
    paths = gift.materialize_suite(str(dist_dir), prefix="p2p_mesh")
    
    assert os.path.exists(paths["artifact"])
    assert os.path.exists(paths["test_suite"])
    
    # Vérification que le fichier de test s'exécute directement et passe sans erreur
    exec_scope = {}
    with open(paths["artifact"], "r", encoding="utf-8") as f:
        exec(f.read(), exec_scope)
    
    assert "run_verification" in exec_scope
    assert exec_scope["run_verification"]() is True


def test_token_arbitrage_financial_metrics():
    """Vérifie l'exactitude des métriques financières délivrées aux décideurs."""
    arb = EnterpriseGateway.calculate_token_arbitrage(code_lines=200, complexity_factor=1.2, iterations_avoided=12)
    assert arb.tokens_saved > 20000
    assert arb.cost_saved_usd > 0.30
    assert arb.local_execution_ratio >= 85.0
    assert arb.carbon_reduction_grams > 0.5
