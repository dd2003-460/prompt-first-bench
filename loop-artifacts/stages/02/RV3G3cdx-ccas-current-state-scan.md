# 阶段 02 — RV3G3cdx-closure-checklist-assert 现状扫描（补记）

## S1 message 措辞关键词集实证
对近 20 轮收口 commit message 枚举划掉类/追加类实际用词：
- 划掉类实见：「queue 划掉」「[ ]→[x]」「核销」（9f48d94 仅用『核销』无『划掉』字样 → FLIP_KW 取并集 `["划掉","标记完成","核销","[ ]→[x]"]`）。
- 追加类实见：「新导出候选 ×N」「追加候选」。APPEND_KW = `["新导出候选","追加候选","导出候选"]`。
- 候选短名提取正则 `(?:RV|R5\.)[\w.-]*`，覆盖 R5.2 系与 RV3 系。

## S2 queue diff 三形态枚举
1. 既有行翻转：`- [ ] X ...` + `+ [x] X ...`（同一行改 checkbox + 结果注记）。
2. 首建即 [x]：目标行在 `<h>~1` 不存在于 queue，diff 只有 `+ [x] X ...`（r146 A13 形态，404ba7e 先例）。
3. 纯插入新候选：`+ [ ] Y ...`（不触发 (a)，只被 (b) 消费）。

## S3 正负样例选择
- 正样例（main 历史真实 commit）：16b063f（r146 收口，含 (a) 翻转 + (b) 两候选）/ 0bb55ce（r147 收口）/ 9f48d94（r145 核销轮，『核销』关键词路径）。
- 负样例（构造性，独立分支 tmp/closurecheck-neg-samples 上构造，标注为样例非真实收口）：
  - N1 = f8acff9：message 声称「queue 划掉」但 diff 将已 `[x]` 行改回 `[ ]`（97d2adf 型漏翻复刻，方向相反但同属「声称↔翻转缺失」缺口）→ 预期 (a) FAIL exit 1。
  - N2 = cc168bd：message 声称「新导出候选 RV3G3cdx-negsample-phantom-candidate」但 diff 无对应插入行 → 预期 (b) FAIL exit 1。
  - 两样例的 diff 面均同时触碰 kappa-formula-adjudicate 行且 message 未提及 → 顺带实证 (c) 双向闭合缺口检出（每样例多 2 条 (c) FAIL，符合设计：(c) 按行独立报告）。

## S4 web-llm 交叉询问
`ralph prompt-first web-llm` 通道：三 provider 登录态失效（r129/r138 先例），本轮规则全部来自仓库内权威源（r146 三列对照表 + r148 02.5 X4 修正），零外部事实依赖 → 记录 unverified 继续，不虚构。