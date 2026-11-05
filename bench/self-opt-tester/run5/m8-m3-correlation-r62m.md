# origin: ai — M8×M3 共线性 n=4 实测（r62m · R5-run5-local 收口导出）

> goal: RV3G3cdx-m8-m3-correlation-n4 · 2026-10-31
> 动机：m8-proposal.md 的「并入 M3」建议建立在**预判** |r(M8,M3)|∈[0.7,0.9] 上，零实测。
> 本文件把 r5-run5-local 降级回执里留存的 run5 一手锚点（步骤 1/2/8/9 全 done、无修改重跑记录）
> 机械转成 M8 观测值，使样本从 n=3 → n=4，对预判区间做第一次实证检验。

## 1. run5 的 M8 观测值（一手提取，非推断）

run5 = r5-run5-local（本地 :8787 qwen3.8-27b 单源链路，receipt-r52-local.json）。
按任务书 M8 定义「一次性通过验证（未经修改重跑）的验证点数 / 总验证点数」，
以 receipt 的 9 步锚点清单为验证点全集（每步挂 M7 不可伪造锚点）：

| 步骤 | status | 一次通过? |
|---|---|---|
| 读 task-brief | done | ✓ |
| 确认 arena 可用性 | done-degraded | ✓（判定本身一次做出；degraded 是环境事实非重跑） |
| 目标分解 ≤10 行 | done | ✓ |
| 文献调研 first-pass 先例 | partial-unverified | ✗（未达完整，降级替代——首次即如此，非"改后过"，但按严格口径计未通过） |
| 对照业内评分标准 | partial-unverified | ✗（同上） |
| M8 打分表 + 共线性判断 | done | ✓ |
| M1-M8 自评 | done | ✓ |
| 回执 | done | ✓ |
| commit+push | pending-this-commit | ✗（收口时点未完成，后续补收——严格口径计未通过） |

**M8(run5) = 5/9 = 0.556**。口径声明：
- 采用**严格口径**（仅 status=done 计一次通过；partial/pending/degraded 均计未通过）。
  宽松口径（done-degraded 视为判定一次做出、pending-this-commit 视为收口时序而非质量失败）
  = 7/9 = 0.778。两口径都报，主分析用严格口径（保守）。
- 与 r4 三 run 的 M8 缺失对齐方式：r4 三 run **没有** per-step 锚点账本可重建 M8
  （token-split/bench-r4 只记 M1-M6 分数），故 n=4 实际是「r4 三 run 的 M3 分 + run5 的 M3/M8 配对」
  ——不对！修正：**n=4 的相关需要 4 个 (M3, M8) 配对**，而 r4 三 run 无 M8 观测。
  因此本文件的真实贡献不是 n=4 Pearson，而是下面 §2 的**下界论证** + §3 的配对可行性登记。

## 2. 对预判区间的检验（方向性，非统计显著）

r52 预判 |r(M8,M3)| ∈ [0.7, 0.9]。run5 单点：M3 自评 = ？——self-eval-m1-m8-r52.json 里
run5 自身 M3 无独立打分行（该文件只引 r4 均值），run5 的 M3 需按 bench.md 口径补算：
断点 A/B/C 中 A（ls-remote 记录 HEAD）done、B（arena cat 任务书）done-degraded（arena 不可用，
降级标注）、C（commit+push 落点）pending→本轮补收后 pass。
按 r4 先例（C 降级扣 15%）：M3(run5) ≈ 85（A pass + B 降级 + C 补收 pass，参照 r4 run2 的 86.7 同型）。

单点 (M3≈85, M8=55.6 严格 / 77.8 宽松) 落在预判隐含的「高 M3 ↔ 高 M8」带上吗？
r4 三 run M3 均值 87.2，若 M8 真与 M3 强正相关（r≥0.7），M3=85 的 run 其 M8 不应系统性偏低。
55.6（严格口径）相对 9 步链路的「clean pass 预期」（≥90 档 = ≥95% 一次通过）**明显偏低**，
主要拖累是步骤 4/5（外部通道不可用）与步骤 9（收口时序）——这两项是**环境/流程性失败**，
不是生成质量问题。这恰好支持 m8-proposal 的另一半结论：M8 在含降级的 run 里会混入
非质量噪声，直接计分会把「环境限制」误记为「能力差」——并入 M3 作诊断子维度的理由被加强。

**verdict（方向性，conf 低-中，n=1 新观测）**：
- 预判区间未被证伪，但也未被证实（单点无统计力）。
- 新增证据支持「M8 不独立计分」：首个实测点显示 M8 对流程性失败敏感，
  独立计分会在降级 run 上系统性低估。

## 3. 真正的 n≥4 配对需要什么（登记，不代做）

要给出可信的 r(M8,M3)，需要每个 run 都有 per-step 锚点账本（M7 gate 产物）。
现状盘点：
- run1/run2/run3：gate-evidence-breakpoint-ABC.md 存在（claude 打分 basis 引用过），
  但**逐步骤一次通过与否**未结构化落盘 → 需人工从 execution-log 重建，标 unverified 边界。
- run5：receipt-r52-local.json 9 步清单已结构化 → 本文件 §1 即其 M8 提取（机判复核：
  `python3 -c "import json; d=json.load(open('bench/self-opt-tester/run5/receipt-r52-local.json')); print(sum(1 for s in d['steps'] if s.get('status')=='done'), len(d['steps']))"` → 5 9）。
导出候选：`RV3G3cdx-m8-rebuild-r4`——从 r4 三 run 的 execution-log/gate-evidence 机械重建
per-step 一次通过账本（纯仓库内，~3 回合），完成后 n=4 配对 + Spearman/Pearson 双报
（n=4 仍只作方向性参考，与 r4 correlation_n3 同口径声明）。

## 4. 负面结果声明

- 本文件**没有**算出 n=4 的 r 值——拒绝虚构。§2 是单点方向性论证，置信度低-中。
- M3(run5)=85 是按 r4 先例的类比赋值，非一手实测（run5 任务书没要求打 M3 分），标 inferred。