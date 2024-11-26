const titulo = document.createElement("h1");
titulo.id = "titulo";
titulo.textContent = "Loja Virtual - Produtos Incríveis!";
document.body.appendChild(titulo);

const produto = document.createElement("div");
produto.id = "produto";

const nomeProduto = document.createElement("h2");
nomeProduto.textContent = "Câmera Fotográfica Digital";

const descricaoProduto = document.createElement("p");
descricaoProduto.textContent = "Capture momentos incríveis com essa câmera de alta resolução, ideal para fotógrafos iniciantes e profissionais.";

const precoProduto = document.createElement("p");
precoProduto.textContent = "Preço: R$ 1.299,99";

const imagemProduto = document.createElement("img");
imagemProduto.src = "https://via.placeholder.com/150";
imagemProduto.alt = "Imagem ilustrativa da câmera";

produto.appendChild(nomeProduto);
produto.appendChild(descricaoProduto);
produto.appendChild(precoProduto);
produto.appendChild(imagemProduto);

document.body.appendChild(produto);
