# N356: 实测高于理论值的原因归因与验证：若实测达到 25-35 tokens/s，则必须采用 FP8/INT8 量化 (Weights ~27GB/13.5GB) 且 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

实测高于理论值的原因归因与验证：若实测达到 25-35 tokens/s，则必须采用 FP8/INT8 量化 (Weights ~27GB/13.5GB) 且 KV Cache 也量化；以 FP8 为例，Weights=27GB, KV Cache=4.3GB (32K, FP8)，理论上限 = 819.2 * 0.8 / (27 + 4.3) ≈ 21.0 tokens/s (效率系数提升至 0.8 因数据量减半减少总线争用)，仍低于 25 tokens/s，剩余差距归因于 Apple 内存控制器的突发读取优化或特定框架 (如 llama.cpp) 的缓存行对齐优化 [待核验: 需引用具体实测日志]。

## Corrected Claim

若实测达到 25-35 tokens/s，推测采用了 FP8/INT8 量化。以 FP8 为例，理论上限约为 21.0 tokens/s（基于 819.2 GB/s 带宽、0.8 效率系数及 31.3GB 总内存占用估算），剩余差距可能归因于内存控制器优化或框架层面的缓存对齐优化，但具体数值需实测验证。

## Evidence

[质询]该陈述包含具体的经验性参数（如效率系数0.8、KV Cache具体大小4.3GB、特定框架优化效果），这些无法从第一性原理严格推导，且缺乏实测日志或权威来源支持，属于未经验证的工程估算。 | 逻辑推导过程自洽（819.2 * 0.8 / 31.3 ≈ 21.0），但作为经验事实（source=knowledge），缺乏具体实测数据或外部来源直接支持其归因结论，故降级。

## Search Query

llama.cpp Apple M3 Ultra FP8 inference speed optimization memory bandwidth
