# N46: Qwen3-27B 采用 GQA 架构，具体参数为：Num Heads = 32, Num KV Heads = 4, Head Dim = 128。公式中 N

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 采用 GQA 架构，具体参数为：Num Heads = 32, Num KV Heads = 4, Head Dim = 128。公式中 N_kv_heads=4 和 D_head=128 是计算 KV Cache 大小的关键架构参数。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，具体参数需参考官方技术报告或模型配置文件确认。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖但非正交冲突（子节点2和3依赖于子节点1的层数参数，且3是对2的条件扩展），这符合层级分解逻辑。然而，完备性不足：父节点明确强调“Num Heads = 32”是架构参数，但所有子节点均未提及该参数，也未说明其虽不直接参与KV Cache大小计算（取决于KV Heads），但属于父节点定义的核心架构特征之一，导致对父节点“具体参数”的覆盖不完整。）

## Search Query

Qwen3-27B GQA num_kv_heads 4 head_dim 128 config.json
