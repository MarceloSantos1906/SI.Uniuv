package entity;

public class Motoboy extends Funcionario{
    private String cnh;

    public Motoboy(String nome, String cpf, double salario, String cnh) {
        super(nome, cpf, salario);
        this.cnh = cnh;
    }

    public String getCnh() {
        return cnh;
    }

    public void setCnh(String cnh) {
        this.cnh = cnh;
    }

    @Override
    public String toString() {
        return super.toString() + ", cnh=" + cnh;
    }
}
