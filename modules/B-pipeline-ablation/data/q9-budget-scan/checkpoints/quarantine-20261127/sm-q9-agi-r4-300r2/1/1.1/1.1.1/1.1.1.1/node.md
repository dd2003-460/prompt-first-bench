# N92: CUDA Context 基础显存开销分解：在 V100-SXM2-16GB 上，CUDA Driver Context 占用约 0.8-1.0 GB，cuBL

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

CUDA Context 基础显存开销分解：在 V100-SXM2-16GB 上，CUDA Driver Context 占用约 0.8-1.0 GB，cuBLAS/cuDNN 工作空间缓存占用约 0.5-0.8 GB，两者之和构成 1.5-2.0 GB 的总开销基底。

## Corrected Claim

CUDA Context 基础显存开销分解：在 V100-SXM2-16GB 上，CUDA Driver Context 占用约 0.8-1.0 GB，cuBLAS/cuDNN 工作空间缓存占用约 0.5-0.8 GB，两者之和构成 1.5-2.0 GB 的总开销基底。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 逻辑矛盾/不正交：父节点定义CUDA Context+cuBLAS/cuDNN开销为1.5-2.0GB，但所有子节点均使用固定的'1.8GB'，未体现区间变化或区分Context与库缓存。2. 严重冗余：三个子节点本质上是同一配置（TP=4, N220模型）在不同 max_num_seqs 下的计算结果，属于参数扫描而非独立概念分解。3. 不完备：父节点强调'基础显存开销分解'，但子节点引入了大量非基础开销（模型权重、KV Cache、Block Manager），偏离了父节点定义的'基底'范畴，且未单独解释cuBLAS/cuDNN缓存的具体分配。）

## Search Query

V100 CUDA context memory overhead cuBLAS workspace size GB
