package entidades;

public class Salgado {
	private String nome;
	private double calorias;
	
	
	public Salgado(String nome, double calorias) {
		this.nome = nome;
		this.calorias = calorias;
	}

	@Override
	public String toString() {
		return "Salgado [nome=" + nome + ", calorias=" + calorias + "]";
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getCalorias() {
		return calorias;
	}

	public void setCalorias(double calorias) {
		this.calorias = calorias;
	}
	
}
