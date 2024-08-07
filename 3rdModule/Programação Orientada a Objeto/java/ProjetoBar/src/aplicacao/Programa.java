package aplicacao;

import entidades.Bebida;
import entidades.Pessoa;
import entidades.Salgado;
import entidades.Sinuca;

public class Programa {

	public static void main(String[] args) {
		Sinuca objetoSinuca = new Sinuca();
		Salgado objetoSalgado = new Salgado("Pastel", 0.30);
		Bebida objetoBebida = new Bebida("xy", 1);
		
		Pessoa objetoPessoa = new Pessoa("Elio", 80, 0, 0);
		
		System.out.println(objetoPessoa);
		
		objetoPessoa.comer(objetoSalgado);
		objetoPessoa.jogar(objetoSinuca);
		objetoPessoa.beber(objetoBebida);
		
		System.out.println(objetoPessoa);

	}

}
