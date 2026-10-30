# 阶段 02：信息调研 — RV3G6-audit8-erratum

> goal: AUDIT-report §8 参考值表绝对值勘误 · 分支 ralph/rv3g6-audit8-erratum · 2026-10-30
> 任务：为 erratum 收集全部证据——错误位置全量盘点 / 权威值独立复算确认 / byte-exact 抄录点核查 / web-llm 强制步骤回执

## 0. web-llm 交叉询问回执（强制步骤）

`ralph prompt-first web-llm . "..." --context "阶段 02"` 已执行：**三 provider 全失败**（perplexity-review: login or UI changed / chatgpt-review: sign in manually / gemini-review: 同）。与 batch1、o3cl、freeze doc 各 goal 记录一致（登录过期状态延续）。外部线索 unverified——本 goal 为纯仓库内数值一致性工作，不阻塞。

**流程改进落地（RV3B1-webllm-receipt-per-goal 前置执行）**：本次发现 `ralph` 工具固定写死回执路径 `loop-artifacts/prompt-first/02-web-llm-cross-check.md`，o3cl goal 运行后覆写了 batch1 的回执（W6 登记项）。本 goal 处置：先 `git checkout --` 恢复 o3cl 版回执到工作树 → 重跑 web-llm → 将新回执 `mv` 为 per-goal 文件 `02-web-llm-cross-check-RV3G6a8e.md` → 原路径文件保持 o3cl 内容不变（git status 验证：原文件零 diff，仅新增 per-goal 文件）。后续 goal 沿用此约定；工具侧修复（ralph 支持 per-goal 路径参数）超出本仓能力边界，登记见 04.5 导出。

## 1. 错误位置全量盘点（J2 清单定稿）

grep 模式 `[2.60|6.40|7.80|8.00|5.20|6.60|6.80|7.00|9.8|=8.2|=7.6]` 对 AUDIT-report.md 全文扫描，命中 **5 处行、8 个数值组**：

| # | 位置 | 现值（错） | 应改为（freeze doc §5） | 性质 |
|---|------|-----------|------------------------|------|
| E1 | L108 §3.2 范围句 | W1 [2.60, 6.40] / W2-orig [7.80, 8.00] / W2-new [5.20, 6.60] / W3-new/W4-new [6.80, 7.00] | W1 [8.60, 12.40] / W2-orig [8.20, 8.40] / W2-new [8.80, 10.20] / W3-new/W4-new [7.40, 7.60] | 区间绝对值 ×4 |
| E2 | L109 落盘顺序值 | orig 侧 W1=9.8、W2=8.2；new 侧 W1=9.8、W2=7.6 | W1=10.2（两侧相同，E3.2）、W2-orig=8.2（正确保留）、W2-new=9.8、W3=W4-new=7.6（正确保留） | id-order 值 ×3 错 + ×3 对 |
| E3 | L109 结论句 | 「换一个合法 tie-break，W1 的最优值（2.60, 0-based）可优于 W3-orig（5.40, 0-based）」 | 「换一个合法 tie-break，W1 的最优值（8.60, 0-based）仍劣于 W3-orig（5.40, 0-based）」 | **语义翻转**（原句在正确值下不成立） |
| E4 | L172 finding #11 | 精确 gmr 范围 [2.60, 6.40] | [8.60, 12.40] | 区间绝对值 |
| E5 | L252 §8 规则 1 引用模板 | 「9.8（0-based，落盘顺序 tie-break；精确范围 [2.60, 6.40]…）」 | 「10.2（0-based，落盘顺序 tie-break；精确范围 [8.60, 12.40]…）」 | 引用模板值（下游引用会复制错误的值） |
| E6 | L265-269 §8 参考值表 | 四行区间列同 E1 | 同 E1 | 主勘误对象（queue 描述所指「§8 表」） |

**不动的位置**（两源一致或属历史溯源）：
- L108/L256/L267 W3-orig/W4-orig = 5.40（tie-robust 单值，两源精确一致）
- L109 new 侧 W3=W4=7.6（与 freeze doc §5 W3-new id-order 7.60 一致）
- L109 orig 侧 W2=8.2（与 freeze doc §5 W2-orig id-order 8.20 一致）
- L172 G5 原引 [9.60,13.40] 的**作废声明**（历史溯源句，L271 勘误声明已覆盖，不改）
- L271 既有勘误声明（针对 G5/G3 舍入问题，与本 erratum 正交，保留）
- tie 组结构列（{5.0: N-2,N-4} 等）——freeze doc §4.1 判定结构一致，保留
- span 跨度标注（3.8/0.2/1.4/0.2）——freeze doc §4.1 判定 span 一致，保留

## 2. 权威值独立复算确认（R3 核查）

`python3 bench/rubric-v3/ablation/scripts/assert-gmr-recompute.py` → **11 PASS / 0 FAIL · exit 0**（2026-10-30 实测输出）：

```
[PASS] W1         computed=[8.60,12.40] id=10.20  expected=[8.60,12.40] id=10.20
[PASS] W2-orig    computed=[8.20,8.40]  id=8.20   expected=[8.20,8.40]  id=8.20
[PASS] W3-orig    computed=[5.40,5.40]  id=5.40   expected=[5.40,5.40]  id=5.40
[PASS] W4-orig    computed=[5.40,5.40]  id=5.40   expected=[5.40,5.40]  id=5.40
[PASS] W2-new     computed=[8.80,10.20] id=9.80   expected=[8.80,10.20] id=9.80
[PASS] W3-new     computed=[7.40,7.60]  id=7.60   expected=[7.40,7.60]  id=7.60
[PASS] W4-new     computed=[7.40,7.60]  id=7.60   expected=[7.40,7.60]  id=7.60
```

数据源 = prior-estimates.json + judge-blindtest-r1.json（冻结数据只读），协议 = rank 0 最高权重 + ID 字典序 tie-break + gmr = Σrank(gold)/5。**R3 关闭**：W2-new id-order 独立复算 = 9.80，与 freeze doc §5 一致，erratum 不会固化任何错误值。

## 3. byte-exact 抄录点核查（R5 核查）

grep 全仓 `BYTE-EXACT|byte-exact`（排除 freeze doc 自身）：
- `bench/rubric-v3/o3-claim-list.md:176` —— 抄录的是 AUDIT **§6** S2 限定语，非 §8 → 不受本 erratum 影响 ✅
- `bench/rubric-v3/gmr-criterion-freeze.md` §4（L106-131 `BEGIN/END BYTE-EXACT QUOTE: AUDIT-report.md §8`）—— 唯一受影响的抄录点 → D2 同步更新
- `revision-log-batch1.md:88` —— 提及 o3-claim-list 的 byte-exact 属性，非 AUDIT 抄录 → 不影响 ✅

**结论**：修改 AUDIT §8 文本仅需连锁更新 freeze doc §4 一处。

## 4. 定性结论稳定性预检（R1 缓解材料）

erratum 前后必须不变的定性断言（04 阶段 grep 复核清单）：
1. 「W3/W4-orig 最优且 tie-robust 单值 5.40」（L108/L256/L267 + freeze doc §5 关键事实 1）
2. 「W1 最差且对 tie-break 高度敏感」（L172/L252 + freeze doc §5 关键事实 2）
3. 跨方案排序方向 W3=W4-orig < W3=W4-new < W2-orig < W2-new < W1（freeze doc §5 L168）
4. 「跨方案比较必须在预注册 tie-break 下进行，禁止各方案取各自最优」（L109 尾句 + §8 规则 3）
5. L109 前半句「gmr 下 W3/W4 优于 W1/W2 只在同一预注册 tie-break 下成立」——**逻辑加强而非改动**：原句用「换 tie-break 可能反转」论证必要性；erratum 后改为「即使换任何合法 tie-break 也不反转」，必要性论证从「防反转」变为「结论本身更稳健」，前半句保留原文不动。

## 5. 未解决空缺

| # | 空缺 | 影响 | 处置 |
|---|------|------|------|
| U1 | web-llm 外部线索（erratum 惯例：就地修订 vs 独立文件） | 无（J1 已由 queue 描述「同步修正…消除双源困惑」+ 单一事实源原则裁决为就地修订） | unverified 登记，不阻塞 |
| U2 | ralph 工具回执路径写死（per-goal 分文件需手工 mv） | 低（本 goal 已手工处置；后续 goal 沿用约定） | 04.5 导出候选（工具侧修复超出本仓边界） |

## verdict

**pass** — 错误位置 5 行 8 组全量盘点完成（§1，含 queue 描述未覆盖的 E2/E4/E5 扩展项，每处带 freeze doc §5 evidence）；权威值经 assert-gmr-recompute.py 独立复算 11/11 PASS 确认（§2，R3 关闭）；byte-exact 连锁点唯一且已定位（§3，R5 关闭）；定性结论零改动清单预置（§4）。web-llm 三 provider 失败如实记录（§0），per-goal 回执约定首次落地。进入 02.5。