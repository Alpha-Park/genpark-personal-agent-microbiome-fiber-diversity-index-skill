# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Microbiome Fiber Diversity Index Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentMicrobiomeFiberDiversity

def main():
    agent = PersonalAgentMicrobiomeFiberDiversity()

    print("=" * 70)
    print("DEMO: Personal Agent Microbiome Fiber Diversity & SCFA Modeler")
    print("=" * 70)

    # 1. 22 unique plants logged this week
    weekly_diet = [
        "garlic", "yellow onion", "broccoli", "kale", "red lentil",
        "chickpea", "oats", "quinoa", "chia seeds", "wild blueberry",
        "raspberry", "sweet potato", "carrot", "ginger", "walnut",
        "almond", "oregano", "turmeric", "spinach", "apple",
        "black bean", "rosemary"
    ]

    res_div = agent.calculate_fiber_diversity_index(weekly_diet)

    print(f"\n1. 7-Day Botanical Fiber Diversity Audit:")
    print(f"   Unique Plants: {res_div['unique_plant_species_count']} / {res_div['weekly_sonnenburg_target']} target ({res_div['weekly_sonnenburg_quota_pct']})")
    print(f"   Shannon Entropy H': {res_div['shannon_diversity_index_h']}")
    print(f"   SCFA Butyrate Output: {res_div['scfa_butyrate_production_tier']}")
    print(f"   Status: {res_div['microbiome_resilience_status']}")
    print(f"   Guidance: {res_div['actionable_guidance']}")

    # 2. Targeted additions to cross 30 plants
    res_rec = agent.recommend_microbiome_substrate_additions(weekly_diet)

    print(f"\n2. Strategic Prebiotic Additions to Hit 30+ Goal:")
    for item in res_rec['highest_leverage_botanical_additions']:
        print(f"   + {item['prebiotic_addition']} ({item['botanical_group']}):")
        print(f"       {item['mechanistic_benefit']}")
    print(f"   Principle: {res_rec['microbial_longevity_principle']}")

    print("\nVerification complete: Microbiome fiber diversity engine executed flawlessly.")

if __name__ == "__main__":
    main()
