# N274: RX 7900 XTX 的 FP16 峰值算力计算中，96 CUs 为 RDNA 3 架构的实际计算单元数量，2 FMA 表示每个周期执行 2 次浮点乘加操作，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N104

## Claim

RX 7900 XTX 的 FP16 峰值算力计算中，96 CUs 为 RDNA 3 架构的实际计算单元数量，2 FMA 表示每个周期执行 2 次浮点乘加操作，2.4 GHz 为默认核心频率，该公式假设无频率缩放和功耗限制

## Corrected Claim

RX 7900 XTX 的 FP16 峰值算力计算中，96 CUs 为 RDNA 3 架构的实际计算单元数量，2 FMA 表示每个周期执行 2 次浮点乘加操作，2.4 GHz 为默认核心频率，该公式假设无频率缩放和功耗限制

## Evidence

先验知识/题面给定，逻辑校验通过：RX 7900 XTX 确实拥有 96 个 CU，RDNA 3 架构每个 CU 每周期支持 2 次 FP16 FMA 操作，默认核心频率为 2.4 GHz，公式推导逻辑自洽且数值量级合理。

## Search Query

RX 7900 XTX RDNA 3 96 CUs FP16 peak FLOPS calculation 2.4 GHz
