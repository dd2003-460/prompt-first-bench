# N97: 激活值缓冲 (Activation Memory) 在 BF16 精度下随批量大小 (Batch Size) 和序列长度线性增长；对于单请求 (Batch=1)

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

激活值缓冲 (Activation Memory) 在 BF16 精度下随批量大小 (Batch Size) 和序列长度线性增长；对于单请求 (Batch=1) 32K 上下文，激活值峰值约为 2-4GB (取决于层数和中间维度)，需从总显存中预留，因此 BF16 总显存需求 = 54GB (权重) + 40GB (KV Cache, 见N25) + 4GB (激活) + 2GB (运行时) ≈ 100GB。

## Corrected Claim

激活值缓冲 (Activation Memory) 在 BF16 精度下随批量大小 (Batch Size) 和序列长度线性增长；对于单请求 (Batch=1) 32K 上下文，激活值峰值约为 2-4GB (取决于层数和中间维度)，需从总显存中预留，因此 BF16 总显存需求 = 54GB (权重) + 40GB (KV Cache, 见N25) + 4GB (激活) + 2GB (运行时) ≈ 100GB。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 完备性严重缺失：父节点明确列出了四项显存组成（权重54GB + KV 40GB + 激活4GB + 运行时2GB），但子节点仅覆盖了‘激活值’和‘KV Cache’两项，完全遗漏了‘权重显存’和‘运行时显存’的关键方面。2. 正交性/逻辑矛盾：子节点2直接推翻了父节点中关于KV Cache为40GB的陈述（修正为8GB），导致子节点与父节点在核心数据上存在直接矛盾，且父节点作为结论性的总显存估算（100GB）因KV Cache计算错误而失效，子节点未能涵盖父节点中‘总显存需求’这一核心结论的正确修正版本。）

## Search Query

LLM activation memory footprint batch size 1 32k context BF16
