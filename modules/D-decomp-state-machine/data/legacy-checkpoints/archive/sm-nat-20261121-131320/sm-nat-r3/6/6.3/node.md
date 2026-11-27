# N50: LRU 策略下，对象 i 的稳态命中率贡献项 h_i = min(1, C / (S_i * f_i / R))，其中 R 为总请求率，该公式量化了 LRU 对

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

LRU 策略下，对象 i 的稳态命中率贡献项 h_i = min(1, C / (S_i * f_i / R))，其中 R 为总请求率，该公式量化了 LRU 对头部高频对象的锁定能力，是计算 H_LRU 下界的核心积分被积函数。

## Corrected Claim

LRU 策略下，对象 i 的稳态命中率贡献项 h_i = min(1, C / (S_i * f_i / R))，其中 R 为总请求率，该公式量化了 LRU 对头部高频对象的锁定能力，是计算 H_LRU 下界的核心积分被积函数。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 794)
