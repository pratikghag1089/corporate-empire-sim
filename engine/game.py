import pygame
from engine.game_state import GameState

class Game:
    """Main game controller that orchestrates all components."""
    
    def __init__(self, width=1024, height=768):
        """Initialize the game with window and core systems."""
        # Display setup
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Business Tycoon Simulation")
        
        # Core systems
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        
        # Game loop control
        self.running = True
        self.paused = False
        self.simulation_speed = 1.0  # 1.0 = normal speed
        self.simulation_accumulator = 0.0
        self.simulation_timestep = 1.0 / 60.0  # 60 Hz simulation
        
        # Initialize placeholder components (to be implemented later)
        self.simulation = None
        self.ai_director = None
        self.renderer = None
        self.input_handler = None
    
    def run(self):
        """Main game loop with fixed timestep for simulation."""
        while self.running:
            # Calculate delta time
            dt = self.clock.tick(60) / 1000.0  # Convert to seconds
            
            # Process input
            self._handle_events()
            
            # Update simulation with fixed timestep
            if not self.paused:
                self.simulation_accumulator += dt * self.simulation_speed
                while self.simulation_accumulator >= self.simulation_timestep:
                    self._update_simulation(self.simulation_timestep)
                    self.simulation_accumulator -= self.simulation_timestep
            
            # Update AI (runs at simulation speed)
            self._update_ai(self.simulation_timestep if not self.paused else 0)
            
            # Render frame
            self._render()
    
    def _handle_events(self):
        """Process pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    self.simulation_speed = min(4.0, self.simulation_speed * 1.5)
                elif event.key == pygame.K_MINUS:
                    self.simulation_speed = max(0.25, self.simulation_speed / 1.5)
    
    def _update_simulation(self, dt):
        """Update economic simulation systems."""
        # Placeholder for simulation updates
        # Will be implemented in future issues
        self.game_state.current_cycle += 1
    
    def _update_ai(self, dt):
        """Update AI decision making."""
        # Placeholder for AI updates
        # Will be implemented in future issues
        pass
    
    def _render(self):
        """Render the current game state."""
        # Clear screen
        self.screen.fill((30, 30, 40))
        
        # Draw placeholder UI
        font = pygame.font.SysFont(None, 36)
        
        # Title
        title_text = font.render("Business Tycoon Simulation", True, (255, 255, 255))
        self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 20))
        
        # Status information
        status_font = pygame.font.SysFont(None, 24)
        pause_status = "PAUSED" if self.paused else "RUNNING"
        status_text = status_font.render(
            f"Status: {pause_status} | Speed: {self.simulation_speed:.2f}x | Cycle: {self.game_state.current_cycle}",
            True, (200, 200, 200)
        )
        self.screen.blit(status_text, (20, 60))
        
        # Controls
        controls_text = status_font.render(
            "Controls: SPACE=Pause | +/-=Speed | ESC=Quit",
            True, (150, 150, 150)
        )
        self.screen.blit(controls_text, (20, self.height - 40))
        
        # Update display
        pygame.display.flip()