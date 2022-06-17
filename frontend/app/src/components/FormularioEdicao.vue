<template>
    <div>
        <v-dialog v-model="caixa" max-width="700px" persistent>
            <template v-slot:activator="{on, attrs}">
                <v-btn icon v-bind="attrs" v-on="on" @click="acao()">
                    <v-icon>mdi-text-box-edit-outline</v-icon>
                </v-btn>
            </template>
            <v-card elevation="0" class="pa-2">
                <v-card-title>Cadastro de Veículos</v-card-title>
                <v-divider class="ma-2"></v-divider>
                <v-text-field
                    v-model="veiculo.veiculo"
                    prepend-inner-icon="mdi-car-estate"
                    label="Veículo"
                    outlined
                    placeholder="Versa"
                ></v-text-field>
                <v-select
                    :items="listaMarcas"
                    prepend-inner-icon="mdi-watermark"
                    item-text="texto"
                    item-value="valor"
                    v-model="veiculo.marca"
                    label="Selecione uma Marca"
                    outlined
                ></v-select>
                <v-text-field
                    v-model="veiculo.ano"
                    type="number"
                    prepend-inner-icon="mdi-calendar"
                    label="Ano"
                    outlined
                    placeholder="2010"
                ></v-text-field>
                <v-textarea
                    v-model="veiculo.descricao"
                    prepend-inner-icon="mdi-sticker-text-outline"
                    label="Descrição"
                    outlined
                    placeholder="Este é o carro do ano ..."
                ></v-textarea>
                <v-select
                    :items="valoresRadio"
                    item-text="texto"
                    item-value="valor"
                    v-model="veiculo.vendido"
                    label="Carro Vendido?" outlined>
                </v-select>
                <v-text-field
                    v-model="veiculo.created"
                    prepend-inner-icon="mdi-archive-clock-outline"
                    disabled
                    label="Created"
                    outlined
                ></v-text-field>
                <v-text-field
                    v-model="veiculo.updated"
                    prepend-inner-icon="mdi-archive-clock-outline"
                    disabled
                    label="Updated"
                    outlined
                ></v-text-field>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text @click="caixa = false">Fechar</v-btn>
                    <v-btn text @click="alterar">Atualizar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </div>
</template>

<script>
import Veiculo from "@/domain/veiculo"
import {mapActions} from "vuex";
export default {
    name: "Formulario",
    props: ["dados"],
    created() {
        this.formatacaoDados();
    },
    data:() => ({
        caixa: false,
        veiculo: new Veiculo(),
        valoresRadio:  [{"texto": "Sim", "valor": true}, {"texto": "Não", "valor": false}],
        listaMarcas: [
            {"texto": "Chevrolet", "valor": "Chevrolet"},
            {"texto": "Nissan", "valor": "Nissan"},
            {"texto": "Fiat", "valor": "Fiat"}
        ]
    }),
    methods: {
        ...mapActions([
            "atualizarParcialVeiculo",
            "retornarTodosVeiculos"
        ]),
        acao() {
            this.caixa = !this.caixa;
        },
        formatacaoDados() {
            this.veiculo.veiculo = this.dados.veiculo;
            this.veiculo.marca = this.dados.marca;
            this.veiculo.ano = this.dados.ano;
            this.veiculo.descricao = this.dados.descricao;
            this.veiculo.vendido = this.dados.vendido;
            this.veiculo.created = this.dados.created;
            this.veiculo.updated = this.dados.updated;
        },
        alterar() {
            let dados = {
                "id": this.dados.id,
                "corpo": this.veiculo
            }
            this.atualizarParcialVeiculo(dados)
                .then(() => {
                    this.retornarTodosVeiculos();
                    this.acao();
                })
        }
    }

}
</script>

<style scoped>

</style>