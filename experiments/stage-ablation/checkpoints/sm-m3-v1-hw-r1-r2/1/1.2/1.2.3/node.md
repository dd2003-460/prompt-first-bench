# N36: 随着上下文长度 S 增加，KV Cache 读取带宽占比从 S=4k 时的 ~10% 上升至 S=262k 时的 ~45%，导致单 Token 生成时间 T_g

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

随着上下文长度 S 增加，KV Cache 读取带宽占比从 S=4k 时的 ~10% 上升至 S=262k 时的 ~45%，导致单 Token 生成时间 T_gen 从 0.05s 线性增长至 0.12s；当 S > 100k 时，Memory-Bound 特征显著增强，此时增加 max-num-seqs 反而因 KV 竞争降低单序列吞吐。

## Corrected Claim

随着上下文长度 S 增加，KV Cache 读取带宽占比显著上升，导致单 Token 生成时间 T_gen 增加；当 S 超过一定阈值（如 100k）时，Memory-Bound 特征显著增强，此时增加 max-num-seqs 可能因 KV 竞争降低单序列吞吐。

## Evidence

[质询]陈述中关于KV Cache带宽占比的具体数值（~10%到~45%）以及T_gen的具体线性增长区间（0.05s到0.12s）属于高度依赖硬件架构、模型规模及实现细节的经验数据，缺乏通用性；此外，'线性增长'这一描述在长上下文场景下往往过于简化，实际性能曲线通常受内存层级和计算瓶颈转换影响，并非严格线性。 | 先验知识/题面给定，逻辑校验通过：随着S增加，KV Cache体积增大，读取带宽需求上升，Memory-Bound特征增强符合LLM推理的基本物理直觉；但具体数值缺乏来源支持，故降级。

## Search Query

long context inference latency kv cache bandwidth bound scaling behavior
