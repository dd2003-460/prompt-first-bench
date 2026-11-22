# N25: 工作点1 (高性低成/极致性价比)：使用单张 RTX 4090 (24GB) 运行 Qwen3-27B 的 INT4/AWQ 量化版本。量化依据：4090 显存

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

工作点1 (高性低成/极致性价比)：使用单张 RTX 4090 (24GB) 运行 Qwen3-27B 的 INT4/AWQ 量化版本。量化依据：4090 显存 24GB 可容纳 27B 模型 INT4 (~14GB) + 32K 上下文 KV Cache (~4-6GB)，剩余显存充足。性能预估：~50-80 tokens/s (batch=1)，质量损失 Q_score ~0.95 (基于 LLM 量化误差经验值 [待核验])。

## Corrected Claim

工作点1 (高性低成/极致性价比)：使用单张 RTX 4090 (24GB) 运行 Qwen3-27B 的 INT4/AWQ 量化版本。量化依据：4090 显存 24GB 可容纳 27B 模型 INT4 (~14GB) + 32K 上下文 KV Cache (~4-6GB)，剩余显存充足。性能预估：预计可达较高推理速度（具体数值需实测验证），质量损失较小（具体Q_score需实测验证）。

## Evidence

[质询]参考来源仅涉及RTX 4090的租赁市场与硬件版本评测，完全未覆盖Qwen3-27B模型在INT4量化下的显存占用、推理速度（tokens/s）及质量损失（Q_score）等具体软件/模型性能数据，属于经验事实且缺乏直接来源支持。 | 逻辑上24GB显存容纳14GB模型+5GB KV Cache是合理的，但具体性能指标（50-80 tokens/s, Q_score 0.95）为经验事实，参考来源[1][2]均与模型推理性能无关，无法提供外部证据支持。

## Search Query

RTX 4090 Qwen 27B INT4 inference speed tokens per second 32k context

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2030657934590486428&rut=14528e3b15901c7a57e5b5fc850cf63623e72f8bc1a2394e3709a6fc6de7645c', 'type': 'ddg', 'title': '全网最全!10款rtx 4090租赁平台横评，第一名实至名归 - 知乎'}
- {'url': 'https://www.sohu.com/a/1083749929_122471764&rut=f706a7d1cf4cf957a9a4806097241324024e282802de98fb716ca02bd60f1765', 'type': 'ddg', 'title': '2026年rtx 4090显卡全解析：从工包到涡轮版，哪款才是你的性价比之选？'}
