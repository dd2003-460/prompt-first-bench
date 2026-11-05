# 双裁判盲评任务书

## 背景
7 个 prompt 变体 × 3 独立 run = 21 份答卷已完成。现在需要两个独立裁判对每份答卷按统一评分标准打分，用于计算评分者间一致性和消融归因。

## 输入文件
- `blind-eval/doc-*.md` — 21 份匿名答卷（A1-A3, B1-B3, C1-C3, D1-D3, E1-E3, F1-F3, G1-G3）
- `judge-packet-template.json` — 评分标准（rubric_items + O3 claim 清单）

## 匿名映射

> **2026-11-02 r180 泄漏修复**：映射表原内嵌于此（裁判读任务书即失去盲态，JUDGE-PROTOCOL.md §5 登记）。现移至 `blind-eval/anon-mapping.json`（仅 Lead 持有），本处不再保留任何映射内容。历史溯源见 git log。

## 评分要求
1. **盲评**：裁判只看 doc-*.md 的内容和 rubric 标准，不知道哪份是哪个变体。
2. **双裁判**：两份独立的评分（Judge-1 和 Judge-2），各自独立打分。
3. **每个 rubric item 独立打分**：按 judge-packet-template.json 里 rubric_items 的 criteria 逐项打 0/1/2 分。
4. **O3 claim 覆盖**：对每份答卷检查 o3_claim_list_embedded 里的每条 claim 是否被覆盖（covered/not_covered）。
5. **输出格式**：JSON，结构见下方 schema。

## 输出 schema
```json
{
  "judge_id": "Judge-1",
  "scores": {
    "A1": {
      "items": {"item_id_1": 2, "item_id_2": 1},
      "o3_claims": {"claim_1": "covered", "claim_2": "not_covered"},
      "total_score": 15.5,
      "max_score": 20
    }
  }
}
```

## 提交要求
- 两个裁判各一个 JSON 文件：`blind-eval/judge-1-scores.json`, `blind-eval/judge-2-scores.json`
- 提交到当前分支
- commit message: `feat(blind-eval): dual-judge scores for 21 docs`
