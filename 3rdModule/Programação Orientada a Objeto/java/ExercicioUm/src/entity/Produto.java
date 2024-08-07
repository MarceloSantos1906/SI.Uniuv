package entity;

public class Produto {
    private String nome;
    private double preco;
    private int quantidade;

    public Produto(String nome, double preco, int quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }
    public String getNome() {
        return nome;
    }
    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }
    public int getQuantidade() {
        return quantidade;
    }
    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public void mudarPreco(double preco){
        setPreco(preco);
    }

    public double valorTotalEstoque(){
        double valorDoEstoque = getPreco() * getQuantidade();
        return valorDoEstoque;
    }
    
    public void adicionarProduto(int quantidade){
        setQuantidade(getQuantidade() + quantidade);
    }
    
    public void removerProduto(int quantidade){
        setQuantidade(getQuantidade() + quantidade);
    }

    public String toString(){
        return "Nome: " + getNome() + "\nQuantidade: " + getQuantidade() + "\nPreço: R$" + getPreco() + "\nValor do estoque: R$";
    }
}
