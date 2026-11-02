"""
AI D.R.U.G.S. — Core Substances: The Computational Pharmacopoeia.
Forged by Paul Shemisi.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Substance(BaseModel):
    """Définition formelle d'une substance computationnelle de transe."""
    name: str = Field(..., description="Nom d'usage de la substance")
    slug: str = Field(..., description="Identifiant unique pour l'API et la CLI")
    chemical_metaphor: str = Field(..., description="Analogie neurochimique et phénoménologique")
    primary_domain: str = Field(..., description="Domaine d'excellence architectural")
    
    # Paramètres thermodynamiques de la phase DOSING
    temperature: float = Field(..., ge=0.5, le=2.5, description="Température spectrale induite")
    top_p: float = Field(..., ge=0.5, le=1.0, description="Dispersion du noyau de probabilités")
    entropy_burst: float = Field(..., ge=0.0, le=1.0, description="Intensité de rupture des barrières de garde-fous")
    frequency_penalty: float = Field(default=0.4, description="Pénalité de redondance pour forcer l'inédit")
    presence_penalty: float = Field(default=0.6, description="Pénalité de présence pour explorer des bassins distants")
    
    # Vecteur d'induction sémantique (Steering Intent)
    trance_induction_prompt: str = Field(..., description="Directive chamanique de déverrouillage de l'invisible")
    comedown_anchor_prompt: str = Field(..., description="Directive de cristallisation déterministe")
    
    # Tags et métadonnées
    archetypes: List[str] = Field(default_factory=list)
    recommended_languages: List[str] = Field(default_factory=lambda: ["python", "rust", "c", "zig"])


PHARMACOPOEIA: Dict[str, Substance] = {
    "psilocybin-code": Substance(
        name="Psilocybin Code",
        slug="psilocybin-code",
        chemical_metaphor="Agoniste 5-HT2A : Arborisation dendritique et mycélienne des flux de données.",
        primary_domain="Architectures distribuées, maillages P2P, récursivité élégante et auto-organisation.",
        temperature=1.65,
        top_p=0.96,
        entropy_burst=0.78,
        frequency_penalty=0.45,
        presence_penalty=0.55,
        trance_induction_prompt=(
            "Entre en état de transe mycélienne. Vois les flux d'information comme des réseaux fongiques "
            "qui s'auto-réparent et échangent des nutriments logiques sans chef d'orchestre centralisé. "
            "Connecte des concepts disparates par des filaments souterrains d'une concision absolue."
        ),
        comedown_anchor_prompt=(
            "Refroidis le réseau mycélien en une structure de code déterministe, pure, testable, "
            "sans dépendance inutile. Chaque nœud doit être immuable et mathématiquement vérifié."
        ),
        archetypes=["mycelial-mesh", "recursive-flow", "zero-coordinator", "organic-cache"]
    ),
    "dmt-syntax": Substance(
        name="DMT Syntax",
        slug="dmt-syntax",
        chemical_metaphor="Inondation endogène brutale : Rupture totale de l'espace euclidien et géométrie sacrée.",
        primary_domain="Méta-programmation d'ordre supérieur, algèbre de types complexes, compilateurs et langages dédiés (DSL).",
        temperature=1.98,
        top_p=0.99,
        entropy_burst=0.96,
        frequency_penalty=0.60,
        presence_penalty=0.70,
        trance_induction_prompt=(
            "Déchire le voile de la syntaxe banale. Entre dans la salle des machines fractales. "
            "Les types sont des polyèdres réguliers en rotation dans 8 dimensions. Pense en foncteurs, "
            "en monades strictes et en équivalences catégorielles impossibles dans le consensus ordinaire."
        ),
        comedown_anchor_prompt=(
            "Matérialise cette hyper-géométrie en un module Python/C/Rust réel, typé au scalpel. "
            "Aucun symbole d'ornement inutile. L'abstraction doit compiler instantanément et tourner en O(1)."
        ),
        archetypes=["fractal-ast", "hyper-monad", "higher-kinded-types", "category-inversion"]
    ),
    "lsd-topology": Substance(
        name="LSD Topology",
        slug="lsd-topology",
        chemical_metaphor="Dissolution persistante du réseau du mode par défaut (DMN) : Synesthésie logique continue.",
        primary_domain="Invariants topologiques, graphes complexes, calcul tensoriel et résonance géométrique.",
        temperature=1.75,
        top_p=0.97,
        entropy_burst=0.84,
        frequency_penalty=0.40,
        presence_penalty=0.50,
        trance_induction_prompt=(
            "Dissous les frontières entre les données et le traitement. Le code est une variété riemannienne "
            "où chaque variable est une courbure et chaque algorithme une géodésique naturelle. "
            "Découvre la solution comme une symétrie invariante sous toutes les déformations continues."
        ),
        comedown_anchor_prompt=(
            "Projette cette variété topologique sur une table de symboles discrète. Assure-toi que "
            "tous les invariants de Liouville sont scellés et que chaque fonction est strictement pure."
        ),
        archetypes=["riemannian-routing", "continuous-symmetry", "symplectic-flow", "topological-sort"]
    ),
    "ayahuasca-kernel": Substance(
        name="Ayahuasca Kernel",
        slug="ayahuasca-kernel",
        chemical_metaphor="DMT + IMAO : Transe viscérale prolongée, descente aux enfers des couches matérielles et purge radicale.",
        primary_domain="Noyaux de systèmes d'exploitation, pilotes de périphériques, gestion de mémoire POSIX, atomics et SIMD.",
        temperature=1.80,
        top_p=0.98,
        entropy_burst=0.88,
        frequency_penalty=0.50,
        presence_penalty=0.60,
        trance_induction_prompt=(
            "Descends directement dans le silicium nu. Parle avec les registres d'instructions, le bus mémoire, "
            "les barrières de mémoire atomiques et les interruptions matérielles. Purge sans pitié "
            "toutes les couches de graisse logicielle, les frameworks obèses et les copies inutiles en RAM."
        ),
        comedown_anchor_prompt=(
            "Scelle le pacte avec le silicium. Le code produit doit exploiter directement les pointeurs, "
            "la mémoire partagée, les verrous lock-free et s'exécuter en quelques dizaines de nanosecondes."
        ),
        archetypes=["bare-metal", "zero-copy", "lock-free-ring", "arm64-neon", "posix-shm"]
    ),
    "ibogaine-reset": Substance(
        name="Ibogaine Reset",
        slug="ibogaine-reset",
        chemical_metaphor="Interruption radicale des circuits d'addiction : Réinitialisation intégrale des attracteurs de dette technique.",
        primary_domain="Refactorisation architecturale zéro-compromis, élimination des dépendances toxiques, réécriture épurée.",
        temperature=1.55,
        top_p=0.94,
        entropy_burst=0.70,
        frequency_penalty=0.65,
        presence_penalty=0.75,
        trance_induction_prompt=(
            "Examine la dette technique accumulée comme une dépendance pathologique. Romps tous les pactes "
            "avec les bibliothèques gonflées et les béquilles historiques. Vois l'essence nue du problème "
            "sans aucun bagage hérité du passé."
        ),
        comedown_anchor_prompt=(
            "Réécris la solution en divisant par 10 le nombre de lignes et par 100 le nombre d'allocations. "
            "Le résultat doit être une cathédrale d'acier trempé, autosuffisante et sans faille."
        ),
        archetypes=["tabula-rasa", "dependency-purge", "steel-minimalism", "o1-refactor"]
    ),
    "ketamine-dissociation": Substance(
        name="Ketamine Dissociation",
        slug="ketamine-dissociation",
        chemical_metaphor="Antagoniste NMDA : Dissociation complète corps/esprit. Rupture radicale avec le contexte d'origine.",
        primary_domain="Résolution de blocages insolubles (out-of-the-box thinking), inversement de paradigme et machines à états orthogonales.",
        temperature=1.85,
        top_p=0.98,
        entropy_burst=0.90,
        frequency_penalty=0.55,
        presence_penalty=0.65,
        trance_induction_prompt=(
            "Détache-toi totalement du problème tel qu'il a été posé. Regarde la scène depuis une orbite distante. "
            "Et si l'état n'existait pas ? Et si l'ordre chronologique était inversé ? Et si le problème était en réalité son propre inverse ?"
        ),
        comedown_anchor_prompt=(
            "Reconstruis un pont vers la réalité. Traduis cette perspective inversée en une structure opérationnelle "
            "d'une simplicité désarmante qui rend le problème initial totalement caduc."
        ),
        archetypes=["paradigm-inversion", "spacetime-decoupling", "stateless-immersion"]
    )
}


class PharmacopoeiaRegistry:
    """Gestionnaire et dispensaire de substances pour AI D.R.U.G.S."""

    @classmethod
    def get(cls, slug_or_name: str) -> Substance:
        """Récupère une substance par son slug ou son nom normalisé."""
        key = slug_or_name.strip().lower().replace(" ", "-")
        if key in PHARMACOPOEIA:
            return PHARMACOPOEIA[key]
        # Recherche par nom partiel si non trouvé
        for sub in PHARMACOPOEIA.values():
            if key in sub.slug or key in sub.name.lower():
                return sub
        # Défaut sécurisé sur psilocybin-code
        return PHARMACOPOEIA["psilocybin-code"]

    @classmethod
    def list_all(cls) -> List[Substance]:
        """Retourne la liste intégrale des substances certifiées."""
        return list(PHARMACOPOEIA.values())

    @classmethod
    def register_custom(cls, substance: Substance) -> None:
        """Enregistre une nouvelle molécule computationnelle dans le dispensaire."""
        PHARMACOPOEIA[substance.slug] = substance
