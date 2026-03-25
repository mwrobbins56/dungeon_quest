import random

def main():
    def setup_player():
        # Ask the user for their name
        name = input("Enter your name: ")
        
        # Initialize dictionary with keys: "name", "health", and "inventory"
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }

        # Return the dictionary
        return player

    def create_treasures():
        # Creates a dictionary of treasures, where each treasure has a value.
        treasures = {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12)
        }
           
        # Return the dictionary
        return treasures

    def display_options(room_number):

        # Print the room number and the 4 menu options listed above    
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")

    # Simulate searching the current room
    def search_room(player, treasures): 
        
        # Randomly choose outcome = "treasure" or "trap" 
        outcome = random.choice(["treasure", "trap"])

        # If treasure: choose a random treasure, add to inventory, and print
        # If trap: subtract 2 from player health and print warning.
        if outcome == "treasure":
            item = random.choice(list(treasures.keys()))
            player["inventory"].append(item)
            print(f"You found a {item}!")
        else:
            player["health"] -= 2
            print("You triggered a trap! You lost 2 health points.")
      
    # Display the player health and inventory.
    def check_status(player):
        print(f"Health: {player['health']}")
        if player["inventory"]:
            print(f"Inventory: {', '.join(player['inventory'])}")
        else:
            print("Inventory: You have no items yet.")
    
    # End the game and display summary.
    def end_game(player, treasures):
    # Calculate total score by add the value of collected treasures
        total_score = sum(treasures[item] for item in player["inventory"] if item in treasures)
        
    # Print final health, items, and total value, Thanks for playing
        print(f"\n--- Game Over ---")
        print(f"Final Health: {player['health']}")
        if player["inventory"]:
            print(f"Items Collected: {', '.join(player['inventory'])}")
        else:
            print("Items Collected: None")
        print(f"Total Score: {total_score}")
        print("Thanks for playing, " + player["name"] + "!")
 
    # Inside each room, prompt player choice
    # Use if/elif to handle each choice (1–4)
    # Break or return when player quits or dies
    # Call end_game() after all rooms are explored
    def run_game_loop(player, treasures):
        for room_number in range(1, 6):
            while True:
                display_options(room_number)
                choice = input("Enter your choice (1-4): ").strip()
 
                if choice == "1":
                    search_room(player, treasures)
                    if player["health"] < 1:
                        print("You have run out of health!")
                        end_game(player, treasures)
                        return
                elif choice == "2":
                    print("Moving to the next room...")
                    break
                elif choice == "3":
                    check_status(player)
                elif choice == "4":
                    print("You chose to quit.")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid choice. Enter a number from 1 to 4.")
 
        end_game(player, treasures)
        
    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
