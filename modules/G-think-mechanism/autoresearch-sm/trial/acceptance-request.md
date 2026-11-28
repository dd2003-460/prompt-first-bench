# Acceptance Request — idea53 核心数字复算 (零上下文验收)

# origin: ai
验收方: 跨模型族 reviewer (非 qwen 族) · 验收对象: run idea53-repro 的 REPRODUCE + VERIFY 两 phase (均 done, 未 accepted)

## 材料清单 (仅 raw 数据 + 重算脚本 + 回执, 无过程叙述)

| 材料 | 路径 | 用途 |
|---|---|---|
| 重算脚本 (独立重写, 非原脚本) | pfb/tasks/autoresearch-sm/trial/independent_recompute.py | 复现 flip/shift/H(D\|S)/flat/24置换 |
| 重算结果 | pfb/tasks/autoresearch-sm/trial/independent_recompute.json | 重算数字 |
| 核验脚本 | pfb/tasks/autoresearch-sm/trial/verify_checks.py | T5000 手算 flip + flat=0 多 seed/常数 |
| 核验结果 | pfb/tasks/autoresearch-sm/trial/verify_results.json | 核验数字 |
| 回执 | pfb/tasks/autoresearch-sm/trial/TRIAL-RECEIPT.md | 数字表 + 状态机记录 + 局限 |
| 原始脚本 (被复现对象) | pfb/modules/F-theory/research/idea53-theory-{flip,mi,reorder}.py | 对照 |
| 原始结果 JSON | pfb/modules/F-theory/research/idea53-theory-{flip,mi,reorder}.json | 对照基准 |
| 预注册 commit | eb1b0598c (2026-11-24 17:39:54 +0800) | 时间序核验 |
| 数据 commit | 718394ece (2026-11-24 18:06:28 +0800) | 时间序核验 |

## 验收问题清单

1. **数字对不对?** 重算值 (independent_recompute.json) 是否落在预期区间:
   flip 43–56% / shift 0.17–0.23 / H(D|S) 0.71–0.77 bits / flat 对照=0 / 24 置换一致?
   (注意: T5000 shift=0.1655 低于下沿 0.17, 与原 JSON 一致 — 请裁定是否算 match。)
2. **预注册时间序成立吗?** eb1b0598c 是否早于 718394ece 且为其祖先 (git merge-base --is-ancestor)?
3. **flat=0 稳健吗?** verify_results.json 的 9/9 configs (3 seed × 3 flat 常数) 是否支持 "flat-rate 下深层修正精确=0 非巧合"?

## 状态机终态 (验收起点)

```
run idea53-repro
  ✓(unaccepted)  REPRODUCE  [done]  → independent_recompute.json
  ✓(unaccepted)  VERIFY     [done]  → verify_results.json
  resume → REPRODUCE
```
验收通过 → 由 reviewer 调 run_state.py accept (verdict_id + reviewer, 跨族)。
