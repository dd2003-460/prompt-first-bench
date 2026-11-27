# N169: Qwen3-27B 在 BF16 精度下 32K 上下文的 KV Cache 显存占用计算结果为 10.74 GB，计算过程为 2 × 64 (layers) 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N42, N43, N50

## Claim

Qwen3-27B 在 BF16 精度下 32K 上下文的 KV Cache 显存占用计算结果为 10.74 GB，计算过程为 2 × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 32768 (tokens) × 2 (bytes) = 8,589,934,592 bytes ≈ 8.00 GiB (注意：此处需区分 GB 与 GiB，若按 1GB=10^9 bytes 则为 8.59 GB，若按 1GiB=2^30 bytes 则为 8.00 GiB；根据 N109 已验证事实 10.74 GB，需核实 N109 的计算口径或参数是否有误，此处以 N109 的 10.74 GB 为基准进行一致性校验，若 N109 正确则需重新检查 N147-N149 参数或 N109 公式系数)。[待核验：N109 与 N147-N149 参数推导结果的一致性]。

## Corrected Claim

Qwen3-27B 在 BF16 精度下 32K 上下文的 KV Cache 显存占用，若按 64 层、8 KV heads、128 head_dim 计算，约为 8.59 GB (8.00 GiB)；若实际占用为 10.74 GB，则需核实模型具体参数（如层数、head 数）或计算口径是否包含额外开销。

## Evidence

[质询]陈述内部存在严重的数值矛盾：根据提供的参数（2×64×8×128×32768×2）计算出的字节数为 8,589,934,592 bytes，换算后约为 8.59 GB 或 8.00 GiB，这与陈述开头声称的“10.74 GB”结果直接冲突。虽然陈述试图通过“以 N109 为基准”来调和，但作为事实节点，其核心数值（10.74 GB）与展示的计算过程（得出 ~8.6 GB）不一致，且未提供 N109 的具体参数以证明 10.74 GB 的正确性，导致该节点无法自洽地确立 10.74 GB 这一事实。 | 逻辑校验失败：陈述中给出的计算公式结果（~8.59 GB）与声称的最终结果（10.74 GB）不符，且缺乏外部来源或 N109 的具体数据来解释这一差异（如是否包含其他组件或参数不同），导致事实无法验证。

## Search Query

Qwen3-27B KV cache size 32k BF16 calculation verification
