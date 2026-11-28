# N73: Qwen3-27B-Instruct 在 GPQA Diamond (Open) 基准上的 FP16 准确率实测值为 44.2% (基于 HuggingFace

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

Qwen3-27B-Instruct 在 GPQA Diamond (Open) 基准上的 FP16 准确率实测值为 44.2% (基于 HuggingFace Open LLM Leaderboard 2024-06 数据)，该分数低于 '可发表级' 所需的 85% 逻辑严谨度阈值，差距为 40.8 个百分点。

## Corrected Claim

Qwen3-27B-Instruct 在 GPQA Diamond 基准上的实际表现需参考其官方发布时的技术报告（2025年），而非2024年6月的数据；该模型在逻辑推理任务上的具体得分应以官方公布为准，'85%可发表级阈值'亦非行业标准定义。

## Evidence

[质询]模型名称与时间线严重不符：Qwen3系列（包括Qwen3-27B）于2025年发布，不可能出现在2024年6月的HuggingFace Open LLM Leaderboard数据中；且参考来源显示当前最新模型为Qwen3.8-27B，暗示Qwen3系列已迭代多代，进一步证实2024年6月不存在Qwen3-27B的公开基准测试数据。 | 参考来源[1][2][3]均指向Qwen3.5/3.6/3.8版本，表明Qwen3系列发布时间晚于2024年6月，与claim中'2024-06数据'存在时间逻辑矛盾；且GPQA Diamond基准在2024年6月尚未成为主流公开榜单标准指标，该具体数值44.2%缺乏可信来源支持。

## Search Query

Qwen3-27B-Instruct GPQA Diamond accuracy Open LLM Leaderboard

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.5-27B&rut=b98abe58c1eb296e8a9a310bfec52df8838f1793313d981bb354e276f058e2f8', 'type': 'ddg', 'title': 'Qwen/Qwen3.5-27B · Hugging Face'}
- {'url': 'https://github.com/AlibabaCloud-Official/Qwen3.8-27B&rut=a332b0ce380d5c34328ba249051c409a073159eaa8056b4b8ce330676a0a4380', 'type': 'ddg', 'title': 'GitHub - AlibabaCloud-Official/Qwen3.8-27B: Native multimodal dense LLM ...'}
- {'url': 'https://huggingface.co/Qwen/Qwen3.6-27B&rut=bf878984c20b3d898a4e6c6962fab20b5cdd6ccc184b0bab8031efdf32ec87f6', 'type': 'ddg', 'title': 'Qwen/Qwen3.6-27B · Hugging Face'}
