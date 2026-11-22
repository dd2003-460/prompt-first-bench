# N158: RTX 4090 单卡 INT8 部署的 KV Cache 瓶颈量化：24GB 显存 - 27GB 权重 = -3GB（不足），因此必须使用量化权重压缩（如 W

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

RTX 4090 单卡 INT8 部署的 KV Cache 瓶颈量化：24GB 显存 - 27GB 权重 = -3GB（不足），因此必须使用量化权重压缩（如 W4 或 NVFP4）或启用 PagedAttention 动态管理。若强制使用 INT8，需限制最大上下文至 8K tokens，此时 KV Cache 占用约为 1.0GB，总占用 28GB，仍超出 24GB 物理显存，故 4090 单卡 INT8 在 32K 上下文下不可行，必须限制上下文或使用更激进量化。

## Corrected Claim

RTX 4090 单卡 INT8 部署的 KV Cache 瓶颈量化：24GB 显存无法容纳 27GB 的 INT8 权重，因此必须使用量化权重压缩（如 W4 或 NVFP4）或启用 PagedAttention 动态管理。若强制使用 INT8，需限制最大上下文至 8K tokens，此时 KV Cache 占用约为 1.0GB，总占用 28GB，仍超出 24GB 物理显存，故 4090 单卡 INT8 在 32K 上下文下不可行，必须限制上下文或使用更激进量化。

## Evidence

父节点级核验未通过：不完备（子节点存在事实性错误导致逻辑矛盾，且未覆盖父节点中关于'8K tokens'的具体量化验证。子节点1中Qwen3-27B的KV头数假设（4头）极大概率错误（通常27B模型GQA KV头数为8或更多，若为4头则模型结构异常或为更小模型），导致后续计算基础错误；此外，父节点明确提到'8K tokens时KV Cache约1.0GB'，但子节点仅计算了32K和W4情况，缺失了父节点中'8K tokens INT8'这一关键分支的独立验证节点，导致完备性不足。）

## Search Query

RTX 4090 24GB INT8 27B model KV cache limit context length
