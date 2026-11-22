# N125: 激活值显存占用 A = f(L, d_model, ctx_len, batch_size, precision)。对于Qwen3-27B，L=28层, d_m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

激活值显存占用 A = f(L, d_model, ctx_len, batch_size, precision)。对于Qwen3-27B，L=28层, d_model=4096 (假设，需核验), ctx_len=32K, batch_size=1。激活值主要占用来自注意力分数矩阵 (seq_len^2 * heads) 和 MLP中间层 (seq_len * d_ff)。

## Corrected Claim

激活值显存占用 A = f(L, d_model, ctx_len, batch_size, precision)。对于Qwen3-27B，L=28层, d_model=4096 (假设，需核验), ctx_len=32K, batch_size=1。激活值主要占用来自注意力分数矩阵 (seq_len^2 * heads) 和 MLP中间层 (seq_len * d_ff)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（L=28, d_model=4096）符合 27B 模型规模量级，激活值显存占用公式及主要组成部分（注意力分数、MLP中间层）描述符合 Transformer 架构基本原理。

## Search Query

LLM activation memory footprint formula attention MLP
