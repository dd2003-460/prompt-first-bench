# N224: AMD RX 7900 XTX (24GB GDDR6) 运行 Qwen3-27B BF16 (54GB) 显存不足，必须量化至 INT8 (27GB) 或 W

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

AMD RX 7900 XTX (24GB GDDR6) 运行 Qwen3-27B BF16 (54GB) 显存不足，必须量化至 INT8 (27GB) 或 W4 (13.5GB)；其 RDNA 3 架构对 INT8 矩阵加速支持有限，实测 INT8 吞吐量约为 NVIDIA 同级卡 (RTX 4090) 的 50-70%，具体数值需查阅 ROCm 社区 benchmark 或 llama.cpp 在 RX 7900 XTX 上的实测数据。

## Corrected Claim

AMD RX 7900 XTX (24GB GDDR6) 运行 Qwen3-27B BF16 (54GB) 显存不足，必须量化至INT8或W4以适配显存；其RDNA 3架构对INT8矩阵加速支持有限，实测INT8吞吐量通常显著低于NVIDIA同级卡 (RTX 4090)，具体性能差距需查阅ROCm社区benchmark或llama.cpp在RX 7900 XTX上的实测数据。

## Evidence

[质询]该陈述包含具体的经验性能数据（INT8吞吐量约为RTX 4090的50-70%）和具体的量化后显存占用数值（27GB/13.5GB），这些属于经验事实而非第一性原理可推导内容。由于检索无可用来源，无法验证这些具体数值是否准确，且不同量化方案（如GPTQ vs AWQ）和软件栈（ROCm vs llama.cpp）可能导致显著差异，存在数值偏差风险。 | 逻辑自洽：24GB显存确实无法容纳54GB的BF16模型，量化至INT8或W4是必要措施；RDNA 3架构在AI推理上确实弱于NVIDIA同级卡，50-70%的性能差距符合业界普遍认知。但作为search节点，缺乏来源直接支持具体数值，依据经验事实排除条款降级。

## Search Query

RX 7900 XTX Qwen 27B INT8 inference benchmark tokens per second ROCm
