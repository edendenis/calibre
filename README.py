#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar o `Calibre` no `Linux Ubuntu`
#
# ## Resumo
#
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Calibre` no `Linux Ubuntu`.
#
# ## _Abstract_
#
# _This document contains the main commands and settings for configuring/installing `Calibre` on `Linux Ubuntu`._

# ## Descrição [2]
#
# `Calibre`
#
# O `Calibre` é uma aplicação de código aberto amplamente utilizada para gerenciar e organizar bibliotecas de e-books. Ele oferece uma plataforma abrangente para os entusiastas de leitura digital, permitindo que os usuários gerenciem sua coleção de e-books, convertam formatos de arquivo, sincronizem e-books com dispositivos e leiam e-books em uma interface intuitiva. O `Calibre` suporta uma variedade de formatos de e-books e oferece recursos avançados, como edição de metadados, capas personalizadas, busca e classificação, tornando-o uma ferramenta essencial para aqueles que desejam organizar e desfrutar de sua coleção de e-books. Além disso, o `Calibre` é compatível com diversos dispositivos de leitura e pode ser usado para gerenciar e-books em leitores de e-books, tablets e smartphones, tornando-se uma escolha popular entre os leitores digitais.

# ## 1. Configurar/Instalar/Usar o `Calibre` no `Linux Ubuntu` [1][3]
#
# Para configurar/instalar/usar o `Calibre` no `Linux Ubuntu`, você pode seguir estas etapas:
#
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
#
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean`
#
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
#
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
#
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
#
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
#
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean`
#
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
#
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#
# Para instalar o `Calibre` no `Linux Ubuntu`, siga estes passos:
#
# 1. **Abra o Whisker Menu** ou o menu de aplicativos.
#
# 2. **Acesse o Gerenciador de Software:** procure por `Software` e abra o aplicativo correspondente.
#
# 3. **Busque por `Calibre`:** pesquise por `Calibre` e selecione-o para instalar.
#
# 4. **Instale o `Calibre`:** clique no botão de instalação e aguarde a conclusão.
#
# 5. **Acesse o `Calibre`:** após a instalação, abra o `Calibre` pelo menu ou digitando `calibre` no terminal.
#
# 6. **Verifique a instalação:** confirme que o `Calibre` está funcionando.
#
# 7. Após concluir esses passos, o `Calibre` estará pronto para uso.

# ## 1.1 Código completo configurar/instalar/usar
#
# Para configurar/instalar/usar o `Calibre` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
#
# Para instalar o `Calibre` rapidamente via terminal, execute:
#
# ```bash
# sudo apt update
# sudo apt install -y calibre
# ```

# ## Referências
#
# [1] OPENAI. ***Como instalar o calibre no Linux Ubuntu.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 06/12/2023 22:15.
#
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 04/11/2023 22:15.
#
# [3] OPENAI. ***Comandos de manutenção do ubuntu.*** Disponível em: <https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830>. ChatGPT. Acessado em: 15/12/2023 08:25.
