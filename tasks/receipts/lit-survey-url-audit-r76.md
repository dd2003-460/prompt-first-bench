# 文献调研来源链接可达性审计回执（r76）

- **对象**：`research/interpretability/literature-survey.md`（308 行，c241a8f 回填的 arena 原文）§7 完整来源列表 + 正文内联引用
- **动机**：该文件是 C3 v3 R1-R5 修正的依据链上游；若来源链接失效，下游"已核验"声明会跟着悬空。趁 r76 把 P2 里"survey 回填"项的尾巴（交付路径对齐 + 来源可用性）一次清掉。
- **方法**：正则抽取全部 http(s) URL → 去重得 34 条 → 逐条 `curl -sI` 取 HTTP 状态码（max-time 15s）→ 失败项带浏览器 UA 复测区分"链接失效"与"反爬"。

## 结果

| 指标 | 值 |
|---|---|
| 唯一 URL 总数 | 34 |
| 直接可达（HTTP < 400） | 29 |
| 尾部全角括号清洗后可达 | 4（arxiv.org/html/2410.10781v2、gradientscience.org/contextcite/、llm-judge-bias.github.io/、github.com/antonsoo/errorbars——正文中 URL 后粘连了「）。」类标点，链接本身 200） |
| 裸 curl 403 但带 UA 200 | 1（scite.ai/reports/all-bark-and-no-bite-mOPWmvL1 — Timkey & van Schijndel EMNLP 2021 rogue dims 报告页，反爬非失效） |
| **真实失效链接** | **0** |

**判定：PASS**。34/34 来源链接全部有效，C3 v3 依据链的上游引用无悬空。

## 顺带发现的排版瑕疵（不阻塞，登记备查）

survey 正文 4 处 URL 尾部粘连全角括号（如 `https://arxiv.org/html/2410.10781v2）。`），系 arena 生成时中文标点未与 URL 分词所致。不影响人工点击阅读，但若未来有脚本按行抓 URL 会抓到脏串。修复 = 4 处各删一个字符，属对 c241a8f 回填原文的微改——本轮不动原文（保持 arena 产出原样可追溯），仅在此登记；若要修，单独一个小 commit 做。

## 交付路径对齐结论（r51 回执遗留问题）

`tasks/T8-lit-research.md` L39 要求交付到 `experiments/T8-lit/lit-survey-pipeline-prompts.md`（三方向表格格式），实际落的是 `research/interpretability/literature-survey.md`（对照结论格式，按旧任务卡 T8-interp-research-task.md 执行）。核查两任务书：T8-lit-research.md 的三张表（消融方法/内部归因/judge 偏差）在 literature-survey.md §1/§2/§3 均有对应且更完整的表格，内容覆盖成立，差异仅在文件路径与标题结构。**裁定：以 research/interpretability/literature-survey.md 为权威交付物**（它是 C3 v3 实际消费的文件，且含 §4 R1-R5 修正建议这一 T8-lit-research 没要求的增量）；T8-lit-research.md 的交付路径视为过期规格，下轮若动该任务书再同步改路径，本轮不改任务书（避免无关 diff）。
