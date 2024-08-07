package entity;

public class Funcionario {
    private String nome;
    private double salarioBruto;
    private double taxa;
    public Funcionario(String nome, double salarioBruto, double taxa) {
        this.nome = nome;
        this.salarioBruto = salarioBruto;
        this.taxa = taxa;
    }
    private String getNome() {
        return nome;
    }
    private double getSalarioBruto() {
        return salarioBruto;
    }
    private void setSalarioBruto(double salarioBruto) {
        this.salarioBruto = salarioBruto;
    }
    private double getTaxa() {
        return taxa;
    }

    public double salarioLiquido(){
        double salarioLiquido = getSalarioBruto() - getTaxa();
        return salarioLiquido;
    }
    
    public void aumentarSalario(double porcentagem){
        setSalarioBruto(porcentagem);
    }
    
    public String toString(){
        return "Nome: " + getNome() + "\nSalario Liquido: R$";
    }
    
}
