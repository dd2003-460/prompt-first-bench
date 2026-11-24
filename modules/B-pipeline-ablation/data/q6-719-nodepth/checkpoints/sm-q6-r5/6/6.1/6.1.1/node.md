# N100: 流量波动系数 K_t 的时域分解：K_t = K_base(t) + K_event(t) + K_noise(t)，其中 K_base 为昼夜周期性基线（正弦

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

流量波动系数 K_t 的时域分解：K_t = K_base(t) + K_event(t) + K_noise(t)，其中 K_base 为昼夜周期性基线（正弦/余弦拟合），K_event 为突发热点事件（阶跃函数，持续时间 30min-4h，幅度 +50%~+200%），K_noise 为随机噪声（高斯分布，σ≈5%）。

## Corrected Claim

流量波动系数 K_t 的时域分解：K_t = K_base(t) + K_event(t) + K_noise(t)，其中 K_base 为昼夜周期性基线（正弦/余弦拟合），K_event 为突发热点事件（阶跃函数，持续时间 30min-4h，幅度 +50%~+200%），K_noise 为随机噪声（高斯分布，σ≈5%）。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性/完备性严重缺失：父节点明确为'流量波动系数 K_t 的时域分解'，但子节点前4个（缓存容量、工作集、回源延迟、边缘延迟）属于CDN基础设施与性能指标，与 K_t 的数学分解无关，导致子节点未覆盖父节点核心（即 K_base/event/noise 的具体定义），反而引入了大量无关概念。2. 冗余/逻辑矛盾：子节点5、6、7、8 分别对应 K_base、K_event、K_noise 及其衍生指标，这部分是相关的，但子节点1-4与5-8属于两个完全不同的知识域（基础设施 vs 流量模型），强行放在同一父节点下导致结构混乱。此外，子节点5和8都涉及 K_base，虽角度不同（参数 vs 峰值识别），但存在内容重叠风险。）
