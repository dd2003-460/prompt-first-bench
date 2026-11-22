# Judge v1.0 标定记录（2026-11-22 冻结）

> origin: ai · 标定数据：15 budget scan runs × gold 36 unit（judge-v1-cov-calibration.json）
> 脚本：judge_v1.py（代码）+ judge_v1_calibrate.py（标定）

## 标定结果

### 覆盖层阈值（cosine）

| 阈值 | mean coverage (15 runs) | 判定 |
|---|---|---|
| 0.50 | 1.000 | 全匹配，无区分度 |
| 0.55 | 0.941 | 太松 |
| 0.60 | 0.796 | 偏松 |
| 0.65 | 0.589 | 旧值，偏松 |
| **0.70** | **0.350** | **冻结**：per-run 区分度 0.11-0.56，能分开好 run 和差 run |
| 0.75 | 0.098 | 覆盖塌 |
| 0.80 | 0.015 | 几乎全 0（spec 初值，标定推翻） |

**冻结：COS_THRESHOLD = 0.70**（spec 初值 0.80 被数据推翻——0.80 时 15 runs 覆盖几乎全 0，judge 失效）。

### 结构层

- node_score（节点数/gold 37）饱和：模型 100-747 节点 → 全 1.0，无区分度
- depth_score（去重后 max depth / gold 5）：0.6-1.0，有区分度
- **冻结：结构轴 = depth_score**，node_score 降级为诊断字段（node_score_sat）

### 机械层（sympy 公式验证）

- 15 runs 全部 0 分：模型节点公式符号与 gold 不对齐（模型用 Total_Mem/Weights_MB，gold 用 c_pass/c_hour）
- **冻结：移出综合分，只作诊断**（mech_diag）。符号对齐是独立工作项（J8 遗留），不阻塞 judge 主流程
- 这是诚实的已知 gap，不是 judge 失效——公式验证需要符号对齐预处理，当前 27b 输出符号与 gold 命名体系不同

## 综合分（冻结）

`total = 0.5 * depth_score + 0.5 * coverage`（mech 移出）

15 runs 实测分布：total 0.356-0.597，depth 0.6-1.0，cov 0.056-0.333。

## 与旧 judge 的口径差异（判分校准规则）

- 旧 depth_score（run json 里的）= 旧 LLM judge 的 cov15 相关（r=0.861），**不是**新 judge 的 depth
- 新 judge 的 depth = 去重后树 max depth / 5（机械计算）
- 跨轮比较必须用同一 judge 版本，新数据用 judge_v1.py 重算

## 待办（不阻塞）

1. 机械层符号对齐（J8 遗留）：模型符号 → gold 符号映射表
2. 权重 0.5/0.5 是拍的 [待标定]：补重复后用消融验证（去掉 depth 或 cov 看 total 变化）
3. 数值容差 10% 未启用（机械层移出后暂不用）
