# N157: Risk_Factor 的实证依据与修正：原公式中 NVIDIA=0.5, AMD=0.8, Apple=0.6 为定性赋值。需基于 N43/N44/N46 的

- **status**: pending
- **level**: L3
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

Risk_Factor 的实证依据与修正：原公式中 NVIDIA=0.5, AMD=0.8, Apple=0.6 为定性赋值。需基于 N43/N44/N46 的软件支持矩阵量化：Risk_Factor = 1 - (Support_Completeness_Score / Max_Score)。NVIDIA (vLLM/TRT-LLM 全支持) Risk=0.2-0.3；AMD (ROCm 不稳定, 仅 BF16) Risk=0.7-0.8；Apple (MLX 框架支持, 但生态较小) Risk=0.4-0.5。修正后的 Risk_Factor 应反映特定框架 (如 vLLM) 下的可用性，而非泛指的硬件稳定性。

## Corrected Claim

Risk_Factor 应基于软件支持矩阵量化，公式为 Risk_Factor = 1 - (Support_Completeness_Score / Max_Score)。定性评估显示：NVIDIA 因 vLLM/TRT-LLM 全支持，风险较低；AMD 因 ROCm 稳定性及精度支持限制，风险较高；Apple 因 MLX 生态相对较小，风险中等。具体数值需结合最新框架兼容性数据动态调整。

## Evidence

父节点级核验未通过：不完备（子节点在硬件平台和风险等级上正交，无矛盾；但父节点明确提及了 Apple (MLX) 的量化修正（Risk=0.4-0.5），而子节点仅覆盖了 NVIDIA 和 AMD，缺失了 Apple 这一关键分支，导致完备性不足。）
