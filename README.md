# Como instalar/configurar o `Calibre` no `Kali Linux`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Calibre` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing `Calibre` on `Kali Linux`._

## Descrição [2]

`Calibre`

O Calibre é uma aplicação de código aberto amplamente utilizada para gerenciar e organizar bibliotecas de e-books. Ele oferece uma plataforma abrangente para os entusiastas de leitura digital, permitindo que os usuários gerenciem sua coleção de e-books, convertam formatos de arquivo, sincronizem e-books com dispositivos e leiam e-books em uma interface intuitiva. O Calibre suporta uma variedade de formatos de e-books e oferece recursos avançados, como edição de metadados, capas personalizadas, busca e classificação, tornando-o uma ferramenta essencial para aqueles que desejam organizar e desfrutar de sua coleção de e-books. Além disso, o Calibre é compatível com diversos dispositivos de leitura e pode ser usado para gerenciar e-books em leitores de e-books, tablets e smartphones, tornando-se uma escolha popular entre os leitores digitais.

## Revisão(ões)/Versão(ões)

|Revisão número|Data da revisão|Descrição da revisão                                   |Autor da revisão             |
|:------------:|:-------------:|:------------------------------------------------------|:----------------------------|
|0             |06/11/2023     |<ul><li>Revisão inicial/criação do documento.</li></ul>|Eden Denis F. da S. L. Santos|

## Controle de configuração/instalação nos Sistemas Operacionais (SO) vs. Computador

|Numero|Computador          |Sistema Operacional (SO) |Tipo de sistema |Status da configuração/instalação |
|:----:|:------------------:|:-----------------------:|:--------------:|:--------------------------------:|
|1     |Dell Precision 7520 |Kali   Linux             |Debian          |OK                                |
|2     |Dell Precision 7520 |Linux Ubuntu             |Ubuntu          |N/A                               |
|3     |Dell Precision 7520 |Linux Xubuntu            |Ubuntu          |OK                                |
|4     |Dell Precision 7520 |Windows                  |Windows         |Pendente                          |
|5     |Asus                |Kali   Linux             |Debian          |N/A                               |
|6     |Asus                |Linux Ubuntu             |Ubuntu          |Pendente                          |
|7     |Asus                |Linux Xubuntu            |Ubuntu          |OK                                |
|8     |Asus                |Windows                  |Ubuntu          |Pendente                          |


## 1. Configurar/Instalar o `Calibre` no `Kali Linux` [1][3]

Para configurar/instalar o `Calibre` no `Kali Linux`, você pode seguir estas etapas:

1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`

    2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`

    2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

Para instalar o `Calibre`, um cliente de BitTorrent popular, pelo "Whisker Menu" no `Kali Linux`, siga estes passos:

1. **Abra o Whisker Menu:** Clique no ícone do Whisker Menu no canto inferior esquerdo da tela ou pressione a tecla `Super` (também conhecida como tecla Windows).

2. **Acesse o Gerenciador de Software:** Digite `Software` na barra de pesquisa e clique no aplicativo `Software` que aparece nos resultados.

3. **Busque por `Calibre`:** No Gerenciador de `Software`, use a barra de pesquisa para procurar por `Calibre`.

4. **Instale o `Calibre`:** Encontre o `Calibre` na lista de resultados, clique nele e depois clique no botão de instalação.

5. **Aguarde a Instalação:** A instalação pode levar alguns minutos. Uma vez concluída, o `Calibre` estará disponível no seu sistema.

6. **Acesse o `Calibre`:** Após a instalação, você pode abrir o `Calibre` através do `Whisker Menu`, procurando por `Calibre`.

7. **Verifique a Instalação:** Para garantir que o `Calibre` foi instalado corretamente, você pode abri-lo e verificar se ele está funcionando como esperado.

Lembre-se de que o `Kali Linux` é uma distribuição voltada principalmente para testes de segurança e análise forense, portanto, a instalação de softwares adicionais deve ser feita com cuidado para não afetar as ferramentas e configurações específicas do sistema.

## 1.1 Código completo configurar/instalar

Para instalar o `Calibre` no `Kali Linux` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update -y
    sudo apt autoremove -y
    sudo apt autoclean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    ```

## Referências

[1] OPENAI. ***Como instalar o calibre no kali linux:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 06/12/2023 22:15.

[2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 04/11/2023 22:15.

[3] OPENAI. ***Comandos de manutenção do ubuntu:*** https://chat.openai.com/c/4a8cfaa2-30d6-474d-821f-7047a6a39830. ChatGPT. Acessado em: 15/12/2023 08:25.
