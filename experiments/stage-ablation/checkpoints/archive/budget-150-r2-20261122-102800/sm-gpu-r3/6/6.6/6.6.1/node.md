# N144: NVIDIA单卡方案（RTX 4090/A100/H100）的驱动与CUDA环境安装耗时约为30-60分钟，主要取决于CUDA版本匹配与网络下载速度。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

NVIDIA单卡方案（RTX 4090/A100/H100）的驱动与CUDA环境安装耗时约为30-60分钟，主要取决于CUDA版本匹配与网络下载速度。

## Corrected Claim

NVIDIA单卡方案（RTX 4090/A100/H100）的驱动与CUDA环境安装耗时约为30-60分钟，主要取决于CUDA版本匹配与网络下载速度。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了下载和验证两个主要阶段，正交性良好。但父节点明确提到耗时“主要取决于CUDA版本匹配”，而子节点仅以CUDA 12.4为例，未涵盖不同CUDA版本（如11.x与12.x）在驱动兼容性检查、依赖库安装差异上的耗时影响，导致对‘版本匹配’这一关键变量的覆盖不完备。）

## Search Query

NVIDIA driver CUDA installation time estimate
