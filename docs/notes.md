\# HOCKEY STICK RECOMMENDER





\## Purpose

The goal is to recommend a precise hockey stick for the user: length, flex, kick point and curve.

Depending on the characteristic of the user: height, weight, position on the ice and style.





\## Input

| Input    | Allowed values                    |

|----------|-----------------------------------|

| Height   | 100–210 cm                        |

| Weight   | 20–150 kg                         |

| Position | forward, defense                  |

| Style    | sniper, playmaker, power          |



Invalid inputs are rejected with an error message.



\## Outputs

| Output     | Unit / values             |

|------------|---------------------------|

| Length     | cm and inches             |

| Flex       | 30–110 (multiple of 5)    |

| Kick point | low, mid, high            |

| Curve      | toe, mid, heel            |



\## Formulas



\*\*Length\*\* = 0.81 × height (cm)

* If the the player is playing forward -> round down
* If the player prefers short stick -> -0.5



* If the player is playing defence -> round up
* If the player prefers long stick -> +2. Else -> +1



\*\*Flex\*\* = weight(kg)\*0.45

* If player prefers stiff stick -> round up
* If player prefers soft stick -> round down



\*\*Kick point\*\* = depending on the players way of playing 

* Sniper -> low
* Slaymaker -> mid
* Power -> high.



\*\*Curve\*\* =  depending on the players way of playing

* Sniper -> toe
* Playmaker -> mid, power → heel.

