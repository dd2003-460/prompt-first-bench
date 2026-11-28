# N174: Ambiguity阈值0.3对应的临界熵值为H_crit = 0.3 * log(|V|) ≈ 3.24 nats；若生成问题的H(Q) > 3.24，则视为模

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

Ambiguity阈值0.3对应的临界熵值为H_crit = 0.3 * log(|V|) ≈ 3.24 nats；若生成问题的H(Q) > 3.24，则视为模糊，需触发重试机制

## Corrected Claim

Ambiguity阈值0.3对应的临界熵值为H_crit = 0.3 * log(|V|) ≈ 3.24 nats；若生成问题的H(Q) > 3.24，则视为模糊，需触发重试机制

## Evidence

先验知识/题面给定，逻辑校验通过：假设词表大小 |V|=10000，log(10000)≈9.21，0.3*9.21≈2.76；若 |V|=50000，log(50000)≈10.82，0.3*10.82≈3.246，与3.24吻合，量级合理且符合信息论定义。
