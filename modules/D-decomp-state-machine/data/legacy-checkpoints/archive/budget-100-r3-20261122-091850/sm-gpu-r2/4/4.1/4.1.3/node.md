# N75: 在 BF16 精度工作点下，Qwen3-27B 满足 32K 上下文的最小显存需求为 54GB (权重) + 8GB (KV Cache) + 5GB (激活/

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

在 BF16 精度工作点下，Qwen3-27B 满足 32K 上下文的最小显存需求为 54GB (权重) + 8GB (KV Cache) + 5GB (激活/开销) = 67GB；对应候选硬件为 80GB 显存 GPU (如 A100 80GB, H100 80GB, 或 MI300X 192GB, 价格约 $10,000-$25,000 [待核验])，该工作点代表最高质量保留但 CAPEX 最高，适用于对精度极其敏感且预算充足的场景。

## Corrected Claim

在 BF16 精度工作点下，Qwen3-27B 满足 32K 上下文的最小显存需求约为 67GB（权重 54GB + KV Cache 8GB + 激活 5GB）；对应候选硬件为 80GB 显存 GPU（如 A100 80GB, H100 80GB）或更大显存 GPU（如 MI300X），该工作点代表最高质量保留但 CAPEX 最高，适用于对精度极其敏感且预算充足的场景。

## Evidence

[质询]KV Cache 8GB 的估算可能偏低或偏高，取决于具体的注意力头配置和序列长度细节；此外，硬件价格区间 $10,000-$25,000 对于 A100/H100 80GB 而言，在二手或特定渠道可能成立，但在新品市场通常更高，且 MI300X 192GB 的价格通常远高于此区间，存在价格口径混淆风险。 | 先验知识/题面给定，逻辑校验通过：BF16 下 27B 模型权重约 54GB 符合 27e9 * 2 bytes 的量级；总显存 67GB 小于 80GB 硬件容量，逻辑自洽。但作为 knowledge 节点，虽逻辑自洽，但硬件价格属于波动较大的经验事实，且 MI300X 价格通常高于 $25k，存在轻微事实偏差风险，故降级为定性表述以规避具体价格错误。

## Search Query

NVIDIA A100 80GB price 2024 used new
