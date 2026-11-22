# N74: Belady's Anomaly 在字节级缓存中的修正项：当对象大小不等时，LRU 的字节命中率可能随缓存增加而下降，修正公式为 H_corrected = H

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Belady's Anomaly 在字节级缓存中的修正项：当对象大小不等时，LRU 的字节命中率可能随缓存增加而下降，修正公式为 H_corrected = H_LRU - Δ_Belady，其中 Δ_Belady 由大小-热度负相关系数 ρ 决定。

## Corrected Claim

Belady's Anomaly 主要出现在非栈性质缓存替换算法（如 FIFO）中，表现为增加缓存容量反而导致命中率下降。LRU 算法具有栈性质，其命中率随缓存容量增加单调不减，不存在 Belady 异常。对于对象大小不等的场景，需考虑字节命中率与对象请求命中率的差异，但不能简单用基于 ρ 的修正公式描述 LRU 的行为。

## Evidence

[质询]Belady's Anomaly 通常指页面置换算法中，增加缓存页框数导致缺页率上升的现象，其发生与具体算法（如 FIFO）和访问序列有关，并非由‘大小-热度负相关系数 ρ’直接决定的通用修正项。该陈述将 Belady 异常简化为一个由单一统计系数 ρ 决定的确定性修正公式 H_corrected = H_LRU - Δ_Belady，缺乏理论依据，且 LRU 本身在标准定义下不表现出 Belady 异常（LRU 是包含栈性质的算法，命中率随缓存增加单调不减）。 | 先验知识/题面给定，逻辑校验未通过：LRU 算法具有栈性质（Stack Property），其命中率随缓存容量增加是单调不减的，不存在 Belady 异常。Belady 异常主要出现在非栈性质算法（如 FIFO）中。此外，将异常量化为与大小-热度相关系数 ρ 的简单线性修正项缺乏理论支持。

## Search Query

Belady anomaly variable size objects cache
