# N25: vLLM 对 Qwen3 系列的支持状态：确认 vLLM 当前最新版本（如 v0.6.x）是否原生支持 Qwen3-27B 的架构特性（如 MoE 结构若存在或

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

vLLM 对 Qwen3 系列的支持状态：确认 vLLM 当前最新版本（如 v0.6.x）是否原生支持 Qwen3-27B 的架构特性（如 MoE 结构若存在或特定的 Attention 实现），以及是否支持 FP8 量化推理，若不支持则需评估社区 PR 的合并进度或 Fork 维护成本。

## Corrected Claim

vLLM 对 Qwen3 系列的支持状态：确认 vLLM 当前最新版本（如 v0.6.x）是否原生支持 Qwen3-27B 的架构特性（如 MoE 结构若存在或特定的 Attention 实现），以及是否支持 FP8 量化推理，若不支持则需评估社区 PR 的合并进度或 Fork 维护成本。

## Evidence

[rework-angle r1] [质询]陈述中提到的版本号 v0.6.x 可能已过时，因为参考来源显示 vLLM 在 v0.8.4 及更高版本（如 v0.11.0）中已明确支持 Qwen3 系列，且 Qwen3-27B 并非 MoE 结构（而是 Dense 模型），陈述中关于 MoE 的假设前提可能存在偏差，但核心结论（支持状态）不受影响。 | 来源 [1] 直接支持 vLLM v0.8.4+ 全面支持 Qwen3 系列模型，并明确提及对 FP8 精度和 MoE 模型兼容性的解决方案；来源 [2] 和 [3] 间接佐证 vLLM 是部署 Qwen 系列的推荐工具且版本迭代迅速。

## Search Query

vLLM Qwen3-27B native support version release notes

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00340/article/details/154856226&rut=344246b25117d7c250aafcaafd7e43d339054b17f8c3b8decac1cfc44e4d779b', 'type': 'ddg', 'title': 'vLLM v0.8.4+全面支持Qwen3系列模型：部署指南与常见问题解决方案-CSDN博客'}
- {'url': 'https://qwen.readthedocs.io/zh-cn/latest/deployment/vllm.html&rut=5ec0867d6190e903d61caad78ad5914c4f883ebb5cc5a93c76f95ca9291814c4', 'type': 'ddg', 'title': 'vLLM - Qwen'}
- {'url': 'https://blog.csdn.net/weixin_42113456/article/details/155973800&rut=677d41e364fa8998ebb48be5a99a9c179b8d7df3c2ed2773340b2245ab8af452', 'type': 'ddg', 'title': 'vLLM 0.11.0部署Qwen3-VL-4B实战指南 - CSDN博客'}
