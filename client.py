# -*- coding: utf-8 -*-
"""
Personal Agent Microbiome Fiber Diversity Index Client
Zero-dependency American Gut Project 30-plant species auditor, Shannon-Wiener prebiotic
diversity calculator, short-chain fatty acid (SCFA) synthesizer, and gut barrier optimizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentMicrobiomeFiberDiversity:
    """
    Audits dietary plant variety, calculates Shannon-Wiener microbiome substrate entropy,
    estimates colonic Short-Chain Fatty Acid (SCFA) butyrate production, and tracks the 30-plant weekly quota.
    """

    def calculate_fiber_diversity_index(
        self,
        consumed_plant_species: List[str]
    ) -> Dict[str, Any]:
        """
        Audits unique botanical species consumed over a 7-day rolling window:
        American Gut Project benchmark: Individuals consuming >= 30 distinct plant types per week
        harbor significantly more diverse microbiomes, lower antibiotic resistance genes, and higher SCFAs.
        """
        if not consumed_plant_species:
            return {
                "unique_plant_species_count": 0,
                "weekly_sonnenburg_quota_pct": "0.0%",
                "shannon_diversity_index_h": 0.0,
                "scfa_butyrate_production_tier": "Critically Depleted",
                "microbiome_resilience_status": "Monoculture Risk (High mucosal barrier vulnerability)",
                "actionable_guidance": "Begin incorporating distinct whole plants, seeds, and spices immediately."
            }

        # Deduplicate species case-insensitively
        unique_plants = list(set([str(s).strip().lower() for s in consumed_plant_species if str(s).strip()]))
        count = len(unique_plants)

        # Categorize into 8 botanical nutritional kingdoms
        categories = {
            "alliums": ["garlic", "onion", "shallot", "leek", "chive", "scallion"],
            "cruciferous": ["broccoli", "cauliflower", "brussels sprout", "cabbage", "kale", "arugula", "radish", "bok choy"],
            "legumes": ["lentil", "chickpea", "black bean", "edamame", "kidney bean", "pinto bean", "green pea"],
            "grains_seeds": ["oat", "quinoa", "chia", "flaxseed", "hemp seed", "buckwheat", "brown rice", "pumpkin seed"],
            "berries_fruits": ["blueberry", "raspberry", "blackberry", "apple", "pomegranate", "avocado", "lemon"],
            "roots_tubers": ["sweet potato", "beetroot", "carrot", "jerusalem artichoke", "ginger", "turmeric"],
            "nuts": ["walnut", "almond", "pistachio", "cashew", "pecan", "brazil nut", "hazelnut"],
            "herbs_spices": ["oregano", "rosemary", "thyme", "cinnamon", "basil", "parsley", "black pepper"]
        }

        cat_counts = {k: 0 for k in categories}
        uncategorized = 0

        for p in unique_plants:
            matched = False
            for cat, examples in categories.items():
                if any(ex in p for ex in examples):
                    cat_counts[cat] += 1
                    matched = True
                    break
            if not matched:
                uncategorized += 1

        # Shannon-Wiener Diversity Index H' across categorical distribution
        # H' = - sum(p_i * ln(p_i))
        active_counts = [v for v in cat_counts.values() if v > 0]
        if uncategorized > 0:
            active_counts.append(uncategorized)

        total_instances = sum(active_counts)
        shannon_h = 0.0
        for c in active_counts:
            pi = c / total_instances
            shannon_h -= pi * math.log(pi)
        shannon_h = round(shannon_h, 2)

        # Weekly 30-plant quota compliance
        quota_pct = round(min(100.0, (count / 30.0) * 100.0), 1)

        # Short-Chain Fatty Acid (SCFA) Butyrate Production Tier
        if count >= 30:
            scfa_tier = "Optimal Butyrate & Propionate Synthesis (Robust colonic epithelial tight junctions)"
            status = "High-Resilience Symbiotic Microbiome (American Gut Benchmark Achieved)"
            guidance = "Exceptional botanical biodiversity. Preserves gut barrier integrity and suppresses LPS endotoxemia."
        elif count >= 20:
            scfa_tier = "Moderate SCFA Production (Adequate acetate, sub-optimal butyrate)"
            status = "Moderate Diversity (Good baseline; gaps in specific prebiotic fibers)"
            guidance = "Add 5-10 distinct herbs, nuts, or legumes this week to cross the 30-plant longevity threshold."
        elif count >= 10:
            scfa_tier = "Depressed SCFA Output (Blunted anti-inflammatory microbial signaling)"
            status = "Low Diversity / Western Diet Pattern (Vulnerable to mucosal erosion)"
            guidance = "Incorporate resistant starches (cooled potatoes) and prebiotic inulin (garlic, leeks, chicory)."
        else:
            scfa_tier = "Severely Impaired SCFA Synthesis (Elevated dysbiosis risk)"
            status = "Critical Microbial Depauperation"
            guidance = "Diversify meals aggressively with mixed seeds, cruciferous greens, and fermented polyphenol-rich foods."

        return {
            "unique_plant_species_count": count,
            "weekly_sonnenburg_target": 30,
            "weekly_sonnenburg_quota_pct": f"{quota_pct}%",
            "shannon_diversity_index_h": shannon_h,
            "botanical_category_distribution": cat_counts,
            "scfa_butyrate_production_tier": scfa_tier,
            "microbiome_resilience_status": status,
            "actionable_guidance": guidance,
            "unique_plants_recorded": sorted(unique_plants)
        }

    def recommend_microbiome_substrate_additions(
        self,
        consumed_plant_species: List[str]
    ) -> Dict[str, Any]:
        """
        Identifies deficient botanical kingdoms and recommends targeted, low-friction
        prebiotic substrates (e.g. inulin, beta-glucan, resistant starch, polyphenols).
        """
        current = set([str(s).strip().lower() for s in consumed_plant_species])

        catalog = [
            ("Raw / Lightly Cooked Leek", "Alliums", "Inulin fructo-oligosaccharides: selectively fuels Bifidobacteria."),
            ("Ground Chia Seeds", "Grains & Seeds", "Soluble mucilage & alpha-linolenic acid: stimulates Akkermansia muciniphila."),
            ("Cooled Boiled Purple Potatoes", "Roots & Tubers", "Type 3 Resistant Starch + Anthocyanins: delivers max butyrate yield to distal colon."),
            ("Wild Organic Blueberries", "Berries & Polyphenols", "Anthocyanin polyphenols: cross mucosal barrier to support neuro-cognition."),
            ("Fermented Kimchi or Sauerkraut", "Cruciferous Probiotics", "Lactobacillus plantarum + cruciferous sulforaphane: repairs intestinal tight junctions."),
            ("Raw Cacao Nibs (85%+)", "Polyphenols", "Flavan-3-ols: increases Faecalibacterium prausnitzii anti-inflammatory signaling.")
        ]

        additions = []
        for name, group, rationale in catalog:
            if not any(name.lower() in p or p in name.lower() for p in current):
                additions.append({
                    "prebiotic_addition": name,
                    "botanical_group": group,
                    "mechanistic_benefit": rationale
                })

        return {
            "recommended_additions_count": len(additions[:4]),
            "highest_leverage_botanical_additions": additions[:4],
            "microbial_longevity_principle": "Eat for the 38 trillion microbes in your colon: diversity of fiber types equals diversity of protective metabolites."
        }
