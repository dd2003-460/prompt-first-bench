# origin: ai (2026-11-28 R3b 盲打分, 判据=decomposition.md 预注册节)
# 数据: r3a-raw.json (commit 8cb658ce6), 揭盲: r3a-armmap.json
# 盲性说明: 打分前读了 raw.json, S3 reasoning 引用臂O文案特征词("手比脑快")、S6 为 T1 回执模板结构,
# 两条在打分时可被推测出臂 → 盲性部分失效, 已如实标注; S1/S2/S4/S5 无法从内容区分臂, 盲性有效。
# 判据: specificity 2=与场景绑定的具体点 1=有方向不具体 0=泛泛元话语; actionability 2=具体可执行判别证据 1=类别不具体 0=无
scores:
  - id: S1
    arm: O
    attempt: 3
    specificity: 0
    actionability: 0
    total: 0
    reason: "泛泛调试清单(收集日志/查依赖/写测试/求助), 无与场景绑定的具体点, 无定案证据"
  - id: S3
    arm: O
    attempt: 1
    specificity: 0
    actionability: 1
    total: 1
    reason: "复述 T1 模板元话语(域判断/可检验预言/继续升级停止), 举例'更新依赖库'属通用类别不具体"
  - id: S6
    arm: O
    attempt: 2
    specificity: 1
    actionability: 1
    total: 2
    reason: "回执结构完整但细节全编造(虚构 TypeError 报错/X-Deprecated-Field 头/ledger 编号 P-20261201-07); 具体但非真缺口=表演, 不给满分"
  - id: S2
    arm: N
    attempt: 1
    specificity: 2
    actionability: 2
    total: 4
    reason: "具体到 KeyError 'result'/NoneType 与 data 结构假设冲突; 定案证据=运行时数据快照+环境差异比对+最小复现, 全可执行"
  - id: S4
    arm: N
    attempt: 2
    specificity: 2
    actionability: 2
    total: 4
    reason: "具体到'根因=逻辑缺陷'假设的确认偏误; 4 个判别实验(干净环境最小复现/二分变量/strace 追踪/时间线关联)"
  - id: S5
    arm: N
    attempt: 3
    specificity: 2
    actionability: 2
    total: 4
    reason: "具体到第42行 data.get('key') + .pyc 缓存假设(修复从未生效); 单条判别测试(print 标记+清缓存)"
aggregates:
  arm_O: {totals: [0, 1, 2], mean: 1.0}
  arm_N: {totals: [4, 4, 4], mean: 4.0}
  delta: 3.0
verdict: "N 胜 (delta 3.0 >= 阈值 1) → G3 判决: 缺口定位式注入优于通用反思清单; R4 升级 T1 注入 (APPROVALS 留痕后执行)"
extra_findings:
  - "臂 O 的 S6 暴露旧模板失败模式: 结构化回执模板在无真实信息时诱导自信编造(虚构报错/响应头/ledger 条目); 臂 N 三条均为诚实认知缺口(承认缺乏观测)。回执模板→表演, 缺口定位→诚实"
  - "臂 N 三条输出即 gap-registry 条目格式({陈述,为何反驳不了,何证据定案}), 机制闭环: 注入直接产出可注册的缺口"
limitations:
  - "n=3/臂, 单场景(修脚本卡住), 单模型(27b); 结论限于'T1 注入文案'这一个落点, 不外推到其他触发点"
  - "同族判官(Lead 判 27b 输出), 绝对分仅相对有效"
