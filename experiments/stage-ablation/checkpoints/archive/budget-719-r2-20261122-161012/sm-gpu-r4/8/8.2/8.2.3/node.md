# N280: 延迟容忍度 T_max > 70ms/token 的条件需量化：M3 Ultra (13-14 tokens/s) 对应延迟 71-77ms/token，RTX

- **status**: pending
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

父节点级核验未通过：非正交（子节点1与父节点存在事实性矛盾。父节点断言M3 Ultra在71-77ms/token且不可行，子节点1基于修正后的带宽数据（800GB/s）推导出~50ms/token并判定可行，两者结论直接冲突，未体现‘修正’关系而是相互排斥。此外，子节点3的TCO分析依赖于子节点1和2得出的延迟结论，若子节点1的修正成立，父节点的‘不可行’前提已失效，导致逻辑链条断裂。）
