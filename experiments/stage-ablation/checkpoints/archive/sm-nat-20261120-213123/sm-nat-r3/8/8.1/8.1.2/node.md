# N159: 工作点3（高纯度/高成本）：设定请求频次占比阈值 R(k) = 99%。解得 k_eff ≈ 10^5 * (0.01)^(1/0.9) ≈ 10^5 * 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

工作点3（高纯度/高成本）：设定请求频次占比阈值 R(k) = 99%。解得 k_eff ≈ 10^5 * (0.01)^(1/0.9) ≈ 10^5 * 0.021 ≈ 2100 个对象。此工作点仅保留极热门对象，缓存命中率最高，但大量中频对象被逐出，导致 LFU 策略在此工作点下优势更明显，因为 LFU 能更精准地识别这些高频对象。

## Corrected Claim

工作点3（高纯度/高成本）：设定请求频次占比阈值 R(k) = 99%。解得 k_eff ≈ 10^5 * (0.01)^(1/0.9) ≈ 10^5 * 0.021 ≈ 2100 个对象。此工作点仅保留极热门对象，缓存命中率最高，但大量中频对象被逐出，导致 LFU 策略在此工作点下优势更明显，因为 LFU 能更精准地识别这些高频对象。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 10^5 * (0.01)^(1/0.9) ≈ 2100 正确，LFU 在高纯度工作点下优于 LRU 符合缓存理论直觉。

## Search Query

Pareto distribution request frequency coverage k_eff calculation beta 0.9
