# 04 — RV3G6-kappa-formula-adjudicate · 执行验证

> goal: U-K1 κ 公式裁定备料（三方案对照，不代裁）· 分支 ralph/rv3g6-kappa-formula-adjudicate · 2026-10-30
> 输入：03 动作表 A1-A5。本文件 = A1-A5 的逐项验收记录。

## A1 — 主材料落盘 ✅

`bench/rubric-v3/kappa-u1k1-adjudication-materials.md` 落盘，六节结构：

| 节 | 内容 | jaccard-m5 先例对齐 |
|----|------|---------------------|
| §1 溯源 byte-exact | §4.3 L162-166 / DRAFT L16+L208+L307 / protocol L71 五处原文逐字 | ✅ 同构 |
| §2 关键发现 | F-A「预注册下限」无数字落点 / F-B 0.6 = 2-judge 沿用值且当时已知切分缺陷 / F-C 判者数错配 / F-D schema 已隐含 Cohen's+2judge 既成矛盾 + 硬门禁不在机判层 | ⚠️ 按 X2 差异登记改为发散型四事实（非收敛型单结论） |
| §3 三方案对照表 | F1/F2/F3 × 11 维 + §3.4 手算小例（S1/S2/S3，精确 Fraction） | ✅ 同构且维度更多 |
| §4 排序 + 适用条件 | F1 出局（数学事实）；F2 vs F3 权重问题表；runner 排序 F2 略优先（显式声明非强推荐）；折中出口（降 SIGNAL，与公式正交）；阈值处置 α/β/γ 三选项 | ✅ 措辞降级为「排序+适用条件」（X2/X4 纪律） |
| §5 裁定后执行清单 | D1-D6 × diff 面（含 assert-kappa-receipt.py judges 放宽项 F-D 处置）+ 回归义务 | ✅ 同构 |
| §6 边界声明 | 冻结件零修改 / unverified 标注 / 不算真实 κ / α 选项外部依赖 | ✅ 同构 |

## A2 — 溯源 byte-exact 核验 ✅（15/15 PASS）

独立 Python 脚本对五处引用做「源文件提取 vs 材料内文本」双向比对（源中存在 + 材料中存在 + §4.3 整块逐字相等）：

```
[PASS] §4.3 L162-166（整块 strip 后逐字相等）
[PASS] DRAFT L16 in source / in materials
[PASS] DRAFT L208 in source / in materials
[PASS] DRAFT L307 in source / in materials
[PASS] protocol L71 in source（整行相等）/ in materials
[PASS] AKR '条目层二值 Cohen's κ' claim（F-D 引文锚点存在）
[PASS] AKR judges exactly-2 claim
[PASS] AKR SIGNAL-not-FAIL semantics
[PASS] T8 L10 R5 quote / T8 L17 quote（F-B 出处锚点）
[PASS] F-A: o3-claim-list zero '0.6'（全文 grep 零命中——「预注册下限无数字落点」实证）
```

渲染省略：无（五处引用全部完整逐字，未触发 jaccard-m5 先例的「首字符省略」豁免条款）。

## A3 — 数值自检终验 ✅（13/13 PASS，含一处算术错误拦截记录）

独立 Fraction 精确复算（吃原始矩阵，不吃 02 计算过程）：

```
[PASS] k_yes=[2,1,0,3]  P_bar=1/9  p_bar=1/2  Pe=1/4
[PASS] fleiss = −5/27
[PASS] pair(1,2)=1/2  pair(1,3)=1/5  pair(2,3)=1/2
[PASS] pw_mean = 2/5  pw_median = 1/2  naive_agree = 0
[PASS] S1a κ=0  S1b κ=1/2
```

**算术错误拦截记录（负面结果，如实登记）**：初稿 pairwise-mean 误写 **13/30 ≈ 0.433**。根因 = (1/2+1/5+1/2) 的分子加法笔误（1/2+1/5+1/2 = 6/5，除以 3 = **2/5 = 0.4**；13/30 系把和错算为 13/15 的变体）。A3 独立重算捕获 → 主材料 §3.4 两处 + 02 F5 + 02.5 X5 三文件同步修正。**此事件验证了 02.5 X6 风险声明第 3 条的真实性**（抄写/算术错误确实发生，且被预注册的独立重算机制拦截而非漏出）。修正后全量 13/13 零 mismatch。

## A4 — 冻结面零修改 ✅

`git status --short`（收口前）改动面 = 仅三个 loop-artifacts 文件（02/02.5 修正 + 本文件待提交）+ 新文件 `bench/rubric-v3/kappa-u1k1-adjudication-materials.md`。

`git diff main --stat` 对六个冻结件（o3-claim-list.md / DRAFT-rubric-v3-v2.md / judge-protocol-batch1.md / assert-kappa-receipt.py / revision-log-batch1.md / hit-matrix.json）= **0 行 diff**。✅

## A5 — 回归基线维持 ✅（与 r142 收口基线一致）

| 脚本 | exit | 输出 | 基线对照 |
|------|------|------|---------|
| assert-o3-claim-list.py | 0 | 4/4 检查组 PASS | 一致（r142 基线 4/4） |
| assert-gmr-recompute.py | 0 | 11 PASS / 0 FAIL | 一致（r142 基线 11 PASS） |
| assert-kappa-receipt.py | 1 | RESULT: FAIL (1 checks failed)——kappa-receipt.json 不存在 | 一致（预期常态 FAIL，r136 语义：回执缺失 = 评分无效声明，不伪造转绿） |
| assert-o3-claim-rejudge.py | 0 | [SIGNAL] blocked-on-external | 一致（r141 语义） |

注：assert-o3-claim-list.py / assert-gmr-recompute.py 使用 CWD 相对路径，须从仓库根运行（首次从 scripts/ 目录运行报 FileNotFoundError 为路径问题非基线漂移，改从根运行后与基线一致）。

## 验收标准对照（current-goal【验收标准】逐项）

- [x] kappa-u1k1-adjudication-materials.md 落盘，五要素齐（§1-§6，先例结构 + X2 差异修正）
- [x] §4.3 原文 + DRAFT v2 0.6 阈值原文 byte-exact 引用（A2：15/15）
- [x] 三方案对照表每格有依据（F3.4 定义式 + N=3 适用性论证 + S2 实测值行）
- [x] 数值自检 ≥1 手算小例（S1/S2/S3 三例，精确 Fraction，A3 独立复算 13/13）
- [x] 裁定后执行清单可照做（§5：D1-D6 具体文件 + 行级位置 + 改写方向 + 回归义务）
- [ ] 冻结件零修改（A4 ✅）；04.5 verdict pass（下一阶段）；queue 更新（收口阶段）