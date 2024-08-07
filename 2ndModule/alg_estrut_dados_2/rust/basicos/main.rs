use std::io; //importa uma dependencia

fn main() {
    println!("Hello, world!"); //Hello World

    let mut x = 4; //define x como uma variavel mutavel inicialmente valendo 4
    let y = 1; //define y como uma variavel imutavel valendo 1
    let mut input = String::new(); //define input como string e importa new() de io
    println!("x é: {}", x); //exibe o valor inicial de x
    x = 3; //muda o valor de x de 4 para 3
    println!("agora x é: {}", x);
    println!("y is: {}", y);
    x -= y; //faz a conta x - y (3 - 1) e armazena em x
    println!("x - y : {}", x); //mostra o novo valor de x definido na linha de cima

    println!("Insira algum texto:");
    io::stdin().read_line(&mut input).expect("erro ao ler a linha"); //usando o pacote io recebe input do usuario e exibe a mensagem em expect caso ocorra algum erro
    println!("Vc escreveu: {}", input);

    //condições and="&&" or="||" not="!"

}
