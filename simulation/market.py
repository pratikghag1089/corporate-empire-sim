import math
from typing import Dict, List, Optional

class Market:
    """Manages supply/demand dynamics and pricing for products."""
    
    def __init__(self, game_state):
        """Initialize market with reference to game state."""
        self.game_state = game_state
        self.base_elasticity = 0.1  # How sensitive demand is to price changes
        self.marketing_effectiveness = 0.05  # How much marketing affects demand
        self.supply_decay = 0.98  # Supply naturally decays each cycle
        self.demand_growth = 1.01  # Demand naturally grows each cycle
    
    def update_market_cycle(self):
        """Update market dynamics for one business cycle."""
        # Apply natural supply decay and demand growth
        for product_id in self.game_state.market_data['supply']:
            self.game_state.market_data['supply'][product_id] *= self.supply_decay
            self.game_state.market_data['demand'][product_id] *= self.demand_growth
        
        # Update prices based on supply/demand
        self._update_prices()
    
    def _update_prices(self):
        """Calculate new prices based on supply and demand."""
        for product_id in self.game_state.products:
            supply = self.game_state.market_data['supply'].get(product_id, 0)
            demand = self.game_state.market_data['demand'].get(product_id, 0)
            
            # Avoid division by zero
            if supply == 0:
                supply = 0.1
            
            # Price calculation: base price adjusted by supply/demand ratio
            base_price = self.game_state.products[product_id].get('base_price', 10.0)
            ratio = demand / supply
            
            # Apply logarithmic scaling to prevent extreme price swings
            price_multiplier = 1.0 + math.log(max(0.1, ratio)) * self.base_elasticity
            new_price = base_price * price_multiplier
            
            # Ensure price doesn't go negative
            new_price = max(0.1, new_price)
            
            self.game_state.update_market_price(product_id, new_price)
    
    def add_supply(self, product_id: str, amount: float):
        """Add supply to the market for a product."""
        if product_id not in self.game_state.market_data['supply']:
            self.game_state.market_data['supply'][product_id] = 0.0
        self.game_state.market_data['supply'][product_id] += amount
    
    def add_demand(self, product_id: str, amount: float):
        """Add demand to the market for a product."""
        if product_id not in self.game_state.market_data['demand']:
            self.game_state.market_data['demand'][product_id] = 0.0
        self.game_state.market_data['demand'][product_id] += amount
    
    def apply_marketing_effect(self, product_id: str, marketing_budget: float):
        """Apply marketing budget to increase demand for a product."""
        if marketing_budget <= 0:
            return
        
        # Marketing increases demand based on budget
        demand_increase = marketing_budget * self.marketing_effectiveness
        self.add_demand(product_id, demand_increase)
    
    def get_market_summary(self) -> Dict:
        """Get summary of current market conditions."""
        summary = {}
        for product_id in self.game_state.products:
            supply = self.game_state.market_data['supply'].get(product_id, 0)
            demand = self.game_state.market_data['demand'].get(product_id, 0)
            price = self.game_state.get_product_price(product_id)
            
            summary[product_id] = {
                'supply': supply,
                'demand': demand,
                'price': price,
                'ratio': demand / max(0.1, supply)
            }
        return summary