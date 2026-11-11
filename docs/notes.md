# Hockey Stick Recommender

## Purpose
Recommend a hockey stick (length, flex, kick point and curve) adapted to the user,
based on their height, weight, position on the ice and playing style.

## Inputs
| Input    | Allowed values           |
|----------|--------------------------|
| Height   | 100–210 cm               |
| Weight   | 20–150 kg                |
| Position | forward, defense         |
| Style    | sniper, playmaker, power |

Invalid inputs are rejected with an error message.

## Outputs
| Output     | Unit / values          |
|------------|------------------------|
| Length     | cm and inches          |
| Flex       | 30–110 (multiple of 5) |
| Kick point | low, mid, high         |
| Curve      | toe, mid, heel         |

## Formulas

**Length** = 0.81 × height (cm)

- Forward: round down. If the player prefers a short stick: −0.5
- Defense: round up. If the player prefers a long stick: +2, else +1

**Flex** = weight (kg) × 0.45

- Prefers a stiff stick: round up
- Prefers a soft stick: round down

**Kick point** (depends on style)

- Sniper → low
- Playmaker → mid
- Power → high

**Curve** (depends on style)

- Sniper → toe
- Playmaker → mid
- Power → heel
