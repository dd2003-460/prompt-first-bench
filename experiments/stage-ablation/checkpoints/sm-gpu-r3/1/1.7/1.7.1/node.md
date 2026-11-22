# N92: Qwen3-27B 在 FP8 (E4M3) 精度下的权重文件大小为 27 GB (27B * 1 byte)，相比 BF16 (54 GB) 节省 50% 权

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重文件大小为 27 GB (27B * 1 byte)，相比 BF16 (54 GB) 节省 50% 权重显存，但需注意 KV Cache 若保持 BF16 则总显存节省比例低于 50%。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重文件大小为 27 GB (27B * 1 byte)，相比 BF16 (54 GB) 节省 50% 权重显存，但需注意 KV Cache 若保持 BF16 则总显存节省比例低于 50%。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1专注于权重文件的大小及量化细节，子节点2专注于KV Cache的计算公式及不同精度下的大小。两者分别处理模型显存占用的两个主要组成部分（权重 vs. 激活/KV Cache），内容互不重叠且无矛盾，共同完整覆盖了父节点关于权重节省和KV Cache影响的论述。）
