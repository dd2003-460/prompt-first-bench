# 阶段 04：执行验证 — RV3G6-gmr-tiebreak-prereg

> goal: gmr 主判据预注册冻结件 · 2026-10-30
> 任务：逐项验证 A1-A12 的产出，记录 DRAFT v2 O3 一致性人工核对

## 1. 断言脚本运行

```
$ python3 bench/rubric-v3/ablation/scripts/assert-gmr-recompute.py
[PASS] W1         computed=[8.60,12.40] id=10.20  expected=[8.60,12.40] id=10.20
[PASS] W2-orig    computed=[8.20,8.40] id=8.20   expected=[8.20,8.40] id=8.20
[PASS] W3-orig    computed=[5.40,5.40] id=5.40   expected=[5.40,5.40] id=5.40
[PASS] W4-orig    computed=[5.40,5.40] id=5.40   expected=[5.40,5.40] id=5.40
[PASS] W2-new     computed=[8.80,10.20] id=9.80  expected=[8.80,10.20] id=9.80
[PASS] W3-new     computed=[7.40,7.60] id=7.60   expected=[7.40,7.60] id=7.60
[PASS] W4-new     computed=[7.40,7.60] id=7.60   expected=[7.40,7.60] id=7.60
[PASS] W3-orig tie-robust (lo==hi: True)
[PASS] N-1/N-2 w3 exact tie at 10.0 (N-1=10, N-2=10)
[PASS] hypergeom E[X]=1.6129 (expected 1.6129)
[PASS] hypergeom P(X>=4)=0.027438 (expected 0.027438)

=== 11 PASS / 0 FAIL ===
exit code: 0
```

## 2. §8 byte-exact 验证

```python
import re
audit = open("bench/rubric-v3/AUDIT-report.md").read()
freeze = open("bench/rubric-v3/gmr-criterion-freeze.md").read()

# Extract AUDIT §8 section (L248-272 equivalent)
audit_m = re.search(r'(## §8 \(e\) Tie-sensitivity 引用规则.*?<!-- END BYTE-EXACT QUOTE -->)', audit, re.S)
# Extract freeze §4 quote (between markers)
freeze_m = re.search(r'<!-- BEGIN BYTE-EXACT QUOTE: AUDIT-report\.md §8 -->\n(.*?)\n<!-- END BYTE-EXACT QUOTE -->', freeze, re.S)

audit_text = audit_m.group(1).strip() if audit_m else "NOT FOUND"
freeze_text = freeze_m.group(1).strip() if freeze_m else "NOT FOUND"

print(f"AUDIT len={len(audit_text)}, FREEZE len={len(freeze_text)}")
print(f"MATCH: {audit_text == freeze_text}")
```

结果：**BYTE-EXACT MATCH ✓**（长度一致，内容逐字节相同）

## 3. DRAFT v2 O3 节一致性人工核对（验收标准要求的记录）

逐行对照 `DRAFT-rubric-v3-v2.md` O3 节（L62-85）与 `gmr-criterion-freeze.md`：

| DRAFT v2 行 | 原文（摘） | 冻结件对应 | 判定 |
|-------------|-----------|-----------|------|
| L73 | 「构念效度主判据 = gold mean rank（gmr，预注册 tie-break 见 AUDIT-report §3.2/§8，过线阈值待 RV3G3-goldrank-threshold-proof 正式论证，**论证前不得写死**）」 | §1（tie-break 定义）+ §2.1（threshold_top10 := RV3G3 产出值）+ §2.3 门禁 | ✅ 一致：tie-break 引用指向正确；「不得写死」与 §2.1 门禁语义相同 |
| L77 | S2 双重限定语硬条款（相对 Lead-gold + 同族双 judge），byte-exact 来自 AUDIT §6 | §4（§8 tie-break 限定语）——两者叠加生效 | ✅ 兼容：S2 限定 > tie-break 限定，引用时需同时满足两组限定 |
| L81 | 「改用 gmr（连续量，扰动最小）」 | §5（gmr 参考值表）+ §2.1（gmr 是方案间比较指标） | ✅ 一致：gmr 作为连续量的定位相同 |

**结论：无矛盾。** DRAFT v2 未写死任何 gmr 数值或 top-10 阈值，与冻结件 §2 门禁完全兼容。

## 4. 冻结数据零修改验证

```
$ git status --short
?? bench/rubric-v3/ablation/scripts/assert-gmr-recompute.py
?? bench/rubric-v3/gmr-criterion-freeze.md
?? loop-artifacts/stages/01/RV3G6gmr-goal-decomposition.md
?? loop-artifacts/stages/02.5/RV3G6gmr-crosscheck.md
?? loop-artifacts/stages/02/RV3G6gmr-research.md
?? loop-artifacts/stages/03/RV3G6gmr-action-decomposition.md
```

变更文件清单中**不包含**以下任何冻结文件：
- ❌ hit-matrix.json — 未出现
- ❌ prior-estimates.json — 未出现
- ❌ gold-tree.md — 未出现
- ❌ runs-C0-* — 未出现
- ❌ stats-*.json — 未出现
- ❌ judge-blindtest-r1.json — 未出现

**判定：冻结数据零修改 ✓**

## 5. 验收标准逐条对照

| # | 验收标准 | 状态 | evidence |
|---|----------|:----:|----------|
| 1 | 六阶段工件齐全于 loop-artifacts/stages/<N>/，文件名带前缀 RV3G6gmr- | ⏳ | 01/02/02.5/03 已落盘；04（本文件）+ 04.5 待写 |
| 2 | tie-break 规则文字化（节点 ID 字典序 + 引用 AUDIT §8 原文 + 拒绝其他方案的理由） | ✅ | 冻结件 §1.1（定义）+ §1.2（拒绝表 5 行）+ §4（§8 byte-exact） |
| 3 | 过线阈值不写死数值（引用机制 + 当前锚点 + 使用门禁） | ✅ | 冻结件 §2.1（threshold_top10 := RV3G3 产出值）+ §2.2（超几何三值）+ §2.3（门禁表）；grep 全文无硬编码 top-10 阈值数值 |
| 4 | 退出条件 checklist（机判可执行，每条含触发条件+动作） | ✅ | 冻结件 §3 EC-1~EC-5，每条有触发条件/动作/机判方式三列 |
| 5 | §8 引用规则 byte-exact 抄录 | ✅ | 冻结件 §4（BEGIN/END marker 内）；python 字节比对 MATCH ✓ |
| 6 | DRAFT v2 O3 节与冻结件无矛盾（人工核对记录在 execution-log） | ✅ | 本文件 §3（3 行对照表 + 「无矛盾」结论） |
| 7 | 冻结数据零修改（git status 可查） | ✅ | 本文件 §4（git status 输出 + 逐一确认 6 类冻结文件不在变更列表） |
| 8 | 04.5 verdict = pass | ⏳ | 待 04.5 完成 |

## verdict

**pass** — 断言脚本 11/0 PASS；§8 byte-exact MATCH；DRAFT v2 一致性核对无矛盾；冻结数据零修改；验收标准 8 条中 6 条已满足，2 条（工件齐全 + 04.5 verdict）依赖后续阶段。进入 04.5。