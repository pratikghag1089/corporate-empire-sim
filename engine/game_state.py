class GameState:
    """Central data store for the entire game simulation."""
    
    def __init__(self):
        """Initialize all game data structures."""
        # Core game state
        self.current_cycle = 0
        self.game_time = 0.0  # Total elapsed time in seconds
        
        # Companies (player and AI)
        self.companies = []  # List of Company objects
        self.player_company_id = None  # ID of player's company
        
        # Facilities and production
        self.facilities = []  # List of Facility objects
        self.production_chains = {}  # Mapping of product ID to production chain
        
        # Products and market
        self.products = {}  # Mapping of product ID to Product definition
        self.market_data = {
            'supply': {},  # product_id -> total supply
            'demand': {},  # product_id -> total demand
            'prices': {},  # product_id -> current price
            'history': {}  # product_id -> list of historical prices
        }
        
        # Financial systems
        self.financial_data = {
            'stock_market': {},  # company_id -> stock price
            'interest_rates': 0.05,  # Base interest rate for loans
            'economic_cycle': 'expansion',  # Current economic phase
            'inflation_rate': 0.02
        }
        
        # World map and resources
        self.world_map = {
            'width': 100,
            'height': 100,
            'resource_nodes': [],  # List of resource deposits
            'terrain': []  # 2D grid of terrain types
        }
        
        # Game settings
        self.settings = {
            'difficulty': 'normal',
            'starting_capital': 1000000,
            'simulation_speed': 1.0
        }
    
    def reset(self):
        """Reset all game state to initial values."""
        self.__init__()
    
    def get_company(self, company_id):
        """Retrieve a company by ID."""
        for company in self.companies:
            if company.id == company_id:
                return company
        return None
    
    def get_facility(self, facility_id):
        """Retrieve a facility by ID."""
        for facility in self.facilities:
            if facility.id == facility_id:
                return facility
        return None
    
    def get_product_price(self, product_id):
        """Get current market price for a product."""
        return self.market_data['prices'].get(product_id, 0.0)
    
    def update_market_price(self, product_id, new_price):
        """Update market price and maintain history."""
        old_price = self.market_data['prices'].get(product_id, new_price)
        self.market_data['prices'][product_id] = new_price
        
        # Maintain price history (last 100 cycles)
        if product_id not in self.market_data['history']:
            self.market_data['history'][product_id] = []
        
        history = self.market_data['history'][product_id]
        history.append(new_price)
        if len(history) > 100:
            history.pop(0)