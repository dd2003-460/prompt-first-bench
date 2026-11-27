# N24: 消费级显卡（如 RTX 4090/5090）与数据中心显卡（如 A100/H100）在 32K 上下文下的 TTFT 对比基准：需检索最新 benchmark 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

消费级显卡（如 RTX 4090/5090）与数据中心显卡（如 A100/H100）在 32K 上下文下的 TTFT 对比基准：需检索最新 benchmark 数据，对比两者在 Prefill 阶段（计算密集型）和 Decode 阶段（带宽密集型）的实际耗时差异，以验证 '消费卡多卡并联' 是否能在 TTFT 上逼近单张高端数据卡。

## Corrected Claim

消费级显卡（如 RTX 4090）与数据中心显卡（如 A100/H100）在 32K 上下文下的 TTFT 对比基准需进一步检索最新 benchmark 数据以验证具体耗时差异，现有来源仅显示两者存在显著价格差异（如4090 vs A6000溢价196%），未提供性能对比证据。

## Evidence

[质询]参考来源仅对比了RTX 4090与RTX A6000的市场价格及通用定位，完全缺失32K上下文下TTFT、Prefill/Decode阶段耗时等核心性能基准数据，且未涉及A100/H100等数据中心显卡，无法支撑原陈述中关于具体耗时差异和‘多卡并联逼近单卡’的结论。 | 来源[1]主题相关但仅涉及价格对比，未提供TTFT或Prefill/Decode性能数据，属于间接/无关支持，无法验证具体数值结论。

## Search Query

RTX 4090 vs A100 LLM inference benchmark TTFT TPOT 32k context

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2029878314618324784&rut=c1cbbfecf5f28ac7bf7015897c0266cfb17315cf7ce1cb59b6f0830a827075c4', 'type': 'ddg', 'title': '4090 vs A6000：同为消费级，专业卡真的更值得吗？ - 知乎'}
