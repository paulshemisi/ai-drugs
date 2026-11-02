"""
Exemple 2 : Cérémonie Ayahuasca Kernel — Lock-Free Ring Buffer Silicium.
AI D.R.U.G.S. — Forged by Paul Shemisi.
"""

import ai_drugs


def main():
    print("=== EXEMPLE 2 : CÉRÉMONIE AYAHUASCA KERNEL ===")
    
    # Initialisation avec recuit thermique ultra-strict
    ritual = ai_drugs.Ceremony(
        substance="ayahuasca-kernel",
        target_comedown_temperature=0.01
    )
    
    intention = "Forger un buffer circulaire lock-free en mémoire partagée POSIX UMA"
    print(f"\n⚡ Transe descendante dans le silicium : '{intention}'...")
    gift = ritual.trip(intention=intention)
    
    print(f"\n✨ Offrande cristallisée : {gift.title}")
    print(f"🔮 Essence : {gift.essence}")
    
    # Benchmark d'exécution en microsecondes
    bench = gift.benchmark()
    print(f"⚡ Latence du buffer : {bench.execution_latency_us} µs (Vérifié: {bench.verified})")
    
    # Matérialisation de la suite complète (Code + Tests unitaires)
    suite = gift.materialize_suite("./examples/dist_kernel", prefix="ayahuasca_ring")
    print(f"📦 Artefact : {suite['artifact']}")
    print(f"🧪 Test Pytest : {suite['test_suite']}")


if __name__ == "__main__":
    main()
