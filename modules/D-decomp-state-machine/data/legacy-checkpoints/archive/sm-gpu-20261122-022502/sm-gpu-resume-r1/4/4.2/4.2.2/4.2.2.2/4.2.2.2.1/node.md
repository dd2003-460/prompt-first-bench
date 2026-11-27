# N806: 在 2x RTX 4090 (PCIe 4.0 x16) 上运行 Qwen3-27B FP8 时，Decode 阶段每生成 1 token 需传输的激活值总量为

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N251, N252, N253

## Claim

在 2x RTX 4090 (PCIe 4.0 x16) 上运行 Qwen3-27B FP8 时，Decode 阶段每生成 1 token 需传输的激活值总量为 27B params × 1 byte (FP8) = 27 GB（假设全量权重参与每步计算且无缓存复用），而非 N251 中隐含的 471.6ms 对应的 30GB 数据量，需修正通信数据量模型。

## Corrected Claim

在 2x RTX 4090 (PCIe 4.0 x16) 上运行 Qwen3-27B FP8 时，Decode 阶段每生成 1 token 需传输的激活值总量为 27B params × 1 byte (FP8) = 27 GB（假设全量权重参与每步计算且无缓存复用），而非 N251 中隐含的 471.6ms 对应的 30GB 数据量，需修正通信数据量模型。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8精度下每字节1字节，总权重体积确为27GB，且Decode阶段每步需读取全量权重，计算自洽。
