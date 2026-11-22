# N335: 修正 N116 错误：PyTorch 原生 FP8 推理后端并非从 2.1.0 开始支持，而是依赖 `torchao` 库（PyTorch 2.4+ 集成）或 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

修正 N116 错误：PyTorch 原生 FP8 推理后端并非从 2.1.0 开始支持，而是依赖 `torchao` 库（PyTorch 2.4+ 集成）或 NVIDIA 专用插件；在 RTX 4090/5090 (Ada/Blackwell) 上运行 Qwen3-27B FP8，最低稳定环境为 PyTorch 2.4.0 + torchao 0.3.0 + CUDA 12.3，若使用 PyTorch 2.1.0 则必须完全依赖 vLLM 内部编译的 Triton FP8 内核，此时 `torch.backends` 设置无效。

## Corrected Claim

PyTorch 原生 FP8 推理支持主要依赖 torchao 库或 NVIDIA 插件，而非早期版本原生内置；在 RTX 4090/5090 上运行 Qwen3-27B FP8 需较新的 PyTorch 与 torchao 版本组合，具体最低稳定版本需查阅官方文档确认。

## Evidence

[质询]具体版本号（PyTorch 2.4.0, torchao 0.3.0, CUDA 12.3）及硬件兼容性细节属于经验事实，且无来源支持，存在版本迭代导致的最小稳定环境描述过时的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体版本号与硬件组合的准确性）

## Search Query

PyTorch torchao FP8 inference RTX 4090 minimum version requirement Qwen3
