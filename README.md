# trmnl-plugin-whos-that-pokemon
A trmnl plugin that displays a random Pokémon every day

[![Run Tests](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/test.yml/badge.svg)](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/test.yml)
[![Send random Pokemon to trmnl](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/send_pokemon_to_trmnl.yml/badge.svg)](https://github.com/sriniketh/trmnl-plugin-whos-that-pokemon/actions/workflows/send_pokemon_to_trmnl.yml)

# What is it?
This repo fetches data for a Pokémon at random every day at 12:00 UTC and POSTs it to TRMNL via a webhook configured for a private plugin.

<img src="https://github.com/user-attachments/assets/ee7beab9-906b-49cf-9248-66ae7f270c27" alt="full" width="200"/> <img src="https://github.com/user-attachments/assets/a4460266-ec73-4901-9f78-77c5766e242d" alt="half horizontal" width="200"/> <img src="https://github.com/user-attachments/assets/3f2e1e89-01eb-4a36-80cd-2ae1e04ed920" alt="half vertical" width="200"/> <img src="https://github.com/user-attachments/assets/2ebbfa96-3029-4d5d-a074-a3221b1d9c70" alt="quadrant" width="200"/>

# How to use it?
## Step 1: Setup private plugin
Create a [private plugin](https://usetrmnl.com/plugin_settings?keyname=private_plugin) from the TRMNL dashboard.
Set the strategy to `Webhook`.
Copy the Webhook URL.

## Step 2: Clone this repo
Fork this repository and add the Webhook URL as TRMNL_WEBHOOK_URL to secrets.

The Github Action will trigger once a day and POST to the Webhook URL that's been set.

# Attributions
The data is obtained from [PokéAPI](https://pokeapi.co/).

This repository includes data related to Pokémon and Pokémon characters. 
© 2025 Pokémon. © 1995–2025 Nintendo/Creatures Inc./GAME FREAK inc. Pokémon and Pokémon character names are trademarks of Nintendo. All rights reserved.

The use of this data is intended for educational and non-commercial purposes only. No copyright infringements are intended. Redistribution of this repository must retain this notice along with the original licenses of any included third-party libraries. Users should be aware that the inclusion of Pokémon-related content is subject to copyright laws, and any use is at their own legal risk.

# License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
