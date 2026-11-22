# N71: LFU vs LRU 在 M/C=1.0 下的数值差异归零验证：由于缓存容量（128GB）大于或等于总工作集大小（~128GB），LFU 和 LRU 均能容纳所

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

LFU vs LRU 在 M/C=1.0 下的数值差异归零验证：由于缓存容量（128GB）大于或等于总工作集大小（~128GB），LFU 和 LRU 均能容纳所有 100,000 个对象。此时，策略差异导致的驱逐行为消失，ΔH = H_LFU - H_LRU = 0 百分点。任何非零增益仅存在于 M/C < 1.0 的场景，需明确标注此数值结果为边界条件特例。

## Corrected Claim

LFU vs LRU 在 M/C=1.0 下的数值差异归零验证：由于缓存容量（128GB）大于或等于总工作集大小（~128GB），LFU 和 LRU 均能容纳所有 100,000 个对象。此时，策略差异导致的驱逐行为消失，ΔH = H_LFU - H_LRU = 0 百分点。任何非零增益仅存在于 M/C < 1.0 的场景，需明确标注此数值结果为边界条件特例。

## Evidence

逻辑推导成立，来源未直接覆盖

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2069556046839001951&rut=97716e9723be89c2057c60394c504a982bd8057fe5623f618fe4d716aa98f22f', 'type': 'ddg', 'title': '吃透Redis缓存核心：淘汰策略、LRU/LFU区别与四大缓存问题全解'}
