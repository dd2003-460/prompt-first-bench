# N161: H_TTL 公式中 (1-u) 项的适用性修正：若更新事件会重置 TTL 计时器（常见行为），则有效失效率不再是 u，而是 min(u, 1/TTL)，需修正公

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

H_TTL 公式中 (1-u) 项的适用性修正：若更新事件会重置 TTL 计时器（常见行为），则有效失效率不再是 u，而是 min(u, 1/TTL)，需修正公式为 H_TTL = H_static * (1 - min(u, 1/TTL)) * P_TTL_hit + ...，以消除高更新率下的过度折损估计

## Corrected Claim

H_TTL 公式中 (1-u) 项的适用性修正：若更新事件会重置 TTL 计时器（常见行为），则有效失效率不再是 u，而是 min(u, 1/TTL)，需修正公式为 H_TTL = H_static * (1 - min(u, 1/TTL)) * P_TTL_hit + ...，以消除高更新率下的过度折损估计

## Evidence

先验知识/题面给定，逻辑校验通过：在TTL机制下，若更新重置计时器，则条目在TTL过期前被更新视为有效，有效失效率受限于TTL倒数，逻辑自洽。
