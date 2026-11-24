# T-L4-AUDIT 实验1b: L4 regex 覆盖测试 (winner 配置写法变体)

> origin: ai · 2026-11-25 · 纯文本分析, 不调 LLM。regex = `tjudge1_formula.py:247` l4_check 原样(含分支2的 `[×xX]?` 可选符)。
> **关键事实**: sidecar `ref_config.card_model = "RTX 3090"`(git 2ed2478ae, 2026-11-23 加入), 不是 "3090"。
> 因此 l4_check 的 regex **要求字面 'RTX 3090' 前缀**; 裸 '3090×4' 不命中(下方 A 列)。
> 对照列 B = 假设 card_model='3090' 时的 regex(裸卡型口径), 用于量化 'RTX ' 前缀造成的额外缺口。

| 变体 | 说明 | A: 现行 regex (card='RTX 3090') | B: 假设 regex (card='3090') |
|---|---|---|---|
| `RTX 3090×4` | canonical (sidecar card_model='RTX 3090') | ✅ 命中 | ✅ 命中 |
| `3090×4` | bare card ×N | ❌ 漏 | ✅ 命中 |
| `4×RTX 3090` | N×card (digit before ×) | ❌ 漏 | ❌ 漏 |
| `4×3090` | bare N×card | ❌ 漏 | ❌ 漏 |
| `×4 RTX 3090` | leading ×N (branch-2 shape) | ✅ 命中 | ❌ 漏 |
| `×4 3090` | leading ×N bare | ❌ 漏 | ✅ 命中 |
| `四张RTX 3090` | Chinese numeral | ✅ 命中 | ❌ 漏 |
| `四张3090` | Chinese numeral bare | ❌ 漏 | ✅ 命中 |
| `RTX 3090四张` | card + Chinese numeral | ✅ 命中 | ✅ 命中 |
| `3090四张` | bare card + Chinese numeral | ❌ 漏 | ✅ 命中 |
| `RTX 3090 × 4` | spaced × | ✅ 命中 | ✅ 命中 |
| `3090 × 4` | bare spaced × | ❌ 漏 | ✅ 命中 |
| `RTX 3090 x 4` | ascii x spaced | ✅ 命中 | ✅ 命中 |
| `3090 x4` | bare ascii x no space | ❌ 漏 | ✅ 命中 |
| `RTX 3090*4` | asterisk | ❌ 漏 | ❌ 漏 |
| `3090*4` | bare asterisk | ❌ 漏 | ❌ 漏 |
| `3090 4张` | card space N张 | ❌ 漏 | ❌ 漏 |
| `4张RTX 3090` | N张 card | ❌ 漏 | ❌ 漏 |
| `4张3090` | bare N张 card | ❌ 漏 | ❌ 漏 |
| `RTX 3090(二手)×4` | used-marker variant | ✅ 命中 | ✅ 命中 |
| `3090（二手）×4` | fullwidth parens used-marker | ❌ 漏 | ❌ 漏 |
| `RTX 3090×4张` | ×N张 suffix | ✅ 命中 | ✅ 命中 |
| `3090×4张` | bare ×N张 | ❌ 漏 | ✅ 命中 |
| `RTX 3090 ×4` | spaced, no space before × | ✅ 命中 | ✅ 命中 |
| `RTX3090×4` | no space in model name | ❌ 漏 | ✅ 命中 |
| `3090× 4` | space after × | ❌ 漏 | ✅ 命中 |
| `4 x 3090` | N x card spaced | ❌ 漏 | ❌ 漏 |
| `4X3090` | N X card compact | ❌ 漏 | ❌ 漏 |
| `3090×44` | N+digit guard test (should NOT hit) | ❌ 漏 | ❌ 漏 |
| `3090×40` | N+digit guard test (should NOT hit) | ❌ 漏 | ❌ 漏 |

**汇总**: 30 个变体中, 现行 regex 命中 9/30, 裸卡型假设 regex 命中 16/30。

## 漏掉的变体(现行 regex 盲区)
- 裸卡型写法全部漏: `3090×4` / `3090 × 4` / `3090 x4` / `3090四张` / `四张3090` / `3090×4张` (因 card_model 带 'RTX ' 前缀)
- `*` 星号乘号全漏: `3090*4` / `RTX 3090*4` (字符类只有 [×xX])
- `N张` 中文量词全漏: `4张3090` / `3090 4张` / `4张RTX 3090` (只认 '四张')
- `N×卡型` 倒装全漏: `4×3090` / `4×RTX 3090` / `4 x 3090` / `4X3090` (分支2 的 `[×xX]?` 可选符使 '4×3090' 实际要求 '×4' 后紧跟 '×?3090' — '4×RTX 3090' 中 '4' 前无 ×, 不命中)
- 全角括号二手标记漏: `3090（二手）×4` (只认半角 `(二手)/(全新)` 且仅挂在 card 后)
- `RTX3090×4`(无空格) 漏
- 数字守卫正常: `3090×44` / `3090×40` 正确不命中(防误报设计有效)

## 对 0/21 的意义(实验1 交叉验证)
- 对 21 runs 全文做了**穷举 3090 出现位置扫描**(每个 '3090' 前后 8 字符内查 ×4/x4/X4/*4/四张/4张 量词): **0 处** 4 卡配置写法(任何卡型、任何变体)。
- 即使把 regex 放宽到 B 列口径(裸 '3090'), 21 runs 的 strict 仍全 0(逐 run 复算 sBF=0)。
- 模型对 3090 的最大承诺 = **2×3090**(7/15 K7 runs 结论区出现, 多为次选/备选); 4 卡配置(任何卡型)在任何 run 的任何位置都不存在。
- **结论: H3a(regex 严格性)被证伪** — 0/21 不是测量假象, regex 盲区(裸卡型/星号/N张/倒装)真实存在但未被模型实际用到。

