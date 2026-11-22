# N343: 在 BF16 精度下，MI300X 剩余 109.87GB 显存中需扣除框架基础开销（CUDA Context, PyTorch Runtime, 约 2-4G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129, N130, N131

## Claim

在 BF16 精度下，MI300X 剩余 109.87GB 显存中需扣除框架基础开销（CUDA Context, PyTorch Runtime, 约 2-4GB）及 KV Cache 分页管理元数据（约 1-2GB），实际可用于并发 KV Cache 的净余量约为 103-106GB，这将最大并发 Batch Size 从理论值 4 下调至保守估计 3-4。

## Corrected Claim

在 BF16 精度下，MI300X 剩余 109.87GB 显存中需扣除框架基础开销（CUDA Context, PyTorch Runtime, 约 2-4GB）及 KV Cache 分页管理元数据（约 1-2GB），实际可用于并发 KV Cache 的净余量约为 103-106GB，这将最大并发 Batch Size 从理论值 4 下调至保守估计 3-4。

## Evidence

先验知识/题面给定，逻辑校验通过：109.87GB 减去 3-6GB 开销得到 103-106GB 净余量，算术正确；Batch Size 从 4 下调至 3-4 符合显存减少后的保守估计逻辑。
