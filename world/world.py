import random
from typing import List, Tuple, Optional

class ResourceNode:
    """Represents a resource deposit on the map."""
    
    def __init__(self, resource_type: str, quantity: float, position: Tuple[int, int]):
        self.resource_type = resource_type
        self.quantity = quantity
        self.position = position
        self.extraction_rate = 0.1  # Base extraction rate per cycle
    
    def extract(self, amount: float) -> float:
        """Extract resources, returning actual amount extracted."""
        actual = min(amount, self.quantity)
        self.quantity -= actual
        return actual
    
    def is_depleted(self) -> bool:
        """Check if resource node is depleted."""
        return self.quantity <= 0


class World:
    """Represents the game world with map and resource nodes."""
    
    def __init__(self, width: int = 100, height: int = 100):
        self.width = width
        self.height = height
        self.resource_nodes: List[ResourceNode] = []
        self.terrain = self._generate_terrain()
        self._generate_resources()
    
    def _generate_terrain(self) -> List[List[str]]:
        """Generate basic terrain grid."""
        terrain_types = ['grass', 'water', 'mountain', 'forest']
        terrain = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Simple terrain generation - mostly grass with some features
                if random.random() < 0.1:
                    row.append(random.choice(['water', 'mountain', 'forest']))
                else:
                    row.append('grass')
            terrain.append(row)
        return terrain
    
    def _generate_resources(self):
        """Generate resource nodes on the map."""
        resource_types = ['iron', 'copper', 'oil', 'coal', 'wood', 'stone']
        
        for _ in range(20):  # Generate 20 resource nodes
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            
            # Check if position is valid for resource
            if self.terrain[y][x] in ['grass', 'forest']:
                resource_type = random.choice(resource_types)
                quantity = random.uniform(1000, 10000)
                self.resource_nodes.append(ResourceNode(resource_type, quantity, (x, y)))
    
    def get_resource_node_at(self, x: int, y: int) -> Optional[ResourceNode]:
        """Get resource node at specific position."""
        for node in self.resource_nodes:
            if node.position == (x, y):
                return node
        return None
    
    def is_valid_build_location(self, x: int, y: int) -> bool:
        """Check if a facility can be built at the given position."""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        
        # Can't build on water or mountains
        if self.terrain[y][x] in ['water', 'mountain']:
            return False
        
        # Check if there's already a facility at this position
        # This will be checked by the Game class using facilities list
        return True
    
    def get_terrain_at(self, x: int, y: int) -> str:
        """Get terrain type at position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.terrain[y][x]
        return 'invalid'