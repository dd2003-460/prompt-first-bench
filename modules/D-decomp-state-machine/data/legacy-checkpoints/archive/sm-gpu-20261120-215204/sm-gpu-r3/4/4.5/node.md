# N26: Token生成速度（Tokens/s）受限于显存带宽而非计算能力，计算公式为 Tokens/s ≈ 显存带宽(GB/s) / 每Token读取权重字节数；例如R

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Token生成速度（Tokens/s）受限于显存带宽而非计算能力，计算公式为 Tokens/s ≈ 显存带宽(GB/s) / 每Token读取权重字节数；例如RTX 4090（1008 GB/s）运行BF16 Qwen3-27B时，理论峰值约为18.8 Tokens/s（1008/54）。

## Corrected Claim

Token生成速度（Tokens/s）受限于显存带宽而非计算能力，计算公式为 Tokens/s ≈ 显存带宽(GB/s) / 每Token读取权重字节数；例如RTX 4090（1008 GB/s）运行BF16 Qwen3-27B时，理论峰值约为18.8 Tokens/s（1008/54）。

## Evidence

父节点级核验未通过：不完备（子节点在内容上互不重叠（正交性良好），且未出现简单的参数重复（无冗余）。但完备性不足：父节点核心是‘带宽受限’的原理与基础公式，子节点1和3仅提供了特定硬件/量化下的计算实例，子节点2提供了修正公式，但缺失了‘为何是带宽瓶颈’的底层原理（如算术强度/计算-访存比分析）以及‘每Token读取权重字节数’这一核心变量的通用定义与推导逻辑，导致无法独立复现父节点中的基础计算逻辑。）
