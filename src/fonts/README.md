# E27（batch-11）渲染字体资产

batch-11 风格锚（docs/style-analysis.md §3）要求：中文黑体无衬线、英文数字等宽，正文禁用像素字体。
沙箱系统无 CJK 字体，故随仓库携带以下两个字体文件，供 `src/render_E27_time_arena.js` 注册使用：

| 文件 | 用途 | 来源 |
|---|---|---|
| `SimHei.ttf` | 中文黑体无衬线（气泡 / 旁白 / HUD 中文标签） | https://github.com/StellarCN/scp_zh （`fonts/SimHei.ttf`，codeload tarball） |
| `LiberationMono-Regular.ttf` | 英文/数字等宽（时间 01:36→23:59、百分比、底条工具行） | 同上仓库 `fonts/LiberationMono-Regular.ttf`（Liberation fonts，SIL OFL） |

注册名分别为 `StoryHei` / `StoryMono`，仅用于 E27 及后续 batch-11 渲染器；不替换 d1 各集的 Fusion Pixel 管线。
