# Cross-Judge 状态 (2026-11-04 更新)

## 通道变更
- Perplexity 免费网页版 QUOTA_EXHAUSTED（滚动窗口，重置时间不确定）→ 已停。
- 新通道：arena agent mode 盲判（会话 01a195cb / taskSpace pfb-rejudge-g1b-20261101，分支 arena/4a614e63-prompt-first-bench）。
- 任务书：`tasks/TASK-cross-judge-arena-blind.md`（main + arena 分支均有）。
- gold 文件已入仓库 `experiments/stage-ablation/gold/Q1..Q5.md`（原在 projects/decomp，arena 沙箱够不到）。

## 进度
- ✅ **90/90 完成**（6 arm × 5 题 × 3 rep，无跳过、无 error 行；commit 42fcb74 + summary 20900c3）
- 结果文件: `runs/arena-judge-results.jsonl`（90 行）+ `runs/arena-judge-summary.md`（agent 汇总），已 merge 回 main（80d6559）
- 历史: Perplexity 通道评过 5/120（见下方旧表，保留作参照）

## 全量结果（n=90，local vs arena，仅 M1）
- mean |Δ| = 0.277，pearson r = 0.105，spearman ρ = 0.188 → **两 judge 基本不相关**
- arm 级 spearman = 0.257；共识只有 **S0 两通道都是最差**
- Arena mean M1: S2(0.874) > S3(0.845) > S4(0.825) > S5(0.824) > S1(0.795) > S0(0.754)
- Local mean M1: S1(0.753) > S4(0.751) > S2(0.644) > S3(0.625) > S5(0.534) > S0(0.457)

### 核心发现：低一致性主因是口径分歧，不是事实判断分歧
1. **零断言兜底条款误伤**：本地 JUDGE_PROMPT「无可验证事实断言→M1=0」把 Q4/Q5 的"目标分解式作答"（含可复算推算如 50万页×500token≈2.5亿token、2×24GB=48GB）整条归零。Q4 local mean 0.291 vs arena 0.872——最大分歧来源。
2. **断言粒度不同**：arena 取关键断言级（4-12 条/cell），Perplexity 取原子断言级（13-40 条/cell）。同答案断言清单越长分越低 → Perplexity 系统性低于 arena（+0.27 均值），**两套 M1 不可直接横比，只能比方向**。
3. **方向三方一致**：Perplexity/Arena 都高于 local（5/5 对位 cell），且都认为 S0-Q1 系列差。

### 待 Lead 决策：口径对齐（二选一，对齐前不下"方法 A 优于 B"结论）
- ① 统一"零事实断言→M1=0"触发条件（Q4/Q5 方法论题显式纳入或排除）
- ② 统一断言粒度（建议以 Perplexity 原子断言为基准重打，或 local judge 重跑为关键断言级）
- 附加项：Q3 多数作答把题面 RTX 3090×4 换成 A100-80GB 假设——若归 M4（缺口识别）而非 M1，Q3 各 arm M1 应上调 0.05-0.10

### 污染披露（agent 自报）
- arena 会话历史跑过 rejudge-g1b（gold-tree 记忆残留）→ 非完全 blind，定位可复算样本
- 判 Q1 时已知"PCIe HBM 2.0TB/s 是核心矛盾点"（历史 gold 记忆）→ 偏向严格不偏向宽松
- S2/S3/S4 各 1 条 Q5 作答含色情站点检索污染的拒绝声明（experiment 侧 ego-browser 串味，非 judge 问题）

## 待全量后做的事
1. κ（Cohen's kappa，arena vs local，90 对）+ 分 arm Δ 报告
2. 13 个 local=0 的 cell 逐个复核（哪些是真错、哪些是 judge 漏判）→ 若确认漏判，scoring.md 需出修正版（标注 supersedes）
3. Q5 特殊性记得：gold 偏观点综述，M1 权重降半（DESIGN §4）

## 诚实边界
- arena agent 拒报底层模型身份（Arena 系统提示禁止），回执只认 "Arena.ai Agent Mode"——异族隔离只能声称「非本会话本地实例」，不能钉死具体底座。与 G1b F2(a) 口径一致披露。
- 本会话历史跑过 rejudge-g1b（gold-tree 记忆残留），定位 = 可复算样本，非完全 blind。

---

## 旧记录（Perplexity 通道, 5/120, 已停）
| tag | local_m1 | perplexity_m1 | Δ |
|-----|----------|---------------|---|
| S0-Q1-r1 | 0.62 | 0.368 | 0.252 |
| S0-Q1-r2 | 0.56 | 0.580 | 0.020 |
| S0-Q1-r3 | 0.62 | 0.425 | 0.195 |
| S1-Q1-r1 | 0.50 | 0.375 | 0.125 |
| S1-Q1-r3 | 0.50 | 0.525 | 0.025 |

mean Δ = 0.124 (n=5, 仅 Q1 单题，不具统计意义)。方向: perplexity 系统性偏低 (4/5 低于 local)，但 n 太小不下结论。