import random

player_hp = 5
enemy_hp = 5

print("🐛 Bug Battle Begins!")

while player_hp > 0 and enemy_hp > 0:
    input("\nPress Enter to attack...")
    damage = random.randint(1, 3)
    enemy_hp -= damage
    print(f"You hit the bug for {damage}! Bug HP: {max(enemy_hp, 0)}")

    if enemy_hp <= 0:
        break

    damage = random.randint(1, 3)
    player_hp -= damage
    print(f"The bug hits you for {damage}! Your HP: {max(player_hp, 0)}")

if player_hp > 0:
    print("\n✅ You win!")
else:
    print("\n💀 The bug defeated you.")