# 04 — RV3G6-o3-claim-rejudge-scaffold · 执行验证日志

> goal: claim 级独立重判的仓库内闭环骨架 · 分支 ralph/rv3g6-o3-claim-rejudge-scaffold · 2026-10-30

## A1 — sample-plan.json ✅

机算生成（非手写），源 = 冻结 hit-matrix.json @ commit db820c2：
- counts = {total: 248, P0: 150, P1: 98, gold_strict: 40}（assert 内置断言通过）
- 独立复核（第二次 python 进程）：cell (run,node) 集合 == hit-matrix 全 cell 集（set 相等，无重复无遗漏）；每 cell `h_id_frozen` 与冻结矩阵逐格一致
- 分层语义写入文件头（P0 = FM-2 漏判方向优先；priority 只定顺序不定口径——02.5 X2）

## A2 — judge-protocol-batch1.md ✅

- blind-packet 白名单三字段（B1 run_text / B2 claim_text / B3 node_id）+ 黑名单五条（gold-tree 全文 / hit-matrix 现值含 h_id_frozen / 他判者结论 / 既有评分数字 / 真实判断示例）
- 结果 schema byte-stable（§3 jsonc 块 + 五条硬约束）；与 assert docstring/实现字段一致性 grep 验证 OK
- S2 §5.1 限定语 **byte-exact 引用验证通过**（python difflib 逐字比对 = True）
- U-K1（κ 公式 UNRESOLVED）显式登记于 §4；kappa_receipt_ref 只留存在性引用不复核数值
- 零 h 值红线自查：全文无任何对具体 (run, node) 的实质判定（示例均为占位符 `<非空 str>` / `<run 原文连续子串>`）

## A3 — assert-o3-claim-rejudge.py ✅

三分支主流程实跑（当前 ablation 面常态）：

```
$ python3 bench/rubric-v3/ablation/scripts/assert-o3-claim-rejudge.py
[SIGNAL] blocked-on-external: rejudge-results.json absent (等 fresh-context judge 通道执行 rejudge/judge-protocol-batch1.md 后零改动接入)
exit=0
```

现场修复一处自引入缺陷：PROTOCOL_REF 初版用 `.replace()` 拼字符串（无意义防御写法），改为直接字面量。

## A4 — 变异测试（fixture 写入 rejudge/rejudge-results.json，测毕即删）✅

| 场景 | 构造 | 实测 | 预期 | 判定 |
|------|------|------|------|------|
| M1 零 flip | h_claim := h_id 全 248 cell（evidence 取冻结值，非子串者换 run 前 30 字符真子串） | exit 0；M1 full = 248/248、M1 gold = 40/40、M2 = 8/8；「zero flips」行输出 | PASS + identity 读数 | ✓ |
| M2 已知 flip 集 | 3 个零命中 gold 节点（N-2.1/N-2/N-1.3）×8 run 全翻 0→1（24 cell）+ run1 N-3.2.2 翻 1→0（1 cell）= 25 flip | exit 0；M1 full = 223/248（0.8992）、M1 gold strict = 15/40（0.3750）、M2 = 0/8；flip 切片表逐格正确（N-2.1 0->1: 8 [gold-strict] 等四行） | 偏离量数学正确 + 方向切片报告 | ✓ |
| M3a evidence 编造 | h_claim=1 但 evidence = 不存在句 | exit 2；「NOT a contiguous substring」 | fail-loud | ✓ |
| M3b h=0 带 evidence | 任一 h=0 cell evidence 改字符串 | exit 2；「must have evidence=null」 | fail-loud | ✓ |
| M3c 覆盖缺口 + 非二值 | 删 3 cell + 一 cell h_claim=2 | exit 2；「coverage gap: 3 cells missing」+「h_claim not binary」双报 | fail-loud | ✓ |
| M4 缺文件 | 删除 results JSON | exit 0；[SIGNAL] blocked-on-external | 常态 | ✓ |

M2 偏离量手工核算核对：25 flip 中 24 个在 gold strict 切片（3 节点×8）+ 1 个（N-3.2.2）→ gold 一致 = 40−25 = 15 ✓；全部 8 run 各含 ≥1 flip → M2 = 0/8 ✓。

fixture 清理验证：`rejudge/` 目录最终仅含 judge-protocol-batch1.md + sample-plan.json（git status 确认无 untracked 残留）。

## A5 — 冻结面零修改 + 回归 ✅

- `git status --short`：untracked 仅 `bench/rubric-v3/ablation/rejudge/`（新目录，A1/A2）+ `scripts/assert-o3-claim-rejudge.py`（A3）；hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / o3-claim-list.md / DRAFT v2 / gmr-criterion-freeze.md **零 diff**
- 既有断言回归（repo root 执行，基线维持）：
  - assert-o3-claim-list.py → exit 0，4/4 检查组 PASS
  - assert-goldrank-threshold.py → exit 0，31 PASS / 0 FAIL
  - assert-gmr-recompute.py → exit 0，11 PASS / 0 FAIL
- 注：三个脚本均要求从 repo root 运行（相对路径 BASE），scripts/ 目录下直跑 FileNotFoundError——既有行为非本 goal 引入（r140 crossdomain 同约定用 Path(__file__).parents[4] 绝对化，本脚本沿用该写法故任意 cwd 可跑，两者并存无冲突）

## 负面结果 / 边界声明

1. **U-K1 κ 公式缺口未解决**（非本 goal 范围）：o3-claim-list §4.3 只给 κ 门禁的顺序关系与阈值语义，具体公式（Cohen's/Fleiss'/条目粒度）无任何冻结件文字化。处置 = protocol 只引用 + assert 不计算 + queue 导出裁定候选。若未来裁定为「单判者批次免 κ」，schema 的 kappa_receipt_ref=null 分支已覆盖。
2. **evidence 子串检查严于原协议措辞**：TASK-ablation Step 1 说「真实存在的句子（不许改写）」，本实现机判化为「连续子串」——比「句子」更严（禁止跨句拼接、禁止空白规范化）。这是有意的从严选择（防编造 > 判者便利），已在 protocol §3 硬约束 3 与 02.5 X5 双向登记；若实际 judge 执行中误报率高，放宽需走新 goal（schema 是 byte-stable 冻结件）。
3. **M1/M2 偏离不是 FAIL 条件**（预注册规则 4）：数据齐备分支常态 exit 0——FM-2 检验目标就是找 flip，把偏离当 FAIL 会让整个补数机制自我否定。可信性错误全部由 ② schema 分支拦截（exit 2）。此语义预注册于 docstring，04.5 应重点攻击。