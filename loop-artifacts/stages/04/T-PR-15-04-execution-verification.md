# T-PR-15 阶段 04：执行核验

- 核验脚本：`loop-artifacts/stages/04/verify-t-pr-15.py`（纯 stdlib，可复跑）
- 命令：`python3 loop-artifacts/stages/04/verify-t-pr-15.py`
- 退出码：0（0 FAIL / 1 WARN）

## 1. 逐条 AC 实测输出

```
PASS AC1 survey>=300 lines :: 437 lines
PASS AC2 sources>=20 :: 31 rows
PASS AC2 full-text>=10 :: 15 full
PASS AC2 unique IDs>=20 :: 32 ids
PASS AC3 five verdict lines :: [('部分成立','0.75'),('成立','0.8'),('部分成立','0.72'),('部分成立','0.7'),('成立','0.78')]
PASS AC3 verdict vocabulary
PASS AC3 conf in (0,1)
PASS AC4 five subclasses present
PASS AC4 (a)-(e) each has case or [待核验]
PASS AC5 A=弱 / B=强 / C=强
PASS AC5 v17 root cause stated
PASS AC6 counter_args>=3 :: 6
PASS AC7 suggestions>=3 :: 7 (每条含"落地层："标注)
PASS AC7 prompt-layer tagged
PASS AC8 services>=2 :: 2
WARN AC8 0 real receipts (sandbox has no endpoint); recorded as not_satisfied
PASS AC8 contradictions field exists
INFO duplicated long lines: 0
```

## 2. AC 结论表（诚实版）

| AC | 结果 | 证据 |
|---|---|---|
| AC1 ≥300 行 | ✅ | 437 行 |
| AC2 ≥20 源 / ≥10 全文 / 带 ID | ✅ | 31 源；`full` 15；附录 A 每行有 arXiv ID 或 URL |
| AC3 Q1-Q5 判决句 | ✅ | 5 条，含 成立/部分成立 + conf |
| AC4 Q2 五子类案例 | ✅（(b) 标 `[待核验-原文]`） | §3.1-§3.5 |
| AC5 Q3 三假设分级 + 病根 | ✅ | 弱/强/强；病根 C+B |
| AC6 ≥3 质询 | ✅ | 6 条（search-log `counter_arguments`） |
| AC7 ≥3 条可落地建议 + prompt 层标注 | ✅ | 7 条，6 条 prompt/代码层可做、1 条标不可行 |
| AC8 ≥2 LLM 服务核验 | ❌ **未满足（环境）** | 8/8 dispatch failed（Connection refused）；脚本+设计已交付 |

## 3. append-only / 行数唯一性校验

| 批次 | 追加内容 | 累计行数 |
|---|---|---|
| 1 | 头部 + §0 判决表 + Q1 | 82 |
| 2 | Q2（5 子类） | 143 |
| 3 | Q3（A/B/C + 病根） | 221 |
| 4 | Q4（9 手段 + 顺序） | 253 |
| 5 | Q5 + §7 建议 1-7 | 334 |
| 6 | §8 反方 + §9 限制 + §10 待核验 + 附录 A/B | 437 |

- 单调递增：是（82 < 143 < 221 < 253 < 334 < 437）。
- 整行重复（长度 >40 且出现 >1 次）：**0**。
- 未对已写入内容做覆盖式重写；唯一一次修改是 §0 结论表在 02.5 之后同步 C3/C4 的措辞（属批内追加时一并写入，未回改历史批次）。

## 4. 未改代码的证明

```
$ git status --porcelain experiments/ bench/ | wc -l
0
```
（`s5_hierarchy.py` / `score.py` / `gates.py` 均未修改；§7 的修法建议只写在 survey 里。）

## 5. 未通过的项与处置

- **AC8**：环境限制（沙箱无 LLM endpoint，`Errno 111`）。已按【失败降级】记 `not_satisfied` + conf 整体降档 + 交 Lead 本机跑 `research/web-llm/run_crosscheck.py`。**不伪造回执**。
- 未做项（非 AC，但影响结论强度）：pfb rubric 对抗实测、v17 修法 A/B 测试，已在 §9 列明。
