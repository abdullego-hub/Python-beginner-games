dragon_awake = False
health = 100
energy = 100

print("🐉 Welcome to Dragon Cave – Level 2")
print("Type 'help' to see commands.")

while True:
    command = input("> ").lower()

    if command == "wake":
        if dragon_awake:
            print("The dragon is already awake.")
        else:
            dragon_awake = True
            print("The dragon wakes up.")

    elif command == "sleep":
        if not dragon_awake:
            print("The dragon is already sleeping.")
        else:
            dragon_awake = False
            energy = min(100, energy + 30)
            print("The dragon sleeps and restores energy.")

    elif command == "fly":
        if not dragon_awake:
            print("The dragon is sleeping and cannot fly.")
        elif energy < 20:
            print("The dragon is too tired to fly.")
        else:
            energy -= 20
            print("The dragon flies through the sky!")

    elif command == "fire":
        if not dragon_awake:
            print("The dragon is asleep and cannot breathe fire.")
        elif health < 10:
            print("The dragon is too weak to breathe fire.")
        else:
            health -= 10
            energy -= 10
            print("🔥 The dragon breathes fire!")

    elif command == "status":
        print(f"Health: {health}")
        print(f"Energy: {energy}")
        print("Awake:" , dragon_awake)

    elif command == "help":
        print("wake   - wake the dragon")
        print("sleep  - sleep and restore energy")
        print("fly    - fly (costs energy)")
        print("fire   - breathe fire (costs health & energy)")
        print("status - show dragon status")
        print("quit   - exit game")

    elif command == "quit":
        print("You leave the dragon cave. Goodbye!")
        break

    else:
        print("Unknown command.")

    # GAME OVER CHECK
    if health <= 0:
        print("💀 The dragon has collapsed. Game Over.")
        break
