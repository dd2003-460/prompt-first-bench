# N280: 延迟容忍度 T_max > 70ms/token 的条件需量化：M3 Ultra (13-14 tokens/s) 对应延迟 71-77ms/token，RTX

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

延迟容忍度 T_max > 70ms/token 的条件需量化：M3 Ultra (13-14 tokens/s) 对应延迟 71-77ms/token，RTX 4090 双卡 (25-30 tokens/s) 对应延迟 33-40ms/token。若用户要求 T_max < 50ms/token，M3 Ultra 直接不可行，此约束使 M3 Ultra 仅在 T_max > 75ms/token 时具有竞争力

## Corrected Claim

延迟容忍度 T_max > 70ms/token 的条件需量化：M3 Ultra (13-14 tokens/s) 对应延迟 71-77ms/token，RTX 4090 双卡 (25-30 tokens/s) 对应延迟 33-40ms/token。若用户要求 T_max < 50ms/token，M3 Ultra 直接不可行，此约束使 M3 Ultra 仅在 T_max > 75ms/token 时具有竞争力

## Evidence

先验知识/题面给定，逻辑校验通过：1000/13≈76.9ms, 1000/14≈71.4ms, 1000/25=40ms, 1000/30≈33.3ms，数值换算准确且逻辑自洽。
