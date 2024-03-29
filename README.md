# Primeiro repositório Python

[<img src = "https://www.python.org/static/img/python-logo.png" width = "160">](https://www.python.org/)[<img src="https://pillow.readthedocs.io/en/stable/_static/pillow-logo.png" width="120" >](https://pillow.readthedocs.io/en/stable/index.html)

Em algum momento de minha vida comecei a manipular arquivos com o python. Mais por uma nescessidade de evitar trabalhos repetitivos e por que não tinha tempo para editar uma quantidade considerável de imagens. Este repositório contém scripts feitos exclusivamente para trabalhar com imagens e diretórios. com a finalidade de atribuir rótulos a estas. Basicamente serve para atribuir um código SKU, um preço e um breve nome/ identificador no topo da imagem processada. Logicamente este código não é uma versão atualizada e não segue nenhum padrão de desenvolvimento. Posteriormente será públicada uma versão atualizada e com interface gráfica para melhor aproveitamento da solução. Este código é livre e pode ser complementado se acharem pertinente. 

### Dependências

Para o uso do código é recomendável preparar um ambiente de desenvolvimento isolado. Pois o Pillow por exemplo é um pacote que pode acabar conflitando com outros que já vem por padrão.
>⚠️
>Considerar que a primeira versão do código é desenvolvida em ambiente windows.

Para isso recomenda-se criar um com o cmdlet a seguir:

No PowerShell
````powershell
py -m venv [nome-da-sua-venv]
````
No Linux:

````linux
python3 -m venv [nome-da-sua-venv]
`````
É claro que é valido lembrar que se  não for possível criar o virtual env é possível que você precise instalar a partir da seguinte cmdlet:

````linux
apt install python3.10-venv
````

 Criada a venv basta prosseguir ativando ela na sua IDE dentro do diretório aonde este repositório se encontra 

No Powershell
 `````powershell
venv/Scripts/activate.ps1
 `````
 
No Linux
````
source venv/bin/activate
````
Após ingressar no virtualenv ou ativalo que é o termo correto é esperado que apareça algo assim:

````
(venv) PS C:\Users\rafae\seu_caminho\first_python_repo> |
````
Lembrando é claro que o nome que você definiu na virtual env aparecerá entre parenteses no ícicio da linha da cli, ou linha do terminal.
````
(myenv) ubuntu:/home/fulano/python_environments/first_python_repo# |
````
Instale as dependências em seu ambiente virtual usando a linha a seguir:
````linux
pip install -r requirements.txt
````
>🗨️<br/>
>Até aqui você aprendeu ou teve a experiência de criar um ambiente virtual python

Acesse a pasta inception usando o `cd inception` e dentro da pasta inception inicie o Python

Ao iniciar o python considere importar uma das duas classes, Catalogando ou Catalogando2. Sendo a Catalogando2 à mais atual.

A partir daí defina o objeto que consiste em 8 características, porém para instanciar será nescessário primeiro inicializar, recomenda-se então digitar :

````python
import Catalogando as cat
catalogo=cat.Catalogando()
````
Em seguida será importante inserir o diretório de um endereço de entrada de imagens e um endereço de saída. O endereço pode ser de uma pasta qualquer do Windows que contenha imagens, as quais você queira atribuir a seguinte regra de negócio:

Todas as fotos da pasta deverão ter um mesmo preço e deverão ser de uma mesm a categoria pense que você trabalha com acessórios ou até mesmo em uma padaria, você tem um setor de pães, eles estão já pesados e o valor do pacote é o mesmo porém varia em sabor e consistência. 

Desse modo o objeto criado precisará de mais alguns parâmetros além dos que você já passou quando você o inicializou. Em seguida considere três letras que definirão o tipo de mercadoria e tres números a seguir que definirão o valor da mercadoria. Antes de trabalhar com as imágens considere ter uma cópia da pasta de origem. logo em seguida se a sua mercadoria tem código PAN650, O valor correspondente será 6,50 e o código inicial do seu produto será PAN650. 

````python
catalogo.renomear_arquivos_origem()
````
Em seguida o prompt fará perguntas relativas a regra de negócio, digite o código de acordo com a regra de negócio e na segunda pergunta defina o número inicial, se você tem 0 pães cadastrados digite 1, se tiver 53 digite 54. O Catálogo será gerado na pasta de saida depois que você digitar:

`````python
catalogo.iniciar()
`````

Este é o primeiro projeto que ajudou bastante na elaboração de um catálogo. Utilizei um armazenamento muito conhecido como repositório das imagens e um cms(Content Management System) para disponibilizar o catálogo ao publico a partir de uma interface simples.Esse projeto também envolveu a disponibilização do primeiro site que publiquei. Está em desuso más foi muito bom para o que se propunha na época.

>As imágens são melhoradas no quesito de espaço. Naquele tempo a plataforma  era baseada em espaço então eu podia encher de imagens que não seria um problema. elas pesam menos de 100kb depois de processadas. Dê uma olhada no código e verá que essa otimização está presente. Recomendo bastante o uso do Pillow para trabalhar com imagens durante o desenvolvimento em python. Confesso que um pouco antes de fazer essa automação eu estava aprendendo a manipular imagens com outros softwares open source e foi isso que me motivou a trabalhar com a automação. 