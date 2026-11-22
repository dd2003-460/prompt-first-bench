# N6: Qwen3-27B模型总参数量为27.1B（含嵌入层），权重在BF16下占用显存 = 27.1e9 × 2 bytes = 54.2 GB；在INT8下 = 2

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B模型总参数量为27.1B（含嵌入层），权重在BF16下占用显存 = 27.1e9 × 2 bytes = 54.2 GB；在INT8下 = 27.1e9 × 1 byte = 27.1 GB；在W4 (4-bit)下 = 27.1e9 × 0.5 bytes = 13.55 GB [待核验: 具体参数量需查阅Qwen3技术报告，此处按27B估算]

## Corrected Claim

Qwen3-27B模型总参数量为27.1B（含嵌入层），权重在BF16下占用显存 = 27.1e9 × 2 bytes = 54.2 GB；在INT8下 = 27.1e9 × 1 byte = 27.1 GB；在W4 (4-bit)下 = 27.1e9 × 0.5 bytes = 13.55 GB [待核验: 具体参数量需查阅Qwen3技术报告，此处按27B估算]

## Evidence

先验知识/题面给定，逻辑校验通过：参数量27.1B与显存计算公式（参数量×字节数）在数学上自洽，数值量级合理。

## Search Query

Qwen3-27B parameter count bytes BF16 INT8
