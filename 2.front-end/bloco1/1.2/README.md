## API de Super Heróis

Vamos criar uma aplicação que busca a imagem e o nome de uma super heroína ou um
super herói. Para isso, utilize a
[SuperHero API](https://www.superheroapi.com/). A aplicação deve contar também
com um alerta, para o caso da API retornar algum erro. Aqui vale uma sugestão:
experimente usar a biblioteca [SweetAlert2](https://sweetalert2.github.io/) 😉

1. Crie um projeto `npm` do zero
2. Estruture uma página HTML que contenha: um card com a imagem da super heroína
ou do super herói e um botão
3. O card deve conter a imagem e o nome da pessoa. Esses dados serão providos
pela API (Se liga aí: você pode ler a documentação da API para saber exatamente
quais campos você deve utilizar aqui)
4. O botão deve gerar um número aleatório, que será o ID utilizado para a API
5. O botão deve buscar na API pelo ID e renderizar na tela o nome e a imagem da
pessoa
6. Caso haja algum erro durante a requisição à API, a aplicação deve emitir um
alerta informando o erro ocorrido

## TryPosts

Neste exercício vamos criar uma página para leitura de posts de várias pessoas.
Você já começará com uma página HTML estruturada e com algumas funções
auxiliares prontas.

Seu objetivo será preencher o HTML existente com as informações que você irá
recuperar de várias APIs diferentes. Ao final, sua aplicação deverá ser capaz
exibir uma lista de pessoas, exibir uma lista de posts de acordo com a pessoa
selecionada e também exibir os comentários do post destacado. Cada item dessa
lista (pessoas, posts e comentários), será recuperado através de uma chamada
para API diferente.

Curtiu o desafio? Então vamos aos passos necessários para desenvolver o
exercício:

1. Faça um `fetch` para a API `https://dummyjson.com/users` para recuperar as
informações das pessoas usuárias. Depois de receber os dados, passe um array com
as informações das pessoas usuárias para a função `fillUsersSelect` para que o
select da página seja atualizado.
2. Na estrutura inicial do projeto já existe o eventListener para o evento
change do select que dispara a função a `clearPage`. Depois da chamada dessa
função, faça um `fetch` para a API `https://dummyjson.com/posts/user/{userID}`.
Lembre-se que você deve pegar o id da pessoa selecionada através do atributo
`value` do select.
3. Após receber as informações da API, utilize a função `fillPosts` para exibir
os posts na tela. ℹ️ Essa função recebe um array com os posts e o primeiro item
do array será o post destacado. Os demais posts entram na lista de posts
relacionados.
4. Depois de receber a lista de posts, faça uma requisição usando o `fetch`
para a API `https://dummyjson.com/posts/{featuredPost.id}/comments` para pegar
os comentários do post destacado (o primeiro post da lista). 💡Dica: lembre-se
de usar o `return` e retornar essa chamada de fetch. Dessa forma será possível
encadear mais `.then ` em sequência.
5. Depois de receber da API os comentários do primeiro post, use a função
`fillFeaturedPostComments` para exibi-los. Essa função recebe um array com
comentários.
6. Adicione um `.catch ` ao final do encadeamento de todos os `.then`. Caso
aconteça algum erro, esse `.catch`  deverá chamar a função `fillErrorMessage` e
passar a mensagem de erro.
