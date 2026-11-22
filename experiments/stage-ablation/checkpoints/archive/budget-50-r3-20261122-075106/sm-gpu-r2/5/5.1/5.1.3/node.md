# N94: 工作点C（高成本低性）：采用NVIDIA开发版CUDA 12.5 + PyTorch 2.3 Nightly + vLLM 0.6.0-dev源码编译安装，在U

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

工作点C（高成本低性）：采用NVIDIA开发版CUDA 12.5 + PyTorch 2.3 Nightly + vLLM 0.6.0-dev源码编译安装，在Ubuntu 22.04 LTS环境下，单卡RTX 4090的安装与配置时间平均为6小时，主要耗时在频繁的版本冲突排查（3小时）和非稳定API适配（2小时），故障率（月均）约为1.5%，因为开发版包含未修复的Bug，但可能获得实验性性能提升（如新的量化内核支持）。

## Corrected Claim

工作点C（高成本低性）：采用NVIDIA开发版CUDA 12.5 + PyTorch 2.3 Nightly + vLLM 0.6.0-dev源码编译安装，在Ubuntu 22.04 LTS环境下，单卡RTX 4090的安装与配置通常耗时较长（数小时至一天），主要耗时在版本冲突排查和非稳定API适配，故障率高于稳定版，因为开发版包含未修复的Bug，但可能获得实验性性能提升（如新的量化内核支持）。

## Evidence

[质询]具体数值（6小时、3小时、2小时、1.5%故障率）属于高度依赖具体环境、硬件批次及操作者熟练度的经验性统计数据，缺乏通用性，且‘开发版包含未修复Bug’与‘1.5%月均故障率’之间的因果关联过于简化，未考虑Bug的具体类型和触发条件。 | source=knowledge，逻辑自洽（高成本对应高耗时和低稳定性符合直觉），但具体数值为经验事实，无外部来源支持，依据经验事实排除条款降级。
