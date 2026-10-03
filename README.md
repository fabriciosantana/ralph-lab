# Artefatos privados do agente

Este repositório concentra instruções globais, uma skill de evidência e hooks para o agente. Ele é privado porque pode conter decisões de processo e contexto de trabalho.

## Instalação

```bash
git clone git@github.com:fabriciosantana/ralph-lab.git
cd ralph-lab
./install-agent-artifacts.sh
```

São dois passos: clonar e executar um único script. Para desinstalar, rode `./install-agent-artifacts.sh --uninstall`; o script restaura `settings.json.bak` quando ele existe e remove os artefatos gerenciados.

O instalador faz merge idempotente de um marcador e preserva backup. Ele não fixa versões de pacotes, não é rollback completo e não promete reprodutibilidade do ambiente; é automação de instalação. O harness pode escrever estado compartilhado depois, por isso o script não symlinka settings.json.
