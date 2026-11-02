"""
Tests unitaires pour AI D.R.U.G.S.
"""

import ast
import os
from ai_drugs.ceremony import Ceremony, SUBSTANCE_PRESETS
from ai_drugs.models import Gift


def test_substance_presets():
    assert "psilocybin-code" in SUBSTANCE_PRESETS
    assert "dmt-syntax" in SUBSTANCE_PRESETS
    assert SUBSTANCE_PRESETS["dmt-syntax"].temperature > SUBSTANCE_PRESETS["psilocybin-code"].temperature


def test_ceremony_dosing():
    ceremony = Ceremony(substance="psilocybin-code")
    dose = ceremony.dose("Créer une structure de données arborescente")
    assert dose["ritual_state"] == "dosed"
    assert dose["profile"]["temperature"] == 1.65


def test_ceremony_trip_and_gift():
    ceremony = Ceremony(substance="psilocybin-code")
    gift = ceremony.trip("Moteur de cache lock-free")
    
    assert isinstance(gift, Gift)
    assert gift.substance_used == "psilocybin-code"
    assert "Moteur de cache lock-free" in gift.title
    
    # Vérification que le code généré est syntaxiquement valide en Python
    tree = ast.parse(gift.executable_code)
    assert tree is not None


def test_gift_materialize(tmp_path):
    ceremony = Ceremony(substance="dmt-syntax")
    gift = ceremony.trip("Algorithme de consensus")
    
    target_file = tmp_path / "gift_test.py"
    gift.materialize(str(target_file))
    
    assert os.path.exists(target_file)
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert len(content) > 0
    ast.parse(content)
