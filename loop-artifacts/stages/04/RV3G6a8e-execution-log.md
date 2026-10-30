# 04 Execution Log — RV3G6-audit8-erratum（AUDIT-report §8 参考值表绝对值勘误）

> 执行：2026-10-30 · ralph loop runner（Hermes stop-hook 驱动模式，claude -p 派发 + Hermes 收口验证）
> 依据：`tasks/current-goal.md`（RV3G6-audit8-erratum）+ `bench/rubric-v3/gmr-criterion-freeze.md` §5（权威参考值源）

## 1. 执行摘要

对 `bench/rubric-v3/AUDIT-report.md` 发正式 erratum，消除与 freeze doc §5 的双源困惑。claude 子进程完成 AUDIT 5 处修正 + freeze doc §4 重抄录 + Erratum 节新增；断言脚本由 claude 初写但**语法损坏**（f-string 内 `freez e_block` 笔误），由 Hermes 收口时修复两处（语法 + byte-exact 比对逻辑漏去 BEGIN 注释行）。

## 2. 变更清单

| 文件 | 变更 | 说明 |
|------|------|------|
| `bench/rubric-v3/AUDIT-report.md` | M | E1-E6 六处修正（§3.2 L108/L109、§5 finding #11 L172、§8 规则 1 L252、§8 参考值表）+ 文末新增 Erratum 节（修正清单表 + 错误定位 + 定性结论不变声明 + U3 未并入项导出） |
| `bench/rubric-v3/gmr-criterion-freeze.md` | M | §4 byte-exact 块重抄录为 erratum 后文本（标注 post-erratum 2026-10-30）+ §4.1 处置句追加「erratum 已发」更新注记 |
| `bench/rubric-v3/ablation/scripts/assert-audit8-erratum.py` | NEW | 防漂移断言脚本（4 组检查：定点断言 / 黑名单零命中 / byte-exact diff / 定性关键词） |
| `loop-artifacts/stages/{01,02,02.5,03}/RV3G6a8e-*` | NEW | 阶段工件（goal-decomposition / research / crosscheck / action-decomposition） |
| `loop-artifacts/prompt-first/02-web-llm-cross-check-RV3G6a8e.md` | NEW | web-llm 交叉核对回执（三 provider 登录过期 → unverified，沿用 G5 回执口径） |

## 3. 数值修正对照（E1-E6）

| # | 位置 | 原值（错） | 修正值 | 权威源 |
|---|------|-----------|--------|--------|
| E1 | §3.2 L108 范围句 | W1 [2.60,6.40] / W2-orig [7.80,8.00] / W2-new [5.20,6.60] / W3-W4-new [6.80,7.00] | W1 [8.60,12.40] / W2-orig [8.20,8.40] / W2-new [8.80,10.20] / W3-W4-new [7.40,7.60] | freeze doc §5 + assert-gmr-recompute.py computed 列 |
| E2 | §3.2 L109 落盘顺序值 | orig 侧 W1=9.8；new 侧 W1=9.8、W2=7.6 | W1=10.2（两侧）；new 侧 W2=9.8 | 同上 |
| E3 | §3.2 L109 结论句 | 「W1 最优值（2.60）**可优于** W3-orig（5.40）」 | 「W1 最优值（8.60）**仍劣于** W3-orig（5.40）」——正确值下原句不成立 | 复算下界 8.60 > 5.40 |
| E4 | §5 finding #11 L172 | [2.60, 6.40] | [8.60, 12.40] | 同 E1 |
| E5 | §8 规则 1 L252 引用模板 | 「9.8（…[2.60, 6.40]…）」 | 「10.2（…[8.60, 12.40]…）」 | 同 E1/E2 |
| E6 | §8 参考值表 L263-269 | 四行区间列同 E1 | 同 E1（表头加注记指向 Erratum 节） | 同 E1 |

**错误定位**：仅绝对值有算术错误；tie 组结构、span 宽度（3.8/0.2/1.4/0.2）、W3-orig/W4-orig = 5.40 tie-robust 单值均经独立复算确认正确。

## 4. 机判验证

### 4.1 assert-audit8-erratum.py 全量运行

```
$ python3 bench/rubric-v3/ablation/scripts/assert-audit8-erratum.py
=== 21 PASS / 0 FAIL ===   exit 0
```

- ① 定点断言 9/9 PASS（E1a-d / E2a-b / E3 / E5 / Erratum 节存在）
- ② 旧错误 token 黑名单 6/6 零命中（正文区，Erratum 节溯源引用除外）
- ③ byte-exact 块 == AUDIT §8 实际文本（diff 空）PASS
- ④ 定性关键词 5/5 仍在（tie-robust 单值 / 对 tie-break 规则敏感 / 禁止各方案取各自最优 / 跨方案比较必须在预注册 tie-break 下进行 / W3-orig / W4-orig | 5.40）

### 4.2 变异测试（确认检查实义生效）

把 AUDIT 中首个 `[8.60, 12.40]` 改回 `[2.60, 6.40]` 后重跑：

```
MUTATED EXIT=1 (expect 1)   ← 脚本正确捕获回漂
FAIL 计数 = 2               ← ① E1a + ② 黑名单 '[2.60, 6.40]' 双命中
RESTORED EXIT=0 (expect 0)  ← 恢复原文后回到全绿
```

### 4.3 既有复算脚本回归

`assert-gmr-recompute.py`（r118 产出，expected 表与 freeze doc §5 同源）此前实测 11 PASS / 0 FAIL（Erratum 节修正清单已引用该 evidence）。

## 5. 冻结数据零修改验证

```
$ git status --short
 M bench/rubric-v3/AUDIT-report.md
 M bench/rubric-v3/gmr-criterion-freeze.md
 M tasks/current-goal.md
?? bench/rubric-v3/ablation/scripts/__pycache__/
?? loop-artifacts/prompt-first/02-web-llm-cross-check-RV3G6a8e.md
?? loop-artifacts/stages/01/RV3G6a8e-goal-decomposition.md
?? loop-artifacts/stages/02.5/RV3G6a8e-crosscheck.md
?? loop-artifacts/stages/02/RV3G6a8e-research.md
?? loop-artifacts/stages/03/RV3G6a8e-action-decomposition.md
```

变更文件清单中**不包含**以下任何冻结文件：
- ❌ hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* / stats-*.json / judge-blindtest-r1.json — 均未出现

**判定：冻结数据零修改 ✓**

## 6. 验收标准逐条对照

| # | 验收标准 | 状态 | evidence |
|---|----------|:----:|----------|
| 1 | AUDIT 全部 gmr 绝对值与 freeze doc §5 一致（assert 脚本机判 exit 0） | ✅ | §4.1（21 PASS / 0 FAIL，exit 0） |
| 2 | L109 错误结论句改写为正确表述（8.60 仍劣于 5.40），不再含「W1 可优于 W3-orig」语义 | ✅ | §3 E3 + §4.1 ② 黑名单「可优于 W3-orig」零命中 |
| 3 | freeze doc §4 byte-exact 块更新为 erratum 后 AUDIT §8 原文 + 状态标注 | ✅ | §4.1 ③ byte-exact diff 空 + freeze doc §4 头部版本标注（post-erratum 2026-10-30） |
| 4 | 新增 assert 脚本 exit 0，含变异测试确认检查实义生效 | ✅ | §4.1 + §4.2（mutated exit 1 / restored exit 0） |
| 5 | 定性结论零改动（grep 复核） | ✅ | §4.1 ④ 定性关键词 5/5 + Erratum 节「定性结论不变声明」段 |
| 6 | 冻结数据零修改（git status 验证） | ✅ | §5 |

## 7. 执行过程问题登记

1. **claude 子进程 max-turns 耗尽**（r11 log：`Error: Reached max turns (200)`）：核心修订 + 脚本初写已完成，但 04/04.5 工件未写、queue 未更新、未 commit。由 Hermes 收口补齐（本文件 + 04.5 review + queue 更新 + commit）。
2. **断言脚本语法损坏**：claude 初写的 f-string 含 `freez e_block` 笔误（SyntaxError），且 byte-exact 比对逻辑漏去 BEGIN 注释行导致 ③ 恒 FAIL。Hermes 收口修复两处后全绿。教训：claude 产出的脚本必须 Hermes 侧实跑验证后才算落地，不能只信"已写完"。
3. **web-llm 交叉核对 unverified**：三 provider 登录过期（沿用 G5 回执口径），外部在线复核降级为仓库内双源比对（freeze doc §5 ↔ assert-gmr-recompute.py computed 列），已在 02.5 工件标注。

## verdict

**pass** — 21/0 PASS + 变异测试有效 + 冻结数据零修改 + 验收标准 6/6 满足。进入 04.5。