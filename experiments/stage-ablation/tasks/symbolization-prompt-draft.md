# 符号化 claim 格式 · prompt 注入草案

# origin: ai（D 2026-11-25 批准方向"先变成变量"，Lead 起草）

依据：`repair-loop-design-20261124.md` 21:30 条（40 节点可行性核查）+ `symbolization-40nodes.json`（seed42 样本）。
状态：草案 v1，未注入管线。注入点：P2/P3 生成端（A 段）+ P3_VERIFY（B 段）。Fix-C 臂设计时启用。

---

## A. 生成端注入文本（P2/P3，208 字）

> 写 claim 时严格执行关系-参数分离：①claim 主体只写结构关系（公式/不等式/定性方向），所有数字一律抽成参数符号（如 T_p99、price_per_gb、ρ）；②每个参数附参数卡：symbol / value 或 range / unit / source（具体来源描述）/ observed_at（日期）/ volatility（定价=high、阈值=medium、物理常数=low）；③纯经验常数（定价/商业阈值）禁止裸写数值进 claim 主体，必须走参数卡；④内部算术（如 55000GB×0.15）保留表达式不写死结果，结果由机械重算填入。参数卡统一放节点 params 字段。

## B. verify 端豁免规则（P3_VERIFY，121 字）

> 核验时将 claim 分两部分：关系部分（公式/不等式/定性方向）仍按原 D-质询规则攻击；参数部分（参数卡）不参与"数值无来源"攻击，其验证标准仅三条：①source 字段非空 ②volatility 等级合理 ③observed_at 存在。关系部分通过且参数卡完整 → verified；关系部分攻击点成立 → 按原降档逻辑，不豁免。

## 与现有 D-质询规则的兼容性说明（97 字）

> 本规则不改 D-质询的攻击机制，只收窄攻击面："数值无来源"攻击仅对无参数卡的裸数值（旧格式）成立，对带完整参数卡的 claim 不适用。旧格式 claim 走原逻辑，保证过渡期两臂可比。

---

## 改写示例 1（定价类，N290 r1）

**原 claim 全文**：
> 公有云CDN流量计费单价 Price_flow 的构成：基础流量单价通常为 ¥0.12-0.20/GB，但包含免费额度（如每月5TB）；对于60TB月流量，扣除免费额度后有效计费流量为 55,000GB，若单价为 ¥0.15/GB，则月流量成本为 ¥8,250，而非N97中假设的 ¥7,200。

**符号化后 claim**：
> Cost_month = max(0, Traffic_month − Free_quota) × Price_flow；当 Traffic_month ≫ Free_quota 时 Cost_month 对 Traffic_month 线性。N97 假设的月成本 ¥7,200 与本式代入值不一致，差异源于 N97 单价取值偏低（见 params）。

**参数卡**：

| symbol | value/range | unit | source | observed_at | volatility |
|---|---|---|---|---|---|
| Price_flow | 0.12–0.20（代入 0.15） | 元/GB | 阿里云 CDN 官网定价页 [待核验] | 2026-11-25 | high |
| Free_quota | 5 | TB/月 | 阿里云 CDN 官网免费额度条款 [待核验] | 2026-11-25 | high |
| Traffic_month | 60 | TB/月 | 题面假设 | 2026-11-25 | low |

**机械重算表达式**：`(60 - 5) × 1000 × 0.15` → 结果由 sympy 重算，不写死。

## 改写示例 2（关系类，N232 r1）

**原 claim 全文**：
> 多流并发（Multiplexing）下，总有效吞吐率并非单流吞吐的线性叠加，受限于共享带宽和调度公平性，实际总吞吐率约为 N_streams * Throughput_single * 0.85（N_streams≤4），超过4流后边际收益递减，η_protocol需随并发流数动态修正。

**符号化后 claim**：
> Throughput_total(N) = N × T_single × η_protocol(N)；η_protocol(N) < 1 且对 N 单调递减（边际收益递减），N ≤ N* 时 η_protocol ≈ const，N > N* 后衰减加速。

**参数卡**：

| symbol | value/range | unit | source | observed_at | volatility |
|---|---|---|---|---|---|
| η_protocol(N≤N*) | ≈0.85 | 无量纲 | 行业实测/题面上下文 [待核验] | 2026-11-25 | medium |
| N* | 4 | 流数 | 经验阈值（题面） | 2026-11-25 | medium |
| T_single | 符号 | 吞吐/流 | 上游节点（不实例化） | — | — |

**机械重算**：无（纯结构关系，verify 只攻击"η 单调递减"是否被证据支持）。

---

## 注入点与启用时机

- A 段 → P2/P3 生成 prompt（`s5_pipeline.py` 生成端）
- B 段 → P3_VERIFY prompt（`s5_pipeline.py:231` verify_node）
- 启用：Fix-C 臂（T-REPAIR-1 跑完后设计），与 baseline 对照测"符号化后 verify 墙是否消失"
- 前置：参数卡 schema 进节点 JSON（params 字段）+ 机械重算脚本（接 `source_verify.py`）

## 已知风险

1. **模型不守格式**：27b 可能不严格遵守参数卡 schema → 需解析层容错（params 缺失时退回旧逻辑，不崩）
2. **source 字段造假**：模型可能编造 source 描述 → 参数卡 source 需与检索通道返回的来源做一致性检查（机械比对，非 LLM）
3. **过渡期可比性**：新旧格式 claim 混合时，verify 判定口径不同 → Fix-C 臂与 baseline 臂对比时需按格式分层报告
