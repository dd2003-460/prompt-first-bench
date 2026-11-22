# N46: 基于修正后的 KV Cache (N43) 和精确权重体积 (N39/N40/N41)，重新计算满足 32K 上下文的最小单卡显存阈值：BF16 下，Weigh

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

基于修正后的 KV Cache (N43) 和精确权重体积 (N39/N40/N41)，重新计算满足 32K 上下文的最小单卡显存阈值：BF16 下，Weight (~54GB) + KV_Cache (~8GB) + Activation (~3GB) + Overhead (~1GB) ≈ 66GB；INT8 下，Weight (~27GB) + KV_Cache (~4GB) + Activation (~3GB) + Overhead (~1GB) ≈ 35GB。此阈值显著低于 N8 中基于 MHA 假设的 192GB/96GB，意味着 RTX 4090 (24GB) 在 INT8 下仍可能不足，但 A100 40GB 或 L40S 48GB 可能成为可行选项。

## Corrected Claim

基于修正后的 KV Cache (N43) 和精确权重体积 (N39/N40/N41)，重新计算满足 32K 上下文的最小单卡显存阈值：BF16 下，Weight (~54GB) + KV_Cache (~8GB) + Activation (~3GB) + Overhead (~1GB) ≈ 66GB；INT8 下，Weight (~27GB) + KV_Cache (~4GB) + Activation (~3GB) + Overhead (~1GB) ≈ 35GB。此阈值显著低于 N8 中基于 MHA 假设的 192GB/96GB，意味着 RTX 4090 (24GB) 在 INT8 下仍可能不足，但 A100 40GB 或 L40S 48GB 可能成为可行选项。

## Evidence

父节点级核验未通过：不完备（子节点分别针对 KV Cache 精度和 Activation 随 Batch Size 的变化，二者正交且无冗余。但父节点明确包含 Weight 和 Overhead 两个关键分量，子节点未覆盖 Weight 量化精度对体积的验证（如 N39-N41 的准确性）以及 Overhead 的具体构成，导致对父节点中'重新计算阈值'这一核心逻辑的支撑不完整。）

## Search Query

minimum VRAM requirement LLM inference GQA KV cache weight size
