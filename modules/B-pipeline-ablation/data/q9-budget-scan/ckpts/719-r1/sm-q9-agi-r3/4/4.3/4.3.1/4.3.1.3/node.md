# N222: Recovery Time 中容器重启耗时取决于镜像拉取策略：若镜像已本地缓存（Docker layer cache），vLLM 容器（含 CUDA runti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

Recovery Time 中容器重启耗时取决于镜像拉取策略：若镜像已本地缓存（Docker layer cache），vLLM 容器（含 CUDA runtime 初始化）冷启动耗时约 8-12s；若需从 registry 拉取 3.2GB 镜像，在 1GbE 网络下下载耗时约 32s + 解压 5s，总计约 37-50s，远小于 15min 预算

## Corrected Claim

Recovery Time 中容器重启耗时取决于镜像拉取策略：若镜像已本地缓存（Docker layer cache），vLLM 容器（含 CUDA runtime 初始化）冷启动耗时约 8-12s；若需从 registry 拉取 3.2GB 镜像，在 1GbE 网络下下载耗时约 32s + 解压 5s，总计约 37-50s，远小于 15min 预算

## Evidence

先验知识/题面给定，逻辑校验通过：1GbE理论带宽125MB/s，3.2GB镜像下载耗时约25.6s，加上解压及网络开销估算为32s+5s符合工程常识；容器冷启动8-12s亦在合理范围内，总耗时远低于15分钟预算，逻辑自洽。
