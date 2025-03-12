# trmnl-plugin-whos-that-pokemon
A trmnl plugin that displays a random Pokémon every day

[![Run Tests](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/test.yml/badge.svg)](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/test.yml)
[![Fetch and save random Pokemon](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/fetch_and_save_pokemon.yml/badge.svg)](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/fetch_and_save_pokemon.yml)

# What is it?
This repo fetches data for a Pokémon at random every day at 12:00 UTC and saves it to the repo so that it can be polled from a private plugin on TRMNL.

<img src="https://github.com/user-attachments/assets/ee7beab9-906b-49cf-9248-66ae7f270c27" alt="full" width="200"/> <img src="https://github.com/user-attachments/assets/a4460266-ec73-4901-9f78-77c5766e242d" alt="half horizontal" width="200"/> <img src="https://github.com/user-attachments/assets/3f2e1e89-01eb-4a36-80cd-2ae1e04ed920" alt="half vertical" width="200"/> <img src="https://github.com/user-attachments/assets/2ebbfa96-3029-4d5d-a074-a3221b1d9c70" alt="quadrant" width="200"/>

# How to use it?
## Step 1: Configure private plugin
1. Create a [private plugin](https://usetrmnl.com/plugin_settings?keyname=private_plugin) from the TRMNL dashboard
2. Set the strategy to `Polling`
3. Set the polling URL to https://raw.githubusercontent.com/sriniketh/trmnl-plugin-whos-that-pokemon/refs/heads/main/pokemon_data/response.json
4. Set the polling headers as `content-type=application/json`

Refer [settings.yml](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/blob/main/settings.yml) for more info.

## Step 2: Setup templates
Copy the full, half horizontal, half vertical and quadrant views from the `views/` directory and paste it as markup for the plugin on the dashboard.

The Github Action workflow [Fetch and save random Pokemon](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/fetch_and_save_pokemon.yml) will trigger once a day and save the response in `/pokemon_data`.

# Attributions
The data is obtained from [PokéAPI](https://pokeapi.co/).

This repository includes data related to Pokémon and Pokémon characters. 
© 2025 Pokémon. © 1995–2025 Nintendo/Creatures Inc./GAME FREAK inc. Pokémon and Pokémon character names are trademarks of Nintendo. All rights reserved.

The use of this data is intended for educational and non-commercial purposes only. No copyright infringements are intended. Redistribution of this repository must retain this notice along with the original licenses of any included third-party libraries. Users should be aware that the inclusion of Pokémon-related content is subject to copyright laws, and any use is at their own legal risk.

# License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
