filter_menu = """
Filter menu:
1: CaMeL Filter
2: snake_strings Filter
3: SHOUTING Filter
4: Whispering Filter
0: Exit
"""

filters_text = {
    1: {
        "name": "CaMeL Filter:",
        "description": "Converts text to CamelCase format (no spaces and the first letter of each word is capitalized).\n",
    },
    2: {
        "name": "snake_strings Filter:",
        "description": "Converts text to snake_case format (all spaces are replaced with underscores).\n",
    },
    3: {
        "name": "SHOUTING Filter:",
        "description": "Converts text to SHOUTING Filter format (all letters in capitals).\n",
    },
    4: {
        "name": "Whispering Filter:",
        "description": "Converts text to Whispering Filter format (all letters to lowercase).\n",
    }
}
