# N183: LFU 在更新场景下的有效命中率机制：LFU 不直接抵抗更新失效，而是通过频率计数识别‘更新后仍高频’的对象并优先保留。若更新导致对象内容变化但热度不变，LFU

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

LFU 在更新场景下的有效命中率机制：LFU 不直接抵抗更新失效，而是通过频率计数识别‘更新后仍高频’的对象并优先保留。若更新导致对象内容变化但热度不变，LFU 在更新后若未重置计数器，可能保留旧版本（错误命中）或需额外逻辑。理想 LFU 假设能即时感知更新并更新频率计数，其命中率 H_LFU_eff = H_LFU_static * (1 - P_invalid_LFU)。由于 LFU 同样受限于对象更新导致的缓存失效，P_invalid_LFU 与 LRU 相同，除非 LFU 能利用‘更新前’的预取或版本管理。

## Corrected Claim

LFU 在更新场景下的有效命中率机制：LFU 不直接抵抗更新失效，而是通过频率计数识别‘更新后仍高频’的对象并优先保留。若更新导致对象内容变化但热度不变，LFU 在更新后若未重置计数器，可能保留旧版本（错误命中）或需额外逻辑。理想 LFU 假设能即时感知更新并更新频率计数，其命中率 H_LFU_eff = H_LFU_static * (1 - P_invalid_LFU)。由于 LFU 同样受限于对象更新导致的缓存失效，P_invalid_LFU 与 LRU 相同，除非 LFU 能利用‘更新前’的预取或版本管理。

## Evidence

先验知识/题面给定，逻辑校验通过
