### PINALQUI - Web APP Proyect
### Develop by: Lautaro Lovato y Carlos Pérez Küper.
### Date: 2024/02/14

# ---- DB Design ----:

# Properties:
- Id_Property # Integer
- Title # String
- Address # String
- Id_City FK # Integer
- Id_Type FK # Integer
- Id_Commodities FK # Integer
- Id_Images FK # Integer
- Price ($) # Float
- Id_Currency FK  (Foreign Key referencing Currencies table) # Integer
- Deposit ($) # Float
- Description (Text) # String
### Coordinates are needed if we want to show the property in a map:
- Latitude # String
- Longitude # String

# Cities
- Id_City # Integer
- Id_Province
- Name # String

# Commodities:
- Id_Commoditie Interger Incremental
- Capacity (Number of people that can be in the property) Integer
- Surface (m²) # Float
- Floors (Quantity) # Integer
- Rooms (Quantity) # Integer
- Bedroom (Quantity) # Integer
- Bathroom (Quantity) # Integer
- Parking (Yes or No) # Bool
- Elevator (Yes or No) # Bool
- Air Conditioning (Yes or No) # Bool

# Images
- Id_Image
- Title
- URL
- Id_Property FK #

# ¿Services  (Another table with available services, like water, gas...)?