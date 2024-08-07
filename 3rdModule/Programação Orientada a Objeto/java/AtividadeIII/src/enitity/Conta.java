public class Conta {
    private String numero;
    private double saldo;

    public Conta(String numero, double saldo) {
        this.numero = numero;
        this.saldo = saldo;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void debitar(double valor){
        saldo -= valor;
    }

    public void creditar(double valor){
        saldo += valor;
    }

    public double consultarSaldo(){
        return saldo;
    }

    public String consultarConta(){
        return numero;
    }
}