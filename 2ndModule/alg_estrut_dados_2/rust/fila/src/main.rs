fn main() {
    let mut row = Row::new();
    row.add_element(1);
    row.add_element(2);
    row.add_element(3);

    println!("Tamanho da fila: {}", row.size()); // Ver tamanho da fila

    if let Some(element) = row.get_element(0) {
        println!("Elemento no index 0: {}", element); // Ver primeiro valor da fila
    }

    for element in &row.data {
        println!("Elemento: {}", element); // Mostra cada elemento da fila
    }

    if let Some(old_element) = row.set_element(2, 4) {
        println!("Antigo valor do index 2: {}", old_element); // insere o valor 4 no index 2 e retorna qual valor estava la
    }

    for element in &row.data {
        println!("Elemento: {}", element); // Mostra cada elemento da fila
    }
}

struct Row<T> {
    data: Vec<T>,
}

impl<T> Row<T> {
    // Cria a fila como um vetor vazio
    fn new() -> Row<T> {
        Row { data: Vec::new() }
    }

    // Adiciona elementos a fila
    fn add_element(&mut self, element: T) {
        self.data.push(element);
    }

    // pega valor de um index expecifico da fila
    fn get_element(&self, index: usize) -> Option<&T> {
        self.data.get(index)
    }

    // Move um elemento para um index expecifico e retorna o valor anterior caso exista
    fn set_element(&mut self, index: usize, element: T) -> Option<T> {
        self.data.get_mut(index).map(|old_element| std::mem::replace(old_element, element))
    }

    // Retorna o tamanho da fila
    fn size(&self) -> usize {
        self.data.len()
    }
}
