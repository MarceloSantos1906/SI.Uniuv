package entity;

public class Pedido {
    public void criarRetirar(Clientes cliente, Prato prato, double preco, Caixa caixa){
        caixa.cobrar(preco);
        System.out.println("Pedido " + prato + " retirado por " + cliente + " no valor de R$" + preco);
    }

    public void criarEntrega(Clientes cliente, Prato prato, double preco, Caixa caixa){
        Motoboy obejetoMotoboy = new Motoboy("Motoboy", 0, 15);
        obejetoMotoboy.entrega(prato, caixa, cliente, preco);
    }
}
