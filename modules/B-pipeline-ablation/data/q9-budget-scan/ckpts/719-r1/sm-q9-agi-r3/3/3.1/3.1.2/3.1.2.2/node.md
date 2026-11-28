# N175: Decode 阶段 Memory-Bound 特性验证：在 TP=4 配置下，每 GPU 负责 1/4 的权重，即 ~13.5GB (FP4) 或 ~27GB 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Decode 阶段 Memory-Bound 特性验证：在 TP=4 配置下，每 GPU 负责 1/4 的权重，即 ~13.5GB (FP4) 或 ~27GB (FP16)。若使用 FP16，单 GPU 读取 27GB 权重需 27GB / 900GB/s ≈ 30ms。由于 V100 显存带宽 900GB/s 是共享总线还是独享需确认，若独享，则 4 卡并行读取互不干扰，总时间仍为 30ms，对应 33.3 Tokens/s 理论上限，但实际受 Kernel 调度延迟 (Launch Latency ~5-10ms) 影响，有效上限降至 20-25 Tokens/s [待核验]

## Corrected Claim

Decode 阶段为 Memory-Bound。在 TP=4 且 FP16 精度下，若假设 V100 有效带宽接近 900GB/s 且忽略 Kernel 调度开销，理论上限约为 33.3 Tokens/s；考虑实际带宽损耗及调度延迟，有效上限预计显著低于理论值，具体数值需实测确认。

## Evidence

[质询]V100 显存带宽标称值为 900 GB/s，但实际有效带宽通常低于此值（约 80-90%），且 Kernel Launch Latency 在 5-10ms 量级对于现代 CUDA 环境而言偏高（通常微秒级，除非涉及复杂同步或 CPU-GPU 交互），导致 20-25 Tokens/s 的估算缺乏精确实证支持，属于粗略的经验性推断。 | 来源 [1] 仅定性支持 Decode 阶段为 Memory-Bound，未提供 V100 具体带宽数值或 TP=4 下的具体延迟计算，属于间接支持；具体数值（900GB/s, 30ms, 20-25 tps）为经验事实，逻辑自洽但缺直接来源支持。

## Search Query

V100 SXM2 HBM bandwidth per card shared vs exclusive kernel launch latency impact on LLM decode speed

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2106890270457570862&rut=9c34a9ca8bcc1497003b2d22731e2e28cd9a599ebc6cb9c73c01d356da7911ee', 'type': 'ddg', 'title': '为什么大模型 decode 阶段是 memory-bound？——从 KV cache 的算术说起 - 知乎'}
