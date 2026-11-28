# N7: 4xV100-16GB集群总可用HBM容量为64GB，扣除vLLM系统开销(约2GB)及模型权重占用(NVFP4 27B约13.5GB)后，剩余用于KV Cac

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

4xV100-16GB集群总可用HBM容量为64GB，扣除vLLM系统开销(约2GB)及模型权重占用(NVFP4 27B约13.5GB)后，剩余用于KV Cache的有效内存约为48.5GB

## Corrected Claim

4xV100-16GB集群总可用HBM容量为64GB，扣除vLLM系统开销(约2GB)及模型权重占用(NVFP4 27B约13.5GB)后，剩余用于KV Cache的有效内存约为48.5GB

## Evidence

父节点级核验未通过：不完备（1. 正交性：两个子节点分别讨论'系统预留机制'和'KV Cache容量推导'，逻辑上独立且无矛盾，正交性通过。2. 完备性：父节点核心是'有效内存计算过程'，即 64GB - 2GB - 13.5GB = 48.5GB。子节点1引入了一个未在父节点中出现的变量（12.8GB Safety Margin），这与父节点给出的'2GB系统开销'数值不一致（2GB vs 12.8GB），导致逻辑断裂或事实错误；子节点2仅利用结果进行后续推演，未解释48.5GB的来源。因此，子节点未能完整且正确地覆盖父节点的'计算依据'这一关键方面。3. 冗余：无明显冗余。）
