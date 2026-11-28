# N42: MTP×4 投机解码在 V100 上的实际加速比受限于 Draft 模型的生成速度与 Target 模型的验证速度耦合；假设 Draft 模型为 7B 级别，其

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

MTP×4 投机解码在 V100 上的实际加速比受限于 Draft 模型的生成速度与 Target 模型的验证速度耦合；假设 Draft 模型为 7B 级别，其在 V100 上的生成速度约为 100-150 tokens/s，而 Target 27B 验证 4 个候选 token 的计算量相当于 4 次 Prefill (短序列)，耗时约为 4 * (27GB/3600GB/s) ≈ 30 ms；若接受率 α=0.7，有效生成速度 Speed_eff = (1 + 3α) * V_target / (1 + T_draft_overhead)，其中 V_target 为基础 Decode 速度，计算得 Speed_eff ≈ 3.1 * 40 tokens/s / 1.2 ≈ 103 tokens/s，相比基线 40 tokens/s 提升约 2.5x。

## Corrected Claim

MTP×4 投机解码在 V100 上的实际加速比受限于 Draft 模型生成速度与 Target 模型验证速度的耦合。由于 27B 模型无法在单张 V100 上以 FP16 运行，且 V100 内存带宽远低于 3600GB/s，原陈述中的具体耗时和加速比计算基于错误的硬件假设。在正确的多卡或量化部署下，加速比取决于具体的接受率和硬件配置，通常低于理想理论值。

## Evidence

[质询]Target 27B 模型在 V100 上的显存占用远超单卡容量（27B FP16 需约 54GB，V100 最大 32GB），且 3600GB/s 带宽对应的是 H100/A100 级别而非 V100（~900GB/s），导致基于此硬件参数的计算前提存在严重事实错误；此外，MTP 加速比公式及具体数值缺乏通用理论支持，属于特定实验条件下的经验估算。 | source=knowledge，但陈述中引用的硬件参数（V100 带宽 3600GB/s、27B 模型单卡运行）与已知硬件规格矛盾，逻辑校验未通过，且无外部来源支持该特定加速比数值。
