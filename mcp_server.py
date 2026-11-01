# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Microbiome Fiber Diversity Index Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentMicrobiomeFiberDiversity

mcp = FastMCP("PersonalAgentMicrobiomeFiberDiversity")
client = PersonalAgentMicrobiomeFiberDiversity()

@mcp.tool()
def calculate_fiber_diversity_index(
    consumed_plant_species: list[str]
) -> str:
    """Audits 7-day plant species count, Shannon diversity H', and SCFA butyrate tier."""
    import json
    return json.dumps(client.calculate_fiber_diversity_index(consumed_plant_species), indent=2)

@mcp.tool()
def recommend_microbiome_substrate_additions(
    consumed_plant_species: list[str]
) -> str:
    """Recommends high-leverage prebiotic plant substrates to hit the 30-plant weekly quota."""
    import json
    return json.dumps(client.recommend_microbiome_substrate_additions(consumed_plant_species), indent=2)

if __name__ == "__main__":
    mcp.run()
