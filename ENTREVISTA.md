# Entrevista antes da implementação

**Agente:** Você está em Linux, com bash, Python, git e gh instalados. Recomendo um script bash porque os destinos são arquivos e diretórios, a execução é local e o shell evita dependência extra. Ele não entrega isolamento de pacotes nem reprodutibilidade total. Você concorda?

**Aluno:** Concordo com bash, pois esta máquina usa `/bin/bash` e os hooks já são executáveis. Registro o limite: o script instala artefatos, mas não fixa versões.

**Agente:** Recomendo symlinkar `settings.json` para o repositório, o que simplifica sincronização. Alternativas: merge idempotente preservando o arquivo local, ou gerar o arquivo inteiro. Qual escolhe?

**Aluno:** Discordo do symlink. O harness pode escrever settings por arquivo temporário e rename; isso substitui o link sem aviso. Escolho merge por marcador e backup para que o estado compartilhado continue pertencendo ao harness.

**Agente:** Recomendo instalar tudo em `~/.agent-artifacts` e remover o diretório inteiro no uninstall. Isso é simples, mas pode apagar arquivos do usuário. Qual é sua decisão?

**Aluno:** Discordo de remover tudo. O uninstall só remove arquivos gerenciados, restaura `settings.json.bak` e tenta remover diretórios vazios. A razão é preservar artefatos que o usuário tenha criado depois.

**Agente:** O script deve ser Python ou bash? Bash permite `cp`, `grep` e `mkdir`, mas exige cuidado com espaços; Python dá abstrações melhores, mas adiciona uma decisão de ambiente.

**Aluno:** Escolho bash porque o alvo é Linux, a máquina já tem bash e os hooks também serão shell. O script verifica marcador antes de escrever, não cria backup novo na segunda execução e aceita `--uninstall`.

**Agente:** Quais regras globais entram?

**Aluno:** Ler README antes de mudar, separar fato de inferência, não inventar credenciais e sempre registrar um verificador. A skill `evidence` documenta esse procedimento.

**Agente:** Como testará?

**Aluno:** Em uma pasta temporária: executar instalação, executar de novo, verificar que o marcador não duplica, depois executar `--uninstall` e confirmar restauração do backup. A saída bruta ficará em `evidencia-instalacao.txt`.
