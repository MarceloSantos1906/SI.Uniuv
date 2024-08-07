package entidades;

public class Bebida {
	private String nome;
	private int teorAlcoolico;
	
	public Bebida(String nome, int teorAlcoolico) {
		this.nome = nome;
		this.teorAlcoolico = teorAlcoolico;
	}

	@Override
	public String toString() {
		return "Bebida [nome=" + nome + ", teorAlcoolico=" + teorAlcoolico + "]";
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getTeorAlcoolico() {
		return teorAlcoolico;
	}

	public void setTeorAlcoolico(int teorAlcoolico) {
		this.teorAlcoolico = teorAlcoolico;
	}
	
}
