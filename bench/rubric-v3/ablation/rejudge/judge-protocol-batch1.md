# claim 级独立重判 · 判者协议 batch1（judge-protocol-batch1）

> goal: RV3G6-o3-claim-rejudge-scaffold · r141 · 分支 ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30
> 上游：`o3-claim-list.md` §4.4（「在独立重判完成前，本清单只定义判据、不产生任何新的 h 值」）+ §5.2 U1
> 状态：**协议冻结件**——本文定义 blind-packet 输入边界与结果 JSON schema；修改 = 新 goal + APPROVALS.md 登记。
> **本协议不产生任何 h 值**。它只规定未来 judge 批次「能看到什么 / 必须交出什么」。

---

## 1. 执行对象与采样面

- 判据源：`o3-claim-list.md` §2.2 的 31 条原子 claim（唯一定义源，不得另行定义或退回 ID 判据——§6 规则 1）
- 产出源：`ablation/runs-C0-run1.md` … `runs-C0-run8.md`（冻结，只读）
- 采样面：`rejudge/sample-plan.json`（r141 落盘）——**全量 248 cell 无抽样**；`priority` 字段（P0=h_id=0 共 150 / P1=h_id=1 共 98）只定执行顺序，不定统计口径（02.5 X2）。judge 批次按 P0→P1 顺序消费以优先覆盖 FM-2 漏判方向。
- 分层标签来源声明：sample-plan 的 `h_id_frozen` 字段是冻结 hit-matrix 现值的**只读镜像**（用于分层与未来偏离计算），不是本 goal 的新判定。

## 2. blind-packet 结构（输入白名单，机判化 §4.1 独立性定义）

每个 (run, node) cell 的判者输入 = 且仅 = 以下三件（白名单外内容出现在判者上下文中即该 cell 判定作废）：

| # | 字段 | 内容 | 来源 |
|---|------|------|------|
| B1 | `run_text` | run 产出**全文**（原样，不改写不截断） | `ablation/runs-C0-run{N}.md` |
| B2 | `claim_text` | 该 node 对应行的 claim 文本（§2.2 表第二列原文）+ 「方向内嵌说明」列（no 的典型情形） | `o3-claim-list.md` §2.2 |
| B3 | `node_id` | 节点 ID（如 N-3.2.2）——仅作输出定位键，**不携带 gold-tree 语义**（gold-tree 全文不在白名单内） | sample-plan.json |

**黑名单（判者上下文禁止出现）**：
- gold-tree.md 全文（含 SHARE 份额 / 瓶颈标记 ■/★ / 数值）
- hit-matrix.json 现值（含 `h_id_frozen` 分层标签——防止锚定效应；judge 不知道旧判据怎么判）
- 他判者结论 / 分歧日志
- gmr / top-10 / 任何既有评分数字
- 本协议 §3 的输出示例中除占位符外的任何真实判断

> 边界注记：B2 的 claim 文本本身经过防泄漏检查（assert-o3-claim-list.py ②，零 gold 专有数值），故 claim 进白名单不构成答案通道。B1 是 run 自产文本，天然合法。

## 3. 结果 schema（byte-stable，消费侧 = assert-o3-claim-rejudge.py docstring 同源）

落盘文件：`bench/rubric-v3/ablation/rejudge/rejudge-results.json`（judge 批次产出；本 goal 不创建该文件）

```jsonc
{
  "schema_version": "rejudge-results/v1",
  "judge_id": "<非空 str>",            // 判者标识（家族信息可另注，见 §5 S2）
  "judge_family": "<str>",             // 底座家族声明（S2 限定语消费用；同族 = 不消除 S2）
  "blind_protocol_ref": "rejudge/judge-protocol-batch1.md",
  "kappa_receipt_ref": null,           // 可选：指向 kappa-receipt.json 相对路径（§4.3 顺序：κ 门禁先于聚合；
                                        //   公式 UNRESOLVED U-K1，本 schema 只留存在性引用，不复核数值）
  "cells": [
    {
      "run": "run1",                   // ∈ sample-plan runs（8 个）
      "node": "N-0",                   // ∈ sample-plan nodes（31 个）
      "h_claim": 1,                    // ∈ {0,1} —— 判者对该 cell 的二值判定
      "evidence": "<run 原文连续子串>"  // h_claim=1 时必填：必须是 run_text 的连续子串（机判 in 检查）；
                                        //   h_claim=0 时 = null（无 evidence 义务，§2.2 只要求 yes 附依据）
    }
    // … 覆盖 sample-plan 全部 248 cell（缺一即 schema 违例 exit 2）
  ]
}
```

**schema 硬约束（assert 机判，违例 = ERROR exit 2 fail-loud）**：
1. `cells` 的 (run, node) 集合 == sample-plan 全集（248，无重复无遗漏）
2. `h_claim ∈ {0,1}`（严格二值，无 null/中间态）
3. `h_claim=1 → evidence 为非空 str 且是 `runs-C0-{run}.md` 全文的连续子串`（防编造 evidence；X5 边界情形：多句拼接/空白改写均 FAIL，判者须原样复制单句）
4. `h_claim=0 → evidence == null`（双向封闭，防「no 也附理由文本」混入字符串域）
5. `schema_version` / `blind_protocol_ref` 固定值（防版本漂移张冠李戴）

## 4. 聚合与质检引用（只引用，不改写）

- **聚合规则**：o3-claim-list §4.2（N=3，≥2/3 yes → h_v=1；无平票态）。本协议 batch1 定义的是**单判者**结果格式；多判者聚合在 ≥2 个 judge 批次落盘后按 §4.2 执行，聚合产物另开文件（不覆写单判者原始结果）。
- **κ 门禁顺序**：o3-claim-list §4.3——条目层 κ 质检在聚合之前；低于预注册下限则本轮判定作废重判。**U-K1（UNRESOLVED）**：κ 具体计算公式（Cohen's/Fleiss'、条目粒度）未在冻结件中文字化，本协议不发明；裁定候选已导出 queue。`kappa_receipt_ref` 字段的存在性可机判、数值不复核。
- **M1/M2 口径**：o3-claim-list §3.1 定义式（M1 = cell 级一致率，全量 248 + gold strict 40 两切片强制并报；M2 = run 级 per-run 向量完全一致率）。实际读数 = 与 1.0 identity 锚点的偏离量，偏离按 (node, 方向) 切片逐格报告（§3.2 口径声明 3）——复算由 assert-o3-claim-rejudge.py 承担，judge 不自报 M1/M2（防双源漂移）。

## 5. S2 同源偏置限定（byte-exact 引用 o3-claim-list §5.1，叠加生效）

> 本文引用的 O3 构念效度数字（gold mean rank / top-10 计数 / top-5 计数）**均为「相对 Lead-gold」的度量**：gold 树由单一作者构建，rubric 题面补丁与该 gold 答案结构同构，故「命中 gold」与「被题面引导写出 gold 形状」在当前设计下不可区分；且全部 p̃ 估计来自**同族双 judge**（qwen3.8-27b 底座，上下文独立但非家族独立），p̃ 层的系统性偏差（零命中高估 + 保守下界效应）未被消除。**在以下二者之一闭环前，这些数字不得作为 rubric-v3 有效性的独立证据对外宣称**：(i) 双 gold——由未参与 pfb 的第三方/异族模型独立构建同域 gold，报两 gold 命中差值作为同源偏置上界；(ii) 异源第三 judge（queue 项 R5.2-third-scorer）完成 p̃ 重估 + 构念效度复测。

本批 rejudge 结果同样受此限定：`judge_family` 字段如实申报；同族判者的 rejudge 产出**不构成** S2 闭环证据，只构成判据可执行性（#13）的补数。引用本批任何 M1/M2 数字时，本段限定语 + gmr-criterion-freeze.md §4 tie-break 限定**叠加生效**（o3-claim-list §5.1 末句）。

## 6. 执行降级与常态

- 当前状态：**unverified（blocked-on-external）**——需 fresh-context judge 通道（arena 会话；工具纪律禁 subagent）。通道到来后按本协议零改动执行：逐 cell 组 blind-packet → 判者盲判 → 结果按 §3 schema 落盘 `rejudge-results.json` → 跑 `assert-o3-claim-rejudge.py` 取 verdict。
- 常态断言行为：`rejudge-results.json` 缺失时 assert 输出 `[SIGNAL] blocked-on-external` + exit 0（中性状态，非门禁失败——区别于 assert-kappa-receipt.py 的 FAIL 语义，理由见 loop-artifacts/stages/02.5 X3）。