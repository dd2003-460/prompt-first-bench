# N117: 修正后的LFU增益公式应基于字节命中率而非请求命中率：ΔH_bytes_corrected = [Σ_{i=1}^{K} q_i s_i / Σ q_i s_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

修正后的LFU增益公式应基于字节命中率而非请求命中率：ΔH_bytes_corrected = [Σ_{i=1}^{K} q_i s_i / Σ q_i s_i]_LFU - [Σ_{i∈LRU} q_i s_i / Σ q_i s_i]_LRU，其中K为缓存容量对应的对象数，需区分请求命中率与字节命中率的差异。

## Corrected Claim

修正后的LFU增益公式应基于字节命中率而非请求命中率：ΔH_bytes_corrected = [Σ_{i=1}^{K} q_i s_i / Σ q_i s_i]_LFU - [Σ_{i∈LRU} q_i s_i / Σ q_i s_i]_LRU，其中K为缓存容量对应的对象数，需区分请求命中率与字节命中率的差异。

## Evidence

先验知识/题面给定，逻辑校验通过
