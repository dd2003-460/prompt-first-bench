# N249: FP8 KV Cache 在 V100 (Compute Cap 7.0) 上并非原生硬件加速，vLLM 需在 CPU/GPU 间进行 FP8<->FP16 转

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97

## Claim

FP8 KV Cache 在 V100 (Compute Cap 7.0) 上并非原生硬件加速，vLLM 需在 CPU/GPU 间进行 FP8<->FP16 转换或仅用于存储，若启用 FP8 需额外 5-10% 的带宽开销用于反量化，实际有效吞吐下降约 5-10%，等效于 Bytes_per_token 在时间维度上增加 5-10%。

## Corrected Claim

FP8 KV Cache 在 V100 (Compute Cap 7.0) 上并非原生硬件加速，vLLM 需在 CPU/GPU 间进行 FP8<->FP16 转换或仅用于存储。由于 V100 缺乏 FP8 计算单元，启用 FP8 存储会增加反量化带来的额外带宽和计算开销，导致实际有效吞吐相比原生 FP16 有所下降，具体降幅取决于模型结构和序列长度，通常表现为等效 Bytes_per_token 处理时间的增加。

## Evidence

[质询]具体数值（5-10% 带宽开销及吞吐下降）缺乏通用基准测试支持，不同模型架构和序列长度下差异巨大，且 V100 不支持 FP8 计算单元，主要瓶颈在于内存带宽而非计算，反量化开销占比取决于具体实现细节，不能一概而论为固定百分比。 | 先验知识/题面给定，逻辑校验通过：V100 (CC 7.0) 确实不支持 FP8 硬件加速，FP8 仅作为存储格式，需反量化为 FP16/BF16 进行计算，这必然引入额外的内存读写和转换开销，导致有效吞吐下降。但具体 5-10% 的数值属于经验估计，缺乏统一标准，故降级为定性描述。
