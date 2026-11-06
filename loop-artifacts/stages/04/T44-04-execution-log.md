# T44 · Related Work Update (Nov 2026) — 阶段 04：执行与客观验证记录（execution-log.md）

> 创建时间：2026-11-06 UTC · 阶段：04（执行与验证）
> 规则包：`loop/prompt-first/00-common-review.md` + `04-execution-verification.md` + `04.5-final-review.md` + `loop/modules/gates-postcheck.md`（闸 1 & 闸 2）

---

## 1. 步骤执行轨迹（严格对照阶段 03 S1–S3 计划）

| 步骤 | 执行动作 | 结果与中间修正记录 |
|-----|---------|------------------|
| **S1** | 编写主交付物 `loop-artifacts/stages/04/T44-related-work-update.md` | 初稿生成完成，含前置范围/局限披露、17 篇新增引用总表（`#32`–`#48`）、`§2.1`–`§2.6` 英文建议段落 + 新增 References、以及 `T1`–`T6` 六条矛盾/张力清单。 |
| **S2 (第 1 轮)** | 执行一次性内存模拟合入与正则校验脚本 | 发现两处需立即修正的精确度问题：① 初稿英文段落偏长（1,191 词），且导语中的词数估算未实测；② 初稿行号锚点相对偏移了 4–5 行（如 `L32` 实为 `L37`、`L380` 实为 `L376`）。 |
| **S2 (第 2 轮修订与复验)** | 逐行核对 `paper-draft.md` 真实 1-based 行号（`L37`, `L43`, `L49`, `L53`, `L57`, `L61`, `L376`），精炼 §2 英文段落，并重跑内存模拟合入断言脚本 | **全部断言 `EXIT 0` 通过**：17 篇引用双向完全闭合、零孤儿引用、与既有 31 篇零重叠；合入后正文（不含 References 与 Appendices）由 `6,085` 词增至 **`6,713` 词**（净增 `+628` 词，严格处于 `4,000–8,000` 词正文区间内），含全量 References（新增 `+422` 词）与 Appendices 全文件由 `7,091` 词增至 `8,141` 词；导语数字已同步为精确机测值。 |

---

## 2. 确定性机器校验回执（原始 stdout 留存）

执行校验命令（沙箱仓库根目录 `/home/user/prompt-first-bench`，零临时文件残留）：
```json
{
  "table_1_count": 17,
  "new_refs_total": 17,
  "new_refs_2026_09_to_11": 14,
  "new_refs_2026_07_to_08": 3,
  "all_have_arxiv_or_doi": true,
  "overlap_with_existing_31": [],
  "orphan_refs_missing_in_sec2_prose": [],
  "draft_body_words_before": 6085,
  "merged_body_words_after": 6713,
  "net_sec2_body_words_added": 628,
  "new_refs_words_added": 422,
  "draft_full_words_before": 7091,
  "merged_full_words_after": 8141
}
ALL SIMULATED-MERGE & CITATION ASSERTIONS PASSED (EXIT 0)
```

---

## 3. 三道闸阶段 04 交付前自检（对照 `loop/modules/gates-postcheck.md`）

- [x] **闸 1（数字必溯源）**：
  - 交付文档中的全部外部文献实证数字均逐一锚定阶段 02 一手 arXiv Atom API / ACL Anthology 摘要与正文（如 AgentHop `1,011` 题；CXBench `80.1%` 假通过 / `13.8%` 双通过；Backtrader-Bench `90.0%` vs `73.0%` / `+17 pp`；CausalCoT `+12` 至 `+21 pp`；RE-ZS-CoT `20` 模型 / `+44 pp`；Jia & Mu `28,584` 轨迹 / `98.8%` / `16×`；Ayyagari v2 `~5%` / `~40%` / $\tau=0.42\text{–}0.64$ / `8/15`；Kumar `100%` 自洽 vs `51%` 真值准确率；WANDR `500` 任务 / `0.363` Soft F1 / `0.133` Hard F1 / `96.9%–99.4%` vs `55.6%–80.4%`；MisKnow-Agent `0% → 54.7%`；DAGent `+5.3 / +5.8`；Schwager ECE `0.20 → 0.006`）。
  - 交付文档中的本文自身实验数字全部精确对齐 `experiments/stage-ablation/paper-draft.md`（S5 vs S0 `+0.182`；M7 `0.306 → 0.256`；M2 `0.037–0.618`；同族裁判偏严 `~0.15`；噪声底 `±0.10`；S7T M1 `0.771 → 0.480`；S7V M1 `0.762`）。
  - 合入词数与行号全部以 Python 脚本实测值为准，彻底消除了首轮未测先估数字。
- [x] **闸 2（自洽不双标）**：
  - 对支持本文的文献（如 Meyer `2609.20541`、Hsiao `2609.10996`、Chae `2608.18091`）与挑战本文的文献（如 Ghosh `2610.25846`、Yin `2610.24320`、MisKnow-Agent `2607.20891`）采用**完全一致的证据权重与审慎标准**——例如对 10 月下旬预印本统一披露未同行评议状态，对 WANDR 披露厂商利益背景，对本文 M2 与 S7V 主动依据反方证据收窄外推口径。

**阶段 04 自检结论**：执行产物真实落盘并通过确定性机检（status: pass → 推进至阶段 04.5 最终复核）。
