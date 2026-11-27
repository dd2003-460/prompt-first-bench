# N60: vLLM PagedAttention的KV Cache分页管理开销：每页16 tokens，FP8下每页大小16*12KB=192KB，500 tokens生

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

vLLM PagedAttention的KV Cache分页管理开销：每页16 tokens，FP8下每页大小16*12KB=192KB，500 tokens生成需32页，页表查找与物理块映射开销约0.1-0.2ms/token，占总延迟的0.7-1.3%

## Corrected Claim

vLLM PagedAttention采用分页管理KV Cache，典型页大小为16 tokens。具体每页内存占用及页表查找开销取决于模型架构（如hidden size）和硬件环境，通常页表操作开销极低（微秒级），占总延迟比例较小，具体数值需结合特定模型基准测试确定。

## Evidence

[质询]数值量级存疑：0.1-0.2ms/token 的页表查找开销在现代 GPU 架构下显得过高（通常内存访问延迟在微秒级，除非涉及大量同步或低效实现），且 FP8 下 12KB/layer/token 的具体数值依赖于模型维度（如 hidden size 和 head count），并非通用常数，缺乏特定模型上下文导致计算基础模糊。 | 先验知识/题面给定，逻辑校验通过（算术关系 16*12=192, 500/16≈32 成立），但具体性能指标（0.1-0.2ms）和内存占用（12KB）为经验事实，无外部来源支持，且数值合理性依赖特定硬件/模型配置，故降级。
