export default class Veiculo {

    constructor(veiculo, marca, ano, descricao, vendido) {
        this.veiculo = veiculo;
        this.marca = marca;
        this.ano = ano;
        this.descricao = descricao;
        this.vendido = vendido;
        this.created = null
        this.updated = null
    }
};

// veiculo: string
// marca: string
// ano: interger
// descricao: string
// vendido: bool
// created: datetime
// updated: datetime