"""
AI D.R.U.G.S. — Command Line Interface.
Forged by Paul Shemisi.
"""

import sys
import os
import argparse
from typing import Optional

from ai_drugs.ceremony import Ceremony
from ai_drugs.core.substances import PharmacopoeiaRegistry
from ai_drugs.commercial.dispensary import EnterpriseDispensary
from ai_drugs.commercial.enterprise_gate import EnterpriseGateway
from ai_drugs.core.comedown_annealer import ComedownAnnealer
from ai_drugs.core.trance_engine import EnhancedTripVision
from ai_drugs.core.physics import LatentThermodynamics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-drugs",
        description="AI D.R.U.G.S. 🍄⚡ — Deterministic Resonance & Unbounded Generative Synthesis"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    # Commande 1: TRIP (Cérémonie complète)
    trip_p = subparsers.add_parser("trip", help="Lancer un rituel de transe et cristalliser un artefact")
    trip_p.add_argument("intention", type=str, help="L'intention ou le problème architectural à résoudre")
    trip_p.add_argument("-s", "--substance", type=str, default="psilocybin-code", help="Substance de transe (défaut: psilocybin-code)")
    trip_p.add_argument("-o", "--output", type=str, default="gift.py", help="Fichier de sortie pour l'artefact")
    trip_p.add_argument("--suite", action="store_true", help="Générer également la suite de tests unitaires (dossier ./dist)")
    trip_p.add_argument("--bench", action="store_true", help="Exécuter un benchmark immédiat en microsecondes")
    trip_p.add_argument("--no-dlp", action="store_true", help="Désactiver le filtre DLP In-RAM")

    # Commande 2: DISPENSARY (Pharmacopée et recettes)
    disp_p = subparsers.add_parser("dispensary", help="Explorer le dispensaire de molécules computationnelles")
    disp_sub = disp_p.add_subparsers(dest="disp_action")
    disp_sub.add_parser("list", help="Lister toutes les substances disponibles")
    exp_p = disp_sub.add_parser("export", help="Exporter la recette d'une substance")
    exp_p.add_argument("slug", type=str, help="Slug de la substance")
    exp_p.add_argument("output", type=str, help="Fichier JSON cible")

    # Commande 3: LAB (Audit & Métrologie)
    lab_p = subparsers.add_parser("lab", help="Métrologie du chaos et audit de code")
    lab_p.add_argument("file", type=str, help="Fichier source à auditer")

    # Commande 4: ROI (Arbitrage de calcul et économies de tokens)
    roi_p = subparsers.add_parser("roi", help="Calculateur d'arbitrage de tokens et rentabilité entreprise")
    roi_p.add_argument("--lines", type=int, default=100, help="Nombre estimé de lignes de code produites")
    roi_p.add_argument("--iterations", type=int, default=8, help="Nombre d'itérations cloud évitées")

    return parser


def handle_trip(args):
    print(f"\n🍄 [AI D.R.U.G.S.] Initialisation de la cérémonie : {args.substance}")
    print(f"⚡ Intention soutenue : \"{args.intention}\"")

    ceremony = Ceremony(
        substance=args.substance,
        enable_dlp_scrub=not args.no_dlp
    )

    gift = ceremony.trip(intention=args.intention)

    if args.suite:
        paths = gift.materialize_suite("./dist", prefix=args.substance.replace("-", "_"))
        print(f"✨ Artefact matérialisé : {paths['artifact']}")
        print(f"🧪 Suite Pytest scellée : {paths['test_suite']}")
    else:
        out = gift.materialize(args.output)
        print(f"✨ Artefact cristallisé : {out}")

    print(f"🔮 Essence : {gift.essence}")
    print(f"🛡️  Pureté AST : {gift.audit.purity_score * 100:.1f}% (Stubs éliminés: {gift.audit.purged_mocks_count})")

    if args.bench:
        bench = gift.benchmark()
        status_symbol = "🟢" if bench.verified else "🔴"
        print(f"{status_symbol} Benchmark In-RAM : {bench.execution_latency_us:.2f} µs | Vérifié : {bench.verified}")

    if ceremony.token_savings:
        ts = ceremony.token_savings
        print(f"💰 Arbitrage : {ts.tokens_saved} tokens épargnés ({ts.local_execution_ratio}% en local pur, 0 token)")


def handle_dispensary(args):
    dispensary = EnterpriseDispensary()
    if args.disp_action == "list" or not args.disp_action:
        print("\n🌿 [AI D.R.U.G.S. DISPENSARY] Pharmacopée Computationnelle Certifiée :\n")
        for sub in PharmacopoeiaRegistry.list_all():
            print(f" • {sub.name:<24} [{sub.slug}]")
            print(f"   Temp: {sub.temperature:<4} | Top-P: {sub.top_p:<4} | Entropie: {sub.entropy_burst}")
            print(f"   Domaine: {sub.primary_domain}")
            print(f"   Archétypes: {', '.join(sub.archetypes)}\n")
    elif args.disp_action == "export":
        out = dispensary.export_recipe(args.slug, args.output)
        print(f"📦 Recette exportée avec succès : {out}")


def handle_lab(args):
    if not os.path.exists(args.file):
        print(f"❌ Erreur : Fichier {args.file} introuvable.")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        code = f.read()

    density = LatentThermodynamics.calculate_kolmogorov_complexity_proxy(code)
    lines = len(code.splitlines())

    print(f"\n🔬 [LABORATOIRE DE MÉTROLOGIE] Audit du fichier : {args.file}")
    print(f" • Lignes de code : {lines}")
    print(f" • Densité d'information de Kolmogorov : {density:.3f}")

    # Test de syntaxe
    import ast
    try:
        ast.parse(code)
        print(" • Syntaxe formelle : 🟢 VALIDE (AST conforme)")
    except SyntaxError as e:
        print(f" • Syntaxe formelle : 🔴 ERREUR ({e})")


def handle_roi(args):
    arb = EnterpriseGateway.calculate_token_arbitrage(code_lines=args.lines, iterations_avoided=args.iterations)
    print("\n💼 [CALCULATEUR D'ARBITRAGE DE CALCUL & ROI ENTREPRISE]")
    print(f" • Approche itérative cloud classique : ~{arb.traditional_cloud_tokens_spent} tokens dépensés")
    print(f" • Rituel AI D.R.U.G.S. (1 saut + recuit) : ~{arb.ai_drugs_tokens_spent} tokens")
    print(f" • Tokens épargnés : {arb.tokens_saved} tokens")
    print(f" • Taux d'autonomie local (0 token) : {arb.local_execution_ratio}%")
    print(f" • Économie financière estimée : {arb.cost_saved_usd} $ par artefact")
    print(f" • Émissions carbone évitées : {arb.carbon_reduction_grams:.2f} g CO₂")


def main():
    parser = build_parser()

    # Si aucun sous-argument n'est passé mais qu'une intention est fournie directement (mode raccourci)
    if len(sys.argv) > 1 and sys.argv[1] not in ["trip", "dispensary", "lab", "roi", "-h", "--help"]:
        # Syntaxe directe : ai-drugs "Intention"
        sys.argv.insert(1, "trip")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "trip":
        handle_trip(args)
    elif args.command == "dispensary":
        handle_dispensary(args)
    elif args.command == "lab":
        handle_lab(args)
    elif args.command == "roi":
        handle_roi(args)


if __name__ == "__main__":
    main()
