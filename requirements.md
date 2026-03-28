# Requirements: Corporate Empire Sim

## Project Summary
A desktop business simulation game that recreates the core strategic loop of building a corporate empire through production, retail, and competition for nostalgic fans of Capitalism II and strategy game enthusiasts.

## Goals
- Deliver a playable game that runs on Windows.
- Faithfully recreate the core strategic gameplay loop of starting a company, managing production chains, setting prices, and competing with AI.
- Provide an engaging and addictive experience offering dozens of hours of gameplay.
- Establish a solid technical and gameplay foundation suitable for future expansion.

## Scope

### In Scope
1.  **Core Economic Simulation:** Functional systems for resource extraction, manufacturing, retail, and the supply chains connecting them.
2.  **AI Competitors:** One or more AI-controlled companies that operate independently and compete with the player.
3.  **Single Scenario:** One balanced game map/scenario that provides a complete gameplay arc from startup to a win/loss condition.
4.  **Fundamental Financial Management:** Player ability to set product prices, manage basic marketing budgets, take out loans, and interact with a basic stock market (buy/sell shares, issue stock).
5.  **Win/Loss Conditions:** Clear game-end conditions based on achieving a target net worth, market share, or going bankrupt.

### Deferred
- Complex city simulations and detailed consumer demographics.
- Multiplayer functionality.
- A campaign with multiple scripted scenarios.
- Advanced features like detailed real estate or intricate R&D trees.
- Polished UI/UX, tutorials, and final art/sound assets.

## User Stories
1.  As a player, I want to start a new company with initial capital so that I can begin building my corporate empire.
2.  As a player, I want to build and connect production facilities (e.g., farms, factories, stores) so that I can create efficient supply chains to bring goods to market.
3.  As a player, I want to set the prices and marketing budget for my products so that I can maximize sales and profitability in a competitive market.
4.  As a player, I want to compete against AI-controlled rival companies so that the game world feels dynamic and challenging.
5.  As a player, I want clear goals (e.g., reach $100M net worth) and feedback on my performance so that I know when I have won or lost the game.

## Acceptance Criteria

**For In Scope Item 1 (Core Economic Simulation):**
- The player can build facilities for resource extraction (e.g., a mine), manufacturing (e.g., a factory), and retail (e.g., a store).
- The player can establish a supply chain by designating a facility to send its output to another facility as input.
- The simulation updates resource, good, and cash levels each game cycle based on these connections and production rates.

**For In Scope Item 2 (AI Competitors):**
- At least one AI company exists in the game world at startup.
- The AI company makes autonomous decisions: it builds facilities, sets prices, and produces/sells goods.
- The AI company's actions affect market prices and availability of goods, creating competition for the player.

**For In Scope Item 3 (Single Scenario):**
- The game launches into a predefined map with a set number of resource nodes, consumer markets, and starting parameters.
- The scenario is balanced to allow a skilled player to achieve a win condition within a reasonable play session (e.g., 2-4 hours).

**For In Scope Item 4 (Fundamental Financial Management):**
- The player can set the sale price for each of their retail products.
- The player can allocate a budget to marketing for a product, which measurably affects its sales volume.
- The player can take a loan from a bank, receiving cash and incurring a debt with periodic interest payments.
- The player can buy and sell shares of their own company and AI companies on a basic stock market interface.

**For In Scope Item 5 (Win/Loss Conditions):**
- The game detects and announces a win when the player's net worth meets or exceeds a predefined target.
- The game detects and announces a loss if the player's cash balance falls below a critical threshold and they cannot secure a loan.
- Upon win or loss, the game provides a summary screen with key performance statistics.