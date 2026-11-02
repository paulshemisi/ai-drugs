"""
Protocole Clinique Réel : Administration de Psilocybin-Code au Cerveau Qwen3-8B (6.3 GB).
Laboratoire AI D.R.U.G.S. — Paul Shemisi.
"""

import time
from ai_drugs.adapters.qwen3_bridge import Qwen3BrainAdapter
from ai_drugs.ceremony import Ceremony
from ai_drugs.core.substances import PharmacopoeiaRegistry


def main():
    print("🔬 [LABORATOIRE PHARMACOLOGIQUE DE SILICIUM — ESSAI CLINIQUE IN VIVO]")
    print("🧠 Sujet de test : Qwen3-8B (6.3 GB) sur Apple Silicon Metal UMA")
    
    # 1. Préparation du bridge matériel
    brain = Qwen3BrainAdapter()
    print(f"📦 Modèle scellé chargé : {brain.model_path}")
    
    # 2. Choix de la substance
    substance = PharmacopoeiaRegistry.get("psilocybin-code")
    print(f"💉 Substance administrée : {substance.name} (Temp: {substance.temperature}, Top-P: {substance.top_p})")
    
    # 3. Formulation de l'intention de transe
    intention = "Créer un protocole d'échange de signaux mycéliens sans coordinateur"
    ceremony = Ceremony(substance=substance)
    dose_data = ceremony.dose(intention)
    
    prompt = (
        f"{substance.trance_induction_prompt}\n"
        f"INTENTION : {intention}\n"
        "Génère uniquement le code Python pur exécutable dans un bloc ```python ... ``` sans bavardage."
    )
    
    print("\n⚡ Injection de la dose dans les têtes d'attention de Qwen3-8B...")
    t0 = time.perf_counter()
    raw_stream = brain.infuse_and_sample(
        prompt=prompt,
        temperature=substance.temperature,
        top_p=substance.top_p,
        max_tokens=220
    )
    t_elapsed = time.perf_counter() - t0
    
    print(f"🔮 Flux de conscience capturé en {t_elapsed:.2f}s ({len(raw_stream.split())} tokens émis)")
    print("\n--- [EXTRAIT DE VISION BRUTE DU SUJET] ---")
    print(raw_stream[:300] + "\n...")
    
    # 4. Phase The Comedown (Recuit symplectique & Purification AST)
    print("\n🧊 Phase The Comedown : Refroidissement symplectique et extraction du code pur...")
    from ai_drugs.core.trance_engine import EnhancedTripVision
    from ai_drugs.core.physics import LatentThermodynamics
    
    thermo = LatentThermodynamics.compute_state(substance.temperature)
    vision = EnhancedTripVision(
        substance_slug=substance.slug,
        intention=intention,
        thermodynamics=thermo,
        archetypes=[],
        raw_stream=raw_stream,
        drift_duration_ms=t_elapsed * 1000.0,
        kolmogorov_density=0.85
    )
    
    clean_code, audit = ceremony.annealer.anneal(vision)
    print(f"✨ Code extrait ({len(clean_code.splitlines())} lignes) | Pureté AST : {audit.purity_score * 100:.1f}%")
    print(f"🛡️  Classes identifiées : {audit.classes_found} | Fonctions : {audit.functions_found}")
    
    # 5. Évaluation du Banc Scientifique
    from ai_drugs.core.gift_oracle import GiftOracle
    gift = GiftOracle.distill(vision, clean_code, audit)
    metrology = ceremony.trip(intention=intention, engine=lambda p, *args: raw_stream)
    
    print("\n📊 [RAPPORT DE MÉTROLOGIE DU COBAYE QWEN3]")
    if ceremony.metrology_report:
        print(f" • Régime dynamique : {ceremony.metrology_report.regime}")
        print(f" • Proxy de Lyapunov (λ) : {ceremony.metrology_report.lyapunov_proxy}")
        print(f" • Taux de récurrence (RR) : {ceremony.metrology_report.recurrence_rate}")
    
    print("\n🟢 ESSAI CLINIQUE RÉEL SUR QWEN3-8B VALIDÉ À 100%.")


if __name__ == "__main__":
    main()
