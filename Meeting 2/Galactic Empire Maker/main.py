import random


def main():
    materials = [
        "Unobtanium",
        "Quantumium",
        "Hyperfuel",
        "Exotic Matter",
        "Nano-alloys",
        "Bio-nanites",
        "Dark Matter Crystals",
        "Synthetically Engineered DNA",
        "Quantum Entanglement Crystals",
        "Hypercrystals",
        "Antimatter",
        "Graviton Resonators",
        "Plasma Conduits",
        "Chrono-Crystals",
        "Neural Interface Chips",
        "Neutrino Lenses",
        "Zero-Point Energy Extractors",
        "Genesis Seeds",
        "Quantum Encryption Protocols",
        "Omni-Replicators"
    ]

    class Alien:
        def __init__(self, name, needed_materials, num_of_suggestions):
            self.name = name
            self.needed_materials = needed_materials
            self.num_of_suggestions = num_of_suggestions

    aliens = [
        Alien('Xenolians', random.sample(materials, 3), random.randint(2, 10)),
        Alien('Dracorians', random.sample(materials, 3), random.randint(2, 10)),
        Alien('Nebulites', random.sample(materials, 3), random.randint(2, 10)),
        Alien('Eldari', random.sample(materials, 3), random.randint(2, 10))
    ]

    # Create a counter to represent how many alien delegations accepted to cooperate
    acceptance_counter = 0
    for alien in aliens:
        print(f'Negotiations with {alien.name} started.')

        # Create a copy to chose random materials from it
        temp_materials = materials
        delegation_status = False

        for i in range(alien.num_of_suggestions - 1):
            # If not materials left to suggest the negotiation will fail
            if len(temp_materials) == 0:
                print(f'\nDelegation failure. {alien.name} refused to cooperate.\n')

            # Generate a random material
            material_suggestion = random.choice(temp_materials)

            # Check if alien delegation needs that material
            if material_suggestion in alien.needed_materials:
                # Raise the number of successful delegation by one
                acceptance_counter += 1
                # Delete the material
                materials.remove(material_suggestion)
                print(f'Negotiation success. {alien.name} accepted {material_suggestion}.\n')
                print(f'Delegation success. {alien.name} accepted to cooperate.\n')
                delegation_status = True
                break

            print(f'Negotiation failure. {alien.name} refused {material_suggestion}.')
            temp_materials.remove(material_suggestion)

        if not delegation_status:
            print(f'\nDelegation failure. {alien.name} refused to cooperate.\n')

    # Determine the success rate
    success_rate = acceptance_counter / len(aliens)
    if success_rate >= 0.7:
        print(f'I succeeded. I was able to convince {success_rate} of the alien delegations to cooperate.')
    else:
        print(f'I failed. Only {success_rate} of the alien delegations accepted to cooperate.')


if __name__ == '__main__':
    main()