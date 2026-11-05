# 阶段 04 执行验证 — RV3G4-prior-source-assert

> origin: ai · 2026-10-30 · 对象 `bench/rubric-v3/ablation/scripts/assert-prior-source.py`（唯一改动文件）+ `prior-estimates.json`（只读）

## J1 基线复验

```
$ python3 assert-prior-source.py; echo $?
SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict
[PASS] ① p_tilde_provenance top-level object exists
[PASS] ① independent_sources is non-empty list
[PASS] ② source[0] (primary) judge_id non-empty str
[PASS] ② source[0] (primary) artifact resolvable under ROOT
[PASS] ② source[1] (blind-reestimate) judge_id non-empty str
[PASS] ② source[1] (blind-reestimate) artifact resolvable under ROOT
[PASS] ② blind-reestimate judge_id byte-exact vs judge-blindtest-r1.json:judge
[PASS] ③ distinct judge_id count >= N_MIN=2
RESULT: PASS (all checks green; signal-only — see header)
0
```
8/8 PASS exit 0，与 r130 落盘基线一致。

## J2 变异测试（防单源/缺失能力实证，/tmp 沙盒，冻结面零触碰）

沙盒方法：脚本副本改 `ROOT` + `PRIOR` 指向 /tmp 变异数据（原脚本在原路径跑会因 `Path(__file__).parents[4]` 在 /tmp 下 IndexError——首个沙盒尝试即暴露此点，已修正为显式绝对路径）。

| 变异 | 数据操作 | exit | FAIL 行 |
|---|---|---|---|
| M1 单源 | independent_sources 截为 1 条 | 1 | `[FAIL] ③ distinct judge_id count >= N_MIN=2 — distinct=['lead-main-session …']` |
| M2 无 provenance 块 | 删除顶层 p_tilde_provenance | 1 | `[FAIL] ① p_tilde_provenance top-level object exists — type=NoneType` + `[FAIL] ① independent_sources is non-empty list` |
| M3 空列表 | independent_sources = [] | 1 | `[FAIL] ① independent_sources is non-empty list — len=0` + `[FAIL] ③ distinct … distinct=[]` |

三场景全部显式 FAIL exit 1，FAIL 行定位到具体检查项——「source 字段缺失/单源 = FAIL」是机判实证，非纸面声明。

## J3 队列原文四项核销表

| 队列候选原文要求 | 落地位置 | 状态 |
|---|---|---|
| 「≥N 个独立 p̃ 生成源」 | 检查③ `distinct judge_id count >= N_MIN=2`（docstring 声明 ≥3 异族属遗留 #1 范围） | ✓ 核销（N=2 最小分界，限定语双登记） |
| 「source 字段缺失 = FAIL」 | 检查①（M2/M3 实证 exit 1） | ✓ 核销 |
| 「单源 = FAIL」 | 检查③（M1 实证 exit 1） | ✓ 核销 |
| 「signal-only 或 verdict 二选一在 01 定」 | verdict 型（exit 1 阻断）——r130 选定，本 goal 01 F1-④ 复核确认正确（协议硬约束非待归类信号） | ✓ 核销（选择已固化于实现） |

## J4 尾行措辞修复

```
< RESULT: PASS (all checks green; signal-only — see header)
> RESULT: PASS (all checks green; metadata gate — NOT a family-independence verdict, see header)
```

diff 仅此一行；exit 0 维持；8/8 PASS 不变。消费方 grep 实证：仓库内无其他文件引用旧字符串（仅 assert-psf-freeze.py 有同族但不同的尾行，不受影响）。

## J5 冻结面

```
$ git status --short
 M bench/rubric-v3/ablation/scripts/assert-prior-source.py
 ?? loop-artifacts/stages/01/RV3G4psa-stages01-03.md
```

prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json 等冻结数据零触碰（变异全走 /tmp 副本）。

## web-llm 交叉核验

unverified 降级——三 provider 登录态失效（同族判据，机械验证边际贡献 ≈ 0）。

## 04 判定

pass——五项验收标准全部满足（基线复验 / M1-M3 防失效实证 / 四项核销表 / 冻结面零触碰 / 措辞瑕疵顺手修复且输出面变化受控）。