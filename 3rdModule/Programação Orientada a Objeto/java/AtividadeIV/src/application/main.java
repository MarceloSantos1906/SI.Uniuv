import java.util.Random;
public class main {
    public static void main(String[] args) {
        System.out.println("Criando Objetos:");
        Random gerador = new Random(0);
        double rangeMin = 10.00;
        double rangeMax = 100.00;
        double randomValue;

        Pessoas pessoa1 = new Pessoas("pessoa1", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        Pessoas pessoa2 = new Pessoas("pessoa2", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        Pessoas pessoa3 = new Pessoas("pessoa3", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());

        Animais animal1 = new Animais("animal1", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        Animais animal2 = new Animais("animal2", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        Animais animal3 = new Animais("animal3", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());

        Anime anime1 = new Anime("anime1", "genero1");
        Anime anime2 = new Anime("anime2", "genero2");
        Anime anime3 = new Anime("anime3", "genero3");

        Manga manga1 = new Manga("manga1", "genero1");
        Manga manga2 = new Manga("manga2", "genero2");
        Manga manga3 = new Manga("manga3", "genero3");

        Computador computador1 = new Computador("marca1", "modelo1");
        Computador computador2 = new Computador("marca2", "modelo2");
        Computador computador3 = new Computador("marca3", "modelo3");

        Jogo jogo1 = new Jogo("jogo1", "genero1");
        Jogo jogo2 = new Jogo("jogo2", "genero2");
        Jogo jogo3 = new Jogo("jogo3", "genero3");

        Serie serie1 = new Serie("serie1", "genero1");
        Serie serie2 = new Serie("serie2", "genero2");
        Serie serie3 = new Serie("serie3", "genero3");

        Veiculos veiculos1 = new Veiculos("veiculo1", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        Veiculos veiculos2 = new Veiculos("veiculo2", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        Veiculos veiculos3 = new Veiculos("veiculo3", randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());

        System.out.println("Pessoas:");
        System.out.println("Nome: "+ pessoa1.consultarNome() + "\nPeso: " + pessoa1.consultarPeso() + "\n");
        System.out.println("Nome: "+ pessoa2.consultarNome() + "\nPeso: " + pessoa2.consultarPeso() + "\n");
        System.out.println("Nome: "+ pessoa3.consultarNome() + "\nPeso: " + pessoa3.consultarPeso() + "\n");

        System.out.println("Métodos pessoas:");
        System.out.println("Pessoa caminha random distancia:");
        pessoa1.caminhar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        pessoa2.caminhar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        pessoa3.caminhar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        System.out.println("Nome: "+ pessoa1.consultarNome() + "\nPeso: " + pessoa1.consultarPeso() + "\n");
        System.out.println("Nome: "+ pessoa2.consultarNome() + "\nPeso: " + pessoa2.consultarPeso() + "\n");
        System.out.println("Nome: "+ pessoa3.consultarNome() + "\nPeso: " + pessoa3.consultarPeso() + "\n");

        System.out.println("Pessoa corre random distancia:");
        pessoa1.correr(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        pessoa2.correr(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        pessoa3.correr(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        System.out.println("Nome: "+ pessoa1.consultarNome() + "\nPeso: " + pessoa1.consultarPeso() + "\n");
        System.out.println("Nome: "+ pessoa2.consultarNome() + "\nPeso: " + pessoa2.consultarPeso() + "\n");
        System.out.println("Nome: "+ pessoa3.consultarNome() + "\nPeso: " + pessoa3.consultarPeso() + "\n");

        System.out.println("Animais:");
        System.out.println("Tipo: "+ animal1.consultarTipo() + "\nPeso: " + animal1.consultarPeso() + "\n");
        System.out.println("Tipo: "+ animal2.consultarTipo() + "\nPeso: " + animal2.consultarPeso() + "\n");
        System.out.println("Tipo: "+ animal3.consultarTipo() + "\nPeso: " + animal3.consultarPeso() + "\n");

        System.out.println("Métodos animais:");
        System.out.println("Animal come random:");
        animal1.alimentar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        animal2.alimentar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        animal3.alimentar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        System.out.println("Tipo: "+ animal1.consultarTipo() + "\nPeso: " + animal1.consultarPeso() + "\n");
        System.out.println("Tipo: "+ animal2.consultarTipo() + "\nPeso: " + animal2.consultarPeso() + "\n");
        System.out.println("Tipo: "+ animal3.consultarTipo() + "\nPeso: " + animal3.consultarPeso() + "\n");

        System.out.println("Animal passeia random distancia:");
        animal1.passear(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        System.out.println("Tipo: "+ animal1.consultarTipo() + "\nPeso: " + animal1.consultarPeso() + "\n");
        System.out.println("Tipo: "+ animal2.consultarTipo() + "\nPeso: " + animal2.consultarPeso() + "\n");
        System.out.println("Tipo: "+ animal3.consultarTipo() + "\nPeso: " + animal3.consultarPeso() + "\n");

        System.out.println("Anime:");
        System.out.println("Nome: "+ anime1.consultarNome() + "\nGenero: " + anime1.consultarGenero() + "\n");
        System.out.println("Nome: "+ anime2.consultarNome() + "\nGenero: " + anime2.consultarGenero() + "\n");
        System.out.println("Nome: "+ anime3.consultarNome() + "\nGenero: " + anime3.consultarGenero() + "\n");

        System.out.println("Manga:");
        System.out.println("Nome: "+ manga1.consultarNome() + "\nGenero: " + manga1.consultarGenero() + "\n");
        System.out.println("Nome: "+ manga2.consultarNome() + "\nGenero: " + manga2.consultarGenero() + "\n");
        System.out.println("Nome: "+ manga3.consultarNome() + "\nGenero: " + manga3.consultarGenero() + "\n");

        System.out.println("Serie:");
        System.out.println("Nome: "+ serie1.consultarNome() + "\nGenero: " + serie1.consultarGenero() + "\n");
        System.out.println("Nome: "+ serie2.consultarNome() + "\nGenero: " + serie2.consultarGenero() + "\n");
        System.out.println("Nome: "+ serie3.consultarNome() + "\nGenero: " + serie3.consultarGenero() + "\n");

        System.out.println("Jogo:");
        System.out.println("Nome: "+ jogo1.consultarNome() + "\nCategoria: " + jogo1.consultarCategoria() + "\n");
        System.out.println("Nome: "+ jogo2.consultarNome() + "\nCategoria: " + jogo2.consultarCategoria() + "\n");
        System.out.println("Nome: "+ jogo3.consultarNome() + "\nCategoria: " + jogo3.consultarCategoria() + "\n");

        System.out.println("Computador:");
        System.out.println("Marca: "+ computador1.consultarMarca() + "\nModelo: " + computador1.consultarModelo() + "\n");
        System.out.println("Marca: "+ computador2.consultarMarca() + "\nModelo: " + computador2.consultarModelo() + "\n");
        System.out.println("Marca: "+ computador3.consultarMarca() + "\nModelo: " + computador3.consultarModelo() + "\n");

        System.out.println("veiculos:");
        System.out.println("Tipo: "+ veiculos1.consultarTipo() + "\nodometro: " + veiculos1.consultarOdometro() + "\n");
        System.out.println("Tipo: "+ veiculos2.consultarTipo() + "\nodometro: " + veiculos2.consultarOdometro() + "\n");
        System.out.println("Tipo: "+ veiculos3.consultarTipo() + "\nodometro: " + veiculos3.consultarOdometro() + "\n");

        System.out.println("veiculo anda random:");
        veiculos1.acelerar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        veiculos2.acelerar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        veiculos3.acelerar(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        System.out.println("Tipo: "+ veiculos1.consultarTipo() + "\nodometro: " + veiculos1.consultarOdometro() + "\n");
        System.out.println("Tipo: "+ veiculos2.consultarTipo() + "\nodometro: " + veiculos2.consultarOdometro() + "\n");
        System.out.println("Tipo: "+ veiculos3.consultarTipo() + "\nodometro: " + veiculos3.consultarOdometro() + "\n");

        System.out.println("veiculo da ré random distancia:");
        veiculos1.re(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        veiculos2.re(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        veiculos3.re(randomValue = rangeMin + (rangeMax - rangeMin) * gerador.nextDouble());
        System.out.println("Tipo: "+ veiculos1.consultarTipo() + "\nodometro: " + veiculos1.consultarOdometro() + "\n");
        System.out.println("Tipo: "+ veiculos2.consultarTipo() + "\nodometro: " + veiculos2.consultarOdometro() + "\n");
        System.out.println("Tipo: "+ veiculos3.consultarTipo() + "\nodometro: " + veiculos3.consultarOdometro() + "\n");
    }
}
