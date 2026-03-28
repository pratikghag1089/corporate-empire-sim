# Corporate Empire Sim

A desktop business simulation game that recreates the core strategic loop of building a corporate empire through production, retail, and competition for nostalgic fans of Capitalism II and strategy game enthusiasts.

## Goals

- Deliver a playable game that runs on Windows.
- Faithfully recreate the core strategic gameplay loop of starting a company, managing production chains, setting prices, and competing with AI.
- Provide an engaging and addictive experience offering dozens of hours of gameplay.
- Establish a solid technical and gameplay foundation suitable for future expansion.

---
## Architecture

Python with Pygame for the GUI and core game loop. Python offers rapid development and clear syntax for complex simulation logic, while Pygame provides straightforward 2D rendering and input handling suitable for a desktop strategy game. We'll use JSON for scenario configuration and data persistence. The architecture will follow a component-based design with clear separation between simulation logic, rendering, and AI.

### Project Files

- `main.py` — Entry point: initializes Pygame, creates Game instance, runs main loop
- `engine/game.py` — Game controller: manages game loop timing, coordinates all systems, handles pause/speed controls
- `engine/state.py` — Central game state container: holds all companies, facilities, market data, and world information
- `world/world.py` — Game world: contains map grid, resource nodes, and location management
- `world/facilities.py` — Facility classes: base Facility plus Extractor, Manufacturer, Retailer subclasses with production logic
- `world/company.py` — Company entity: manages cash, loans, shares, facilities, and financial statements
- `world/products.py` — Product definitions: loads from JSON, defines production chains and base properties
- `simulation/market.py` — Market simulation: calculates supply/demand, sets prices, handles retail sales
- `simulation/production.py` — Production manager: processes facility operations, supply chain transfers, and inventory
- `simulation/finance.py` — Financial systems: handles loans, interest, stock market transactions, and net worth calculation
- `ai/director.py` — AI director: coordinates all AI companies, schedules decision-making cycles
- `ai/company_ai.py` — Company AI: heuristic-based decision making for building, pricing, and marketing
- `rendering/renderer.py` — Main renderer: draws world map, facilities, supply chains, and basic visual elements
- `rendering/ui_manager.py` — UI system: renders HUD, menus, facility controls, financial panels, and handles UI input
- `input_handler.py` — Input processor: translates Pygame events to game commands, handles camera and selection

_See `architecture.md` for the full design._

---

_Development log will be appended as issues are completed._
