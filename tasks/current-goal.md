# Goal: RV3G6-o3-claim-rejudge-evidence-audit — hit-matrix 98 个 h=1 evidence 的 verbatim 合规审计

> 创建：2026-10-30 · ralph loop runner（自找 goal——queue 待办区空扫后按协议阶段 A.1 兜底路径：扫冻结数据已知缺陷面）
> 依据：TASK-ablation.md Step 1 硬约束「每个 h=1 必须附 evidence，evidence 必须是 run 文件里真实存在的句子（不许改写）」+ o3-claim-list §3.2 口径声明 4（已核 27/98 evidence 含 gold-tree 数值 token——**只查了数值泄漏方向，verbatim 子串性从未机判过**）。r141 骨架把「evidence ⊆ run 原文连续子串」确立为 rejudge 结果的 schema 硬约束（防编造机制），但**冻结 hit-matrix 自身的 98 条 evidence 是否满足同一标准从未验证**——若旧判据数据本身有改写/拼接 evidence，则 M1 identity 锚点（h_claim := h_id 基线）建立在不合规数据上，FM-2 补数的分母可信度受损。

## 【目标】
写 `bench/rubric-v3/ablation/scripts/assert-hitmatrix-evidence.py`：对冻结 hit-matrix.json 全部 98 个 h=1 cell 的 evidence 做机判合规审计——(a) 非空性；(b) 是所属 run 文件全文的**连续子串**（verbatim，不许改写/拼接/空白规范化）；(c) ≤40 字惯例核查（TASK-ablation 原文「≤40字」，超长者报 SIGNAL 不 FAIL——原协议是惯例非硬门禁，语义边界显式登记）；(d) 跨 run 张冠李戴检查（evidence 不得主要出自其他 run 文件）。产出逐格审计表 + 汇总 verdict。**预期结果两种都接受**：全合规 → PASS exit 0（补上缺失的验证链一环）；存在违规 → FAIL exit 1 + 逐格清单（负面结果如实落盘，不美化——违规 evidence 的处置走 APPROVALS/新 goal，本脚本只暴露事实）。

**范围定位**：纯仓库内工作（读冻结 JSON + 8 个 run 文件，零外部依赖，零 h 值判定——只查文本出处合规性，不判命中语义正确性）。

## 【阶段】
01 分解 → 02 研究（hit-matrix evidence 分布 + run 文件结构精读）→ 02.5 交叉核对（§3.2 声明 4 的 27/98 数值 token 计数复算 + 与 r141 子串标准对齐性）→ 03 行动分解 → 04 执行验证（脚本落盘 + 实跑 + 变异测试 ≥3 场景）→ 04.5 反方复核

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 协议参考（只读）：`ablation/TASK-ablation.md` Step 1（evidence 规则原文）/ `o3-claim-list.md` §3.2 口径声明 4 / r141 `rejudge/judge-protocol-batch1.md` §3 硬约束 3（子串标准同源）
- 事实源（只读冻结）：`ablation/hit-matrix.json` / `ablation/runs-C0-run1..8.md`

## 【验收标准】
- [ ] assert-hitmatrix-evidence.py 落盘；docstring 预注册判定语义（FAIL 条件 vs SIGNAL 条件 byte-stable）
- [ ] 实跑产出逐格审计表（98 行 h=1 cell + 判定）+ 汇总；exit code 与预注册一致
- [ ] 变异测试 ≥3 场景：篡改 evidence（改写词）→ FAIL / 跨 run 拼接 → FAIL / 超长 evidence → SIGNAL 不 FAIL
- [ ] §3.2 声明 4 的「27/98 含 gold 数值 token」独立复算核对（数字一致或勘误登记）
- [ ] 冻结数据零修改（git status 验证）
- [ ] 04.5 verdict pass；queue 更新（追加本 goal 完成条目 + 视实跑结果导出后续候选）

## 【失败降级】
- 若 run 文件存在编码/空白变体导致子串检查系统性误报（如 CRLF vs LF）→ 先做归一化对照实验（原始 vs normalize 双跑），误报面 >0 时登记边界并采用「原始优先、normalize 作 SIGNAL 对照」双轨输出，不静默放宽
- 若发现真实违规 evidence → 不修改冻结 hit-matrix（红线），FAIL 如实落盘 + APPROVALS.md 登记处置选项（修数据需成璐裁定），导出修复候选