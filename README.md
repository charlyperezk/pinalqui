# PINALQUI - Web APP Proyect
#### Develop by: Lautaro Lovato y Carlos Pérez Küper.
#### Date: 2024/02/14

# ---- DB Design ----:

## Properties:
- Id_Property PK # Integer Incremental
- Title # String
- Address # String
- Id_City FK # Integer
- Id_Type FK # Integer
- Id_Commodities FK # Integer
- Price ($) # Float
- Id_Currency FK  (Foreign Key referencing Currencies table) # Integer
- Deposit ($) # Float
- Description (Text) # String

#### Coordinates are needed if we want to show the property in a map:
- Latitude # String
- Longitude # String

## Cities
- Id_City PK # Integer Incremental
- Id_Province # Integer
- Name # String

## Provincies
- Id_Province PK # Integer Incremental
- Name # String

## Types (Property types)
- Id_Type PK # Integer Incremental
- Name # String

## Currencies (USD/ARS, etc.)
- Id_Currency PK # Integer Incremental
- Name # String

## Commodities:
- Id_Commodity PK # Integer Incremental
- Capacity (Number of people that can be in the property) Integer
- Surface (m²) # Float
- Floors (Quantity) # Integer
- Rooms (Quantity) # Integer
- Bedroom (Quantity) # Integer
- Bathroom (Quantity) # Integer
- Parking (Yes or No) # Bool
- Elevator (Yes or No) # Bool
- Air Conditioning (Yes or No) # Bool

## Images
- Id_Image PK # Integer Incremental
- Title # String
- URL # String
- Id_Property FK # Integer

## ¿Services  (Another table with available services, like water, gas...)?
