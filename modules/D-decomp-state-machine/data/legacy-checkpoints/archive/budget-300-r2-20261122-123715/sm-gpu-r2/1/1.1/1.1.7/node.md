# N34: AMD RX 7900 XTX 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

AMD RX 7900 XTX 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 24GB 物理显存，无需 Offload，但 ROCm 生态对 Qwen3-27B 的优化程度低于 CUDA，实际吞吐量可能损失 10-20%

## Corrected Claim

AMD RX 7900 XTX 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用约为 20GB，小于 24GB 物理显存，无需 Offload；ROCm 生态对 Qwen3-27B 的优化程度可能低于 CUDA，实际吞吐量可能存在一定损失，但具体幅度需实测验证。

## Evidence

[质询]KV Cache 4.5GB 的估算可能偏低或偏高取决于具体实现（如 GQA 头数、精度），且 ROCm 对 Qwen3 的优化程度及 10-20% 的性能损失属于经验性估计，缺乏官方基准数据支持，存在口径混淆风险。 | 先验知识/题面给定，逻辑校验通过：显存占用估算量级合理（27B W4 权重约 13.5GB，32K 上下文 KV Cache 约 4-5GB，总计约 20GB < 24GB），但性能损失比例为经验推测，无直接来源支持，故降级。
