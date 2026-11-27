# N118: RTX 4090 在 27B 模型 INT8 推理下的典型功耗 (Watts) 与能效比 (Tokens/Watt)，需基于实测 TPS 除以 GPU 实时功耗

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33, N34

## Claim

RTX 4090 在 27B 模型 INT8 推理下的典型功耗 (Watts) 与能效比 (Tokens/Watt)，需基于实测 TPS 除以 GPU 实时功耗计算，以对比数据中心卡的能效优势。

## Corrected Claim

RTX 4090 的 TDP 为 450W。在 27B 模型 INT8 推理下，其具体功耗与能效比需实测；现有证据表明，在消费级卡上 INT8 量化未必比 FP16 更节能，能效比可能低于预期，需具体实测数据以对比数据中心卡。

## Evidence

[质询]该陈述要求提供具体的“典型功耗”和“能效比”数值，但参考来源仅提供了TDP上限（450W）和定性结论（INT8可能比FP16更耗能），缺乏针对27B模型INT8推理的实测具体数值（如具体瓦数和Tokens/Watt），且来源[2]指出INT8量化在消费级卡上能效可能反而下降，与“对比数据中心卡能效优势”的隐含前提存在潜在冲突或需更细致的条件限定。 | 来源[3]提供了RTX 4090的TDP为450W，来源[2]提供了INT8在RTX 4090上的能耗定性分析（比FP16高50%-242%），但均无27B模型INT8的具体实测能效数值，属于经验事实且缺乏直接数值支持。

## Search Query

RTX 4090 power consumption LLM inference INT8 watts per token

## Retrieval Sources

- {'url': 'https://www.spheron.network/blog/rtx-4090-for-ai-ml/&rut=afab2ec4917745b986bd63270b62dd8c8d92296b897971b83c79d6f250bb4eda', 'type': 'ddg', 'title': 'RTX 4090 for AI: 24GB VRAM, TFLOPS, Specs and Benchmarks | Spheron'}
- {'url': 'https://cloud.tencent.com/developer/article/2746949&rut=d4317ea20b1874630c91941e91018e762c6c1bceb391183cf66e2b2c970d4c13', 'type': 'ddg', 'title': '量化不一定省电：我们在 Rtx 4090 上实测了 Int8，它比 Fp16 多耗 50%-242% 的能量'}
- {'url': 'https://www.promptquorum.com/local-llms/local-llm-power-consumption&rut=84f2d0969bab3f29e38454df2d7aa4405679c75318f0d55d8f26279fd46b77d7', 'type': 'ddg', 'title': 'Local LLM Power Consumption 2026: RTX 4090 450W = $39/mo'}
