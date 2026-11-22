# N97: RTX 4090 单卡推理 Qwen3-27B (W4) 的功耗修正：满载功耗并非恒定 450W，而是随 batch size 和序列长度变化；在 32K 长上

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

RTX 4090 单卡推理 Qwen3-27B (W4) 的功耗修正：满载功耗并非恒定 450W，而是随 batch size 和序列长度变化；在 32K 长上下文推理场景下，显存读取主导，功耗可能降至 350-400W，导致原 TCO 计算中的电力成本高估 10-15%。

## Corrected Claim

RTX 4090 单卡推理 Qwen3-27B (W4) 的功耗并非恒定 450W，而是随负载变化；在 32K 长上下文推理场景下，由于显存读取主导，功耗可能低于峰值，导致原 TCO 计算中的电力成本存在高估风险。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了高算力负载（Prefill）、显存瓶颈负载（Decode）以及两者混合后的加权平均模型，逻辑上互斥且共同构成了完整的功耗修正闭环。工作点C是基于A和B推导出的综合结论，而非简单的参数重复，因此不构成冗余。）

## Search Query

RTX 4090 LLM inference power consumption 32k context batch size watts
