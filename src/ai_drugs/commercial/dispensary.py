"""
AI D.R.U.G.S. — Commercial Dispensary: Custom Formulation & Enterprise Substance Vault.
Forged by Paul Shemisi.
"""

import json
import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

from ..core.substances import Substance, PharmacopoeiaRegistry, PHARMACOPOEIA


class SubstanceRecipe(BaseModel):
    """Fiche recette d'une substance exportable/importable pour les équipes d'ingénierie."""
    substance: Substance
    author: str = Field(default="Paul Shemisi")
    version: str = Field(default="1.0.0")
    organization: Optional[str] = Field(default="Sovereign AI Labs")
    tags: List[str] = Field(default_factory=list)


class EnterpriseDispensary:
    """
    Le Dispensaire Moléculaire d'Entreprise.
    Permet aux entreprises de concevoir, stocker et distribuer des substances de transe
    adaptées à leurs architectures spécifiques (ex: FinTech HFT, BioTech, Cyber-Offense).
    """

    def __init__(self, vault_path: Optional[str] = None):
        self.vault_path = vault_path or os.path.expanduser("~/.ai_drugs/dispensary_vault.json")

    def craft_substance(
        self,
        name: str,
        slug: str,
        domain: str,
        temperature: float,
        top_p: float,
        entropy_burst: float,
        induction_prompt: str,
        anchor_prompt: str,
        author: str = "Enterprise Architect",
        archetypes: Optional[List[str]] = None
    ) -> Substance:
        """Crée une nouvelle molécule computationnelle et l'enregistre au dispensaire."""
        # Sécurité thermodynamique : bornage strict
        temp = max(0.5, min(2.5, temperature))
        tp = max(0.5, min(1.0, top_p))
        burst = max(0.0, min(1.0, entropy_burst))

        new_substance = Substance(
            name=name,
            slug=slug,
            chemical_metaphor=f"Synthèse sur mesure pour le domaine : {domain}",
            primary_domain=domain,
            temperature=temp,
            top_p=tp,
            entropy_burst=burst,
            trance_induction_prompt=induction_prompt,
            comedown_anchor_prompt=anchor_prompt,
            archetypes=archetypes or ["custom-entropy", "domain-resonance"]
        )

        PharmacopoeiaRegistry.register_custom(new_substance)
        return new_substance

    def export_recipe(self, slug: str, output_file: str) -> str:
        """Exporte la fiche technique d'une substance sous forme de recette partageable."""
        substance = PharmacopoeiaRegistry.get(slug)
        recipe = SubstanceRecipe(
            substance=substance,
            author="Paul Shemisi",
            version="1.0.0",
            tags=substance.archetypes
        )

        os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(recipe.model_dump_json(indent=2))

        return output_file

    def import_recipe(self, recipe_file: str) -> Substance:
        """Importe une recette partagée dans le dispensaire local."""
        with open(recipe_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        recipe = SubstanceRecipe.model_validate(data)
        PharmacopoeiaRegistry.register_custom(recipe.substance)
        return recipe.substance

    def list_available_substances(self) -> List[Dict[str, Any]]:
        """Liste l'ensemble du catalogue du dispensaire avec les paramètres clés."""
        return [
            {
                "name": s.name,
                "slug": s.slug,
                "domain": s.primary_domain,
                "temperature": s.temperature,
                "entropy_burst": s.entropy_burst,
                "archetypes_count": len(s.archetypes)
            }
            for s in PharmacopoeiaRegistry.list_all()
        ]
