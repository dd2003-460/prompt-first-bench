# kill-argument verdict — idea53-repro 核心 claim 对抗审查
# origin: ai
audit_skill: kill-argument · 协议: pfb/tools/aris/prompts/kill-argument.md
executed_at: 2026-11-25 (C4 验收) · executor: qwen3.8-27b (本地 subagent)
audited_claim: "idea53 闭式计算可独立复现: flip 0.4344–0.5627 / shift 0.1655–0.2307 /
  H(D|S) 0.7128–0.7667 / flat 对照精确=0 / 24 置换不变 (4 硬件平台, seed=42, 40k workload)"
audited_inputs:
  - tasks/autoresearch-sm/trial/TRIAL-RECEIPT.md
  - tasks/autoresearch-sm/trial/acceptance-request.md
  - tasks/autoresearch-sm/trial/C3b-verdict.md
  - tasks/autoresearch-sm/trial/independent_recompute.json
  - tasks/autoresearch-sm/trial/verify_results.json
  - tasks/autoresearch-sm/trial/.aris/runs/idea53-repro.json (终态: 两 phase accepted)

## 合规声明 (双线程独立性)
- 任务书规定: kill-argument 双线程由本 subagent (qwen3.8-27b) 撰写, 批判角色≠验收角色
  (C3b 验收方是 deterministic:lead-verify, 非 LLM), 合规。
- 线程1 (攻击) 与线程2 (裁定) 在本文件中按顺序独立撰写: 线程2 只以线程1 备忘录逐字
  原文 + trial/ 证据文件为输入, 不共享线程1 的推理草稿。
- 未调用任何 LLM API, 未联网 (任务书边界)。
- verdict 由下方映射表从逐点计数机械算出, 不由任一线程自评。

## Thread 1 — 最强拒绝备忘录 (攻击线程, 逐字原文)

> 这份复现是同义反复, 它产出的数字不可信。整条验证链 (TRIAL-RECEIPT.md「状态机使用
> 记录」、independent_recompute.py) 与原 run 共用同一 seed=42、同一采样: 重算值与原
> JSON 逐项一致 (independent_recompute.json ALL_MATCH) 只是确定性代码的必然结果, 不是
> 数字正确的证据——它只证明两个程序算了同一个东西, 不证明它们算对了东西。所谓"独立
> 重算"是把 surface/deep/H 逻辑重写一遍, 不是换算法、不是换数据来源: 若原代码与重写
> 代码共享同一个建模错误 (例如闭式模型的某个理想化假设错了), 这套验证结构性失明,
> 而 TRIAL-RECEIPT.md「已知局限」第 2 条自己承认了这一点。更糟的是, claim 自己声明的
> 预期区间已经被打破: T5000 shift=0.1655 低于预注册下沿 0.17 (independent_recompute.json
> per_hardware.T5000.shift), 验收方只能事后宽免 (C3b-verdict.md §1)。而理论路线本身
> ——按信息增益对特征重排——与教科书先例 ID3/C4.5 正面撞车, 试跑材料对此只字未提。
> 资深审稿人不会接受"可复现"作为"正确"的证据。

## Thread 2 — 逐点裁定 (adjudication 线程)

输入: Thread 1 备忘录逐字原文 + trial/ 证据文件 (TRIAL-RECEIPT.md / acceptance-request.md /
C3b-verdict.md / independent_recompute.json / verify_results.json)。零先前上下文。
将攻击分解为 5 个原子拒绝点, 逐点三分类 (answered_by_current_text / partially_answered /
still_unresolved), 证据引文件:行。

### Point P_1: 同 seed 同采样 → 复现是同义反复
**Attack claim**: 重算与原 run 共用 seed=42 与采样, 逐项一致只是确定性代码的必然, 不构成数字正确的证据。
**Verdict**: answered_by_current_text
**Evidence (or lack of)**: TRIAL-RECEIPT.md 行 39 与 C3b-verdict.md 行 44 明示该局限: 复现目标本就是"计算正确"而非"采样代表性"。claim 文本 (acceptance-request.md 行 22) 也只主张"重算值落在预期区间", 未把"代表真实数据分布"作为主张对象。
**Severity if unresolved**: major
**If unresolved, recommended fix**: (不适用 — 已化解; 若扩大 claim 至"代表性", 需多 seed/多采样重跑。)

### Point P_2: "独立重算"实为同逻辑重写, 共享建模错误则结构性失明
**Attack claim**: independent_recompute 是重写 surface/deep/H 逻辑, 非换算法; 若两套代码共享同一建模错误, 验证无法捕获。
**Verdict**: answered_by_current_text
**Evidence (or lack of)**: TRIAL-RECEIPT.md 行 40 与 C3b-verdict.md 行 45 逐字承认该局限 ("无法捕获两套代码共享同一建模错误")。claim 范围限于"闭式计算可复现", 不主张"闭式模型对真实系统的普适正确性"。
**Severity if unresolved**: major
**If unresolved, recommended fix**: (不适用 — 已化解; 若要主张模型正确性, 需对真实 trace 做端到端验证。)

### Point P_3: 预注册预期区间被打破 (shift 下沿 0.1655 < 0.17)
**Attack claim**: claim 自声明预期 shift 0.17–0.23, 但 T5000 实测 0.1655 低于下沿, 验收方只能事后宽免。
**Verdict**: partially_answered
**Evidence (or lack of)**: independent_recompute.json per_hardware.T5000.shift=0.1654691039364547 (事实成立); TRIAL-RECEIPT.md 行 11/18 标注"边缘 [不确定]"; C3b-verdict.md 行 29–30 裁定 match 但理由是"复现目标达成, 非新发现"。这是验收方的有意立场 (intentional position), 非文本自动化解: 复现目标下成立, 但若把"落在预期区间"当作 claim 的一部分, 则该点未被化解。
**Severity if unresolved**: minor
**If unresolved, recommended fix**: 在 claim 文本中显式区分"复现一致性"与"预期区间符合性"两个断言, 或把 T5000 预期下沿修正为 0.165 并记录修正理由。

### Point P_4: 教科书先例 ID3/C4.5 information gain 撞车, 材料只字未提
**Attack claim**: 按信息增益对特征重排与 ID3/C4.5 的 information-gain 分裂准则正面撞车, 试跑材料未引用、未区分, novelty/定位存疑。
**Verdict**: still_unresolved
**Evidence (or lack of)**: trial/ 全部 6 份材料 (TRIAL-RECEIPT.md / acceptance-request.md / C3b-verdict.md / independent_recompute.json / verify_results.json / idea53-repro.json) 中无任何对 ID3/C4.5 或 information-gain 先例的引用、区分或定位声明 (逐文件通读确认)。
**Severity if unresolved**: major
**If unresolved, recommended fix**: 在 claim 材料中补一段定位: idea53 的信息增益重排与 ID3/C4.5 分裂准则的异同 (闭式 vs 贪心建树、flip/shift/H(D|S) 指标 vs 纯度增益), 或明确本试跑不主张 novelty、仅主张复现。

### Point P_5: "24 置换不变"证据强度
**Attack claim**: 24 置换不变性仅由"range 窄"佐证, 未证明精确不变。
**Verdict**: answered_by_current_text
**Evidence (or lack of)**: independent_recompute.json perm.*.n=24 且各平台 flip/shift range 极窄 (如 5090 flip [0.525125,0.5304], 宽度 0.0053; T5000 shift 宽度 ~0.0017); TRIAL-RECEIPT.md 行 15 将其判 match。claim 主张"24 置换一致", 窄 range 与该主张相符。
**Severity if unresolved**: minor
**If unresolved, recommended fix**: (不适用 — 已化解; 若要"精确不变", 需报告置换间最大绝对差而非 range。)

## Summary
Total rejection points: 5
- answered_by_current_text: 3  (P_1, P_2, P_5)
- partially_answered: 1  (P_3, severity minor)
- still_unresolved: 1  (P_4, severity major)

## Net assessment
该 claim 在"闭式计算可独立复现"的限定范围内能扛住攻击: 攻击最强的两点 (P_1 同 seed
同义反复、P_2 共享建模错误) 都被材料自身的局限性声明化解, 因为 claim 从未越界主张
"代表性"或"模型正确性"。但仍有 1 个 still_unresolved 点 (P_4, major) 直接打在理论路线
的定位上 (ID3/C4.5 撞车未引用), 另有 1 个 partially_answered 点 (P_3, minor, 验收方有意
立场)。按映射表, 只要存在 major 级 still_unresolved, 就不能 PASS。

## Top action items (in priority order, max 3)
1. 补 ID3/C4.5 定位段 (化解 P_4): 说明信息增益重排与分裂准则的异同, 或显式声明本试跑仅主张复现。
2. claim 文本区分"复现一致性"与"预期区间符合性" (化解 P_3 的残余)。
3. 若要升级 claim 至"代表性/模型正确性", 增加多 seed 重跑与真实 trace 端到端验证 (当前范围不需要)。

## verdict 映射表 (机械计算, 非模型自评)

输入 (来自上方 Summary):
- still_unresolved = 1, 其中 critical = 0, major = 1 (P_4), minor = 0
- partially_answered = 1, 其中 major/critical = 0, minor = 1 (P_3)

逐行匹配 kill-argument.md 映射表 (首个命中行生效):
| 候选行 | 条件 | 命中? |
|---|---|---|
| FAIL / unresolved_critical | ≥1 still_unresolved @ critical | ✗ (critical=0) |
| WARN / unresolved_major_or_minor | ≥1 still_unresolved @ major 或 minor, 且无 critical | ✓ (P_4 major) |
| WARN / partial_critical_or_repeated_major | 0 still_unresolved | ✗ |
| PASS / defense_survives_with_minor_partial_only | 0 still_unresolved | ✗ |
| PASS / defense_survives | 0 still_unresolved 且 0 partially_answered | ✗ |

## 最终 verdict
verdict: **WARN**
reason_code: **unresolved_major_or_minor**
summary: "复现 claim 在限定范围内可防御; 1 个 major 未化解 (ID3/C4.5 定位缺失) 挡住 PASS"

## 可测数字 (C4 病②)
kill-argument verdict=WARN, still_unresolved=1 点 (P_4 major), 其中 3/5 点已被现有
证据化解 (answered_by_current_text), 1 点部分化解 (P_3 minor, 有意立场)。
