# N23: 可复现性哈希校验：对每次生成的研究结论及其引用的代码/数据片段计算 SHA-256 哈希值，存储于版本控制系统中。建立断言：若重跑相同 Prompt+Conte

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

可复现性哈希校验：对每次生成的研究结论及其引用的代码/数据片段计算 SHA-256 哈希值，存储于版本控制系统中。建立断言：若重跑相同 Prompt+Context 产生的哈希值偏差 > 0，则判定为不可复现。在 vLLM 非确定性内核（CUDA non-determinism）存在的情况下，需设置 `--enforce-eager` 或固定种子 `seed=42` 以将随机性方差控制在 $\sigma^2 < 10^{-6}$ 范围内。

## Corrected Claim

可复现性哈希校验：对每次生成的研究结论及其引用的代码/数据片段计算 SHA-256 哈希值，存储于版本控制系统中。建立断言：若重跑相同 Prompt+Context 产生的哈希值偏差 > 0，则判定为不可复现。在 vLLM 非确定性内核（CUDA non-determinism）存在的情况下，需设置 --enforce-eager 或固定种子 seed=42 以降低随机性影响。

## Evidence

[质询]声称通过设置 --enforce-eager 或 seed=42 能将随机性方差控制在 σ² < 10⁻⁶ 这一具体数值阈值缺乏普遍成立的理论或实证支持，属于过度精确的经验断言。 | 先验知识/题面给定，逻辑校验通过，但具体方差阈值缺乏来源支持

## Search Query

vLLM deterministic inference reproducibility hash check
