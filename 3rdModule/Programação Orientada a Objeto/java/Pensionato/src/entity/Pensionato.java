package entity;

public class Pensionato {
    private String nome;
    private String email;
    private int numeroDoQuarto;
    public Pensionato() {
    }
    public Pensionato(String nome, String email, int numeroDoQuarto) {
        this.nome = nome;
        this.email = email;
        this.numeroDoQuarto = numeroDoQuarto;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public int getNumeroDoQuarto() {
        return numeroDoQuarto;
    }
    public void setNumeroDoQuarto(int numeroDoQuarto) {
        this.numeroDoQuarto = numeroDoQuarto;
    }
    @Override
    public String toString() {
        return "Pensionato [nome = " + nome + ", email = " + email + ", numeroDoQuarto = " + numeroDoQuarto + "]";
    }
    
}
