package application;

import entity.Aluno;
import entity.Professor;
import entity.enums.Titulacao;

public class Main {
    public static void main(String[] args) {
        Aluno objetoAluno1 = new Aluno("Marcelo", "1356-6", 24);
        Professor objetoProfessor1;
        Professor objetoProfessor2;
        String nome = "Elio";
        
        if (nome.equals("Elio")){
            objetoProfessor1 = new Professor(nome, "Si", Titulacao.MESTRADO, 50);
            objetoProfessor1.associarAluno(objetoAluno1);
            objetoAluno1.associarProfessor(objetoProfessor1);
        };
        nome = "Luiz";
        if (nome.equals("Luiz")){
            objetoProfessor2 = new Professor(nome, "TI", Titulacao.MESTRADO, 34);
            objetoProfessor2.associarAluno(objetoAluno1);
            objetoAluno1.associarProfessor(objetoProfessor2);
        }
        System.out.println(objetoAluno1);
    }
}
