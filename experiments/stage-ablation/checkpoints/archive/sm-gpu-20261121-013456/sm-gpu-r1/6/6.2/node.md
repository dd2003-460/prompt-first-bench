# N40: 边界条件与失效场景：当(1) 吞吐量需求>20 tokens/s时，单卡4090失效，需升级为2×4090或A100；(2) 上下文窗口>32K tokens时

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

边界条件与失效场景：当(1) 吞吐量需求>20 tokens/s时，单卡4090失效，需升级为2×4090或A100；(2) 上下文窗口>32K tokens时，24GB显存不足，需48GB+方案（2×4090或A100 80GB）；(3) 使用年限<2年时，硬件折旧成本占比>50%，电力成本优势消失，TCO排序反转；(4) 电价>$0.20/kWh时，高功耗方案（2×4090）TCO劣势扩大，低能效方案（M3 Ultra）优势凸显

## Corrected Claim

边界条件与失效场景：当吞吐量需求显著超过单卡4090处理能力（具体阈值依模型而定）时，需升级多卡或更高显存方案；当上下文窗口导致显存占用超过24GB时，需48GB+方案；在硬件折旧周期短或电价较高时，高功耗方案的TCO优势可能消失或反转。

## Evidence

[质询]阈值数值（如20 tokens/s、32K上下文、2年折旧、$0.20/kWh）缺乏通用标准支持，属于特定场景下的经验估算，不同模型架构、量化精度及电价波动下结论可能不成立。 | 先验知识/题面给定，逻辑校验通过（量纲与因果方向合理），但具体阈值缺乏外部来源直接支持，且属于经验事实范畴，故降级。

## Search Query

GPU TCO sensitivity analysis usage years electricity price context window constraints
