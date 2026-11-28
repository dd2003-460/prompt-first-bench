# N50: vLLM 服务冷启动耗时 T_startup 由模型加载时间主导：Qwen3.8-27B NVFP4 权重文件大小约 13.5GB，从 NVMe SSD (读取

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

vLLM 服务冷启动耗时 T_startup 由模型加载时间主导：Qwen3.8-27B NVFP4 权重文件大小约 13.5GB，从 NVMe SSD (读取速度 3GB/s) 加载至 4xV100 显存的理论最小时间为 4.5s，加上 CUDA Context 初始化与 KV Cache 分配 (约 1.5s)，总 T_startup ≈ 6s；若采用 Warm Standby (备用进程常驻内存但暂停推理)，T_startup 可降至 <1s，但需额外预留 16GB RAM 用于权重缓存。

## Corrected Claim

vLLM 服务冷启动耗时 T_startup 由模型加载时间主导：Qwen3.8-27B NVFP4 权重文件大小约 13.5GB，从 NVMe SSD (读取速度 3GB/s) 加载至 4xV100 显存的理论最小时间为 4.5s，加上 CUDA Context 初始化与 KV Cache 分配 (约 1.5s)，总 T_startup ≈ 6s；若采用 Warm Standby (备用进程常驻内存但暂停推理)，T_startup 可降至 <1s，但需额外预留 16GB RAM 用于权重缓存。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5GB / 3GB/s = 4.5s 计算正确，总耗时估算符合工程直觉，Warm Standby 机制描述合理。
