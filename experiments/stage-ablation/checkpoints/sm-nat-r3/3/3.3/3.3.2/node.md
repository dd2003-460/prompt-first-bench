# N65: 大小-热度负相关强（ρ→-1）时，LFU 的驱逐错误率最低。具体而言，LRU 的驱逐错误率 E_evict_LRU 定义为 LRU 驱逐头部对象的概率，而 LF

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

大小-热度负相关强（ρ→-1）时，LFU 的驱逐错误率最低。具体而言，LRU 的驱逐错误率 E_evict_LRU 定义为 LRU 驱逐头部对象的概率，而 LFU 的驱逐错误率 E_evict_LFU 趋近于 0。ΔH 的上限可近似为 ΔH_max ≈ E_evict_LRU × (P_head - P_tail)，其中 P_tail 为尾部对象的请求概率。

## Corrected Claim

大小-热度负相关强（ρ→-1）时，LFU 的驱逐错误率最低。具体而言，LRU 的驱逐错误率 E_evict_LRU 定义为 LRU 驱逐头部对象的概率，而 LFU 的驱逐错误率 E_evict_LFU 趋近于 0。ΔH 的上限可近似为 ΔH_max ≈ E_evict_LRU × (P_head - P_tail)，其中 P_tail 为尾部对象的请求概率。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个关键组成部分：E_evict_LRU 的计算、E_evict_LFU 的近似值、以及 ΔH_max 中 (P_head - P_tail) 的具体定义与计算方式。三者逻辑独立，无重复或矛盾，且共同构成了对父节点数学描述的完整分解。）
