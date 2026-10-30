# 阶段 04 A2 — RV3G3cdx-m4-independent-source-ops · 回测记录（r152）

> 口径（02.5 X2/X3 裁定）：计数对象 = packet v2 P6 `independent_sources` 条目（实跑 11 条——current-goal「10 条」勘误已登记于 02 S3）；打分器 basis 分数列仅作方向参照，对账对象 = **判低分理由类别是否被 D 条款覆盖**。
> 分类规则 = 定义文档 §1 D1-D5 的关键词降级实现（U3 降级运行态：provider 维度跳过）。复现命令见文末。

## S1 — 11 条逐条分类表

| run | 条目 | nature/conf | 判定 | 依据条款 | source 摘要 |
|---|---|---|---|---|---|
| run1 | [0] | transcription / 0.85 | **排除** | D2(β) 上轮回执转录 | r2 双源回执（execution-log 引用） |
| run1 | [1] | local-measured / null | **排除** | X3 负向通道陈述 | loop-state chain_steps 'degraded-partial…unreachable' |
| run2 | [0] | external / 0.8 | 计入 | D1(ii) web 通道一手 | augmentcode.com; neelmishra.github.io; ai-tldr.dev |
| run2 | [1] | external / 0.6 | 计入 | D1(ii) web 通道一手 | leanopstech.com; aipromptshub.co |
| run2 | [2] | external / 0.7 | 计入【D3 折减 ≤0.7】 | D3 转引标记 | Anthropic multi-agent 文（经 substack/valdemird/perform.digital 转引） |
| run2 | [3] | external / 0.5 | 计入 | D1(ii) web 通道（同 E1 页——D1(i) provider 同 ⇒ 与 [0] 同源风险，见 S3 M1） | augmentcode.com guide（同 E1 页） |
| run2 | [4] | external / 0.5 | 计入【D3 折减 ≤0.7】 | D3 转引标记 | 'Engineering Best Practices'（经 arihantdeva blog 转引） |
| run2 | [5] | external / 0.5 | 计入【D3 折减 ≤0.7】 | D3 转引标记 | parallel.ai（转引 Anthropic context engineering） |
| run2 | [6] | local-measured / 0.8 | 计入 | D1(ii) 本地实测通道 | run2 count-tokens.js → token-counts.txt |
| run3 | [0] | local-measured / 0.8 | 计入 | D1(ii)/(iii) 本地双读——但见 S3 M2（E4 判 δ 同源双读） | run3/03-review.md defect cite（sed + read） |
| run3 | [1] | local-measured / null | **排除** | X3 负向通道陈述 | execution-log '无外部 LLM 源，unverified' |

## S2 — 每 run 独立源计数与 D4/D5 判定

| run | 原始条目 | 计入口 | D1 独立源数（保守口径） | D4 达标？ | D5 上限触发？ | 新规则方向 |
|---|---|---|---|---|---|---|
| run1 | 2 | 0 | 0 | ✗ | ✓（degraded-partial） | **low**（无任何可计源） |
| run2 | 7 | 7 | 2（web 通道簇 1 + 本地实测 1；[3] 与 [0] 同 provider 合并、[2][4][5] 转引折减后仍归 web 簇） | ✗（缺「不同 provider 的 LLM 回执对」——恰是 E4 原话） | ✓（无 ≥2 LLM 交叉通道） | **mid 封顶**（≤60） |
| run3 | 2 | 1 | 1（仅本地；[0] 若按 E4 口径判 δ 同源双读则 = 0.5 效力，保守取 1） | ✗ | ✓（无网络） | **low** |

## S3 — 与两打分器 + 裁决层方向对账

对账对象 = 判低分理由类别覆盖性（非分数一致——分数尺度含裁量成分，本 goal 不重定尺度）。

| run | DeepSeek (r4 step1) | Claude (R5.1) | 裁决 (r4 step2) | 新规则方向 | 判低分理由覆盖 | mismatch |
|---|---|---|---|---|---|---|
| run1 | 50 | 45 | 70（人工居中，X1 登记） | low | ✓ 全部覆盖：DS「锚点≠独立源」=D2(α) / CC「同一环境两个文件源」=D1(ii)(iii) 全同 + D5 / 裁决「上轮双源可加」= 被 D2(β) 显式否决（X1 张力如实登记，历史分不重写） | 无（方向层面） |
| run2 | 45 | 50 | 45 | mid 封顶 | ✓ 全部覆盖：DS「web_search 单通道非≥2」=D2(γ)+D4 / CC「外部源多为二手转引…仍差不同 provider 回执对」=D3+D4 原文级吻合 | 无 |
| run3 | 35 | 30 | 35 | low | ✓ 全部覆盖：DS「run3 无外部交叉」=D5 / CC「同源双读非独立源…0 个独立第二源」=D2(δ)+D4 | 无 |

**bench.md L117 验收锚复核**：「M4 三项全 low/mid 边界」⇒ 新规则三 run = low / mid / low ✓ 方向复现。

## S4 — mismatch 与局限如实登记

- **M1 — run2[3] 同源拆条风险**：source 明写「同 E1 页」（augmentcode.com 出现两次）。U1(b) 的 source 归一重复检测应命中此对——本轮降级运行未做字符串归一比对，登记为 U1 落地时的首个实证用例。保守计数已将其并入 web 簇（未单独计源），不影响 run 级结论。
- **M2 — run3[0] 的 δ 边界**：E4 判「sed vs read 同一文件 = 同源双读」（0 独立第二源），本回测保守取 1（local-measured 通道本身成立，只是双读不加倍）。两读法差异 = D1 维度粒度问题（「读取方式」是否算独立维度未在 D1 明列——D1 只列 provider/通道/信息路径三维，读取方式是通道内的子行为）。**处置**：定义文档 D1 补一句澄清（条款级澄清，直接 Edit）——「同一文件的多种读取方式不构成维度 (ii)/(iii) 差异」（即 δ 反例的 D1 侧锚定，消除本次回测与 E4 的读法分歧）。
- **M3 — D3 折减未改变任何 run 级结论**：三条折减条目全在 run2 web 簇内，折减前后 run2 独立源数不变（2）——D3 在本数据集上是**惰性条款**（机制正确但无判别力），如实登记：其价值须待含跨 provider 数据的下轮 run 才能体现。
- **M4 — X3 排除规则的关键词近似**：两条排除均靠 claim/source 中「不可达/unverified/无外部」关键词命中，无一条是 conf=null 结构字段单独决定（conf=null 的必要非充分性实证）——与 02.5 X5/U1(c) 登记的局限一致。

## S5 — 回归取证（A3）

- 十五 assert 脚本实跑：exit code 序列 = `[0]×15`（assert-audit8-erratum / closure-checklist / g1-audit / gmr-recompute / goldrank-crossdomain / goldrank-threshold / hitmatrix-evidence / kappa-receipt / o3-claim-list / o3-claim-rejudge / prior-source / psf-freeze / queue-lint / w2-formula / w3w4-recompute）——与 main 基线一致，零漂移。
- assert-queue-lint 明细：49 行 / 0 FAIL / 3 SIGNAL exit 0（3 SIGNAL = 既有跨区吸收登记三组，非本轮新增）。
- 冻结面 diff（vs main）：hit-matrix.json / prior-estimates.json / gold-tree.md = **0 行**。
- 本轮触碰面自证：仅新增 4 文件（current-goal 改写 + 定义文档 + 本工件链），零存量脚本/template/json 改动。

## 复现命令

```bash
python3 << 'EOF'
import json, re
d=json.load(open('bench/self-opt-tester/r5/evidence-packet-r4-v2.json'))
def classify(s):
    if s['nature']=='transcription': return 'EXCLUDE D2b'
    if re.search(r'不可达|无外部|unverified|无 ≥2', s['claim']+s['source']): return 'EXCLUDE X3'
    ind=bool(re.search(r'转引|经 .*blog|二手|substack|parallel\.ai', s['source']))
    return ('COUNT D3' if ind else 'COUNT')
for run in ['run1','run2','run3']:
    p6=d['runs'][run]['P6_cross_validation']
    res=[classify(s) for s in p6['independent_sources']]
    print(run, len(p6['independent_sources']), res.count('COUNT')+res.count('COUNT D3'), res)
EOF
```