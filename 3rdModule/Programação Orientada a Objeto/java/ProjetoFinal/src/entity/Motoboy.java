package entity;

public class Motoboy {
    private String nome;
    private double dinheiro;
    private double frete;
    public Motoboy(String nome, double dinheiro, double frete) {
        this.nome = nome;
        this.dinheiro = dinheiro;
        this.frete = frete;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getDinheiro() {
        return dinheiro;
    }
    public void setDinheiro(double dinheiro) {
        this.dinheiro = dinheiro;
    }
    public double getFrete() {
        return frete;
    }
    public void setFrete(double frete) {
        this.frete = frete;
    }
    @Override
    public String toString() {
        return "Motoboy [nome=" + nome + ", dinheiro=" + dinheiro + ", frete=" + frete + "]";
    }

    public void gorjeta(double valor){
        this.dinheiro += this.dinheiro + valor;
    }

    public void entrega(Prato prato, Caixa caixa){
        caixa.cobrar(this.frete + prato.getPreco());
        this.dinheiro += this.dinheiro + this.frete;
    }

}
