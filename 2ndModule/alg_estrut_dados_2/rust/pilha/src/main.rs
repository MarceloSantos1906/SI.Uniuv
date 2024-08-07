fn main() {
    let mut stack = Stack::new();
    stack.push(1); //insere valor
    stack.push(2);
    stack.push(3);

    println!("tamanho da pilha: {}", stack.size()); // retorna o tamanho da pilha

    println!("Ultimo valor: {:?}", stack.peek()); //retorna o ultimo valor sem retiralo da pilha

    while let Some(value) = stack.pop() { //remove os valores um a um e retona
        println!("removido: {}", value);
    }

    println!("Ultimo valor: {:?}", stack.peek()); //ira retornar None pq todos os valores foram removidos

    println!("pilha esta vazia? {}", stack.is_empty()); // verifica se a pilha esta vazia
}

struct Stack<T> { //Cria um vetor vazio do tipo T, T significa que é um tipo generico, poderia ser i32 para aceitar apenas inteiros de 32bits
    data: Vec<T>,
}

impl<T> Stack<T> { //Cria uma estrutura de pilha com o vetor
    fn new() -> Stack<T> {
        Stack { data: Vec::new() }
    }

    fn push(&mut self, value: T) { //insere um valor na pilha
        self.data.push(value);
    }

    fn pop(&mut self) -> Option<T> { //remove e retorna o ultimo valor da pilha 
        self.data.pop()
    }

    fn is_empty(&self) -> bool { //verifica se a pilha esta vazia
        self.data.is_empty()
    }

    fn peek(&self) -> Option<&T> { //retorna o ultimo valor da pilha sem remove-lo
        self.data.last()
    }

    fn size(&self) -> usize { //retorna o tamanho da pilha
        self.data.len()
    }
}
