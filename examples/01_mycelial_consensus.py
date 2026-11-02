"""
Exemple 1 : Cérémonie Psilocybin Code — Protocole Mycélien Auto-Organisé.
AI D.R.U.G.S. — Forged by Paul Shemisi.
"""

import ai_drugs


def main():
    print("=== EXEMPLE 1 : CÉRÉMONIE PSILOCYBIN CODE ===")
    
    # 1. Initialisation de la cérémonie
    ritual = ai_drugs.Ceremony(substance="psilocybin-code")
    
    # 2. Conduite du rituel
    intention = "Créer un protocole d'échange de signaux mycéliens décentralisé sans chef d'orchestre"
    print(f"\n🍄 Démarrage de la transe pour : '{intention}'...")
    gift = ritual.trip(intention=intention)
    
    # 3. Résultats
    print(f"\n✨ Offrande cristallisée : {gift.title}")
    print(f"🔮 Essence : {gift.essence}")
    print(f"🛡️  Pureté AST : {gift.audit.purity_score * 100:.1f}%")
    
    # 4. Benchmark en RAM
    bench = gift.benchmark()
    print(f"⚡ Latence d'exécution : {bench.execution_latency_us} µs (Vérifié: {bench.verified})")
    
    # 5. Métrologie du chaos
    metrology = ritual.metrology_report
    if metrology:
        print(f"🔬 Régime diagnostiqué : {metrology.regime}")
        print(f"🔬 Proxy de Lyapunov : {metrology.lyapunov_proxy} (>0 = bifurcation créative)")
        print(f"🔬 Taux de récurrence RR : {metrology.recurrence_rate}")

    # 6. Matérialisation
    out_file = gift.materialize("./examples/mycelial_artifact.py")
    print(f"\n📦 Code sauvegardé dans : {out_file}")


if __name__ == "__main__":
    main()
