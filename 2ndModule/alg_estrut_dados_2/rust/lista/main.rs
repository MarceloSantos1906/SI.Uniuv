fn main() {
    // Cria uma lista
    let mut list: Vec<i32> = Vec::new();

    // Adciona valores a lista
    list.push(1);
    list.push(2);
    list.push(3);

    // Acessa valoes na lista
    println!("Primeiro valor: {}", list[0]);  // Retorna: Promeiro valor: 1

    // Retorna cada valor da lista
    for element in &list {
        println!("Valor: {}", element);
    }
}
