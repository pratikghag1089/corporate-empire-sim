# architecture.md

## Tech Stack
Python with Pygame for the GUI and core game loop. Python offers rapid development and clear syntax for complex simulation logic, while Pygame provides straightforward 2D rendering and input handling suitable for a desktop strategy game. We'll use JSON for scenario configuration and data persistence. The architecture will follow a component-based design with clear separation between simulation logic, rendering, and AI.

## Component Design

### 1. Game Engine (`main.py`, `engine/`)
- **Responsibility**: Core game loop, timing, state management, and component orchestration.
- **Key Classes**: `Game` (main controller), `GameState` (central data store).
- **Connections**: Initializes and coordinates all other components. Updates simulation, AI, and rendering each frame.

### 2. Economic Simulation (`simulation/`)
- **Responsibility**: Manages production chains, market dynamics, pricing, and financial systems.
- **Key Classes**: `Market` (supply/demand/pricing), `ProductionManager` (facility operations), `FinancialSystem` (loans, stock market).
- **Connections**: Receives player/AI actions from controllers; provides updated economic state to renderer and AI.

### 3. World & Entities (`world/`)
- **Responsibility**: Represents the game map, facilities, products, and companies.
- **Key Classes**: `World` (map with resource nodes), `Facility` (base class for buildings), `Company` (player/AI entity), `Product` (goods definitions).
- **Connections**: Used by simulation for calculations; rendered by display system.

### 4. AI System (`ai/`)
- **Responsibility**: Controls competitor companies with strategic decision-making.
- **Key Classes**: `AIDirector` (manages all AI companies), `CompanyAI` (individual AI logic).
- **Connections**: Reads game state from `GameState`; issues build/price/marketing commands to simulation.

### 5. Rendering & UI (`rendering/`)
- **Responsibility**: Visual display of game world, facilities, and user interface.
- **Key Classes**: `Renderer` (draws world/entities), `UIManager` (handles menus/HUD), `Camera` (viewport control).
- **Connections**: Reads from `GameState` for visual representation; sends player inputs to input handler.

### 6. Input Handling (`input_handler.py`)
- **Responsibility**: Processes mouse/keyboard events and translates to game actions.
- **Key Classes**: `InputHandler` (event processing and command generation).
- **Connections**: Captures Pygame events; sends commands to game engine or UI.

## Data Flow
1. **Input**: Player actions via `InputHandler` → `Game` engine
2. **Processing**: `Game` updates `GameState` via `Simulation` systems (production, market, finance)
3. **AI Update**: `AIDirector` reads `GameState` → issues commands back to `Simulation`
4. **State Update**: All changes consolidated in `GameState`
5. **Output**: `Renderer` reads `GameState` → draws world and UI to screen
6. **Loop**: Repeat each frame with fixed time step for simulation consistency

## Key Design Decisions
- **Turn-based simulation with real-time rendering**: Economic calculations occur in discrete "business cycles" (configurable speed) while rendering runs continuously for smooth UI.
- **Centralized game state**: All data flows through `GameState` to prevent synchronization issues and simplify saving/loading.
- **Component isolation**: Simulation logic has no rendering dependencies, enabling headless testing and future server potential.
- **Data-driven products/facilities**: Defined in JSON files for easy balancing and modding support.
- **AI uses simplified economic models**: Competitors use heuristic-based decisions rather than full economic simulation to maintain performance.