# N190: Qwen3-27B 在 A100 80GB 上运行 BF16 精度时的实际 Prefill 速度 (tokens/s) 约为 1500-2500 tokens/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Qwen3-27B 在 A100 80GB 上运行 BF16 精度时的实际 Prefill 速度 (tokens/s) 约为 1500-2500 tokens/s (取决于 Batch Size)，Decode 速度约为 20-30 tokens/s (受限于 2039 GB/s 带宽但受计算限制)，该速度是评估无量化质量损失方案性能基线的关键参数

## Corrected Claim

Qwen3-27B 在 A100 80GB 上运行 BF16 精度时，Prefill 和 Decode 速度受 Batch Size、序列长度及硬件利用率影响显著，具体数值需根据实际部署配置测量，通常 Prefill 速度在数百至数千 tokens/s 之间，Decode 速度在数十 tokens/s 左右，该速度是评估无量化质量损失方案性能基线的关键参数。

## Evidence

[质询]数值量级存疑：Qwen3-27B 在 A100 80GB 上 BF16 运行，Prefill 速度 1500-2500 tokens/s 对于单卡而言偏高（通常受限于计算或内存带宽，且 27B 模型较大），Decode 速度 20-30 tokens/s 也需结合具体 Batch Size 和硬件利用率评估，缺乏具体配置细节（如 Batch Size、序列长度）导致数值范围过宽且缺乏精确依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于硬件性能经验数据，不适用第一性原理推导）

## Search Query

A100 80GB Qwen3-27B BF16 vLLM prefill decode throughput benchmark
