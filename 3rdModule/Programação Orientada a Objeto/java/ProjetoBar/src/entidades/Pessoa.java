package entidades;

public class Pessoa {
	private String nome;
	private double peso;
	private int nivelAlcoolico;
	private int nivelDiversao;
	
	public Pessoa(String nome, double peso, int nivelAlcoolico, int nivelDiversao) {
		this.nome = nome;
		this.peso = peso;
		this.nivelAlcoolico = nivelAlcoolico;
		this.nivelDiversao = nivelDiversao;
	}

	@Override
	public String toString() {
		return "Pessoa [nome=" + nome + ", peso=" + peso + ", nivelAlcoolico=" + nivelAlcoolico + ", nivelDiversao="
				+ nivelDiversao + "]";
	}
	
	public void comer(Salgado salgado) {
		this.peso+= salgado.getCalorias();
	}
	
	public void beber(Bebida bebida) {
		this.nivelAlcoolico+= bebida.getTeorAlcoolico();
		this.nivelDiversao+=1;
	}
	
	public void jogar(Sinuca sinuca) {
		this.nivelDiversao+=2;
		sinuca.setQuantidadeDeFichas(sinuca.getQuantidadeDeFichas() + 1);
	}
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getPeso() {
		return peso;
	}

	public void setPeso(double peso) {
		this.peso = peso;
	}

	public int getNivelAlcoolico() {
		return nivelAlcoolico;
	}

	public void setNivelAlcoolico(int nivelAlcoolico) {
		this.nivelAlcoolico = nivelAlcoolico;
	}

	public int getNivelDiversao() {
		return nivelDiversao;
	}

	public void setNivelDiversao(int nivelDiversao) {
		this.nivelDiversao = nivelDiversao;
	}
	
}
