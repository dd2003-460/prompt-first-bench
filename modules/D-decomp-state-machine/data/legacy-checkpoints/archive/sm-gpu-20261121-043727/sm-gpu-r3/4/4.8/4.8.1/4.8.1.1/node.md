# N223: NVIDIA 驱动版本与 FP8 支持的最小阈值细化：CUDA 12.0 (Driver 525.60.13) 引入了 FP8 指令集，但早期驱动在 Ada L

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

NVIDIA 驱动版本与 FP8 支持的最小阈值细化：CUDA 12.0 (Driver 525.60.13) 引入了 FP8 指令集，但早期驱动在 Ada Lovelace (RTX 4090) 上可能存在稳定性问题。推荐最低稳定驱动版本为 530.30.02 (CUDA 12.1) 或 535.54.03 (CUDA 12.2)，以解决 Ada 架构 FP8 内存对齐和精度转换的已知 Bug。Ampere (A100/RTX 3090) 硬件层面不支持 FP8 指令，任何驱动版本均无法启用原生 FP8 加速，仅能软件模拟 (速度慢 5-10x)。

## Corrected Claim

CUDA 12.0 引入了 FP8 指令集，Ada Lovelace 架构硬件支持 FP8，而 Ampere 架构硬件不支持原生 FP8 指令（仅能软件模拟）。具体推荐的最小稳定驱动版本需参考 NVIDIA 官方发布说明，早期驱动可能存在稳定性问题。

## Evidence

[质询]具体驱动版本号（530.30.02, 535.54.03）与特定Bug修复的对应关系属于经验事实，且参考来源未提供驱动版本细节，仅确认架构支持情况，无法验证具体阈值。 | 来源[1]间接支持Ampere不支持FP8、Hopper/Ada支持FP8的架构差异，但缺乏对具体驱动版本阈值及Bug修复细节的直接支持，属经验事实缺来源支持。

## Search Query

NVIDIA driver 530.30.02 FP8 support Ada Lovelace RTX 4090

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/8850769686&rut=40ab13973ead1f6e3b8b252531a9117a58d12907a39cef3ad7a057ef4859e4c0', 'type': 'ddg', 'title': '英伟达不同架构显卡支持的精度 - 知乎'}
