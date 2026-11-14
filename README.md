# OpenTrack 工程搭建与验收 Skill

用于在 OpenTrack Railway Simulation 中搭建、修改和复跑铁路仿真工程。从任务书提取验收要求，建立双顶点站场、跨图连接、信号、列车和运营数据，再对正常、限速、追踪及选做场景做逐车验证。

## 使用

将本仓库克隆到 Agent 的技能目录。在使用默认用户目录的 Codex 环境中，可运行：

```powershell
git clone https://github.com/LYGL315/opentrack-project-builder.git "$env:USERPROFILE/.codex/skills/opentrack-project-builder"
```

重新加载技能后，通过 `$opentrack-project-builder` 调用。例如「使用 `$opentrack-project-builder`，按这份任务书搭建 OpenTrack 工程，先用两方向单车验证跨图，再输出三组场景的原生结果。」在支持 Agent Skills 的其他工具中，按其文档加载本仓库目录中的 `SKILL.md`。

- [SKILL.md](SKILL.md) 提供主工作流和验收要求。
- [建模参考](references/modeling.md) 说明图例、信号、Route 与 Path 的设置依据。
- [复跑验收](references/validation.md) 说明场景对照、结果判读和工程迁移。
- [输出对照脚本](scripts/compare_outputs.py) 使用 Python 3.9+，无需额外依赖。

完整工程搭建与原生复跑需要已安装、可运行的 OpenTrack Railway Simulation。图例和迁移经验以已验证的 1.x 工程为基础。示例采用虚构站名和车次，适用于教学仿真。
