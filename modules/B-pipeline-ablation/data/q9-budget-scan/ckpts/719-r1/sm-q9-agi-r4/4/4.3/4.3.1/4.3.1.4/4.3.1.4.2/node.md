# N626: CUDA Context 初始化与 Driver 加载耗时 T_cuda_init 在冷启动（无缓存）下约为 30-60s，主要消耗在 cuInit 与 cuD

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N223

## Claim

CUDA Context 初始化与 Driver 加载耗时 T_cuda_init 在冷启动（无缓存）下约为 30-60s，主要消耗在 cuInit 与 cuDevicePrimaryCtxRetain 调用；若操作系统保留 CUDA 驱动句柄（如通过 systemd 预加载），二次启动耗时可降至 5-10s，需区分冷/热启动场景分别建模。

## Corrected Claim

CUDA Context 初始化与 Driver 加载耗时 T_cuda_init 在冷启动下通常为秒级（具体数值依系统环境而异，可能在 1-10s 范围，极端情况更长），主要消耗在 cuInit 与 cuDevicePrimaryCtxRetain 调用；若操作系统保留 CUDA 驱动句柄，二次启动耗时显著降低。需区分冷/热启动场景分别建模。

## Evidence

[质询]数值量级存疑：CUDA 驱动初始化（cuInit）通常耗时在毫秒到秒级（取决于驱动版本和硬件），30-60s 的冷启动耗时极长，可能混淆了‘驱动加载’与‘完整应用启动/模型加载’的时间，或者特定于极端老旧/复杂环境，缺乏普遍性数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且 30-60s 的初始化耗时远超常规认知，无法从第一性原理推出具体数值）

## Search Query

CUDA context initialization cold start latency cuInit benchmark V100
