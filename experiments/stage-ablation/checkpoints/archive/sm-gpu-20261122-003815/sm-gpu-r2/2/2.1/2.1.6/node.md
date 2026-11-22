# N76: Qwen3-27B 的权重参数量精确值为 27.0 亿（2.7B 错误，应为 27B，需核实官方文档确认精确参数量，例如 27,000,000,000 或更精确

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 的权重参数量精确值为 27.0 亿（2.7B 错误，应为 27B，需核实官方文档确认精确参数量，例如 27,000,000,000 或更精确的数值）。

## Corrected Claim

Qwen3-27B 的权重参数量约为 270 亿（27B），具体精确数值需查阅官方技术报告确认。

## Evidence

[质询]参考来源均指向 Qwen3.5/3.8 版本，未直接覆盖 Qwen3 基础版；且来源仅给出约数（270亿），未提供精确到个位的参数量（如 27,000,000,000），无法证实‘精确值’这一强断言。 | 来源 [1][2][3] 间接支持 Qwen 系列 27B 模型参数量约为 270 亿（27B），逻辑量级自洽，但缺乏针对 Qwen3 基础版精确数值的直接证据，属经验事实且仅获间接支持。

## Search Query

Qwen3-27B exact parameter count billion

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e1a4a75338ea7b8dd9906f6fd7993bdcd78532cfd255bfc4583f3ebbf527f720', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://apxml.com/zh/models/qwen38-27b&rut=0893f3340a7bf25bc450cd9ce27463edaf04540adb33eb49fc96b7697bc58b23', 'type': 'ddg', 'title': 'Qwen 3.8 27B - 显存要求、模型规格与基准测试'}
- {'url': 'https://apxml.com/zh/models/qwen35-27b&rut=b371614aab70c0fa914d8bf711cc41e039e2ec36e107c99b8be280a7c7580e04', 'type': 'ddg', 'title': 'Qwen3.5-27B - 显存要求、模型规格与基准测试'}
